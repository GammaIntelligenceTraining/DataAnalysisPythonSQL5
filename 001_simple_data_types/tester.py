# # age = 35  # Integer (int)
# # print(age)
# # print(type(age))
# #
# # height = 1.76  # Float (float)
# # print(height)
# # print(type(height))
#
# # result = (10 * 9) ** 2
# # print(result)
#
# # print(9 / 2)  # always returns float
# # print(9 // 0.2)  # always returns integer
# # print(9 % 2)  # 2 + 2 + 2 + 2 + 1
# # print(9 % 5)
# # print(81 ** 0.5)
#
# first_name = "123"  # String (str)
# print(first_name)
# print(type(first_name))
# # print(help(int))
#
# print("Hello" + "World")
# print('Hello' + str(123))
# print('*' * 30)
#
# is_popular = False  # Boolean (bool)
#
# nothing = None
#
# x = None
#
# print(bool(x))
#
#
# # print(int(x))
# # print(float(x))
# # # print(int(x))
# # print(type(x))
#
# # FALSE values
# integer = 0
# float_val = 0.0
# string = ""
# none_type = None

side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

semi_perimeter = (side_a + side_b + side_c) / 2

area = (semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) ** 0.5

print(area)
