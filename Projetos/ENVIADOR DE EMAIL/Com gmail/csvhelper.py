"""
Arquivo.py para ajudar a manipular um csv, através das 
funcionalidades mais recorrentes
"""
import csv
import io
from tabulate import tabulate 
from time import sleep



class CsvHelper:
    def __init__(self, name: str):
        """
        Inicializador de classe
        Args:
            name (str): nome do arquivo csv
        Variáveis:    
            rest_time (float): tempo de descanso entre os processos
            _lines (int): número de linhas
            _columns (int): número de colunas
        """
        self._name = self._filter_name(name)
        self.rest_time = 0.5
        self._lines = 0
        self._columns = 0
    
    @staticmethod
    def _filter_name(name: str):
        """
        Checa a terminação do nome atribuído, caso esteja
        sem o sufixo, o adiciona 
        Args:
            name (str): nome atribuído ao arquivo csv
        Returns:
            (str): nome pronto para operações with
        """
        if not name.endswith('.csv'):
            name += '.csv'
        return name
        
    def create(self, headers: list):
        """
        Cria o arquivo csv
        Args:
            headers (list): Adiciona os campos do arquivo
        """
        self.__validate_create(headers)
        headers.insert(0, 'ID')
        sleep(self.rest_time)
        with io.open(self._name, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers) 
        self.size_update()
        
    @staticmethod
    def __validate_create(fields: list):
        """
        Valida os headers
        """
        if len(fields) == 0:
            raise ValueError('Você não adicionou campos')

    def read(self):
        """
        Lê o arquivo csv com python
        Returns:
            (list): lista com todos os dados do csv naquele momento
        """
        sleep(self.rest_time)
        with io.open(self._name, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            data = []
            for df in reader:
                data.append(df)
        return data

    def size_update(self):
        """
        Atualiza contagem de linhas e colunas
        """
        sleep(self.rest_time)
        data = self.read()
        self._lines = len(data)
        self._columns = len(data[0])

    def view(self):
        """
        Exibe a tabela no terminal usando a biblioteca tabulate
        """
        sleep(self.rest_time)
        data = self.read()
        print(tabulate(data[1:], headers=data[0], tablefmt="fancy_grid"))

    def fill(self, *fields):
        """
        Preenche várias linhas do csv simultaneamente, com a entrada
        de várias listas que trazem as informações de cada campo
        """
        self.__validate_fill(*fields)
        sleep(self.rest_time)
        data = self._field_organizer(*fields)
        line_id = self._lines
        with io.open(self._name, 'a', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)  
            for info in data: 
                sleep(0.5)
                info_copy = info[:]
                info_copy.insert(0, line_id)
                writer.writerow(info_copy)
                line_id += 1
        self.size_update()
        
    def __validate_fill(self, *fields):
        """
        Valida a função fill
        """
        full_data = self._field_organizer(*fields)
        if len(list(fields)) != self._columns - 1 or len(list(fields)) == 1:
            raise ValueError(f'Quantidade de informações incorreto')
        for data in full_data:
            if len(data) != self._columns - 1:
                raise ValueError(f'Faltou dados na lista: {data}')

    def _field_organizer(self, *fields):
        """
        Retorna uma lista de listas com dados agrupados de cada
        linha de informação 
        """
        sleep(self.rest_time)
        data_received = list(fields) 
        formated_data = []
        for pos in range(len(data_received)):
            for key, value in enumerate(data_received[pos]):
                try:
                    formated_data[key].append(value)
                except IndexError:
                    formated_data.append([])
                    formated_data[key].append(value)
        return formated_data
    
    def fill_one(self, informations:list):
        """
        Preenche uma linha da tabela
        """
        sleep(self.rest_time)
        self.__validate_fill_one(informations)
        informations.insert(0, str(len(self._lines)))
        with io.open(self._name, 'a', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)   
            writer.writerow(informations)
        self.size_update()
    
    def __validate_fill_one(self, informations: list):
        """
        Valida a função fill_one
        """
        if len(informations) != self._columns - 1:
            raise ValueError('Quantidade de informações incorreto')
        
    def _construct(self, data: list):
        """
        Constrói uma nova tabela apartir de uma base 
        """
        sleep(self.rest_time)
        with io.open(self._name, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for df in data:
                writer.writerow(df) 
        self.size_update()
        
    def insert_data(self, position_id: int, informations: list):
        """
        Insere informações em determinado id da tabela
        """
        sleep(self.rest_time)
        self.__validate_insert_data(position_id, informations)
        data = self.read()
        informations.insert(0, position_id)
        data.insert(position_id, informations)
        self._construct(data)
        self.size_update()
                
    def __validate_insert_data(self, position_id: int, informations: list):
        """
        Valida a função insert_data
        """
        if position_id > self._lines:
            raise ValueError('Valor impróprio de id')
        if len(informations) != self._columns - 1:
            raise ValueError('Quantidade de informações incorreto')
        data = self.read()
        for df in data:
            if df[0] == str(position_id):
                raise ValueError('Id de linha já utilizado')
            

    def del_line(self, line_id:int):
        """
        Deleta uma linha apartir de um id de linha
        """
        sleep(self.rest_time)
        data = self.read()
        del data[line_id]
        self._construct(data)
        self.size_update()

    def  del_column(self, fieldname: str):
        """
        Deleta uma coluna apartir do nome do campo da coluna
        """
        sleep(self.rest_time)
        data = self.read()
        pos = data[0].index(fieldname)
        for c in range(len(data)):
            del data[c][pos]
        self._construct(data)
        self.size_update()
        