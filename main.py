x = "aabcccc"

count = {}
for each in x:
  if count.has_key(each):
    count[each] += 1
  else:
    count[each] = 1

for key in count:
  if count[key] >= 1:
    print str(count[key]) +  str(key)

print count
