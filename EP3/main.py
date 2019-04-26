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

def listGenerate(linha):
    grupo, grupos = [], []
    for palavra in range(len(linha)):
        for letra in range(len(linha[palavra])):
            if linha[palavra][letra] == '1':
                grupo.append([palavra,letra])
                try:
                    if linha[palavra][letra-1] == '1':
                        grupo.append([palavra,letra-1])
                    if linha[palavra-1][letra] == '1':
                        grupo.append([palavra-1,letra])
                    grupos.append(grupo)
                    grupo = []
                except IndexError:
                    break
    print(grupos) 
    return grupos

def merge(grupos):
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
    return grupos

def removeDuplicated(grupos):
    mapa = []
    for j in range(len(grupos)):
        if grupos[j] != []:
            grupos[j].sort()
            temp = [ grupos[j][i] for i in range(len( grupos[j])) if i == 0 or  grupos[j][i] !=  grupos[j][i-1]]
            mapa.append(temp)
    return mapa
def newPrint(linha,mapa):
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

def main(linha):
    grupos = listGenerate(linha)
    gruposOrdenados = merge(grupos)
    gruposOrdenados = removeDuplicated(gruposOrdenados)
    newPrint(linha,gruposOrdenados)

main(linha)