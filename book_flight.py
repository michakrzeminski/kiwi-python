#!/usr/bin/env python

from datetime import datetime
import argparse
import json
import requests
import sys

# get options from user
parser = argparse.ArgumentParser()
parser.add_argument('--date', help='departure date', required=True)
parser.add_argument('--return-length', help='return flight, days in destination', type=int, required=False)
parser.add_argument('--one-way', help='one-way flight (default)', action='store_true', required=False)
parser.add_argument('--cheapest', help='find cheapest flight (default)', action='store_true', required=False)
parser.add_argument('--fastest', help='find fastest flight', action='store_true', required=False)
parser.add_argument('--bags', help='number of bags', type=int, required=False)

args = parser.parse_args()
print(args)

# search flights
search_url = 'https://api.skypicker.com/flights'

search_params = {
	'v': 3,
	'flyFrom': '49.2-16.61-250km',
	'to': 'dublin_ie',
	'typeFlight': 'oneway',
	'adults': 1,
	'sort': 'price',
	'limit': 1
}

# fill in departure date
date_in = datetime.strptime(args.date, '%d-%m-%Y')
date_out = date_in.strftime('%d/%m/%Y')
search_params['dateFrom'] = date_out
search_params['dateTo'] = date_out

'''
fill in return / length
renamed to avoid having an identifier named 'return' (syntax error),
but argument in the form --return is also recognized
'''
if args.return_length:
	search_params['typeFlight'] = 'return'
	search_params['daysInDestinationFrom'] = args.return_length
	search_params['daysInDestinationTo'] = args.return_length

if args.fastest:
	search_params['sort'] = 'duration'

print(search_params)

response = requests.get(search_url, params=search_params)
print(response.status_code)
print(response.content)

# error -- search request failed
if response.status_code >= 400:
	sys.exit('search request failed')

# error -- no flights matching search criteria
if response.json().get('_results') == 0:
	sys.exit('no flights found matching search criteria')

'''
# book flight
booking_url = 'http://128.199.48.38:8080/booking'
booking_body = {
	'currency': 'USD',
	'bags': 2,
	'booking_token': 'b/n57BoTjASi2ByXlxiZP3oDvlzrQBO2CyfmSlMWf797iyUPg9g6AUmQTRMN0LUSLGZwJU1Lf1p3eAZK1HMA49WbjkNwLkAzmc46t627Q2+vu5rOy5FEWfc0SPMohsJpkDhtZlR5sk91ew3DkQ6bcSu09yILirZcDVNilLZ724at+JExC1oNgH8W1Uv4p7vB52NnOZd0HvFLGjXvjpRcKzI/VZqVEEGNQaDsXYjldG5kLKYEE/Eaq3EwZUVxidUiBd5RpxK1BUe4nxPLvek+5OD6dhdnEMlHaMCsK7fol/a/BopzHz/kXjV54+UuDfNr1gl7FpAQHKpwhI2YVSP/wHIkVD9YnGwPdU2cd5z956j6ncGW+/Fmmpne0OzsGsLOnhinINS5jujKehoItfB3h0Hcp0ggilMUht+FMuIJcm7BcixRmOshfqChkwiEMlJTzEF4K1vPlWX3V3giu4Ak0wnoHx72IJ6EZf7XxGwp55SrdKeyh4x/0iPodez3sCubsM4ckPKx414mFEHtrct034C8NWfDfpMiIdS7qe7U3xB/oYRZb5fct285RsbnWcFjNHW+UdCf8b7C5yPZwX5EPsudYMRvh+NUr4YeLOnel6wGENowwfZ4bV/t02z4LFahj58C0sMTDktcvljeeAke6Tuvd9kiRzibyq43vcm4fdPjnAD+UKyjmshOn7QOu99sfmFIYhdYxdfGjuTOXZgQUg==',
	'passengers': [
		{
			'firstName': 'Riva',
			'lastName': 'Nathans',
			'title': 'Mrs',
			'email': 'rivanathans@gmail.com',
			'documentID': 'id',
			'birthday': '1988-07-12'
		}
	]
}

booking_response = requests.post(booking_url, json=booking_body)

print(booking_response.status_code)
print(booking_response.headers['content-type'])
print(json.loads(booking_response.content))
'''