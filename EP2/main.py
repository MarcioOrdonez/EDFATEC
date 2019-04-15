import casamento
import mesa
def main():
	pretendentes = casamento.makeDict()
	pretendentes = casamento.ordenateDict(pretendentes)
	casamentoPossivel = casamento.generateCombinations(pretendentes)
	cavaleiros = mesa.makeDict()
	cavaleiros = mesa.ordenateDict(cavaleiros)
	cavaleiros = mesa.generateCombinations(cavaleiros)
	flag = True
	solteiras = []
	for (key, value) in casamentoPossivel.items():
		if value == '':
			solteiras.append(key)
			flag = False
			break
	if flag:
		print('Casamento possível: ', casamentoPossivel)
	else:
	 	print('Casamento impossível, solteiras: ', solteiras)
	if cavaleiros:
	 	print('Mesa ',cavaleiros)
	else:
	 	print('Não é possivel arrumar mesa')

main()
