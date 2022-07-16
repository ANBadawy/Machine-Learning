"""Tree: BST"""

from binarytree import bst

root = bst()
print('BST of any height : ', root)

root2 = bst(height=4)
print('BST of given height : ', root2)

root3 = bst(height=4, is_perfect=True)
print('Perfect BST of given height : ', root3)

root4 = bst(height=4, is_perfect=False)
print('Non Perfect BST of given height : ', root4)

"""Tree: Heap"""

from binarytree import heap

root = heap()
print('Max-heap of any height : ', root)

root2 = heap(height=4)
print('Max-heap of given height : ', root2)

root3 = heap(height=4, is_max=True, is_perfect=True)
print('Perfect max-heap of given height : ', root3)

root4 = heap(height=4, is_max=True, is_perfect=False)
print('Non Perfect max-heap of given height : ', root4)

root5 = heap(height=4, is_max=False, is_perfect=True)
print('Perfect min-heap of given height : ', root5)

root6 = heap(height=4, is_max=False, is_perfect=False)
print('Non Perfect min-heap of given height : ', root6)
