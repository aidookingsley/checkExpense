# twosums.py
from typing import List


def twoSums(self, nums: List[int], target: int):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(twoSums(0, [2, 7, 11, 15], 9))
