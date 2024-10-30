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
    nums = list(range(50))
    shuffle(nums)
    print(nums)
    nums = MergeSort(nums)
    print(nums)

if __name__ == '__main__':
    main()
