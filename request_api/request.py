import requests


def get_quotes():
    """Retorna um json com  a lista de citações"""
    request = requests.get(
        'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes')
    response = request.json()

    return response


def get_quote(quote_number):
    """Retorna a citação de acordo com o índice passado para o parâmetro"""
    request = requests.get(
        'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/' + str(quote_number))
    response = request.json()

    return response


# Test Functions
if __name__ == '__main__':
    print(get_quote(2))
    print()

    print(get_quotes())
