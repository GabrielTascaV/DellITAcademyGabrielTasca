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
    
    def consulta_nome(data_set,nome):
        dados = []
        #Adiciona na variavel dados se o campo COMERCIALIZAÇÃO 2020 for sim e o nome for igual a coluna PRODUTO
        for i in data_set:
            if(i.comercializado_2020 == 'Sim' and i.produto == nome.upper()):
                dados.append(i)
        #Retorna a variável dados com os medicamento que foram encontrados
        print("Resultado: ")
        for i in range(len(dados)):
            print(dados[i])
        return dados


    def toString(self):
        print( "[" + self.substancia + "], [" + self.ean1 + "], [" + self.produto + "], [" + self.apresentacao + "], [" + 
            self.pf_sem_impostos + "], [" + self.pmc0 + "], [" + self.lista_concessao + "], [" + self.comercializado_2020 + "]")
        
