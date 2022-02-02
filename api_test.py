import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"s":"Avengers Endgame","r":"json","page":"1"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "e6e4a66a7bmsh25672cdfaf30dfep13c2ddjsn4425cca134f1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)