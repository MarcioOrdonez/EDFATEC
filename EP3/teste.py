imagem = '''0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''
linha = imagem.split('\n')

objeto = []
lista = {}
duplas = []
atual = []
cont = 1
xy = 0
for palavra in range(len(linha)):
    for letra in range(len(linha[palavra])):
        if linha[palavra][letra] == '1':
            objeto.append([palavra,letra])
for x in range(1,len(objeto)//2):
    lista[x] = []
    for i in range(len(objeto)):
        if lista[x] == []:
                lista[x].append(objeto.pop(i))
                cont+=1
        if lista[x] != []:
            while(i < cont):
            #for atual in lista[x]:
                if objeto != []:
                    tam = len(objeto)
                    #for xy in range(tam):
                    while(xy > tam):
                        if (lista[x][i][0] == objeto[xy][0]+1 or lista[x][i][0] == objeto[xy][0]-1) and lista[x][i][1] == objeto[xy][1]\
                            or lista[x][i][0] == objeto[xy][0] and (lista[x][i][1] == objeto[xy][1]-1 or lista[x][i][1] == objeto[xy][1]+1):
                            lista[x].append(objeto.pop(xy))
                            cont+=1
                            xy=0
                            break
                        xy+=1
                        
                i+=1



print(lista)


'''for x in range(1,len(objeto)//2):
    lista[x] = []
    for xy in range(len(objeto)):
        if lista[x] == []:
            lista[x] = objeto[xy]
            continue
        if lista[x][0] == objeto[xy][0] and lista[x][1] == objeto[xy][1]-1 or\
             lista[x][0] == objeto[xy][0]-1 and lista[x][1] == objeto[xy][1]:
             if objeto[xy] not in lista[x]:
                lista[x].append(objeto[xy])
'''