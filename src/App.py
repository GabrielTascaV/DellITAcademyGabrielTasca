import csv
from Medicamento import Medicamento

m = Medicamento
data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
out = False
data_set[0].toString()
while(not(out)):
    print("----------------SELECIONE UMA OPÇÃO ABAIXO----------------- ")
    print("1 - Consulte medicamento por nome")
    print("2 - Consultar o preço máximo e mínimo por código de barras")
    print("3 - Consultar a Lista de Concessão de Crédito Tributário (PIS/COFINS)")
    print("0 - Sair do programa")
    print("NÚMERO: ")
    option = input()
    if(option == '1'):
        print("Digite o nome do medicamento: ")
        nome = input()
        print("")
        m.consulta_nome(data_set,nome)
        print("")
    elif(option == '2'):
        print("Digite o código de barras: ")
        codigo_barras = input()
        print("")
        m.consulta_codigo_barras(data_set,codigo_barras)
        print("")
    elif(option == '3'):
        print(" ")
        m.consulta_lista_concessao(data_set)
        print("")
    elif(option == '0'):
        out = True
    else:
        print("")
        print("Erro, nenhum valor digitado. Digite um valor válido")
        print("")


