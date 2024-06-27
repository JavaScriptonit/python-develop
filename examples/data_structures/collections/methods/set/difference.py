# https://www.w3schools.com/python/ref_set_difference.asp

langs = {'js', 'c', 'go', 'python', 'java'}
skills = {'python','bash','ansible','terraform'}

result = skills.difference(langs)

print(result) # {'python'} - Return a set that contains the items that only exist in set langs, and set skills