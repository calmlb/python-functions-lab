# Challenges
# Problem 1: Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
    total = 0
    for i in range(1,n):
        total += i
    return total
result = sum_to(6)
print(result)

# Problem 2: Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:

#largest([1, 2, 3, 4, 0])  # returns 4
#largest([10, 4, 2, 231, 91, 54])  # returns 231\


# def largest (nums):
#     max = 0
#     # 1. search through list of numbers
#     for i in range(1, (len(nums))):
#         max = [i]
#     # 2. compare two numbers in list 
#         if nums[i+1] > nums[i]:
#     # 3. if number in second position is bigger than first position, make it max
#             max = nums[i+1]
#         elif nums [i+1] == nums[i]:
#             max = nums[i]
#         else:
#             max = nums[i]
#     # 4. increment loop
#         return max
    # 5. once done, call function and print max

def largest(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
        elif num == max:
            max = num
        elif num < max:
            max = max
    return max

numbers = [2,3,5,5,6,7,8,98,1,2,3]
numbers2 = [3,5,76,2,3,4,7,88,4]

biggest = largest(numbers)
biggest2 = largest(numbers2)

print(biggest)
print(biggest2)

# Problem 3: Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

#occurances functions accepts two string arguments
def occurances (a, b):
    #declare accumulator variable - number of occurences at start is set to 0
    count = 0
    #search first string for the letter of interest given by second string
    for i in (a):
        if b == i:
        #increase accumulator accordingly by how many occurances there are
            count = count + 1
    #return the count
    return count
    #call function
number_of_occurances = occurances('floop' 'flizooperoo', 'o')
#print function
print (number_of_occurances)


# Problem 4: (Optional) Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product (*args):
    # set result to 1
    multiply = 1
    # search args based on position
    for a in args:
    # multiply args
        multiply *= a
    # return multiply outside loop
    return multiply

args_product = product(1, 2, 3, 4, 5, 6)
args_product2 = product(-1, 5, -3, -2)
print(args_product)
print(args_product2)