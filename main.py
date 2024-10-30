# Dylan Stitt
# Unit 3 Lab 3
# Merge Sort

from random import shuffle

def MergeSort(n):
    if len(n) == 1:
        return n

    l = int(len(n)/2)
    left = MergeSort(n[:l])
    right = MergeSort(n[l:])

    new = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            new.append(left[0])
            left.remove(left[0])

        elif left[0] > right[0]:
            new.append(right[0])
            right.remove(right[0])

    if len(left) != 0:
        new.extend(left)
    else:
        new.extend(right)

    return new

def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = MergeSort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == '__main__':
    main()
