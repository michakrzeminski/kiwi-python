#!/usr/bin/env python

import requests

# find cheapest flight
search_url = "https://api.skypicker.com/flights"
search_params = {
	"v": 3,
	"daysInDestinationFrom": 6,
	"daysInDestinationTo": 7,
	"flyFrom": "49.2-16.61-250km",
	"to": "dublin_ie",
	"dateFrom": "03/04/2018",
	"dateTo": "09/04/2018",
	"typeFlight": "return",
	"adults": 1,
	"limit": 1,
	"sort": "price"
}

response = requests.get(search_url, params=search_params)

print(response.status_code)
print(response.headers['content-type'])
print(response.content)

# find shortest flight
search_url = "https://api.skypicker.com/flights"
search_params = {
	"v": 3,
	"daysInDestinationFrom": 6,
	"daysInDestinationTo": 7,
	"flyFrom": "49.2-16.61-250km",
	"to": "dublin_ie",
	"dateFrom": "03/04/2018",
	"dateTo": "09/04/2018",
	"typeFlight": "return",
	"adults": 1,
	"limit": 1,
	"sort": "duration"
}

response = requests.get(search_url, params=search_params)

print(response.status_code)
print(response.headers['content-type'])
print(response.content)