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



