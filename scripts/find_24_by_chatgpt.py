import itertools

from loguru import logger

def find_24_v1(nums):
    # Generate all possible orderings of the input numbers
    orders = itertools.permutations(nums)
    
    # Generate all possible pairs of numbers in each ordering
    for order in orders:
        for i in range(1, len(nums)):
            for j in range(i):
                # Generate all possible arithmetic operations on each pair of numbers
                ops = ['+', '-', '*', '/']
                for op in ops:
                    # Try each operation and check if the result is 24 (with some tolerance for floating-point error)
                    try:
                        expr = '{}{}{}{}{}{}{}'.format('(', order[i], ')', op, '(', order[j], ')')
                        print(expr)
                        result = eval(expr)
                        if abs(result - 24) < 1e-6:
                            return True
                    except ZeroDivisionError:
                        pass
    return False


def find_24_v2(nums):
    def helper(nums, result):
        # Base case: if there are no more operations to perform, check if the result is 24 (with some tolerance for floating-point error)
        if not nums:
            return abs(result - 24) < 1e-6
        
        # Recursive case: try all possible combinations of 3 operations on the input numbers
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            if helper(rest, result + nums[i]):
                return True
            if helper(rest, result - nums[i]):
                return True
            if helper(rest, result * nums[i]):
                return True
            if nums[i] != 0 and helper(rest, result / nums[i]):
                return True
        
        # If none of the combinations resulted in 24, return False
        return False
    
    # Call the helper function with the input numbers and an initial result of 0
    return helper(nums, 0)

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

# the same as v3
def find_24_v4(nums):
    def helper(nums):
        # Base case: if there is only one number left, check if it is 24 (with some tolerance for floating-point error)
        if len(nums) == 1:
            logger.debug(nums[0])
            return abs(nums[0] - 24) < 1e-6

        # Recursive case: try all possible combinations of 2 numbers and 1 operation on the input numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    # Addition and multiplication are commutative, so we only need to consider each pair once
                    if i < j:
                        if helper(rest + [nums[i] + nums[j]]):
                            logger.debug(rest + [nums[i] + nums[j]])
                            return True
                        if helper(rest + [nums[i] * nums[j]]):
                            logger.debug(rest + [nums[i] * nums[j]])
                            return True
                    # For subtraction and division, we need to consider both (i,j) and (j,i) pairs
                    if helper(rest + [nums[i] - nums[j]]):
                        logger.debug(rest + [nums[i] - nums[j]])
                        return True
                    if nums[j] != 0 and helper(rest + [nums[i] / nums[j]]):
                        logger.debug(rest + [nums[i] / nums[j]])
                        return True

        # If none of the combinations resulted in 24, return False
        return False

    # Call the helper function with the input numbers
    return helper(nums)


def find_24_v5(nums):
    def helper(nums):
        # Base case: if there is only one number left, check if it is 24 (with some tolerance for floating-point error)
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6, str(nums[0])

        # Recursive case: try all possible combinations of 2 numbers and 1 operation on the input numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    # Addition and multiplication are commutative, so we only need to consider each pair once
                    if i < j:
                        is_found, expr = helper(rest + [nums[i] + nums[j]])
                        if is_found:
                            return True, '({} + {})'.format(expr, nums[i] + nums[j])
                        is_found, expr = helper(rest + [nums[i] * nums[j]])
                        if is_found:
                            return True, '({} * {})'.format(expr, nums[i] * nums[j])
                    # For subtraction and division, we need to consider both (i,j) and (j,i) pairs
                    is_found, expr = helper(rest + [nums[i] - nums[j]])
                    if is_found:
                        return True, '({} - {})'.format(expr, nums[j] if j > i else nums[i])
                    if nums[j] != 0:
                        is_found, expr = helper(rest + [nums[i] / nums[j]])
                        if is_found:
                            return True, '({} / {})'.format(expr, nums[j] if j > i else nums[i])

        # If none of the combinations resulted in 24, return False
        return False, ''

    # Call the helper function with the input numbers
    is_found, expr = helper(nums)
    if is_found:
        print('Yes, it is possible to make 24 from', nums, 'using the expression:', expr)
    else:
        print('No, it is not possible to make 24 from', nums)

    return is_found


# Example usage:
nums = [3, 1, 4, 6]
if find_24_v4(nums):
    print('Yes, it is possible to make 24 from', nums)
else:
    print('No, it is not possible to make 24 from', nums)
