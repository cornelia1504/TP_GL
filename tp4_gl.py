#encoding : utf8
"""Program to make a display of an in-depth traversal,
making it possible to represent tree-like tree"""

class Binary_tree():
    """Creat binary tree"""
    def __init__(self) -> None:
        self.root=None
        self.node=None

    def print_tree(self):
        """ Displays the node and all descendants """
        return self.root.display_node()

class Node():
    """ Class allowing to create nodes as well as to add nodes to them (left or right) """
    def __init__(self, value):
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0

    def add(self, left = None, right = None):
        """ Method to add nodes (left and/or right) to a node using recursion """
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """ Method to update the depth of the added nodes (left and/or right)"""
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    # def display_node2(self):
    #     retour = str(self)
    #     if self.right:
    #         retour += " " + self.right.display_node()
    #     if self.left:
    #         retour += " " + self.left.display_node()

    #     return retour

    def display_node(self, level=0): #"level" create an indentation
        """ Method to display each node and all descendants using recursion"""
        retour = str(self)
        if self.right:
            retour += "\n"
            for _ in range(0,level+1): #add a tab at each level of the tree
                retour += "\t"
            retour += self.right.display_node(level+1) #add a right node at each level
        if self.left:
            retour += "\n"
            for _ in range(0,level+1): #add a tab at each level of the tree
                retour += "\t"
            retour += self.left.display_node(level+1) #add a left node at each level
        return retour

    def __str__(self):
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        #return self.left == None and self.right == None
        return not(self.left or self.right)

    def get_max_depth(self,max_depth=0):
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        # je suis le node d'un arbre
        else:
            if self.right:
                max_depth = self.right.get_max_depth(max_depth)

            if self.left:
                max_depth = self.left.get_max_depth(max_depth)
            return max_depth


node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node3.add(node4)
node1.add(node2, node3)
tree1=Binary_tree()
tree1.root=node1

node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node5.add(node6, node7)
node4.add(node5)
node8 = Node(8)
node7.add(node8)

#print(str(node1.get_max_depth(0)))
tree = Binary_tree()
tree.root= node1
print("\n")
print("Binary tree depth-first traversal\n ")
#print(node1.display_node())
print(tree.print_tree())
