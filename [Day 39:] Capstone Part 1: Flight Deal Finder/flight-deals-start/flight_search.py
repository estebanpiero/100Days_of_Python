from flight_data import FlightData
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

TEQUILA_APIKEY = os.getenv('TEQUILA_APIKEY')
TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_QUERY_LOCATIONS = 'locations/query'
TEQUILA_SEARCH_FLIGHTS_ENDPOINT = 'v2/search'

#TEQUILA DATE FORMAT dd/mm/YYYY
TEQUILA_AUTHENTICATION = {
    'apikey' : TEQUILA_APIKEY
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    
    def iataCode_search(self,city):
        TEQUILA_PARAMS = {
                    'term': city,
                    'location_type':'city',
                    'limit' : 1
        }
 
        iataCode_response = requests.get(f'{TEQUILA_ENDPOINT}/{TEQUILA_QUERY_LOCATIONS}',headers= TEQUILA_AUTHENTICATION,params=TEQUILA_PARAMS)
        iataCode_data = iataCode_response.json()['locations']
        iataCode = iataCode_data[0]['code']
        return iataCode
    
    def check_flight(self,origin_city_code,dst_city_code,from_time,to_time):
        query = {
            'fly_from': origin_city_code,
            'fly_to': dst_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 15,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        flight_search = requests.get(f'{TEQUILA_ENDPOINT}/{TEQUILA_SEARCH_FLIGHTS_ENDPOINT}',
        headers= TEQUILA_AUTHENTICATION,
        params=query
        )
        flight_search.raise_for_status()

        try:
            data = flight_search.json()['data'][0]
        except IndexError:
            #print(f'No flights found for {dst_city_code}')
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

    #    print(f'{flight_data.destination_city}: U$D{flight_data.price} ' 
    #    f'from: {flight_data.origin_airport}', 
    #    f'to: {flight_data.destination_airport}',
    #    f'From Date: {flight_data.out_date}',
    #    f'To: {flight_data.return_date}')

        return flight_data
