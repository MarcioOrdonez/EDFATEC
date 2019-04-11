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

def generateCombinations(dic):
	#dic = ordenateDict(makeDict())
	casal = {}
	homem_casado = []
	for mulher, homem_lista in dic.items():
		for homem in homem_lista:
			if homem not in homem_casado:
				pretendente = homem
				break
			pretendente = ''
			continue
		homem_casado.append(pretendente)
		casal[mulher] = pretendente
	return casal