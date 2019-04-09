import casamento
import mesa
def main():
	casamentoPossivel = casamento.generateCombinations()
	flag = True
	for (key, value) in casamentoPossivel.items():
		if value == '':
	 		flag = False
	 		break
	if flag:
	 	print('Casamento Possível:', casamentoPossivel)
	else:
	 	print('Casamento impossível')
	mesa.makeDict()

main()