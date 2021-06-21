def selectionSort():
    arr = [1, 5, 3, 4, 2, 88, 4, 7, -1, 0]

    for i in range(len(arr)):
        minIndex = i
        print('min', minIndex)
        for y in range(i+1,len(arr)):
            if arr[minIndex] > arr[y]:
                minIndex = y
                print(y, arr[y])
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print(arr[i], arr[minIndex])
        print(arr)
        print()

selectionSort()
