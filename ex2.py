def array(n):
    array1 = [0] * n
    sort(array1)
    print(array1)


def sort(array):
    array[0] = 1
    array[1] = 1

    for i in range(n-2):
        array[i+2] = array[i+1] + array[i]



if __name__ == '__main__':
    n = int(input())
    array(n)
