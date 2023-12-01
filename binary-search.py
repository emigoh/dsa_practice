'''Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
https://leetcode.com/problems/binary-search/


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1'''

#return index value or -1
#O(log n) runtime
#arrays are sorted in ascending order

#if array is empty return -1
#if length of array is less than 2, don't need to binary search
#set pointer for left and right bound
#get midpoint - round down
#check if target is equal to midpoint
#if not, check if target is less than or greater than midpoint


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        