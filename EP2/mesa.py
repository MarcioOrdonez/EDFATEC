import config

def makeDict():
	dic = {}
	with open(config.config.mesaFile,'r') as file:
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
	mesa = []
	for i in range(len(dic.keys())):
		for cavaleiros, amigos in dic.items():	
			if mesa == []:
				mesa.append(cavaleiros)
				break
			if cavaleiros in mesa:
				continue
			if mesa[-1] in amigos:
				mesa.append(cavaleiros)
				break
	if len(mesa) == len(dic.keys()):
		return mesa
	else:
		return False


