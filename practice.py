def spiralPrint (arr,n,m): 
    left,top,bottom,right=0,0,n-1,m-1

    while (left <= right) and (top <= bottom) :
        for i in range(left,right+1):
            print(arr[top][i],end='   ')
        top+=1
        for i in range(top,bottom+1):
            print(arr[i][right],end='  ')
        right-=1
        for i in range(right,left-1,-1):
            print(arr[bottom][i],end='  ')
        bottom-=1
        for i in range(bottom,top-1,-1):
            print(arr[i][left],end='  ')
        left+=1
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiralPrint(arr,len(arr),len(arr[0]))

def conversionOfArray (arr):
    flag,i=0,0,len(arr)
    while i in range(0,n-1):
        if flag == 0:
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            flag=1
            i+=1
        else:
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            flag=0
            i+=1
    return arr
arr=[4,3,7,8,6,2,1]
print(conversionOfArray(arr))

from math import factorial as fact
def pattern (n):
    for i in range (0,n):
        for j in range(0,i+1):
            data = fact(i)//(fact(i-j)*fact(j))
            print(data,end=' ')
        print()
    pattern(5)

import math
def triplet (arr):
    n=len(arr)
    s=set()
    for i in arr:
        s.add(i*i)
    for i in range(n-1):
        for j in range(i+1,n):
            if ((arr[i]*arr[i]) +(arr[j]*arr[j])) in s:
                print('triplet found is: ',arr[i],arr[j],int(math.sqrt((arr[i]*arr[i]) +(arr[j]*arr[j]))))
                return
    print('no triplet found')
arr=[1,3,4,5]
triplet(arr)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def createTree(root):
    queue=[]
    data=int(input('enter the data: '))
    node=Node(data)
    queue.append(node)
    if root == None:
        root=node
    while queue != []:
        node=queue.pop(0)
        data=int(input('enter the left child: '))
        if data != -1:
            node1=Node(data)
            node.left=node1
            queue.append(node1)
        data=int(input('enter the right child: '))
        if data != -1:
            node1=Node(data)
            node.right=node1
            queue.append(node1)
    return root
root=createTree(None)
print(root.data)


def leftView (root,level):
    global res,max_level
    if root == None:
        return 
    if max_level < level:
        max_level = level
        res.append(root.data)
    leftView(root.left,level+1)
    leftView(root.right,level+1)
res=[]
max_level=0
leftView(root,1)
print(res)

def topView (root):
    hd = 0
    queue = []
    hash = {}
    queue.append((root,hd))
    while queue != []:
        root = queue.pop(0)
        if root[1] not in hash:
            hash[root[1]] = root[0].data
        if root[0].left != None:
            queue.append((root[0].left,root[1]-1))
        if root[0].right != None:
            hd=hd+1
            queue.append((root[0].right,root[1]+1))

    values = hash.values()
    return values