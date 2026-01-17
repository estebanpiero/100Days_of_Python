from datetime import datetime,timedelta
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users import UserDataBase

ORIGIN_CITY_CODE = 'NYC'

data_manager = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()
user_creation = UserDataBase()

sheet_data = data_manager.fligt_information()

for items in sheet_data:
    if items['iataCode'] == '':
        items['iataCode'] = flight_search.iataCode_search(items['city'])
        
#print(sheet_data)

data_manager.destination_data = sheet_data
data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_CODE,
        destination['iataCode'],
        from_time = tomorrow,
        to_time = six_month_from_now
    )
    
    try:
        if flight.price < destination['lowestPrice']:
            notification.send_sms(
                message = f"Low price alert! Only U$D{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
        else:
            print('The Price is not lower than expected')
    except AttributeError : 
        print(f'Not Flight Found')
