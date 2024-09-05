from typing import List

from models.restaurant_menu.menu_item import MenuItem


class GetRestaurantResponseDto:

	def __init__(self, name: str, menu_items: List[MenuItem]):
		self.restaurant = name
		self.menu = menu_items
