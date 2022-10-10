from itertools import count
import numbers
from tabnanny import check
from typing import List


class Solution:
    def table_multiply(self, a: int, b: int, c: int, d: int) -> None:
        print('\t', end='')
        for i in range(c, d+1):
            print(i, end='\t')
        print()
        for j in range(a, b+1):
            print(j, end='\t')
            for i in range(c, d+1):
                print(i * j, end='\t')
            print()
    
    def mid_of_sum_devided(self, a: int, b: int) -> int:
        mid = 0
        count = 0
        for i in range(a, b+1):
            if i % 3 == 0:
                mid += i
                count += 1
        mid = mid / count
        return mid

    def percent_of_GC(self, genom: str) -> float:
        countOfGenom = len(genom)
        countOfGC = genom.count('g') + genom.count('c')
        return countOfGC/countOfGenom * 100
    
    def code_DNC(self, genom: str) -> str:
        count = 1
        checkSym = genom[0]
        code = ''
        for sym in genom[1:]:
            if sym == checkSym:
                count += 1
            else:
                code = code + str(count) + checkSym
                count = 1
            checkSym = sym
        code = code + str(count) + checkSym
        #s = 'abcdefghijk'
        #print(s[3:6]+ ' ' +s[:6]+ ' ' +s[3:]+ ' ' +s[::-1]+ ' ' +s[-3:]+ ' ' +s[:-6]+ ' ' +s[-1:-10:-2])
        return code
    
    def sumOfNumbers(self) -> int:
        numbers = [int(i) for i in input().split()]
        sum = 0
        for i in numbers:
            sum += i
        return sum
    
    def sum_of_neighbors(self) -> str:
        numbers = [int(i) for i in input().split()]
        sum_of_neighbors = []
        if len(numbers) == 1:
            return numbers
        for i in range(len(numbers)-1):
            if i != len(numbers)-1:
                sum_of_neighbors.append(numbers[i-1]+numbers[i+1])
        sum_of_neighbors.append(numbers[len(numbers)-2]+numbers[0])
        return sum_of_neighbors
    
    def digits_count_more_one(self) -> str:
        numbers = [int(i) for i in input().split()]
        numbers.sort()
        result = []
        result_string = ''
        for num in numbers:
            if num in result:
                continue
            else:
                if numbers.count(num) > 1:
                    result.append(num)
        for res in result:
            result_string += str(res) + ' '
        return result_string
    
    def func_square_of_digits(self) -> int:
        summ = 0
        sqare_summ = 0
        while True:
            num = int(input())
            summ += num
            sqare_summ += (num*num)
            if summ == 0:
                return sqare_summ
    
    def return_sequence(self, num) -> str:
        count_digit = 0
        count_elements = 0
        result = ''
        while True:
            count_digit += 1
            for i in range(count_digit):
                if count_elements == num:
                    return result
                result += str(count_digit) + ' '
                count_elements += 1
    
    def nums_positions(self) -> str:
        numbers = [int(i) for i in input().split()]
        num = int(input())
        count = 0
        result = ''
        for i in numbers:
            if i == num:
                result += str(count) + ' '
            count += 1
        if result == '':
            return 'Отсутствует'
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        for i in range(len(nums)):
            count = count + 1
            for f in range(count,len(nums)):
                if nums[i] + nums[f] == target:
                    return [i, f]
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
        

if __name__ == "__main__":
    result = Solution()
    # print(result.digits_count_more_one())
    # result.table_multiply(1, 10, 1, 10)
    # print()
    # print(result.sumOfNumbers())
    # print(result.sum_of_neighbors())
    # print(result.func_square_of_digits())
    print(result.nums_positions())