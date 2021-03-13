for i in range(int(input())):
    n=int(input())
    arr= [ -120, 0, -102, 68, -472, -463,-28, -305, -81, -169, -348, -184, 79, -262, 13, -459, -345, 70, -24, -343, -308]

    localsum,globalsum = arr[0],arr[0]
    for i in arr[1:] :
        localsum = max(i,i+localsum)
        globalsum = max(localsum,globalsum)
        print(localsum,globalsum)
    print(globalsum)