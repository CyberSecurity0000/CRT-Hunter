"""
API - https://crt.sh/?q=pudim.com.br&output=json
Documentation - https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
"""

# Biblioteca
import requests
from requests import get
from json import loads


# Requiscao HTML
def requisicao(url):

    # Metodo GET
    html = get(url=url)

    try:
        if html.status_code == 200:
            resp_html = html.text

            return resp_html

    except Exception:
        print("Erro de requisicao !")

    return None


# Parsing JSON
def parsing_json(html):

    try:
        json = loads(html)

        if json:
            return json

    except:
        return None


# Principal
def main():

    # Url para usar como requisicao
    URL = f"https://crt.sh/?q={domain}&output=json"

    # Conjunto
    conjunto = set()
    domain = input("Dominio (example.com): ")

    # Metodo
    html = requisicao(URL)

    if html is not None:

        json = parsing_json(html)

        # Analisando dicionario
        for i in json:
            value = i["name_value"]
            conjunto.add(value)

        # Criacao de arquivo
        with open ("subdominios", "w") as file:

            for i in conjunto:

                if len(i.split()) == 1 and not i.startswith("*"):
                    file.write(f"{i}\n")

if __name__ == '__main__':
    main()