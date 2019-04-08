import config
def makeDict():
	dic = {}
	with open(config.config.casamentoFile,'r') as file:
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

def generateCombinations():
	dic = ordenateDict(makeDict())
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
	return newDic