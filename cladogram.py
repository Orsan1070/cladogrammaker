import pydot
import os
from input import tree as input
from input import additionals as additionals
import requests
import graphviz

cladogram = pydot.Dot("cladogram", graph_type="graph")

nodes = {}

drawsize = 5

def getimages(list, additionals=[]):
    if isinstance(list,str):
        if not os.path.isfile("images/" + list):
            url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + list
            data = requests.get(url).content
            f = open("images/" + list,'wb')
            f.write(data)
            f.close()
    elif isinstance(list,dict):
        getimages(list["tree"])
    else:
        for item in list:
            if isinstance(item,str):
                if not os.path.isfile("images/" + item):
                    url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + item
                    data = requests.get(url).content
                    f = open("images/" + item,'wb')
                    f.write(data)
                    f.close()
            elif isinstance(item,dict):
                getimages(item["tree"])
            else:
                getimages(item)
    for item in additionals:
        if not os.path.isfile("images/" + item["new"]) and item["new"].find(".") >= 0:
            url = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/" + item["new"]
            data = requests.get(url).content
            f = open("images/" + item["new"],'wb')
            f.write(data)
            f.close()

def addtotree(item,parentname,num,graph=cladogram,linecolor="#000000"):
    global cladogram
    global nodes
    thisname = parentname + "_" + str(num)
    quantity = 1
    if isinstance(item,dict):
        if "color" in item.keys():
            newcolor = item["color"]
        else: 
            newcolor = linecolor
        if "id" in item.keys():
            nodes[item["id"]] = thisname
        if "anchor" in item.keys() and item["anchor"] and isinstance(item["tree"],tuple):
            for elem in range(len(item["tree"])):
                addtotree(item["tree"][elem],parentname,num + elem, linecolor=newcolor)
        else:
            return addtotree(item["tree"],parentname,num,linecolor=newcolor)
    elif isinstance(item,str):
        graph.add_node(pydot.Node(thisname,label="",image=os.path.abspath("images/" + item),shape="none"))
        return True
    elif isinstance(item,tuple):
        graph.add_node(pydot.Node(thisname,shape="point",width=drawsize/80,height=drawsize/80,color=linecolor))
        for child in range(len(item)):
            if isinstance(item[child],dict) and "color" in item[child].keys() and "colorroot" in item[child].keys() and item[child]["colorroot"]:
                thiscolor = item[child]["color"]
            else:
                thiscolor = linecolor
            outcome = addtotree(item[child],thisname,child,linecolor=linecolor)
            graph.add_edge(pydot.Edge(thisname + "_" + str(child), thisname, penwidth=drawsize, color=thiscolor, headclip=False, tailclip=outcome))
        return False
    elif isinstance(item,list):
        if len(item) == 1:
            addtotree(item[0],parentname,num,linecolor=linecolor)
        else:
            if isinstance(item[0],dict):
                imgpath = item[0]["tree"]
                if "id" in item[0].keys():
                    nodes[item[0]["id"]] = thisname
            else:
                imgpath = item[0]
            graph.add_node(pydot.Node(thisname,label="",image=os.path.abspath("images/" + imgpath),shape="none"))
            if isinstance(item[1],dict) and "color" in item[1].keys() and "colorroot" in item[1].keys() and item[1]["colorroot"]:
                thiscolor = item[1]["color"]
            else:
                thiscolor = linecolor
            addtotree(item[1:],thisname,0,linecolor=thiscolor)
            if isinstance(item[1],dict) and "anchor" in item[1].keys() and item[1]["anchor"] and isinstance(item[1]["tree"],tuple):
                for elem in range(len(item[1]["tree"])):
                    thiscolor=linecolor
                    if isinstance(item[1]["tree"][elem],dict) and "color" in item[1]["tree"][elem].keys():
                        thiscolor = item[1]["tree"][elem]["color"]
                    graph.add_edge(pydot.Edge(thisname + "_" + str(elem), thisname, penwidth=drawsize,color=thiscolor))
            else:
                graph.add_edge(pydot.Edge(thisname + "_0", thisname, penwidth=drawsize,color=thiscolor))
            return True

def addadditionals(list, graph=cladogram):
    global nodes
    for pairnum in range(len(list)):
        if not list[pairnum]["new"] in nodes.keys():
            thisnode = "additional" + str(pairnum)
            if "id" in list[pairnum].keys():
                nodes[list[pairnum]["id"]] = thisnode
            graph.add_node(pydot.Node(thisnode,label="",image=os.path.abspath("images/" + list[pairnum]["new"]),shape="none"))
        else:
            thisnode = nodes[list[pairnum]["new"]]
        if "color" in list[pairnum].keys():
            thiscolor = list[pairnum]["color"]
        else:
            thiscolor = "#000000"
        if "dontaffectvert" in list[pairnum].keys() and list[pairnum]["dontaffectvert"]:
            ranking = False
        else:
            ranking = True
        for id in list[pairnum]["roots"]:
            if id in nodes.keys():
                graph.add_edge(pydot.Edge(thisnode, nodes[id], penwidth=drawsize,color=thiscolor,constraint=ranking))
            


getimages(input, additionals)

addtotree(input,"",0)

addadditionals(additionals)

#cladogram.set("splines","true")

#cladogram.set("overlap","false")

#cladogram.set("concentrate","false")

#graphvizcladogram = graphviz.Source(cladogram.to_string())

cladogram.write_png("output.png")

#graphvizcladogram.render(engine='sfdp')


#graph G {
#  hidden [shape=point style=invis width=0 height=0]
#  Blastoise[image="https://archives.bulbagarden.net/media/upload/9/9e/Menu_HOME_0009.png",label=""]
#  Carracosta -- hidden [headclip=false]
#  hidden -- Terapagos [tailclip=false]
#  hidden -- Blastoise [tailclip=false]
#}