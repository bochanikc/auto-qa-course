from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        for i in range(len(nums)):
            count = count + 1
            for f in range(count,len(nums)):
                if nums[i] + nums[f] == target:
                    return [i, f]

if __name__ == "__main__":
    result = Solution()
    print(result.twoSum([2,7,11,15], 26))