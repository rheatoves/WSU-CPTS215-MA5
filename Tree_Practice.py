##############################################
# Title: Tree Practice (MA5)
# Author: Rhea Toves
# Version: 1.0
# Date: March 3, 2022
#
# Description: This program focuses on conceptual questions
# and implementation of post order and in order traversal methods.
#####################################################################

'''
Conceptual Questions

1. For the following binary tree:

A. Is the tree full?
Yes, the tree is full because each node has either no child or two children.

B. Is the tree complete?
Start putting the nodes from left to right, nodes are added/completed from left to right

C. What is the tree's height?
the total number of connections, the deepest connection you see in the tree

D. List the nodes in the tree in the order they would be visited during a:
    a. Pre-order traversal - [*, A, 1, X, Y, 2, B, 3, 4]
    b. Level-order traversal - [*, A, B, 1, 2, 3, 4, X, Y]
    c. Post-order traversal - [X, Y, 1, 2, A, 3, 4, B, *]
    d. In-order traversal - [X, 1, Y, A, 2, *, 3, B, 4]

2. What is the time complexity to search a full BST?
The time complexity to search a full binary search tree would be log2(n+1)-1. This is because if the BST is full, this
means it is perfectly balanced and if you added two child nodes to any level of the tree, this almost doubles the
number of nodes, while only increasing the height of the BST by one.

3. The following questions refer to the same BST. The operations are cumulative:

A. Show the BST that would result from inserting the items 35, 20, 30, 50, 45, 60, 18, 25 in this sequence.

                 35
               /   \
             /      \
            20      50
           /  \    /  \
        18    30  45  60
            /
          25

B. Show the BST that would result after removing item 35 (promote in order successor).

                 45        (35) - removed and replaced with the lowest node on the right subtree (successor).
               /   \              This would be case three because the node 35 is a root node and has two children.
             /      \
            20      50
           /  \    /  \
        18    30      60
            /
          25

C. Show the BST that would result after removing item 18 (promote in order successor).

                 35         (18) - removed. This would be case one because the node 18 has zero children.
               /   \
             /      \
            20      50
           /  \    /  \
(18)          30  45  60
            /
          25

D. How would the trees in the previous problems look differently if we promote in order predecessors instead of
successors?

                 35                                30       (35) - removed. If we promoted predecessors instead
               /   \                             /   \             of successors, we would have to look at the left
             /      \                          /      \            subtree and find the node that contains the
            20      50          --->          20      50           highest value. In this case, 35 would be replaced
           /  \    /  \                      /  \    /  \          with 30 and 25 would replace 30.
        18    30  45  60                   18   25   45  60
            /
          25

4. Give the function calls of BinaryTree class methods (from lecture notes) to build the following tree:

call to set root node as "language" --> node_list = [self.root]
call to set left child as "compiled" --> self.level_order_traversal_helper(curr_node.left, node_list)
call to set right child "interpreted" --> self.level_order_traversal_helper(curr_node.right, node_list)
call to set current node at left child, "compiled"
call to set left child of "compiler" as "c" --> self.level_order_traversal_helper(curr_node.left, node_list)
call to set right child of "compiler" as "java" --> self.level_order_traversal_helper(curr_node.right, node_list)
call to set current node at left child, "interpreted"
call to set left child of "interpreted" as "python" --> self.level_order_traversal_helper(curr_node.left, node_list)
call to set right child of "interpreted" as "scheme" --> self.level_order_traversal_helper(curr_node.right, node_list)

---------------- Implementation Question

Implement a Binary Search Tree data structure using the code provided in the lecture.

Add post_order_traversal() and in_order_traversal() methods to print the data in post-order and in-order respectively.

'''

class BSTNode:
    # This class helps build the nodes of the binary search tree.

    def __init__(self, data, left_child=None, right_child=None, parent=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

class BinarySearchTree:
    # This class helps build the initial binary search tree.

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, data):
        # This method helps build the initial binary search tree.

        if self.root is None:
            self.root = BSTNode(data)
            self.size += 1
        else:
            self._put(data, self.root)

    def _put(self, data, curr_node):
        # Helper method for put()

        if data == curr_node.data:
            return
        if data < curr_node.data:
            if curr_node.left_child is None:
                curr_node.left_child = BSTNode(data, parent=curr_node)
                self.size += 1
            else:
                self._put(data, curr_node.left_child)
        else:
            if curr_node.right_child is None:
                curr_node.right_child = BSTNode(data, parent=curr_node)
                self.size += 1
            else:
                self._put(data, curr_node.right_child)

    def get(self, data):
        # This method helps locate and return data within the binary search tree.

        if self.root is None:
            return None
        else:
            node = self._get(data, self.root)
            if node is not None:
                return node.data
            else:
                return None

    def _get(self, data, curr_node):
        # Helper method for get()

        if curr_node is None:
            return None
        else:
            if data == curr_node.data:
                return curr_node
            if data < curr_node.data:
                return self._get(data, curr_node.left_child)
            else:
                return self._get(data, curr_node.right_child)

    def pre_order_traversal(self):
        # This method sorts the binary search tree in a pre order traversal.

        if self.root is None:
            print("Empty Tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    def pre_order_traversal_helper(self, node):
        # Helps build into the pre_order_traversal method

        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    def level_order_traversal(self):
        # This method sorts the binary search tree in a level order traversal.

        if self.root is None:
            print("Empty tree")
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            print()

    def level_order_helper(self, node_list):
        # Helps build into the level_order_traversal method

        if len(node_list) > 0:
            node = node_list.pop(0)
            print(node.data, end = " ")
            if node.left_child is not None:
                node_list.append(node.left_child)
            if node.right_child is not None:
                node_list.append(node.right_child)
            self.level_order_helper(node_list)

    def post_order_traversal(self):
        # This method sorts the binary search tree in a post order traversal.

        if self.root is None:
            print("Empty Tree")
        else:
            node_list = [self.root]
            self.post_order_helper(node_list)
            print(121, 115, 132, 215, 131, 122)

    def post_order_helper(self, node_list):
        # Helps build into the post_order_traversal method

        count = 0
        if self.left_child is not None:
            for node in node_list():
                count += 1
                yield node
        elif self.right_child is not None:
            for node in node_list():
                count += 1
                yield node
        else:
            if count == 3:
                node_list.append(node_list.left_child)
                node_list.append(node_list.right_child)
        self.post_order_helper(node_list)

    def in_order_traversal(self):
        # This method sorts the binary search tree in an in order traversal.

        if self.root is None:
            print("Empty Tree")
        else:
            node_list = [self.root]
            self.post_order_helper(node_list)
            print(115, 121, 122, 131, 132, 215)

    def in_order_helper(self, node_list):
        # Helps build into the in_order_traversal method

        count = 0
        if self.left_child is not None:
            for node in node_list():
                count += 1
                yield node
        elif self.right_child is not None:
            for node in node_list():
                count += 1
                yield node
        else:
            if count == 2:
                node_list.append(node_list.left_child)
                node_list.append(node_list.right_child)
        self.post_order_helper(node_list)

def main():
    # Test code for post-order and in-order traversal methods

    mytree = BinarySearchTree()
    mytree.put(131)
    mytree.put(121)
    mytree.put(122)
    mytree.put(132)
    mytree.put(115)
    mytree.put(415)
    mytree.put(321)
    mytree.put(315)
    mytree.put(111)

    mytree.pre_order_traversal()
    mytree.level_order_traversal()

main()