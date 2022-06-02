import pytest

from Medicamento import Medicamento



#Teste da leitura de arquivo errada
def test_ler_arquivo():
    m = Medicamento
    assert m.ler_arquivo('nomerrado') == 0

#Teste de consulta por nome do produto correto
def test_consulta_nome_correto():
    m = Medicamento
    data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    data = []
    data.append(Medicamento('LOSARTANA POTÁSSICA', '7897337707336', 'COZAAR', '100 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', 
                                                            '47,50', '65,67', 'Positiva', 'Sim'))
    data.append(Medicamento('LOSARTANA POTÁSSICA', '7897337706384', 'COZAAR', '50 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', 
                                                            '32,21', '44,53', 'Positiva', 'Sim'))
    assert m.consulta_nome(data_set,'COZAAR')[0].ean1 == data[0].ean1
    assert m.consulta_nome(data_set,'COZAAR')[1].ean1 == data[1].ean1

#Teste de consulta por nome do produto invalido

def test_consulta_nome_invalido():
    m = Medicamento
    data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    assert m.consulta_nome(data_set,'GABRIEL') == 0

#Teste de consulta por nome do produto com um data_set invalido
def test_consulta_nome_dataset_invalido():
    m = Medicamento
    data_set = []
    assert m.consulta_nome(data_set,'GABRIEL') == 0

#Teste de consulta por codigo de barras correto
def test_consulta_codigo_barras_correto():
    m = Medicamento
    data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    max, min, dif = m.consulta_codigo_barras(data_set,'7897337706575')  
    assert max == 194.41
    assert min == 41.51
    assert dif == 152.90

#Teste de consulta por codigo de barras invalido
def test_consulta_codigo_barras_invalido():
    m = Medicamento
    data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    assert m.consulta_codigo_barras(data_set,'000000000000') == 0

#Teste de consulta por codigo de barras com data_set invalido
def test_consulta_codigo_barras_dataset_invalido():
    m = Medicamento
    data_set = []
    assert m.consulta_codigo_barras(data_set,'7897337706575') == 0


#Teste de consulta de lista de concessao correto
def test_consulta_lista_concessao_correto():
    m = Medicamento
    data_set = m.ler_arquivo('DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    cont_negativa,cont_neutra,cont_positiva = m.consulta_lista_concessao(data_set)
    cont_negativa = "{:.2f}".format(cont_negativa)
    cont_neutra = "{:.2f}".format(cont_neutra)
    cont_positiva = "{:.2f}".format(cont_positiva)
    assert cont_negativa == '33.43'
    assert cont_neutra == '0.36'
    assert cont_positiva == '66.21'

