# [ _ for _ in _]

nums = [1,2,3]

print([x*10 for x in nums])

friends = ["ashley", "matt", "michael"]

friends_cap = [friend[0].upper()+friend[1:] for friend in friends]
friends_cap2 = [friend.capitalize() for friend in friends]
print(friends_cap)
print(friends_cap2)

numbers = [1,2,3,4,5,6]

evens = [num for num in numbers if num % 2 == 0]
print(evens)

with_else = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(with_else)

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
[[print(val) for val in l] for l in nested_list]

for l in nested_list:
    for val in l:
        print(val)