import pydot
import os
import requests

# From the input file, import
from input import tree as input
from input import additionals as additionals


# Parameters
drawsize = 5
IMAGEURL = "https://projectpokemon.org/images/sprites-models/sv-sprites-home/"





# Define graph
cladogram = pydot.Dot("cladogram", graph_type="graph")
nodes = {}

def getimages(list, additionals=[]):
    '''
    Automatically pulls all images that are not already in the images/ folder from the source url, treating it as a folder where the nodes are pulled from
    
    :param list: The list of nodes, usually the tree itself. Can be a string, a dictionary containing the key 'tree', or any iterative data type
    :param additionals: The list of extra nodes. Must be an iterative data type containing dictionaries with the key 'new'
    '''
    if isinstance(list,str):
        # if string, get that image
        if not os.path.isfile("images/" + list):
            url = IMAGEURL + list
            data = requests.get(url).content
            f = open("images/" + list,'wb')
            f.write(data)
            f.close()
    elif isinstance(list,dict):
        # if dict, recursively get the tree's images
        getimages(list["tree"])
    else:
        # If other datatype, get images for each
        for item in list:
            getimages(item)
    for item in additionals:
        # For each extra node, if it is a filename (considered by .) gather image
        if not os.path.isfile("images/" + item["new"]) and item["new"].find(".") >= 0:
            url = IMAGEURL + item["new"]
            data = requests.get(url).content
            f = open("images/" + item["new"],'wb')
            f.write(data)
            f.close()

def shouldBeAnchored(item):
    '''
    Docstring for shouldBeAnchored
    
    :param item: A tree node
    :return: Checks if the conditions are valid to use the anchor parameter
    :rtype: bool
    '''
    return isinstance(item,dict) and "anchor" in item.keys() and item["anchor"] and isinstance(item["tree"],tuple)

