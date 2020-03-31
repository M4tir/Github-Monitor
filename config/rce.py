import requests

nr = requests.get(url='https://api.github.com/search/repositories?q=RCE&sort=updated&order=desc').text
with open("2.txt", 'w',encoding='utf-8') as file_object:
    file_object.write(nr)