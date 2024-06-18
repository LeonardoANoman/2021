# {_ : _ for _ in}

numbers = dict(first=1, second=2, thrid=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers)

num_list = [1,2,3,4]

comp = { num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(comp)