
def Second(arr):

    arr.sort()

    for second in arr:
        if second != arr[0]:
            break

    a = arr.index(second)

    foo = []

    for i in arr:
        if i == arr[a]:
            foo.append(i)



    return foo





arr = [5,234,54,23,213,54,76,346,98,23,5,5,23,65,342]

secondmin = Second(arr)

print(secondmin)
