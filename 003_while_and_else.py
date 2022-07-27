initial_list: list = [2, 24, 45, 2, 65, 758, 3, 7, 9, 46, 87, 92, 100]
even = True
for item in initial_list:
    if item % 2 != 0:
        even = False
        break
if even == True:
    print("All numbers are even" )
else:
    print('NO')
