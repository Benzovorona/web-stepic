data = {'a': ['1', '2'], 'b': ['3']}
d =''
for key in data.keys():
	for i in range(len(data[key])):
		d+=key+':'+str(i)+'\n'
print(d)
