# Day 39: Capstone Part 1 - Flight Deal Finder

## Project: Cheap Flight Deal Finder

### Description
An automated flight price monitoring system that searches for cheap flights to your dream destinations. The program uses the Tequila API to find the best flight deals, compares them against your target prices, and can notify you of great deals. This is Part 1 of a two-part capstone project.

### What I Learned
- Working with complex flight APIs
- Data management across multiple modules
- Class-based project structure
- API request optimization
- IATA code handling
- Price comparison logic
- Multi-city flight searching
- Professional code organization

### How to Run
```bash
python3 main.py
```

### Features
- Search multiple destinations
- Compare against target prices
- Find cheapest flights
- Handle IATA airport codes
- Date range searching (next 6 months)
- Direct and 1-stop flights
- Organized data management
- Modular class structure

### Project Structure
```
Day39_FlightDeals/
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
└── notification_manager.py (Part 2)
```

### Classes Implemented

#### 1. DataManager (Google Sheets via Sheety)
```python
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Get data from Google Sheet
        response = requests.get(SHEETY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        # Update IATA codes in sheet
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(f"{SHEETY_ENDPOINT}/{city['id']}",
                        json=new_data)
```

#### 2. FlightSearch (Tequila API)
```python
class FlightSearch:
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.api_key = TEQUILA_API_KEY

    def get_iata_code(self, city_name):
        headers = {"apikey": self.api_key}
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            f"{self.endpoint}/locations/query",
            headers=headers,
            params=query
        )
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin, destination,
                     from_time, to_time):
        headers = {"apikey": self.api_key}
        query = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            f"{self.endpoint}/v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
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
        return flight_data
```

#### 3. FlightData
```python
class FlightData:
    def __init__(self, price, origin_city, origin_airport,
                 destination_city, destination_airport,
                 out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
```

### Google Sheet Structure
| City | IATA Code | Lowest Price |
|------|-----------|--------------|
| Paris | CDG | 100 |
| Berlin | BER | 80 |
| Tokyo | NRT | 500 |

### Main Logic
```python
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()

# Update missing IATA codes
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# Search flights
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight and flight.price < destination["lowestPrice"]:
        print(f"Low price alert! Only £{flight.price} to fly "
              f"from {flight.origin_city}-{flight.origin_airport} "
              f"to {flight.destination_city}-{flight.destination_airport}, "
              f"from {flight.out_date} to {flight.return_date}.")
```

### IATA Codes
Airport codes (e.g., LON = London, PAR = Paris, NYC = New York)

### Search Parameters
- **fly_from**: Origin airport
- **fly_to**: Destination airport
- **date_from/to**: Search date range
- **nights_in_dst**: Stay duration
- **flight_type**: round trip
- **max_stopovers**: 0 for direct

### Key Concepts
- **Class Structure**: Organizing code with classes
- **Separation of Concerns**: Each class has one responsibility
- **API Integration**: Multiple API coordination
- **Data Persistence**: Google Sheets as database
- **Date Manipulation**: Using datetime and timedelta
- **Error Handling**: Try-except for missing data

### Learning Focus
Building a complex, multi-component application with proper code organization, demonstrating professional software development practices.
