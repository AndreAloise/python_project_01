from models.restaurant_menu.menu_item import MenuItem


class Dish(MenuItem):
	def __init__(self, name, price, description ):
		super().__init__(name, price)
		self._description = description