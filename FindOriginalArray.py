class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        import math
        sort_changed = sorted(changed, reverse=True)
        original_list = list()
        should_run = True

        if len(changed) == 0 or changed.count(0) % 2 == 1 or len(changed) % 2 == 1:
            return []
        
        if changed.count(0) == len(changed):
            for i in range(0, len(changed)//2):
                original_list.append(0)
            return original_list

        while should_run:
            if sort_changed[0] == 1 or sort_changed[0] == 3:
                tmp = math.floor(sort_changed[0] / 2)
            else:
                tmp = math.ceil(sort_changed[0] / 2)
            if tmp in sort_changed:
                original_list.append(tmp)
                sort_changed.remove(tmp)
                sort_changed.pop(0)
            else:
                return []
            if len(sort_changed) == 0:
                should_run = False
        return original_list

# 173/179
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# Example 2:

# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
# Example 3:

# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.