# while True:
#     try:
#         number = float(input('Enter number: '))
#     except:
#         print('The value entered is not numeric')
#     else:
#         print(number)
#     finally:
#         print('One more time')
#
#     print('ONE MORE TIME')

# while True:
#     try:
#         number = float(input('Enter number: '))
#     except:
#         print('The value entered is not numeric')
#         continue
#     print(number)
#     break


# for letter in 'python':
#     if letter == 'h':
#         continue
#     if letter == 'p':
#         break
#     print(letter)

# while True:
#     try:
#         user_id = input('Please enter Estonian national id: ')
#         int(user_id)
#         if len(user_id) != 11:
#             raise Exception
#     except ValueError:
#         print('Code you entered is not numeric.')
#         continue
#     except Exception:
#         if len(user_id) > 11:
#             print('TOO LONG')
#         else:
#             print('TOO SHORT')
#         continue
#     print(user_id, 'CORRECT')
#     break

# a = [1, 2, 3]
# b = ['a', 'b', 'c']
#
# # zipped = list(zip(a, b, 'asdeasdasd', {1, 2, 3, 4, 5}, a, a, a))
# #
# # print(zipped)
# # for pair in zipped:
# #     print(pair)
#
# zipped = list(zip(a, b))
# print(zipped)
# nums, letters = zip(*zipped)
# print(nums)
# print(letters)


# x = [1, 2, 3, 4, 5, 6]
# # print(*x)
# # print(x[0], x[1], x[2], x[3], x[4], x[5])
# first, *rest, last = x
# print(first, rest, last)


# def square_list(numbers):
#     squares = []
#     for num in numbers:
#         squares.append(num ** 2)
#     return squares
#
#
# print(square_list([1, 2, 3, 4, 5, 6, 7]))

# def filter_evens(numbers):
#     evens = []
#     for num in numbers:
#         if num % 2 == 0:
#             evens.append(num)
#     return evens
#
#
# print(filter_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# nums = [123, 432, 232, 5231, 123, 2332, 65234, 98899]
#
#
# def filter_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#
#
# # even_numbers = filter(filter_even, nums)
# even_numbers = filter(lambda num: num % 2 == 0, nums)
# print(even_numbers)
# print(list(even_numbers))
# print(nums)

# people = [
#     {
#         'name': 'Jack',
#         'surname': 'Smith',
#         'age': 17
#     },
#     {
#         'name': 'Sarah',
#         'surname': 'Gold',
#         'age': 25
#     },
#     {
#         'name': 'Bob',
#         'surname': 'Summers',
#         'age': 45
#     },
#     {
#         'name': 'Mary',
#         'surname': 'Green',
#         'age': 15
#     },
# ]
#
# modded_people = list(map(lambda person: {f'{person["name"]}': person['age']}, people))
# print(modded_people)
# filtered_people = filter(lambda person: person['age'] >= 18, people)
# print(list(filtered_people))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# squares = list(map(lambda num: num ** 2, numbers))
#
# print(squares)
#
#
# cities = ['london', 'tallinn', 'berlin', 'stockholm', 'helsinki']
#
# upper_cities = list(map(str.title, cities))
#
# print(upper_cities)

# a = [1, 2, 3]
# b = [4, 5, 6]
#
# multiplied = list(map(lambda x, y: x * y, a, b))
# print(multiplied)

numbers = [1, 2, 3, 4, 5, 6]
# squares = [num ** 2 for num in numbers]
# print(squares)
# # squares = []
# # for num in numbers:
# #     squares.append(num ** 2)
# #
# # print(squares)
#
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
#
# labels = [f'{num} even' if num % 2 == 0 else f'{num} odd' for num in numbers]
# print(labels)
#
# x = [1, 2, 3]
# y = ['a', 'b', 'c']
# pairs = [(a, b) for a in x for b in y]
# print(pairs)
#
# p = []
# for a in x:
#     for b in y:
#         p.append((a, b))
# print(p)


# def square(num):
#     return num ** 2
#
#
# squared = [square(n) for n in numbers]
# print(squared)
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# summed = [x + y for x, y in zip(a, b)]
# print(summed)

# squared_dict = {num: num ** 2 for num in numbers}
# print(squared_dict)
#
# numbers = [1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)

# import questionary
#
# first_name = questionary.text('What is your name?').ask()
# print(first_name)