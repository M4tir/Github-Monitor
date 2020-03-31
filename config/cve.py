import requests

nr = requests.get(url='https://api.github.com/search/repositories?q=CVE-2020&sort=updated&order=desc').text
with open("1.txt", 'w') as file_object:
    file_object.write(nr)