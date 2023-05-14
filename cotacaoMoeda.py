import httpx

base_currency = input('Digite a moeda base: ').upper()
currency = input('Digite a moeda desejada: ').upper()

#busca valores de moedas na api publica
response = httpx.get(
    url=f'https://api.exchangerate.host/latest?bse={base_currency}'
).json()

currency_data = response['rates']

print(f'1 {base_currency} vale {currency_data.get(currency)} {currency}')

