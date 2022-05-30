import unittest

from App import consulta_codigo_barras
from App import ler_arquivo
from App import consulta_nome
from App import consulta_lista_concessao


class TestApp(unittest.TestCase):
    def test_consulta_nome(self):
        data_set = []
        data_set = ler_arquivo(data_set,'TA_PRECO_MEDICAMENTO.csv')
        data = []
        data.append(['LOSARTANA POTÁSSICA', '7897337707336', 'COZAAR', '100 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', '47,50', '65,67', 'Positiva', 'Sim'])
        data.append(['LOSARTANA POTÁSSICA', '7897337706384', 'COZAAR', '50 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', '32,21', '44,53', 'Positiva', 'Sim'])
        self.assertEqual(consulta_nome(data_set,'COZAAR'),  data)

    def test_consulta_codigo_barras(self):
        data_set = []
        data_set = ler_arquivo(data_set,'TA_PRECO_MEDICAMENTO.csv')
        data = []
        data.append(['LOSARTANA POTÁSSICA', '7897337707336', 'COZAAR', '100 MG COM REV CT BL AL PVC/PE/PVDC BCO OPC X 30', '47,50', '65,67', 'Positiva', 'Sim'])
        self.assertEqual(consulta_codigo_barras(data_set,'COZAAR'),  data)




if __name__ == '__name__':
    unittest.main()
