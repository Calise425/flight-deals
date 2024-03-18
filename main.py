from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_sheet()
flight_search = FlightSearch()


for row in sheet_data:
    if len(row["iataCode"]) == 0:
        row["iataCode"] = flight_search.get_aita(row["city"])
        body = {
            "price": row
        }
        data_manager.put_sheet(row["id"], body)
    flight_search.search_for_flights(row["iataCode"])

