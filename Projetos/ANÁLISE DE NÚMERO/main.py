"""
Projeto de iniciante - Análise de um número

Objetivo:
    Usando o pacote phonenumber do google obtemos o máximo de informações referente a um número e exportando-o como JSON, podendo usar como base para aplicações maiores.

Variáveis de entrada:
    - phone_number: recebe o número do seu celular nos formatos: '020 8366 1177', '020 8366 1177', '+442083661177'
    - Caso não use informe o código do país indique em phone_number, indique a região na varável region 
"""

from support import get_data, number_analysis
import phonenumbers as phone
import json


#! Variáveis de entrada
phone_number = '99 99999 9999'
region = 'BR'   

#* Obtendo dados do número informado
phone_analisys = phone.parse(phone_number, region)  
initial_number_information = get_data(phone_analisys, region)
number_information = number_analysis(phone_analisys, initial_number_information)

#* Exportando em arquivo JSON 
with open('number_data.json', 'w') as file:
    json.dump(number_information, file, indent=4)
        

