from data_manager import DataManager
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# 3단계 DataManager에서 데이터 가져오기
flight = DataManager()
sheet_data = flight.get_destination_data()

# 뭔가 리스트 컴프리핸션이 될거 같은데...
for tt in sheet_data:
    # 4단계 iatacode 비었는지 확인
    if "" == tt['iataCode']:
        # 5단계 FlightSearch Class로 하나씩 전달..?
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        tt['iataCode'] = flight_search.get_destination_code(tt['city'])

pprint(sheet_data)
# 6단계 구글시트 업데이트
flight.destination_data = sheet_data
flight.update_destination_data()