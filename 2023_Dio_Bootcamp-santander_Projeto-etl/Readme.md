### Esse é um exercício do Santander Bootcamp 2023 - Ciência de Dados com Python da plataforma DIO. <br>
#### Objetivo: criar um pipeline de ETL com Python.
- Será criada uma base de dados de 30 pessoas, com diversas informações;
- A base de dados será reduzida para quatro campos: nome, cpf, email e cep;
- O objetivo será utilizar uma API para resgatar as informações pertinentes ao cep de cada pessoa, e recarregá-la na base de dados.<br>
---

**0. Etapa Preliminar:** criei uma base de dados de treino em formato 'json' com o auxílio do site 'https://www.4devs.com.br/'.

---
**1. Etapa EXTRACT:** serão extraídos os dados da base de dados.

- Importandos todas as Bibliotecas necessárias;
- Carregando a base de dados com todas as informações;
- Reduzindo o número de colunas da base de dados para podermos realizar o exercício.
---
**2. Etapa TRANSFORM:** serão recuperadas as informações relativas ao CEP de cada cliente.

- Importandos todas as Bibliotecas necessárias;
- Criando uma lista vazia para cada coluna que será acrescentada na base de dados;
- Iterando sobre cada linha da base de dados, fazendo uma requisição para a API e salvando as informações na lista criada anteriormente;
- Acrescentando as colunas com as informações atualizadas na base dados.
---
**3. Etapa LOAD:** salvando as novas informações em uma nova base de dados, com a mesma formatação da original.
