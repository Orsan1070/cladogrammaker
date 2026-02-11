CLADOGRAM MAKER
--------------------------------------
Generates a cladogram image at output.png based on the data provided in input.py. To use, simply define the tree you want to generate in input.py as 'tree' and 'additionals', add the images you want, then run cladogram.py.

PREREQUISITES
--------------------------------------
Python 3.x
pydot library
requests library
    (both available on pip)

RESOURCES
--------------------------------------
Images in the images/ folder. These will display at FULL RESOLUTION
Any missing images will be automatically downloaded from the URL provided in the IMAGEURL parameter in cladogram.py
Data in input.py

INPUT.PY FORMATTING
--------------------------------------
input.py takes in, in python format, a tree (in this program's unique format) and a list of additional edges as tree and additionals respectively.

Every object represents some subtree.
The tree format is as follows:
A tuple (using parentheses) is applied as a branch point containing all elements of the tuple.
A list (using square brackets) attaches each node to the one before it in sequence.
A dictionary (using curly braces) allows you to apply various parameters.
The nodes themselves are represented as strings containing their image's filename or file path within images.

TUPLES have no restrictions. All elements can be put into a tuple.
LISTS cannot have tuples in any element except their last.
DICTIONARIES MUST have a "tree" key whose value is the subtree you want to contain. They can also have any number of the following parameters:
    "anchor": Used if the child is a TUPLE. Attaches every element to its parent instead of each branching off a middle, unimaged node.
    "color": Affects the color of every line in the subtree 
    "colorroot": If this is True, the line connecting this subtree to its parent will also be colored. (This is mostly useful for giving multiple anchored children different line colors.)
    "id": Gives this node a simple identifier for the sake of additionals.

ADDITIONALS are additional edges that violate the tree structure. They are defined as dictionaries with the following keys:
    "new" is the UPPER element. Can be a new node (in which case new should contain its filename) or an existing node's ID parameter.
    "roots" is a list of existing IDs that are the ROOTS of this new connection.
    "color" is the color of this connection.
    "id" is the ID of the node, IF 'new' is a new node. Allows for multiple additionals to reference the same new node.
    "dontaffectvert" means that the connection added will not affect any kind of vertical placement. Be careful when using this one, as extreme cases can mess up the renderer.
    If you need no additional edges, simply define it as an empty list.