my_dict = {
    'name': 'Bayel',
    'age': 20,
}


print(my_dict)
print(my_dict['name'])

try:
    print(my_dict['height'])

except:
    print('error')

my_dict['new_value'] = 'Nurash'
del my_dict["age"]
print(my_dict)

my_set={1,2,3,4,5,6,2,3,4,5}
print(my_set)
list_=[7,8]
print(set(list_))
print(my_set.discard(2))
print(my_set)
