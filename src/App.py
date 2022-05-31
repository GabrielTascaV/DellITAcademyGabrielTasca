import csv


#Função para consulta de medicamento por nome e comercializados em 2020
def consulta_nome(data_set,nome):
    dados = []
    #Adiciona na variavel dados se o campo COMERCIALIZAÇÃO 2020 for sim e o nome for igual a coluna PRODUTO
    for i in data_set:
        if(i[7] == 'Sim' and i[2] == nome.upper()):
            dados.append(i)
    #Retorna a variável dados com os medicamento que foram encontrados
    print("Resultado: ")
    for i in range(len(dados)):
        print(dados[i])
    return dados


#Função para consulta de medicamento por código de barras 
def consulta_codigo_barras(data_set,codigo_barras):
    #Cria o valor máximo float e valor mínimo floaT
    cont_max = -float('inf')
    cont_min = float('inf')
    max = 0
    min = 0
    obj = 0
    for i in data_set:
        if(i[1] == codigo_barras):
            obj = i
            if(i[5] == ''):
                print("Valor nulo na tabela. Substituído por 0.")
                obj[5] = '0'
            pmc0 = float(obj[5].replace(',','.'))
            if(pmc0 > cont_max):
                max = pmc0
            if(pmc0 < cont_min):
                min = pmc0
            break
    for k in data_set:
        if(k[2] == obj[2]):
            if(k[5] == ''):
                print("Valor nulo na tabela. Substituído por 0.")
                k[5] = '0'
            pmc0 = float(k[5].replace(',','.'))
            if(pmc0 > max):
                max = pmc0
            if(pmc0 < min):
                min = pmc0
    dif = max - min
    print("Resultado: ")
    print('Valor Máximo: %.2f' %max)
    print('Valor Mínimo: %.2f' %min)
    print('Diferença: %.2f' %dif)
    return 0

#Função para ver a porcentagem da lista de concessão de crédito tributário
def consulta_lista_concessao(data_set):
    cont_negativa, cont_neutra, cont_total, cont_positiva = 0, 0, 0, 0
    for i in data_set:
        if(i[7] == 'Sim'):
            cont_total += 1
            if(i[6] == 'Negativa'):
                cont_negativa += 1
            elif(i[6] == 'Neutra'):
                cont_neutra += 1
            elif(i[6] == 'Positiva'):
                cont_positiva += 1
    cont_negativa /= cont_total/100
    cont_neutra /= cont_total/100
    cont_positiva /= cont_total/100

    s_cont_negativa = '%.2f' %cont_negativa
    s_cont_neutra = '%.2f' %cont_neutra
    s_cont_positiva = '%.2f' %cont_positiva
    print("Resultado: ")
    print('CLASSIFICAÇÃO    PERCENTUAL       GRÁFICO')
    print('Negativa         '+ s_cont_negativa + '%           ' + '*'*int(cont_negativa))
    print('Neutra           '+ s_cont_neutra   +'%            ' +  '*'*int(cont_neutra))
    print('Positiva         '+ s_cont_positiva +'%           ' + '*'*int(cont_positiva))
    return data_set


def ler_arquivo(dados,name): 
    try:
        with open(name) as arq:
            ler = csv.reader(arq,delimiter=";")
            string = ler.__next__()
            colunas = []
            cont = 0
            for i in string:
                if(i == 'APRESENTAÇÃO'):
                    colunas.append(cont)
                elif(i == 'SUBSTÂNCIA'):
                    colunas.append(cont)
                elif(i == 'PRODUTO'):
                    colunas.append(cont)
                elif(i == 'PF Sem Impostos'):
                    colunas.append(cont)
                elif(i == 'EAN 1'):
                    colunas.append(cont)
                elif(i == 'PMC 0%'):
                    colunas.append(cont)
                elif(i == 'LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)'):
                    colunas.append(cont)
                elif(i == 'COMERCIALIZAÇÃO 2020'):
                    colunas.append(cont)
                cont += 1
            for i in ler:
                obj = []
                for k in colunas:
                    obj.append(i[k])
                dados.append(obj)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return 0

data_set = []
data_set = ler_arquivo(data_set,'DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
out = False
while(not(out)):
    print("1 - Consulte medicamento por nome")
    print("2 - Consultar o preço máximo e mínimo por código de barras")
    print("3 - Consultar a Lista de Concessão de Crédito Tributário (PIS/COFINS)")
    print("0 - Sair do programa")
    print("DIGITE UM NÚMERO: ")
    option = input()
    if(option == '1'):
        print("Digite o nome do medicamento: ")
        nome = input()
        consulta_nome(data_set,nome)
        print("")
        print("")
        print("")
    elif(option == '2'):
        print("Digite o código de barras: ")
        codigo_barras = input()
        consulta_codigo_barras(data_set,codigo_barras)
        print("")
        print("")
        print("")
    elif(option == '3'):
        consulta_lista_concessao(data_set)
        print("")
        print("")
        print("")
    elif(option == '0'):
        out = True
    else:
        print("Erro, nenhum valor digitado. Digite um valor válido")
        print("")
        print("")
        print("")


