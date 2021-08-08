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