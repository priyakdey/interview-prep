"""This program shows different ways to find a duplicate number in an array.

Consideration -> array is of length n + 1 with elements [1, n].
One number is duplicate, and we need to return it.

"""

from typing import List


def duplicates_using_sort(nums: List[int]) -> int:
    """Sort the array. And iterate over from 1st element and check with curr - 1
    element. If same, we know it is the duplicate.
    Time complexity would O(nlogn) - merge sort"""

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


def duplicates_using_set(nums: List[int]) -> int:
    """Using a set, we can lookup at numbers we have seen already.
    This is efficient from time as it runs in O(n) time but requires a O(n)
    extra space"""

    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def duplicates_using_negative_marking(nums: List[int]) -> int:
    """Mark indexes negative, if we have seen the value. So we take first abs value of element 1
    and mark nums[1] = -nums[1].

    We take abs value to make sure we are taking the right element. While updating, if we find the num in the
    location already negative, we know that we have seen this value before.

    But this will always work with arrays with all positive integers.
    """

    for i in range(len(nums)):
        num = abs(nums[i])
        if nums[num] < 0:
            return num
        nums[num] = -nums[num]


# Tests
nums = [1, 2, 3, 4, 4, 5]
print("duplicates_using_sort", duplicates_using_sort(nums))
print("duplicates_using_set", duplicates_using_set(nums))
print("duplicates_using_negative_marking", duplicates_using_negative_marking(nums))
