
"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0

Input: nums = [1], target = 0
Output: 0
"""

# nums = [1,3,5,6]
# target = 5

# nums = [1,3,5,6]
# target = 2

# nums = [1,3,5,6]
# target = 7

# nums = [1,3,5,6]
# target = 0

nums = [1]
target = 0


def solution(nums, target) :
    answer = 0

    if target in nums :
        answer = nums.index(target)
    else :
        nums.append(target)
        nums.sort()
        answer = nums.index(target)

    return answer

print(solution(nums,target))

# 다른 사람의 풀이

# def solution(nums, target) :
#     answer = 0
#
#     if target in nums :
#         answer = nums.index(target)
#     else :
#         count = 0
#         for i in nums :
#             if i > target :
#                 return count
#             count += 1
#         return len(nums)
#
#     return answer


