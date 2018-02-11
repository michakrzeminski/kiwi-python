#!/usr/bin/env python

from datetime import datetime
import argparse
import json
import requests
import sys

SEARCH_URL = 'https://api.skypicker.com/flights'
BOOKING_URL = 'http://128.199.48.38:8080/booking'

# get options from command-line arguments
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--date', help='departure date', required=True)
	parser.add_argument('--from-location', help='from (airport code)', required=True)
	parser.add_argument('--to-location', help='to (airport code), omit to see flights to anywhere', required=False)
	parser.add_argument('--return-length', help='return flight, days in destination', type=int, required=False)
	parser.add_argument('--one-way', help='one-way flight (default)', action='store_true', required=False)
	parser.add_argument('--cheapest', help='find cheapest flight (default)', action='store_true', required=False)
	parser.add_argument('--fastest', help='find fastest flight', action='store_true', required=False)
	parser.add_argument('--bags', help='number of bags', type=int, required=False)
	return parser.parse_args()

# search flights
def search_flights(args):

	# initialize search parameters
	search_params = {
		'v': 3,
		'typeFlight': 'oneway',
		'adults': 1,
		'sort': 'price',
		'limit': 1
	}

	# fill in location -- from
	search_params['flyFrom'] = args.from_location

	# fill in location -- to
	if args.to_location:
		search_params['to'] = args.to_location

	# fill in departure date
	date_in = datetime.strptime(args.date, '%d-%m-%Y')
	date_out = date_in.strftime('%d/%m/%Y')
	search_params['dateFrom'] = date_out
	search_params['dateTo'] = date_out

	# fill in return / stay length
	if args.return_length:
		search_params['typeFlight'] = 'return'
		search_params['daysInDestinationFrom'] = args.return_length
		search_params['daysInDestinationTo'] = args.return_length

	# option -- find fastest
	if args.fastest:
		search_params['sort'] = 'duration'

	# use Kiwi search API
	response = requests.get(SEARCH_URL, params=search_params)

	# handle errors
	if response.status_code >= 400:
		sys.exit('search request failed')
	if response.json().get('_results') == 0:
		sys.exit('no flights found matching search criteria')

	return response.json()

# book flight
def book_flight(args, response):

	# initialize booking request
	booking_body = {
		'currency': 'USD',
		'bags': 0,
		'passengers': [
			{
				'firstName': 'Riva',
				'lastName': 'Nathans',
				'title': 'Mrs',
				'email': 'rivanathans@gmail.com',
				'documentID': 'id_string',
				'birthday': '1988-07-12'
			}
		]
	}

	# add booking token
	booking_body['booking_token'] = response.get('data')[0].get('booking_token')

	# add bags, if any
	if args.bags:
		booking_body['bags'] = args.bags

	# use Kiwi fake booking API
	response = requests.post(BOOKING_URL, json=booking_body)

	# handle errors
	if response.status_code >= 400:
		sys.exit('booking request failed')
	if response.json().get('pnr') == None:
		sys.exit('failed to confirm reservation')

	print(booking_body)
	print(response.status_code)
	print(response.headers['content-type'])
	print(response.json())

	return response.json().get('pnr')

args = parse_arguments()
response = search_flights(args)
confirmation = book_flight(args, response)
print('booking confirmation: ' + confirmation)