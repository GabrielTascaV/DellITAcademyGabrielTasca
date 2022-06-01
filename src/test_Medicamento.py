import pytest

from Medicamento import Medicamento

def test_consulta_nome():
    m = Medicamento
    data_set = []
    data_set = m.ler_arquivo(data_set,'DellITAcademyGabrielTasca/TA_PRECO_MEDICAMENTO.csv')
    data = []
    data.append(['LOSARTANA POTÁSSICA', '7897337707336', 'COZAAR', '100 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', '47,50', '65,67', 'Positiva', 'Sim'])
    data.append(['LOSARTANA POTÁSSICA', '7897337706384', 'COZAAR', '50 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', '32,21', '44,53', 'Positiva', 'Sim'])
    assert m.consulta_nome(data_set,'COZAAR') == data 

