#Accessing elements specifically

my_list = [0, 'Sahil', 4, 6, 8, 10]
print(my_list[ : 2])
print(my_list[: 5])
print(my_list)

#Adding elements at the end of the list using append function

my_list.append('MD Irshad')
print("List after adding a new element using (.append) function", my_list)

position = 3
new_element = 'Rachit Sharma'

# Inserting the elements at a specific position

my_list.insert(position, new_element)
print("List after the insertion of the new element at a specific index", my_list)

new_list = [8, 2, 5, 6, 1, 3, 4, 7, 9, 10, 0]
new_list.sort()
print("Sorted Tuple: ",new_list)
length = new_list.__len__()
print("Length of the string: ",length)
