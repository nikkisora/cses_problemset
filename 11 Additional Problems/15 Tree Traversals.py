'''

CSES - Tree Traversals



Time limit: 1.00 s
Memory limit: 512 MB

There are three common ways to traverse the nodes of a binary tree:

Preorder: First process the root, then the left subtree, and finally the right subtree.
Inorder: First process the left subtree, then the root, and finally the right subtree.
Postorder: First process the left subtree, then the right subtree, and finally the root.

There is a binary tree of n nodes with distinct labels. You are given the preorder and inorder traversals of the tree, and your task is to determine its postorder traversal.

Input

The first input line has an integer n: the number of nodes. The nodes are numbered 1,2,...,n.

After this, there are two lines describing the preorder and inorder traversals of the tree. Both lines consist of n integers.

You can assume that the input corresponds to a binary tree.

Output

Print the postorder traversal of the tree.

Constraints

1 <= n <= 10^5

Example

Input:
5
5 3 2 1 4
3 5 1 2 4

Output:
3 1 4 2 5 
'''