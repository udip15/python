#Creating lists
numbers = [1,2,3,4,5]
mixed = [1,"hello",True,3.14]
empty = []

# Accessing elements (0-indexed)

print(numbers[0])  #1(first)
print(numbers[-1])  #5(last)

# Slicing [start:end:step]
print(numbers[1:4])   #[2,3,4]
print(numbers[::-2])  #[1,3,5]
print(numbers[::-1])  #[5,4,3,2,1]

# Modifying lists

numbers[0] = 10    #[10,2,3,4,5]
numbers.append(6)  #[10,2,3,4,5,6]
print(numbers)


