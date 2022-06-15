from datetime import datetime
from re import A
from .data import get_data_from_sheet
import datetime as dt
import requests
import xml.etree.ElementTree as ET


def convert_data(data: list) -> list:
    """
    Input: List of data from GS

    Output: [List] Converted data
    """
    new_data = []
  
    usdrate = usd_rate()
    for pack in data:
        new_value = []
        new_value.append(int(pack[0]))
        new_value.append(int(pack[1]))
        new_value.append(float(pack[2]))
        new_value.append(float(pack[2]) * usdrate)
        new_value.append(dt.datetime.strptime(pack[3], '%d.%m.%Y'))
        new_data.append(new_value)
    
    return new_data


def usd_rate() -> float:
    """
    Get current USD rate from CBR
    Return: [Float] USD rate
    """
    usd_rate = ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text) \
        .find("./Valute[CharCode='USD']/Value").text.replace(',', '.')
    return float(usd_rate)


