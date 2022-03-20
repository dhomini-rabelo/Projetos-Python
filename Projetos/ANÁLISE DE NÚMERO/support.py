"""
Arquivo python para suporte do programa principal
"""
from phonenumbers.phonenumberutil import COUNTRY_CODE_TO_REGION_CODE
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from zoneinfo import ZoneInfo
from datetime import datetime
import phonenumbers as phone
import pycountry
import unidecode


def get_data(phoneobj, region):
    """Gera dados simples sobre o número informado em um dicionário 

    Args:
        phoneobj : resultado da função parse do pacote phonenumbers
        region ([str]): Região onde o número reside

    Returns:
        [dict]: dados simples sobre o número informado em um dicionário
    """
    if region is None:
        region = get_region_by_country_code(phoneobj.country_code)
        region = region[0]
    country = pycountry.countries.get(alpha_2=region)
    initial_data = {'Country code': phoneobj.country_code,
    'National number': phoneobj.national_number,'Possible': False, 'Valid': False, 'Phone operator': None, 'Country': country.name, 'State': None}
    return initial_data


def number_analysis(phoneobj, phone_number_information):
    """Faz uma análise aprofundada de um número

    Args:
        phoneobj: resultado da função parse do pacote phonenumbers
        phone_number_information: contém as informações do número

    Returns:
        [dict]: Dados do número analisado
    """
    if phone.is_possible_number(phoneobj):
        phone_number_information['Possible'] = True
    else:
        return not_possible(phoneobj.national_number, phoneobj.country_code, phone_number_information['Country'])
    if phone.is_valid_number(phoneobj):
        phone_number_information['Valid'] = True
        city_tz = timezone.time_zones_for_number(phoneobj)
        operator = carrier.name_for_number(phoneobj, 'pt-br') 
        phone_state = geocoder.description_for_number(phoneobj, 'pt-br')
        phone_number_information['time zone'] = city_tz
        phone_number_information['Phone operator'] = operator
        phone_number_information['State'] = unidecode.unidecode(phone_state)
    return phone_number_information

def get_region_by_country_code(country_code:int):
    try:
        return list(COUNTRY_CODE_TO_REGION_CODE[country_code])
    except KeyError:
        return []


def list_show(_list:list):
    response = ''
    if len(_list) == 1:
        return _list[0]
    for position, item in enumerate(_list):
        response += item
        if position == len(_list)-1:
            response += f'e {item}'
    return response
    

def not_possible( number:str, country_code:str, country:str):
    data = {
    "Country code": country_code,
    "National number": number,
    "Possible": False,
    "Valid": False,
    "Phone operator": None,
    "Country": country,
    "State": None,
    "time zone": None
    }
    return data