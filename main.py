import json
from pathlib import Path
from typing import List

from fastapi import FastAPI

from models.dtos.get_restaurant_response_dto import GetRestaurantResponseDto
from services.company_service import CompanyService
from services.restaurant_service import RestaurantService

app = FastAPI()


@app.get('/api/getAllRestaurants')
def get_all_restaurants():
	restaurants = get_restaurant_list()

	return restaurants


def get_restaurant_list() -> List[GetRestaurantResponseDto]:
	file_path = Path('raw_data_jsons/company_data.json')
	with file_path.open('r', encoding='utf-8') as file:
		data = json.load(file)

	dto_list = CompanyService.convert_json_to_list_dto(data)
	restaurant_list = RestaurantService.create_restaurants_from_company_data(dto_list)

	response = []
	for restaurant in restaurant_list:
		name = restaurant.get_name()
		menu = restaurant.get_menu()
		dto = GetRestaurantResponseDto(name, menu)
		response.append(dto)

	return response
