from models.restaurant_menu.menu_item import MenuItem


class Drink(MenuItem):
	def __init__(self, name, price, size):
		super().__init__(name, price)
		self._size = size
