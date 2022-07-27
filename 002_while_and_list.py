initial_list: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
removable_item: str = 'eg'
while removable_item in initial_list:
    initial_list.remove(removable_item)
print(initial_list)