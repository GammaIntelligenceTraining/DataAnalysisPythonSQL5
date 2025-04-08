# empty = []  # List (list)
# empty = list()
# print(type(empty))
# print(bool(empty))

# not_empty = [123, 0.323, False, None, 'Hello world!', [1, 2, 3, [4, 5, 6], 7, 8], False]
# print(len(not_empty))
#
# print(not_empty[5][3][1])
# print(not_empty[2:6])
# print(not_empty[1:2])


# *a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print('A', a)
# print('B', b)
# print('C', c)

#
# courses = ['Math', 'Art', 'English', 'Programming', 'History']
#
# # courses[0] = 'Physics'
# # courses[0:2] = ['Math', 'Estonian', 'Literature']
# courses[0] = ['Math', 'Estonian']
# print(courses)

# courses = ['Math', 'Art', 'English', 'Programming', 'History', 'physics', 'Art', '123', '45', '234']
# courses = [1, 2, 6, 3, 8, 4, 0.3, 2.34, -23]
# courses = [[1, 4], [3, 2], [2, 6]]


# courses.append('Physics')
# courses.append('Physics')
# print(courses[3])
# courses.insert(0, 'Music')
# print(courses[3])
# courses.append(['Music', 'Science'])
# courses.extend(['Music', 'Science'])
# print(courses)

# print([1, 2, 3] + [4, 5, 6])
# print([1, 2, 3] * 5)

# courses.remove('Art')
# print(courses[3])
# print(courses.pop(0))
# print(courses[3])
# print(courses)
# print(deleted)

# courses.reverse()
# print(courses[::-1])
# courses.sort()
# print(sorted(courses, reverse=True))
# print(courses)

# print(courses.count('Art'))
# print(courses.index('History', 3, 6))

# text = 'These       words will, be splitted to a list soon!'
# lst = text.split()
# print(lst)
# new_text = ' '.join(lst)
# print(new_text)
#
# print(str([1, 2, 3, 4, 5]))
# print(list('hello'))

# a = 5
# b = a
# a += 5
# print('A', a)
# print('B', b)

# a = 'Hello'
# b = a
# a += ' World'
# print('A', a)
# print('B', b)

# a = [1, 2, 3, 4]
# print(id(a))
# b = a.copy()
# print(id(b))
# a.append(0)
# b.append(5)
# print('A', a)
# print('B', b)

# lst = [1, 2, 3, 4, 5, 6, 7, 7]
# print(sum(lst))
# lst = ['Art', 'Math', 'Physics', '123', 'art']
# print(min(lst))
# print(max(lst))

# empty = ()  # Tuple (tuple)
# print(type(empty))
# print(type((2,)))

# tpl = (1, 2, 3, 4, 5, 6, 7)
# # print((1, 2, 3) + (4, 5, 6))
# print(id(tpl))
# tpl = list(tpl)
# print(id(tpl))
# tpl[0] = 0
# tpl = tuple(tpl)
# print(id(tpl))
# print(tpl)
#
# x = [1, 2, 3, 4, 5, 6]
# print(id(x))
# x[0] = 0
# print(id(x))

# empty = set()  # Set (set)
# print(type(empty))

# st = {'Math', 'Physics', 'Programming', 'Math'}
# print(st)
#
# x = {1, 4, 2, 5, 6, 8, 65, 34, 23, -23, -45}
# print(x)

# x = ['Art', 'Physics', 'History']
# x = list(set(x))
# print(x)

# set1 = {'Math', 'Art', 'Physics', 'History'}
# set2 = {'Math', 'Physics', 'English', 'Programming'}
#
# print(set1.intersection(set2))
#
# print(set1.difference(set2))
# print(set2.difference(set1))
#
# print(set1.symmetric_difference(set2))
#
# print(set1 & set2)
# set1.symmetric_difference_update(set2)
# print(set1)

# x = [1, 2, 3, 4, 5]
# for num in x:
#     print(num ** 2)
#
# print('Good bye')

