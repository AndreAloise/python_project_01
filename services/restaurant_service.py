from collections import defaultdict
from typing import List

from models.dtos.company_raw_data_dto import CompanyRawDataDto
from models.restaurant import Restaurant
from models.restaurant_menu.dish import Dish
from models.restaurant_menu.drink import Drink


class RestaurantService:
	def __init__(self):
		pass

	@staticmethod
	def create_restaurants_from_company_data(data_list: List[CompanyRawDataDto]) -> List[Restaurant]:
		"""
			Create a list of Restaurant objects from raw data.
		"""
		restaurant_map = defaultdict(lambda: {'category': None, 'menu': []})

		for data in data_list:
			if 'oz' in data.item.lower():
				item = Drink(data.item, data.price, "medium")
			else:
				item = Dish(data.item, data.price, data.description)
			restaurant_map[data.company].get('menu').append(item)

		restaurants = []
		for name, info in restaurant_map.items():
			restaurant = Restaurant(name, info.get('category'))
			for menu_item in info.get('menu'):
				restaurant.add_menu_item(menu_item)
			restaurants.append(restaurant)

		return restaurants