def addtotree(item,parentname,num,graph=cladogram,linecolor="#000000"):
    '''
    Adds one node to the tree, then recursively clls itself on the children. Returns a boolean:
        True if the node has an image
        False if the node has no image
    The return value is used in the recursive calls for appropriate formatting.
    :param item: The node / subtree to be added.
    :param parentname: The internal name of the parent. Names are in the format of int_int_int, with each number representing the steps from the leftmost child of the parent.
    :param num: Which number child this should be for the parent, left-to-right. Provided here to construct the correct name.
    :param graph: The pydot.Dot graph file. Defaults to the one defined in the cladogram variable.
    :param linecolor: The line color that should be used by this node.
    '''
    global cladogram
    global nodes
    # The name of this node is constructed here
    thisname = parentname + "_" + str(num)
    # if the item is a dictionary, there are parameters to use.
    if isinstance(item,dict):
        if not "tree" in item.keys():
            raise ValueError("The following dict is missing a 'tree' key: " + str(item))
        # if the color parameter is defined, that color should be used.
        if "color" in item.keys():
            newcolor = item["color"]
        else: 
            newcolor = linecolor
        # if the id parameter is defined, the dictionary of ids to nodes adds a key-value pair of the id and the node's name
        if "id" in item.keys():
            nodes[item["id"]] = thisname
        # if anchor is True, and the child is a tuple, each child should be attached here, directly.
        # Useful for cases such as branched Pokemon evolution, where you want multiple nodes with an image attached to a root that also has an image defined
        # WARNING: this branch's return is arbitrary due to ambiguity.
        if shouldBeAnchored(item):
            for elem in range(len(item["tree"])):
                last = addtotree(item["tree"][elem],parentname,num + elem, linecolor=newcolor)
            return last
        # otherwise, simply call this function again with the newcolor, using the contents of the "tree" parameter.
        else:
            return addtotree(item["tree"],parentname,num,linecolor=newcolor)
    # if the node is a string, take that as a filename
    elif isinstance(item,str):
        graph.add_node(pydot.Node(thisname,label="",image=os.path.abspath("images/" + item),shape="none"))
        return True
    # if the node is a tuple, adds an imageless node and then connects each child to it
    elif isinstance(item,tuple):
        graph.add_node(pydot.Node(thisname,shape="point",width=drawsize/80,height=drawsize/80,color=linecolor))
        for child in range(len(item)):
            # if child is a dict with colorroot parameter, use that instead of the provided color. Allows for multiple nodes in a tuple to have different colored connections
            if isinstance(item[child],dict) and "color" in item[child].keys() and "colorroot" in item[child].keys() and item[child]["colorroot"]:
                thiscolor = item[child]["color"]
            else:
                thiscolor = linecolor
            outcome = addtotree(item[child],thisname,child,linecolor=linecolor)
            graph.add_edge(pydot.Edge(thisname + "_" + str(child), thisname, penwidth=drawsize, color=thiscolor, headclip=False, tailclip=outcome))
        return False
    # if the node is a list, add each element one-by-one, connected to each other.
    elif isinstance(item,list):
        # lists of length 1 are just nodes
        if len(item) == 1:
            return addtotree(item[0],parentname,num,linecolor=linecolor)
        else:
            thiscolor = linecolor
            # check for parameters. store id parameter, apply color parameter
            if isinstance(item[0],dict):
                imgpath = item[0]["tree"]
                if "id" in item[0].keys():
                    nodes[item[0]["id"]] = thisname
                if "color" in item[0].keys():
                    thiscolor = item[0]["color"]
            elif isinstance(item[0], tuple):
                raise TypeError("The following tuple is not the last element of a list: " + str(item[0]))
            else:
                imgpath = item[0]
            # add this node
            graph.add_node(pydot.Node(thisname,label="",image=os.path.abspath("images/" + imgpath),shape="none"))
            # check for colorroot parameter in the next element of the list and apply if applicable
            if isinstance(item[1],dict) and "color" in item[1].keys() and "colorroot" in item[1].keys() and item[1]["colorroot"]:
                thiscolor = item[1]["color"]
            # recursively call addtotree with the rest of the list
            addtotree(item[1:],thisname,0,linecolor=thiscolor)
            # if the next item is the last, and should be anchored, then add an edge to each child
            if len(item) == 2 and shouldBeAnchored(item[1]):
                for elem in range(len(item[1]["tree"])):
                    thiscolor=linecolor
                    if isinstance(item[1]["tree"][elem],dict) and "color" in item[1]["tree"][elem].keys():
                        thiscolor = item[1]["tree"][elem]["color"]
                    graph.add_edge(pydot.Edge(thisname + "_" + str(elem), thisname, penwidth=drawsize,color=thiscolor))
            # otherwise, just add an edge to the single child
            else:
                graph.add_edge(pydot.Edge(thisname + "_0", thisname, penwidth=drawsize,color=thiscolor))
            return True

def addadditionals(list, graph=cladogram):
    '''
    This function adds extra nodes based on the id. Allows for additional connections that violate the tree structure. In the base tree, see Burmy or Oricorio for obvious examples.
    
    :param list: The list of additional nodes
    :param graph: The graph that should be added to
    '''
    global nodes
    # Checks every additional node provided
    for pairnum in range(len(list)):
        # if the 'new' option is not an existing nodes' ID, add the node and, if applicable, ID parameter. This allows for new nodes to be added this way and then used themselves as IDs
        if not list[pairnum]["new"] in nodes.keys():
            thisnode = "additional" + str(pairnum)
            if "id" in list[pairnum].keys():
                nodes[list[pairnum]["id"]] = thisnode
            graph.add_node(pydot.Node(thisnode,label="",image=os.path.abspath("images/" + list[pairnum]["new"]),shape="none"))
        else:
            thisnode = nodes[list[pairnum]["new"]]
        # apply color parameter
        if "color" in list[pairnum].keys():
            thiscolor = list[pairnum]["color"]
        else:
            thiscolor = "#000000"
        # checks dontaffectvert parameter and applies it
        if "dontaffectvert" in list[pairnum].keys() and list[pairnum]["dontaffectvert"]:
            ranking = False
        else:
            ranking = True
        # for every root, connect. roots must be existing nodes, but can be defined individually with no roots first (see Snorunt for an example of that)
        for id in list[pairnum]["roots"]:
            if id in nodes.keys():
                graph.add_edge(pydot.Edge(thisnode, nodes[id], penwidth=drawsize,color=thiscolor,constraint=ranking))
            

# First, gather images
getimages(input, additionals)

# Then, build tree
addtotree(input,"",0)

# Lastly, add extra nodes
addadditionals(additionals)

cladogram.write_png("output.png")
