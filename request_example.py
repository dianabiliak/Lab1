import requests
url = "https://api.github.com/users/dianabiliak"
response = requests.get(url)
print(response.text)