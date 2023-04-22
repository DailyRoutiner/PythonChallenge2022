#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
import datetime
from flight_search import FlightSearch

# Origin City Code
ORIGIN_CITY_IATA = "ICN" # Incheon / Korea

# 3단계 DataManager에서 데이터 가져오기
flight = DataManager()
flight_search = FlightSearch()
sheet_data = flight.get_destination_data()

# 뭔가 리스트 컴프리핸션이 될거 같은데...
for row in sheet_data:
    # 4단계 iatacode 비었는지 확인
    if "" == row['iataCode']:
        # 5단계 FlightSearch Class로 하나씩 전달..?
        row['iataCode'] = flight_search.get_destination_code(row['city'])

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=180)

for destination in sheet_data:
    # 7단계 저렴한 항공권 검색하기 iataCode로 기간은 내일부터 6개월 사이 출발 6*30
    flight_data = flight_search.get_lowest_price(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination['iataCode'],
        date_from=tomorrow,
        date_to=six_month_from_today
    )
    destination['lowestPrice'] = flight_data.price
    print(destination['lowestPrice'])

pprint(sheet_data)
# # 6단계 구글시트 업데이트
# flight.destination_data = sheet_data
# flight.update_destination_data()
