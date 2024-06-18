first_list = [1,2,3,4]
first_list.append(5)
print(first_list)

nums = [1,2,4,5]
nums.insert(2, 3)
print(nums)

popped = nums.pop(2)
print(popped)
print(nums)

nums.remove(2)
print(nums)

numbers = [5,5,6,7,5,8,8,9,10]

numbers.index(5) # 0 
numbers.index(5,1) # 1
numbers.index(5,2) # 4
numbers.index(8,6,8) # 6

numbers.count(5) # 2

# sort sorts reverse reverses

words = ["Coding", "is", "fun"]
print(" ".join(words))