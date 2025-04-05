string_sample = "Hello world world"
                #0123456789
                         #-4-3-2-1
string_sample2 = "first letteR is lowErcase. new SENTENCE"
string_sample3 = "  !!**   extra whitespace string  **  "
german_sample = "der Fluß"

print(string_sample.upper())
print('a' > '[')

print(german_sample.lower())
print(german_sample.casefold())

print(string_sample2.capitalize())
print(string_sample2.title())

print(string_sample3.strip(' *!e'))
print(string_sample3.lstrip())
print(string_sample3.rstrip())

print(string_sample.replace('world', 'planet', 1))
print(string_sample.replace(' ', ''))

print(string_sample.count('world', 7, 12))
print(string_sample.find('world', 7, 12))

txt = "banana"

x = txt.center(20)

print(x)


# [start:end:step]
# print(string_sample[0])
# print(string_sample[-1])
# print(string_sample[4:13])
# print(string_sample[-8:-2])
# print(string_sample[6:])
# print(string_sample[::-1])



# print(len('a\n\'bc'))

# example = 'that\'s'
# example2 = "my favourite book is \"Metro 2033\""
# example = "\\"
# print(example)
#
# print('Hello\n\tWorld')



# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-8'))
# print('hello world'.encode('utf-16'))

# print('123123123123123'.zfill(10))

print('Hello' + ' ' + 'World', end='')
print('Hello', 123, True, sep=', ')

name = 'John'
salary = 2000
string = '{0}\'s salary is {1:.2f}. {0} is good worker.'
print(string.format(name, salary))

p = 'computer'
pr = 1200
string = 'This {product} costs {price:.2f}$.'
print(string.format(price=pr, product=p))

x = f'This is {name.upper()}. His salary is {salary}.'
print(x)
print(r'\user\new_folder\image.png')

# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500
#
# emp_string = ('Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f'
#               % {'name': emp_name, 'salary': emp_salary, 'age': emp_age})
# print(emp_string)


