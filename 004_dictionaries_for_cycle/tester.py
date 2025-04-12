# # # # for num in range(100):
# # # #     print(num ** 4)
# # #
# # #
# # # # a = [1, 2, 3, 4, 5, 6]
# # # # b = ['A', 'B', 'C', 'D', 'E', 'F']
# # # #
# # # # for index in range(len(a)):
# # # #     print(a[index], b[index])
# # #
# # # # for num in a:
# # # #     for letter in b:
# # # #         print(num, letter)
# # #
# # # # for num1 in range(10):  # loops 10 times
# # # #     for num2 in range(10):  # loops 10 * 10 = 100
# # # #         for num3 in range(10):  # loops 10 * 10 * 10 = 1000
# # # #             print(num1, num2, num3)
# # # #
# # # # num = 10
# # # #
# # # # for num in range(10):
# # # #     print(num)
# # # #
# # # # print('NUM', num)
# # #
# # # people = [
# # #     ('Jack', 'Smith', 2000, 'm'),
# # #     ('Sarah', 'Gold', 2500, 'f'),
# # #     ('Bob', 'Summer', 3000, 'm'),
# # #     ('Jane', 'Green', 5000, 'f'),
# # #     ('Simon', 'Bold', 2000, '')
# # # ]
# # # #
# # # for first_name, last_name, salary, gender in people:
# # #     gender_pronounce = ''
# # #     if gender == 'm':
# # #         gender_pronounce = 'his'
# # #     elif gender == 'f':
# # #         gender_pronounce = 'her'
# # #     print(f'This is {first_name} {last_name}. {gender_pronounce.title()} salary is {salary:.2f}$')
# #
# #
# # # x = -49
# # # if x > 0:
# # #     print('X is positive')
# # # if x > 50:
# # #     print('X is half way to a 100')
# # # if x == 100:
# # #     print('X is 100')
# #
# # # idcode = '38803160272a'
# # #
# # # if len(idcode) == 11 and idcode.isdecimal():
# # #     print(idcode, 'correct')
# # # else:
# # #     if len(idcode) > 11:
# # #         print('Code is too long')
# # #     elif len(idcode) < 11:
# # #         print('Code is too short')
# # #     if not idcode.isdecimal():
# # #         print('Code is not all numeric')
# #
# # # if len(idcode) == 11 and idcode.isdecimal():
# # #     print(idcode, 'correct')
# # # elif not idcode.isdecimal():
# # #     print('Code is not all numeric')
# # # elif len(idcode) > 11:
# # #     print('Code is too long')
# # # elif len(idcode) < 11:
# # #     print('Code is too short')
# #
# #
# # # if len(idcode) == 11:
# # #     if idcode.isdecimal():
# # #         print(idcode, 'correct')
# # #     else:
# # #         print('Code is not all numeric')
# # # elif len(idcode) > 11:
# # #     print('Code is too long')
# # # else:
# # #     print('Code is too short')
# #
# #
# # # name = input('Enter name: ')
# # # if name.isalpha():
# # #     print(f'Hello {name}!')
# # # else:
# # #     print('Hello stranger!')
# #
# # # For range of numbers from 1 to 100
# # # If number divided by 3 has no remainder print number and FIZZ
# # # If number divided by 5 has no remainder print number and BUZZ
# # # If number divided by both 3 and 5 has no remainder print number and FIZZBUZZ
# #
# # # for num in range(0, 101):
# # #     if num % 3 == 0 and num % 5 == 0:
# # #         print(num, 'FIZZBUZZ')
# # #     elif num % 3 == 0:
# # #         print(num, 'FIZZ')
# # #     elif num % 5 == 0:
# # #         print(num, 'BUZZ')
# # #
# #
# # # empty = {}
# # # empty = dict()
# #
# # # random_dict = {
# # #     'first_name': 'Jack',
# # #     1: 'integer key',
# # #     0.42: 'float key',
# # #     (1, 2, 3): 'tuple key',
# # #     True: 'bool key'
# # # }
# #
# # # print(random_dict)
# #
person = {
    'first_name': 'Jack',
    'last_name': 'Smith',
    'information': {
        'eye_color': 'blue',
        'height': 168,
        'weight': 100,
    },
    'clothes': [
        'jeans',
        't-shirt',
        'shoes',
        'jacket',
    ]
}
# # people = [
# # {
# #     'first_name': 'Jack',
# #     'last_name': 'Smith',
# #     'information': {
# #         'eye_color': 'blue',
# #         'height': 168,
# #         'weight': 100,
# #     },
# #     'clothes': [
# #         'jeans',
# #         't-shirt',
# #         'shoes',
# #         'jacket',
# #     ]
# # },
# # {
# #     'first_name': 'Jack',
# #     'last_name': 'Smith',
# #     'information': {
# #         'eye_color': 'blue',
# #         'height': 168,
# #         'weight': 100,
# #     },
# #     'clothes': [
# #         'jeans',
# #         't-shirt',
# #         'shoes',
# #         'jacket',
# #     ]
# # },
# # {
# #     'first_name': 'Jack',
# #     'last_name': 'Smith',
# #     'information': {
# #         'eye_color': 'blue',
# #         'height': 168,
# #         'weight': 100,
# #     },
# #     'clothes': [
# #         'jeans',
# #         't-shirt',
# #         'shoes',
# #         'jacket',
# #     ]
# # }
# # ]
# #
# # print(person.get('information'))
# # print(person.get('information').get('eye_color'))
# # print(person['information']['eye_color'])
# # print(person['clothes'][2])
# #
#
# person = {
#     'first_name': 'Jack',
#     'last_name': 'Smith',
# }
#
# person['first_name'] = 'Bob'
# person['phone'] = '555-555-5555'
# person.update({'phone': '444-444-4444', 'salary': 2000})
# del person['phone']
# # print(person.pop('salary'))
# # print(person.popitem())
#
#
# # x = {}
# # for num in range(100):
# #     x[num] = num ** 2
# #
# # print(x)


# my_car = {
#     'make': 'Honda',
#     'model': 'Civic',
#     'info': {
#         'color': 'red',
#         'mileage': 12313
#     }
# }
#
# my_other_car = my_car.copy()
#
# my_car['info']['color'] = 'BMW'
# print(my_other_car)

# person = {
#     'first_name': 'Jack',
#     'last_name': 'Smith',
#     'age': 18,
# }

# for x in person:
#     print(person[x])

# print(person.keys())
# print(person.values())
# print(person.items())
#
# for x in person.items():
#     print(x)
#
# if 'Jack' in person.values():
#     print('YES')


x = [('one', 1), ('two', 2) ]
print(dict(x))