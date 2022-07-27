# 'add',
new_set = {'str', 'set', 'dir'}
new_set.add('int')
# 'clear',
new_set.clear()
# 'copy',
original_set = {'str', 'set', 'dir'}
new_set = original_set.copy()
# 'difference',
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'}
result_set = other_set.difference(new_set)
# 'difference_update',
result_set = other_set.difference_update(new_set)
# 'discard',
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'}
other_set.discard('str')
# 'intersection',
original_set = {'str', 'set', 'dir'}
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'}
new_set = other_set.intersection(original_set)
# 'intersection_update',
original_set = {'str', 'set', 'dir'}
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'}
other_set.intersection_update(original_set)
# 'isdisjoint',
original_set = {'str', 'set', 'dir'}
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'}
new_set = other_set.isdisjoint(original_set)
# 'issubset',
original_set = {'str', 'set', 'dir'}
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'} #False
new_set = other_set.issubset(original_set) #False
new_set1 = original_set.issubset(other_set) #True
# 'issuperset',
original_set = {'str', 'set', 'dir'}
other_set = {'str', 'set', 'dir', 'wheel', 'glass', 'accelerator'} #False
new_set = other_set.issuperset(original_set) #True
new_set1 = original_set.issuperset(other_set) #TrueFalse
# 'pop', delete any object
original_set = {'str', 'set', 'dir'}
pop_element = original_set.pop()
# 'remove',
original_set = {'str', 'set', 'dir'}
original_set.remove('set')
# 'symmetric_difference',
original_set = {'str', 'accelerator', 'dir'}
other_set = {'str', 'set', 'wheel', 'glass'}
new_set = original_set.symmetric_difference(other_set)
# 'symmetric_difference_update',
original_set = {'str', 'accelerator', 'dir'}
other_set = {'str', 'set', 'wheel', 'glass'}
original_set.symmetric_difference_update(other_set)
# 'union',
original_set = {'str', 'accelerator', 'dir'}
other_set = {'str', 'set', 'wheel', 'glass'}
new_set = original_set.union(other_set)
# 'update'
original_set = {'str', 'accelerator', 'dir'}
other_set = {'str', 'set', 'wheel', 'glass'}
original_set.update(other_set)