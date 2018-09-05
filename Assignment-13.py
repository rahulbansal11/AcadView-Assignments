1>>Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints:-
import requests
import json
response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=#5935994c05/")
a = json.loads(response.text)
print(response)
print(response.content)
print(a["quoteText"])
print(a["quoteLink"])
