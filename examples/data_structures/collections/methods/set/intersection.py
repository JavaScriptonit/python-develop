# https://www.w3schools.com/python/ref_set_intersection.asp

langs = {'js', 'c', 'go', 'python', 'java'}
skills = {'python','bash','ansible','terraform'}

result = skills.intersection(langs)

print(result) # {'python'} - Return a set that contains the items that exist in both set langs, and set skills