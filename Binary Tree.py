#!/usr/bin/env python
# coding: utf-8

# ### Binary Tree

# In[ ]:





# In[10]:


#creating binary tree
#printing binary tree 2 methods
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def printtree(root):
        if root==None:
            return
        print(root.data)
        printtree(root.left)
        printtree(root.right)
def printtreedetailed(root):
    if root==None:
        return
    print(root.data,":",end="")
    if root.left!=None:
        print("L",root.left.data,",",end="")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printtreedetailed(root.left)
    printtreedetailed(root.right)
n1=BinaryTree(10)
n2=BinaryTree(20)
n3=BinaryTree(30)
n1.left=n2
n1.right=n3
printtree(n1)
printtreedetailed(n1)


# In[11]:


#taking input
def treeInput():
    rootData=int(input())
    root=BinaryTree(rootData)
    if rootData==-1:
        return None
    lefttree=treeInput()
    righttree=treeInput()
    root.left=lefttree
    root.right=righttree
    return root


# In[ ]:


#print nodes at depth k
def depthK(root,k):
    if root==None:
        return 0
    global count
    if(1+depthK(root.left,k)==k):
        print(root.data,end=" ")
    if(1+depthK(root.left,k)==k):
        print(root.data.left)
    return count
    


# In[16]:


#taking input level wise
import queue
def takeinput():
    q=queue.Queue()
    print("Enter rootdata:")
    rootdata=int(input())
    if rootdata==-1:
        return None
    else:
        root=BinaryTree(rootdata)
        q.put(root)
        while(not(q.empty())):
            currentnode=q.get()
            print("Enter left child of ",currentnode.data)
            leftchild=int(input())
            if leftchild!=-1:
                leftnode=BinaryTree(leftchild)
                currentnode.left=leftnode
                q.put(leftnode)
            print("Enter right child of ",currentnode.data)
            rightchild=int(input())
            if rightchild!=-1:
                rightnode=BinaryTree(rightchild)
                currentnode.right=rightnode
                q.put(rightnode)
        return root

root=takeinput()
printtreedetailed(root)


# In[ ]:


#printing level wise
def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format: 
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    q=queue.Queue()
    if root==None:
        return
    q.put(root)
    while(not(q.empty())):
        currentnode=q.get()
        print(currentnode.data,":",end="",sep="")
        if currentnode.left!=None:
            q.put(currentnode.left)
            print("L:",currentnode.left.data,end="",sep="")
        else:
            print("L:",-1,end="",sep="")
        if currentnode.right!=None:
            q.put(currentnode.right)
            print(",","R:",currentnode.right.data,end="",sep="")
        else:
            print(",","R:",-1,end="",sep="")
        print()


# In[ ]:


def buildTreePreOrder(preorder, inorder):
    # Given Preorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 12 Nodes with following input:
    # preOrder: 1 2 3 4 15 5 6 7 8 10 9 12
    # inOrder: 4 15 3 2 5 1 6 10 8 7 9 12
    if len(preorder)==0:
        return None
    root=BinaryTreeNode(preorder[0])
    for i in range(len(inorder)):
        if(root.data==inorder[i]):
            c=i+1
            break
    inorderlst=inorder[:c-1]
    inorderrst=inorder[c:]
    preorderlst=preorder[1:c]
    preorderrst=preorder[c-1+1:]
    root.left=buildTreePreOrder(preorderlst, inorderlst)
    root.right=buildTreePreOrder(preorderrst, inorderrst)
    return root


# In[19]:


def buildTreePostOrder(postorder, inorder):
    # Given Postorder and Inorder traversal of a binary tree, create the binary
    # tree associated with the traversals.You just need to construct the tree
    # and return the root. For 8 Nodes with following input:
    # postOrder: 8 4 5 2 6 7 3 1
    # inOrder: 4 8 2 5 1 6 3 7
    if len(postorder)==0:
        return None
    rootdata=postorder[-1]
    root=BinaryTreeNode(rootdata)
    rootindex=-1
    for i in range(len(inorder)):
        if(rootdata==inorder[i]):
            rootindex=i
            break
    inorderlst=inorder[:rootindex]
    inorderrst=inorder[rootindex+1:]
    postorderlst=postorder[:len(inorderlst)]
    postorderrst=postorder[rootindex:-1]
    root.left=buildTreePostOrder(postorderlst, inorderlst)
    root.right=buildTreePostOrder(postorderrst, inorderrst)
    return root


# In[ ]:


def printLevelATNewLine(root):
    q=queue.Queue()
    if root==None:
        return
    q.put(root)
    q.put(None)
    while(not(q.empty())):
        currnode=q.get()
        if(q.empty()):
            break
        if currnode!=None:
            print(currnode.data,end=" ")
            if currnode.left!=None:
                q.put(currnode.left)
            if currnode.right!=None:
                q.put(currnode.right)
        else:
            print()
            q.put(None)
            


# In[ ]:




