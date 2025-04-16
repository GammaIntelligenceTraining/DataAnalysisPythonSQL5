# def say_hello(name):
#     # print('Hello stranger!')
#     return f'Hello {name}!'
#
#
# print(say_hello('Jack'))


# def rect_area(a: int | float, b: int | float) -> int | float:
#     return a * b
#
#
# print(rect_area('*', 20))

# def print_employee_message(employee, tax_rate):
#     print(f'Hello {employee['first_name']} {employee['last_name']}. '
#           f'Your salary before tax is {employee['salary'] * tax_rate:.2f}$.')
#
#
# person = {
#     'first_name': 'Jack',
#     'last_name': 'Smith',
#     'salary': 2500,
# }
# #
# # print_employee_message(person['first_name'], person['last_name'], person['salary'], 1.24)
# print_employee_message(person, 1.24)
# print_employee_message(person, 1.24)
# print_employee_message(person, 1.24)
# print_employee_message(person, 1.24)


# def filter_adult(ages):
#     adults = []
#     for age in ages:
#         if age >= 18:
#             adults.append(age)
#     return adults
#
#
# ages = [35, 12, 8, 45, 29, 31, 18, 5]
# print(filter_adult(ages))

# def is_adult(age):
#     if age < 0:
#         print('Wrong age!')
#         return
#     if age >= 18:
#         return True
#     return False
#
#
# print(is_adult(-12))

# def tester(a, b, *args, c=0, **kwargs):
#     print(a + b + c)
#     print(args)
#     print(kwargs)
#
#
# # print(tester(1, 2, 77, 4, 3, 2, 132, 'asdsa', True, c=123, name='Jack', surname="Smith", age=45))
# print(tester(b=10, a=20, c=100))

# def sum_everything(*numbers: int | float) -> int | float:
#     result = 0
#     for num in numbers:
#         result += num
#     return result
#
#
# print(sum_everything(123, 84, 32, 23, 543, 21332, 95, 23))
# import math
# math.sqrt()

# a, b, c = 1, 2, 3
#
#
# def sample():
#     global c, a, b
#     c = 100
#     a, b = 10, 20
#     print(a, b, c)
#
#
# sample()
# print(a, b, c)
#
# def area(a, b):
#     return a * b
#
#
# def count_order_material(order):
#     total = 0
#     for batch in order:
#         carpet_area = area(batch['width'], batch['height'])
#         total_material = carpet_area * batch['amount']
#         total += total_material
#     return total
#
#
# def print_results(order):
#     total_material = count_order_material(order)
#     print(f'Total material needed for order is {total_material} cm2.')
#
#
# order = [
#     {
#         'size': 'small',
#         'width': 30,
#         'height': 20,
#         'amount': 27
#     },
#     {
#         'size': 'medium',
#         'width': 50,
#         'height': 40,
#         'amount': 34
#     }
# ]
#
# print_results(order)

# import my_functions as helpers
# print(helpers.double(200))
# print(helpers.triple(200))

# from my_functions import double, triple
# print(double(12))

# def wrapper(fn):
#     print('Starting...')
#     fn()
#     print('Ending...')
#
#
# def say_hello(name):
#     print(f'Hello {name}!')
#
#
# wrapper(lambda: say_hello('Jack'))
# # wrapper(lambda: print('Hello world!'))
#
# # a = lambda a, b: a * b
# # print(a(20,30))

def sort_method(x):
    return x[1]


lst = [[4, 3], [5, 2], [1, 6], [3, 1], [2, 5]]
lst.sort(key=lambda x: x[1])
print(lst)
