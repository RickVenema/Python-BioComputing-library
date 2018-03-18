"""
This code is in development, at this stage it does not work!!
"""
import multiprocessing


def merge(list1, list2):
    output = []
    while list1 and list2:
        if list1[0] < list2[0]:
            output.append(list1.pop(0))
        else:
            output.append(list2.pop(0))


def test():
    print('worker')


def sort(array_to_sort):
    array_to_sort = sort(array_to_sort)
    return array_to_sort


def split_array(array_to_split):
    n = round(len(array_to_split)/2)
    output = [array_to_split[i:i+n] for i in range(0, len(array_to_split), n)]
    return output


def multithreading(array_to_sort):
    array1, array2 = split_array(array_to_sort)
    print(array_to_sort)
    print(array1)
    print(array2)

    jobs = []
    p1 = multiprocessing.Process(target=sort(array1))
    p2 = multiprocessing.Process(target=sort(array2))
    jobs.append(p1)
    jobs.append(p2)
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    output = merge(p1, p2)
    return output


def main():
    test_array = [5, 9, 1, 5, -4, 129, 28, 3]
    test = multithreading(test_array)
    print(test)


if __name__ == '__main__':
    main()
