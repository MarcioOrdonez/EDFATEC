import time
import random


def generateList(times):
	n=2000*times
	lista = list(range(0,n))
	random.shuffle(lista)
	return lista

def selection(lista):
	menor = 10000000000000
	indice = 0
	for i in range(len(lista)):
		for j in range(i,len(lista)):
			if menor > lista[j]:
				menor = lista[j]
				indice = j
		lista[indice] = lista[i]
		lista[i] = menor
		menor = 10000000000000
	
def merge(listaE, listaD):
    indexE, indexD = 0, 0
    lista = []
    while indexE < len(listaE) and indexD < len(listaD):
        if listaE[indexE] < listaD[indexD]:
            lista.append(listaE[indexE])
            indexE += 1
        else:
            lista.append(listaD[indexD])
            indexD += 1
    lista += listaE[indexE:]
    lista += listaD[indexD:]
    return lista

def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    metade = len(lista) // 2
    listaE = mergeSort(lista[:metade])
    listaD = mergeSort(lista[metade:])

    return merge(listaE, listaD)

def quicksort(lista):
	if len(lista)<=1:
		return lista
	pivo = lista[0]
	iguais = [x for x in lista if x == pivo]
	menores = [x for x in lista if x< pivo]
	maiores = [x for x in lista if x > pivo]
	return quicksort(menores) + \
		iguais + quicksort(maiores)			

def header():
	print('''--------------------------------------------------------------------------------------
	  |                             TEMPO(s)                                     |
	  |MergeSort            QuickSort            Slection            Native      |
--------------------------------------------------------------------------------------''')

def telaDeSaida(lista):
	
	inicio = time.time()
	sorted(lista)
	fim = time.time()
	nat = fim-inicio
	
	inicio = time.time()
	mergeSort(lista)
	fim = time.time()
	merge = fim-inicio
	
	inicio = time.time()
	quicksort(lista)
	fim = time.time()
	quick = fim-inicio
	
	inicio = time.time()
	selection(lista)
	fim = time.time()
	selecao = fim-inicio
	
	saida = "%.2f                 %.2f                 %.2f                %.2f        |" % (merge, quick, selecao, nat)
	if selecao > 10:
		saida = "%.2f                 %.2f                 %.2f               %.2f        |" % (merge, quick, selecao, nat)
	if selecao > 30 or merge > 30 or quick > 30 or nat > 30:
		return saida, 1
	else:
		return saida, 0

def contador(n):
	saida, valida = telaDeSaida(generateList(n))
	tam = n*2000
	tam = str(tam)
	if(len(tam)==4):
		print("%s      |" % (tam)+''.join(saida))
	else:
		print("%s     |" % (tam)+''.join(saida))
	return valida

def footer():
	print('''--------------------------------------------------------------------------------------''')
def main():
	header()
	valida = 0
	n = 0
	while(valida == 0):
		n = n + 1
		valida = contador(n)
	footer()

main()
