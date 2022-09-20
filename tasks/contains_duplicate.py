from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = 1
        for num in nums:
            for checkNum in nums[count:]:
                if checkNum == num:
                    return True
                count = count + 1
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) != 1:
                return True
        return False
    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

if __name__ == "__main__":
    inner = [3,1]
    result = Solution()
    print(result.containsDuplicate(nums=inner))
    print(result.containsDuplicate2(nums=inner))
    print(result.containsDuplicate3(nums=inner))
