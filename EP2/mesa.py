import config


'''Tenho que comparar a Lista do value do dicionario com as keys que estao envolta
Tenho que transformar as keys em uma tuple'''
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
	lista = []
	for i in range(len(dic.keys())):
		for key, values in dic.items():	
			if lista == []:
				lista.append(key)
				break
			if key in lista:
				continue
			if lista[-1] in values:
				lista.append(key)
				break
	if len(lista) == len(dic.keys()):
		return lista
	else:
		return False


