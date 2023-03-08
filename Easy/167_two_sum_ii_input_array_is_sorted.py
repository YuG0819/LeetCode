"""
来源:力扣(LeetCode)
链接:https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def twoSum(numbers, target):
    first = numbers[0]
    first_index = 1
    while True:
        del numbers[0]
        try:
            sec = numbers.index(target - first) + first_index +1
            return [first_index,sec]
        except:
            first = numbers[0]
            first_index += 1

numbers = [0,0,3,4]
target = 0
print(twoSum(numbers,target))


