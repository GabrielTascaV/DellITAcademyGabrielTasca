import csv

class Medicamento:
    def __init__(self,substancia,ean1,produto,apresentacao,pf_sem_impostos,pmc0,lista_concessao,comercializado_2020):
        self.substancia = substancia
        self.ean1 = ean1
        self.produto = produto
        self.apresentacao = apresentacao
        self.pf_sem_impostos = pf_sem_impostos
        self.pmc0 = pmc0
        self.lista_concessao = lista_concessao
        self.comercializado_2020 = comercializado_2020
    
    def ler_arquivo(name): 
        dados = []
        try:
            with open(name) as arq:
                #Le o arquivo csv
                ler = csv.reader(arq,delimiter=";")
                #Retira a primeira linha
                string = ler.__next__()
                colunas = []
                cont = 0
                #Acha o index dos campos necessários
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
                #Adiciona cada objeto numa lista
                for i in ler:
                    obj = []
                    for k in colunas:
                        obj.append(i[k])
                    m = Medicamento(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7])
                    dados.append(m)
            #Retorna o data_set
            return dados
        except FileNotFoundError:
            print("Arquivo não encontrado")
            return 0

    def consulta_nome(data_set,nome):
        if(len(data_set) == 0):
            print("Dados vazios")
            return 0
        dados = []
        #Adiciona na variavel dados se o campo COMERCIALIZAÇÃO 2020 for sim e o nome for igual a coluna PRODUTO
        for i in data_set:
            if(i.comercializado_2020 == 'Sim' and nome.upper() in i.produto):
                dados.append(i)
        #Caso não possua nenhum com o nome selecionado
        if(len(dados) == 0):
            print("Nenhum medicamento encontrado")
            return 0
        print("Resultado: ")
        for i in range(len(dados)):
            print(dados[i].toString_modificado())
        #Retorna a variável dados com os medicamento que foram encontrados
        return dados


    #Função para consulta de medicamento por código de barras 
    def consulta_codigo_barras(data_set,codigo_barras):
        if(len(data_set) == 0):
            print("Dados vazios")
            return 0
        #Cria o valor máximo float e valor mínimo floaT
        cont_max = -float('inf')
        cont_min = float('inf')
        max = 0
        min = 0
        obj = 0
        #Laço para achar o produto com o código de barras e colocar na variavel obj
        for i in data_set:
            if(i.ean1 == codigo_barras):
                obj = i
                if(i.pmc0 == ''):
                    print("Valor nulo na tabela. Substituído por 0.")
                    obj.pmc0 = '0'
                pmc0 = float(obj.pmc0.replace(',','.'))
                if(pmc0 > cont_max):
                    max = pmc0
                if(pmc0 < cont_min):
                    min = pmc0
                break
        
        if (obj == 0):
            print("Código de barras não encontrado")
            return 0
        lista_medicamento = []
        #Laço para achar os outros produtos com o mesmo nome e calcular o max e min 
        for k in data_set:
            if(k.produto == obj.produto):
                lista_medicamento.append(k)
                if(pmc0 == ''):
                    print("Valor nulo na tabela. Substituído por 0.")
                    pmc0 = '0'
                pmc0 = float(k.pmc0.replace(',','.'))
                if(pmc0 > max):
                    max = pmc0
                if(pmc0 < min):
                    min = pmc0
        #Calculo da diferença
        dif = max - min
        print("Registros: ")
        for j in lista_medicamento:
            print(j.toString())
        print(" ")
        print("Resultado: ")
        print('Valor Máximo: %.2f' %max)
        print('Valor Mínimo: %.2f' %min)
        print('Diferença: %.2f' %dif)
        return max,min,dif

    #Função para ver a porcentagem da lista de concessão de crédito tributário
    def consulta_lista_concessao(data_set):
        if(len(data_set) == 0):
            print("Dados vazios")
            return 0
        cont_negativa, cont_neutra, cont_total, cont_positiva = 0, 0, 0, 0
        #Laço para calcular o total, negativa, neutra e positiva
        for i in data_set:
            if(i.comercializado_2020 == 'Sim'):
                cont_total += 1
                if(i.lista_concessao == 'Negativa'):
                    cont_negativa += 1
                elif(i.lista_concessao == 'Neutra'):
                    cont_neutra += 1
                elif(i.lista_concessao == 'Positiva'):
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
        return cont_negativa,cont_neutra,cont_positiva

    def toString(self):
        return "(" + self.substancia + "), (" + self.ean1 + "), (" + self.produto + "), (" + self.apresentacao + "), (" + self.pf_sem_impostos + "), (" + self.pmc0 + "), (" + self.lista_concessao + "), (" + self.comercializado_2020 + ")"

    def toString_modificado(self):
        return "(" + self.substancia + "), (" +  self.produto + "), (" + self.apresentacao + "), (" + self.pf_sem_impostos + ")"
        
