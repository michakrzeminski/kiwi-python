#!/usr/bin/env python

import requests
import json

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

# print(response.status_code)
# print(response.headers['content-type'])
# print(response.content)

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

# print(response.status_code)
# print(response.headers['content-type'])
# print(response.content)

# book flight
booking_url = "http://128.199.48.38:8080/booking"
booking_body = {
	"currency": "USD",
	"bags": 2,
	"booking_token": "b/n57BoTjASi2ByXlxiZP3oDvlzrQBO2CyfmSlMWf797iyUPg9g6AUmQTRMN0LUSLGZwJU1Lf1p3eAZK1HMA49WbjkNwLkAzmc46t627Q2+vu5rOy5FEWfc0SPMohsJpkDhtZlR5sk91ew3DkQ6bcSu09yILirZcDVNilLZ724at+JExC1oNgH8W1Uv4p7vB52NnOZd0HvFLGjXvjpRcKzI/VZqVEEGNQaDsXYjldG5kLKYEE/Eaq3EwZUVxidUiBd5RpxK1BUe4nxPLvek+5OD6dhdnEMlHaMCsK7fol/a/BopzHz/kXjV54+UuDfNr1gl7FpAQHKpwhI2YVSP/wHIkVD9YnGwPdU2cd5z956j6ncGW+/Fmmpne0OzsGsLOnhinINS5jujKehoItfB3h0Hcp0ggilMUht+FMuIJcm7BcixRmOshfqChkwiEMlJTzEF4K1vPlWX3V3giu4Ak0wnoHx72IJ6EZf7XxGwp55SrdKeyh4x/0iPodez3sCubsM4ckPKx414mFEHtrct034C8NWfDfpMiIdS7qe7U3xB/oYRZb5fct285RsbnWcFjNHW+UdCf8b7C5yPZwX5EPsudYMRvh+NUr4YeLOnel6wGENowwfZ4bV/t02z4LFahj58C0sMTDktcvljeeAke6Tuvd9kiRzibyq43vcm4fdPjnAD+UKyjmshOn7QOu99sfmFIYhdYxdfGjuTOXZgQUg==",
	"passengers": [
		{
			"firstName": "Riva",
			"lastName": "Nathans",
			"title": "Mrs",
			"email": "rivanathans@gmail.com",
			"documentID": "id",
			"birthday": "1988-07-12"
		}
	]
}

booking_response = requests.post(booking_url, json=booking_body)

print(booking_response.status_code)
print(booking_response.headers['content-type'])
print(json.loads(booking_response.content))