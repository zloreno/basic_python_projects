from requests import get
from pprint import PrettyPrinter
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://free.currconv.com/"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f'api/v7/currencies?apiKey={API_KEY}'
    url = BASE_URL + endpoint

    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    # printer.pprint(data)

    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        if symbol != '':
            symbol = " - " + symbol

        print(f'{_id} - {name} {symbol}')


def get_fx(currency_1, currency_2):
    # Check if currencies make sense
    endpoint = f'api/v7/convert?q={currency_1}_{currency_2}&compact=ultra&apiKey={API_KEY}'
    url = BASE_URL + endpoint

    data = get(url).json()

    if len(data) == 0:
        print(data)
        print('Invalid currencies')
        return

    rate = list(data.values())[0]
    print(f'1 {currency_1} = {rate} {currency_2}')
    return rate


def fx_convert(currency_1, currency_2, amount):
    rate = get_fx(currency_1, currency_2)
    if not rate:
        return
    new_amount = rate * amount
    print(f'{amount} {currency_1} = {new_amount} {currency_2}')


def main():
    currencies = get_currencies()
    print('Welcome to the currency converter!')
    print('List - List the different currencies')
    print('Convert- Convert two given currencies')
    print('Rate -  get the FX rate of two currencies')
    print('')
    while True:
        command = input(
            "Enter a command (list, convert, rate)\t\t(q to quit): ").lower()
        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency_1 = input('Enter a base currency: ').upper()
            currency_2 = input('Enter a currency to convert to: ').upper()
            ammount = float(input('Enter the ammount you want to convert: '))
            fx_convert(currency_1, currency_2, ammount)
        elif command == 'rate':
            currency_1 = input('Enter a base currency: ').upper()
            currency_2 = input('Enter a currency to convert to: ').upper()
            get_fx(currency_1, currency_2)
        else:
            print('Unrecognized command!')


main()
