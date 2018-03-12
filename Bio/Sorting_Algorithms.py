"""
My sorting algorithms
"""
def BubbleSort(input_list):
    length = len(input_list)
    
    for passnum in range(length-1,0,-1):
        for i in range(passnum):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp
    return input_list    

def InsertionSort(input_list):
    i = 0
    while i < len(input_list):
        j = i
        while j > 0 and input_list[j-1] > input_list[j]:
            temp = input_list[j]
            input_list[j] = input_list[j-1]
            input_list[j-1] = temp
            j = j-1
        i = i + 1
    return input_list

def Top_Down_Merge_Sort(li):
    """
    if len(li) < 2: return li
    m = len(li) / 2
    return merge(Top_Down_Merge_Sort(li[:m]), Top_Down_Merge_Sort(li[m:]))
    """
    if len(input_list) <= 1:
        return input_list

    left = []
    right = []
    length = len(input_list)
    
    for i, x in enumerate(input_list):
        if i < length/2:
            left.append(x)
        else:
            right.append(x)
    left = Top_Down_Merge_Sort(left)
    right = Top_Down_Merge_Sort(right)

    return merge(left, right)
    
def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1            
    result += l[i:]
    result += r[j:]
    return result
        
            
def Bottom_Up_Merge_Sort(input_list):
    pass

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    liest = Top_Down_Merge_Sort(alist)
    print(liest)
    
if __name__ == '__main__':
    main()
