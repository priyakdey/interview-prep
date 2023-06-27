#!/usr/bin/env python3
from typing import List


def generate_all_subsequence(arr: List[int]) -> List[List[int]]:
    """Function to generate all subsequence of an given array"""
    subsequences = []
    if len(arr) == 0:
        return subsequences
    if len(arr) == 1:
        subsequences.append(arr)
        return subsequences

    def generate(array: List[int], index: int, subarr: List[int]) -> None:
        if index == len(array):
            if len(subarr) != 0:
                subsequences.append(subarr)
        else:
            generate(array, index + 1, subarr)
            generate(array, index + 1, subarr + array[index : index + 1])

    generate(arr, 0, [])
    return subsequences


# print(generate_all_subsequence([]))
# print(generate_all_subsequence([1]))
# print(generate_all_subsequence([1, 2, 3]))
print(generate_all_subsequence([1, 2, 3, 4]))
