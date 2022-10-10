from random import randint


def array(n):
    array1 = [randint(10, 80) for x in range(n)]
    print(array1)
    sort(array1)
    print(array1)


def sort(array):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff


if __name__ == '__main__':
    n = int(input())
    array(n)
