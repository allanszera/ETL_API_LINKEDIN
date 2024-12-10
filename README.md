Descrição do Projeto ETL
Este projeto tem como objetivo demonstrar um processo completo de ETL (Extração, Transformação e Carga) de dados de empregos obtidos a partir de uma API do LinkedIn. A solução foi desenvolvida em Python para a etapa de extração e carga inicial e utiliza o SQL Server para armazenamento intermediário, bem como para a aplicação das transformações nos dados. Após as transformações, os dados serão enviados para um Data Warehouse (DW), tornando-os prontos para análises mais avançadas.

Etapas do Processo
Extração (Extract):

Utilização de Python para consumir a API de empregos do LinkedIn, filtrando por palavra-chave e localidade.
Os dados, inicialmente em formato JSON, são convertidos para um DataFrame e, em seguida, inseridos em uma tabela do SQL Server.
Transformação (Transform):

As transformações são realizadas diretamente no SQL Server (T-SQL).
Valores nulos são tratados, substituindo-os por valores padrão adequados ao tipo de dado.
A coluna de localização, que originalmente contém País e Modalidade de Trabalho (ex: “Brasil (Remoto)”), é dividida em duas colunas:
País: “Brasil”
Modalidade de Trabalho: “Remoto”
Padronização do título do cargo. Por exemplo, um título original como “Junior Data Analyst (Analista de Dados Júnior)” é transformado em:
Título: “Analista de Dados”
Senioridade: “Junior”
Carga (Load):

Após a transformação, os dados são enviados para um Data Warehouse (DW), ficando disponíveis para consultas, análises de BI e visualização em ferramentas de inteligência de negócios.
Tecnologias Utilizadas
Python: Extração dos dados da API (Requests, Pandas).
SQL Server: Armazenamento intermediário dos dados e aplicação de transformações via T-SQL.
Pandas: Manipulação inicial dos dados antes da carga no banco.
Data Warehouse (DW): Armazenamento final dos dados prontos para análise.
Benefícios
Automação do processo de coleta de dados do LinkedIn.
Limpeza, padronização e tratamento de inconsistências.
Dados consolidados e padronizados em um DW, prontos para análises mais aprofundadas, relatórios gerenciais e integração com ferramentas de BI.
