

def solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                r -= 1
    return list(set(tuple(el) for el in result))

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution(nums)
    print(result)
    assert result == [[-1,-1,2],[-1,0,1]]