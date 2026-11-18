# Andrew Martinez
# CPSC 335 - Project 3
# Problem 1: Longesst Consecutive Sequence

def longest_consecutive(nums):
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if num - 1 not in numbers:
                current = num
                length = 1

                while current + 1 in numbers:
                    current += 1 
                    length += 1

                if length > longest:
                     longest = length
        
        return longest 

# Test Examples
example1 = [9, 1, -3, 2, 4, 8, 3, -1, -2, 0]
example2 = [10, 5, 12, 3, 55, 30, 4, 11, 2]
example3 = [7, 7, 8, 6, 9, 1]

print("Example1: ", longest_consecutive(example1))
print("Example2: ", longest_consecutive(example2))
print("Example3: ", longest_consecutive(example3))