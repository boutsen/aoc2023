from functools import cache


def parse_data(my_file):
    # Open the file and parse each line to extract rows and nums
    # Convert nums to a tuple of integers and store as (row, nums) pairs in a list
    with open(my_file) as f:
        return [(row, tuple(int(num) for num in nums.split(',')))
                for row, nums in (line.split() for line in f)]


@cache
def springs_finder(row, nums):
    # Recursive function to find the number of valid patterns in the row
    next_part = nums[1:]
    possible_springs = generate_possible_springs(row, nums)
    valid_indices = find_valid_indices(row, possible_springs)
    return sum(springs_finder(row[v:], next_part)
               for v in valid_indices) if next_part else sum('#' not in row[v:] for v in valid_indices)


def generate_possible_springs(row, nums):
    # Generate possible patterns for the given row and nums
    return (f"{spr*'.'}{'#'*nums[0]}."
            for spr in range(len(row) - sum(nums) - len(nums[1:])))


def find_valid_indices(row, possible_springs):
    # Find valid indices where generated patterns match the row
    return (len(spr) for spr in possible_springs
            if all(r in (c, '?') for r, c in zip(row, spr)))


DATA = parse_data('inputs/day12')
print('Part 1: ', sum(springs_finder(r + '.', n) for r, n in DATA))
print('Part 2: ', sum(springs_finder(r + '.', n) for r, n in (('?'.join([r] * 5), n * 5) for r, n in DATA)))
