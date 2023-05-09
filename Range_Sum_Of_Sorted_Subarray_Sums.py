
def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
    x = list()
    
    for index, i in enumerate(nums):
        x.append(i)
        tmp = i
        for j in range(index+1, n):
            tmp = tmp + nums[j]
            x.append(tmp)
    
    y = sorted(x)
    print()
    return sum(y[left-1:right]) % 1_000_000_007



rangeSum(1, [1,2,3,4], 4, 1, 5)