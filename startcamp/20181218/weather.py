from darksky import forecast

seoul = forecast('00ebc1052d5ab59784ec9067f1763825', 37.502909 , 127.039859)

print (seoul['currently']['temperature'])
print (seoul['currently']['summary'])

# import requests

# url = 'https://api.darksky.net/forecast/00ebc1052d5ab59784ec9067f1763825/37.502909,%20127.039859'

# res = requests.get(url)
# data = res.json()

# print(data['currently']['summary'])
