from typing import Optional


def solution(nums: list[int], target: int) -> Optional[list[int]]:
    num_dict = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in num_dict:
            return [num_dict[difference], i]
        
        num_dict[difference] = i
    return None


if __name__ == "__main__":
    nums = [3, 2, 3]
    target = 6
    result = solution(nums, target)
    assert [0, 2] == result