import numpy as np

from src.solution import get_possible_outputs

def find_24_v3(nums):
    def helper(nums):
        # Base case: if there is only one number left, check if it is 24 (with some tolerance for floating-point error)
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        # Recursive case: try all possible combinations of 2 numbers and 1 operation on the input numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    # Addition and multiplication are commutative, so we only need to consider each pair once
                    if i < j:
                        if helper(rest + [nums[i] + nums[j]]):
                            return True
                        if helper(rest + [nums[i] * nums[j]]):
                            return True
                    # For subtraction and division, we need to consider both (i,j) and (j,i) pairs
                    if helper(rest + [nums[i] - nums[j]]):
                        return True
                    if nums[j] != 0 and helper(rest + [nums[i] / nums[j]]):
                        return True

        # If none of the combinations resulted in 24, return False
        return False

    # Call the helper function with the input numbers
    return helper(nums)

for _ in range(10000):
    nums = np.random.randint(1, 14, size=4)
    possible_outputs = get_possible_outputs(tuple(nums.tolist()), hint=False, target=24)
    ans1 = 24 in possible_outputs
    ans2 = find_24_v3(nums)
    assert ans1 == ans2, f'{ans1=} and {ans2=} and {nums=}'
