from LinkedBinaryTree import LinkedBinaryTree

operators = '*/+-'
# 5a
def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split() # * 2 + - 15 6 4
    prefix_exp.reverse() # 4 6 15 - + 2 *
    head = LinkedBinaryTree.Node(prefix_exp.pop()) # 4 6 15 - + 2
    def create_expression_tree_helper(prefix_exp, head):
        '''adds rest of stuff to head passed in'''
        if len(prefix_exp) == 0:
            return
        left = prefix_exp.pop() # 2 -
        if left in operators:
            head.left = LinkedBinaryTree.Node(left)
            create_expression_tree_helper(prefix_exp,head.left)
        else: head.left = LinkedBinaryTree.Node(int(left)) 
        right = prefix_exp.pop() # + 
        if right in operators:
            head.right = LinkedBinaryTree.Node(right)
            create_expression_tree_helper(prefix_exp,head.right)
        else: head.right = LinkedBinaryTree.Node(int(right))
    
    create_expression_tree_helper(prefix_exp, head)
    ret = LinkedBinaryTree(head)
    return ret
# 5b
def prefix_to_postfix(prefix_exp_str):
    ''' 
    Uses create_expression_tree to turn prefix into postfix
    prefix  '* 2 + - 15 6 4' D L R
    infix   '2 * 15 - 6 + 4' L D R
    postfix '2 15 6 – 4 + *' L R D
    '''
    return " ".join([str(item.data) for item in (create_expression_tree(prefix_exp_str)).postorder()])


# b = create_expression_tree('* 2 + - 15 6 4')
# for item in b.iterative_inorder():
#     print(item,end=' ')
# print()

# print(prefix_to_postfix('* 2 + - 15 6 4'))

#         *
#       /   \
#      2     +
#           / \
#          -   4
#         / \
#        15  6