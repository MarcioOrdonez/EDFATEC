def makeDict():
	dic = {}
	with open('casamento.txt','r') as file:
		for line in file:
			for index, word in enumerate(line.split(" ")):
				if index == 0:
					key = word.replace('\n','')
					continue
				else:
					value = word.replace('\n','')
				try:
					dic[key].append(value)
				except KeyError:
					dic[key] = [value]
	return dic

def ordenateDict(dic):
	newd = dict(sorted(dic.items(), key = lambda item : len(item[1])))
	return newd

def generateCombinations(dic):
	for names in dic.keys:
		
print(ordenateDict(makeDict()))
			





#	for names in dic.values():
#		for name in names:
#			print(name)
