import requests

r = requests.get('https://api.github.com/events')

# print(r.text)

with open("codewithharry.txt","w") as f:
    f.write(r.text)

r = requests.post('https://httpbin.org/post', data={'Samir': 'Khamele'})