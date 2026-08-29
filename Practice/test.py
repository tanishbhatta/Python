class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            check = abs(i - target)
            if check in nums:
                index_a = nums.index(i)
                index_b = nums.index(check)

                print(list((index_a, index_b)))
                break
            else:
                print("No combinations available.")

solution = Solution()
solution.twoSum([2,7,11,15], 9)
        