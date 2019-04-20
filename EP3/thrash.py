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

grupos = []
grupo = []
lista = []
mapa = []
temp = []
flag = False
for palavra in range(len(linha)-1):
    for letra in range(len(linha[palavra])-1):
        if linha[palavra][letra] == '1':
            grupo.append([palavra,letra])
            if linha[palavra][letra+1] == '1':
                grupo.append([palavra,letra+1])
            if linha[palavra+1][letra] == '1':
                grupo.append([palavra+1,letra])
            grupos.append(grupo)
            grupo = []
for p in grupos:
    for i in range(len(grupos)):
        flag = False
        for j in range(len(grupos[i])):
            for m in range(len(grupos)):
                if grupos[i] != grupos[m]:
                    if grupos[i][j] in grupos[m]:
                        for elementos in grupos[m]:
                            grupos[i].append(elementos)
                        grupos[m] = []
                        flag = True
        if flag:
            break

for j in range(len(grupos)):
    if grupos[j] != []:
        grupos[j].sort()
        temp = [ grupos[j][i] for i in range(len( grupos[j])) if i == 0 or  grupos[j][i] !=  grupos[j][i-1]]
        mapa.append(temp)
#mapa = [[[0, 2], [0, 3], [1, 1], [1, 2], [2, 2], [2, 3]], [[0, 6], [0, 8], [1, 6], [1, 8], [2, 6], [2, 7], [2, 8]],[[4, 2], [5, 2], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [7, 2], [8, 2]], [[4, 6], [5, 5], [5, 6], [5, 7], [4, 8], [5, 7], [5, 8], [5, 9]], [[7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]]
for i in range(len(linha)):
    for j in range(len(linha[i])):
        flag = False
        for x in range(len(mapa)):
            if [i,j] in mapa[x]:
                print(x+1,end='')
                flag = True
                break
        if flag == False:
            print(linha[i][j],end='')
    print('\n',end='')


#print(mapa)
#print(linha)
[[[0, 2], [0, 3], [1, 2]], [[0, 3]], [[0, 6], [1, 6]]
, [[0, 8], [1, 8]], [[1, 1], [1, 2]], [[1, 2], [2, 2]]
, [[1, 6], [2, 6]], [[1, 8], [2, 8]], [[2, 2], [2, 3]]
, [[2, 3]], [[2, 6], [2, 7]], [[2, 7], [2, 8]], [[2, 8]]
, [[4, 2], [5, 2]], [[4, 6], [5, 6]], [[4, 8], [5, 8]]
, [[5, 2], [6, 2]], [[5, 5], [5, 6]], [[5, 6], [5, 7]]
, [[5, 7], [5, 8]], [[5, 8], [5, 9]], [[6, 0], [6, 1]]
, [[6, 1], [6, 2]], [[6, 2], [6, 3], [7, 2]], [[6, 3]
, [6, 4]], [[6, 4]], [[7, 2], [8, 2]], [[7, 6], [7, 7]
, [8, 6]], [[7, 7], [7, 8], [8, 7]], [[7, 8], [8, 8]]]




'''
[[[0, 2], [0, 3], [1, 1], [1, 2], [2, 2]
, [2, 3]], [[0, 6], [0, 8], [1, 6], [1, 8]
, [2, 6], [2, 7], [2, 8]], [[4, 6], [5, 5]
, [5, 6], [5, 7], [4, 8], [5, 7], [5, 8]
, [5, 9]], [[4, 2], [5, 2], [6, 0], [6, 1]
, [6, 2], [6, 3], [6, 4], [7, 2], [8, 2]]
, [[7, 6], [7, 7], [7, 8], [8, 6], [8, 7]
, [8, 8]]]


'''

# for i in range(len(grupos)):
#     for j in range(len(grupos[i])):
#         lista = [grupos[k] for k in range(len(grupos)) if grupos[i][j] in grupos[k]]
#         grupo.append(lista)


# for i in range(len(grupos)):
#     for j in range(len(grupos[i])):
#         for k in range(i+1,len(grupos)):
#             if grupos[i][j] in grupos[k]:
#                 #print(grupos)
#                 #grupos[i].extend(grupos[k])
#                 lista.append([grupos[i],grupos[k]])
#         grupo.append(lista)
#         lista = []

#print(grupos)
'''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110
'''
'''
for i in range(1,len(fragmento)//2):
    objeto[i] = []
    for xy in fragmento:
        if xy not in check:
            if objeto[i] == []:
                objeto[i].append(xy)
                check.append(xy)
                continue
            for pares in fragmento:
                if pares not in check:
                    if (xy[0] == pares[0]+1 or xy[0] == xy[0-1]) and xy[1] == pares[1]:
                        objeto[i].append(pares)
                        check.append(pares)
                        continue
                    if xy[0] == pares[0] and (xy[1] == pares[1]-1 or xy[1] == pares[1]+1):
                        objeto[i].append(pares)
                        check.append(pares)
                        continue'''