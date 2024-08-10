def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a='hello')
print_params(c=False)
print_params(b=25, c=[1,2,3])

value_list = ['Hello', 254, False]
value_dict = {'a': 500, 'b': True, 'c': 'Bye'}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [100, 'Day']
print_params(*value_list_2, False)
