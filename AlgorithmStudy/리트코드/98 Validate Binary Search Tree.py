
"""
부모노드 : n
자식노드 : 2n, 2n+1

1 2 4 8
3 7 15

"""


# TreeNode = [2,1,3]
import null as null

TreeNode = [5,1,6,null,null,3,6]

def isValidBST(TreeNode) :
    answer = True


    TreeNode.insert(0,0)
    print(TreeNode)
    n = len(TreeNode)
    print(n)

    for i in range(1,n) :
        if ((i*2)+1) > (n-1) :
            break
        else :
            if TreeNode[i] > TreeNode[2*i] and TreeNode[i] < TreeNode[2*i+1] :
                answer = True
            else :
                answer = False
                break

    print(answer)
    return answer

isValidBST(TreeNode)