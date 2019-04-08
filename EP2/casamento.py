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
	#newd = dic
	newd = dict(sorted(dic.items(), key = lambda item : len(item[1])))
	return newd

def generateCombinations(dic):
	newDic = {}
	newList = []
	for key,value in dic.items():
		for v in value:
			if v not in newList:
				temp = v
				break
			temp = ''
			continue
		newList.append(temp)
		newDic[key] = temp
	print(newList)
	return newDic
'''def generateCombinations(dic):
	newDic = {}
	newList = []
	for key,value in dic.items():
		for v in value:
			if v not in newDic:
				try:
					newDic[key].append(value)
				except KeyError:
					newDic[key] = [v]
				#newList.append(v)
				break
			continue
	return newDic'''






print(generateCombinations(ordenateDict(makeDict())))
#	for names in dic.values():
#		for name in names:
#			print(name)