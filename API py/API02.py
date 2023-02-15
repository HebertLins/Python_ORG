from urllib import response
import requests

user = input("informe o seu usuário no github: ")

url = f"https://api.github.com/users/{user}"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}") 
    print(f"Repositórios: {dados['public_repos']}") 
    print(f"Seguidores: {dados['followers']}") 