# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(myList):
    #return max(myList)
    if len(myList) == 0:
        return"the list is empty"
    else:
        max_num = myList[0]
        for num in myList[1:]:
            if num > max_num:
                max_num = num
                
        return max_num
# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(myList):
    if not myList:
        return "the list is empty"
    else:
        product = 1
        for num in myList:
            product = product*num
        return product

# Write a Python function called rev_string() to reverse a string.
def rev_string(myString):
    return myString[::-1]


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, lowerRange, upperRange):
    return lowerRange <= num <= upperRange



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together

def pascal(n):
    # Check if the input number of rows is a positive integer
    if n <= 0:
        print("Number of rows should be a positive integer.")
        return
    
    # Initialize an empty list to store the rows of Pascal's triangle
    triangle = []
    
    # Loop to generate each row
    for i in range(n):
        # Create a new row with (i + 1) elements, all initialized to 1
        row = [1] * (i + 1)
        
        # Compute the interior values of the row (not the edges)
        if i > 1:
            for j in range(1, i):
                # Each interior value is the sum of the two values above it
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        # Append the completed row to the triangle
        triangle.append(row)
        
    # Print each row of the triangle
    for row in triangle:
        # Convert each number to a string and join them with spaces
        print(" ".join(map(str, row)))


        



#Call the functions
myString = "America"
myNumbers = [2, 4, 7, 3, 5]
maxNum = max_num(myNumbers)
print(maxNum)


product = mult_list(myNumbers)
print(product)


reversedString = rev_string(myString)
print(reversedString)


newNum = num_within(3,2,4)
print(newNum)


pascal(5)
