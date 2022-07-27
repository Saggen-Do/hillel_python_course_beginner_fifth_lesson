list_of_methods: str = dir(set)
i=0
while i!= len(list_of_methods):
    if list_of_methods[i][0] == '_':
        list_of_methods.pop(i)
    else:
        i+=1
print(list_of_methods)