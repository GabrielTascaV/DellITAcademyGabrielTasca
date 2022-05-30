# DellITAcademyGabrielTasca
Programa para a prova de estágio do Dell IT Academy
Enunciado: 
1. [Consultar medicamentos pelo nome] Permitir que o usuário informe o nome do medicamento (ou parte do nome do medicamento) que desejar e como resultado o programa deverá exibir:
    a. Uma lista com os medicamentos encontrados e suas informações (Nome, Produto, Apresentação e valor PF Sem Impostos);
    Atenção: somente devem aparecer no resultado os registros de produtos que foram comercializados em 2020 (observar a coluna de dados “COMERCIALIZAÇÃO 2020”).
2. [Buscar pelo código de barras] O programa deverá solicitar ao usuário o número correspondente ao código de barras de um produto (coluna de dados “EAN 1”, por exemplo ‘525516020019503’) e então:
    a. Localizar todos os registros referentes a este produto, independentemente de terem sido comercializados ou não em 2020;
    b. Dentre todos os registos encontrados, identificar o Preço Máximo ao Consumidor (alíquota de 0%, coluna de dados “PMC 0%”) mais alto e o mais baixo. Exibir na tela o mais alto, o mais baixo e a diferença entre eles.
3. [Comparativo da LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)] Com base somente nos produtos que foram comercializados em 2020, o programa deverá:
    a. Consultar a coluna de dados “LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)” para determinar o percentual de produtos classificados como “Negativa”, “Neutra” ou “Positiva” para esta coluna.
    b. Mostrar os respectivos valores percentuais da seguinte maneira (dados fictícios): [* repare que a quantidade de asteriscos é proporcional ao respectivo percentual, por
    exemplo, neste caso são 21 asteriscos para a classificação Negativa.]