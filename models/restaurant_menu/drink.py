from models.restaurant_menu.menu_item import MenuItem


class Drink(MenuItem):
	def __init__(self, name, price, size):
		super().__init__(name, price)
		self._size = size

	def show_item(self, i):
		name = f'Name: {self.name.ljust(25)}'
		price = f'Price: R${str(self.price).ljust(15)}'
		size = f'Size: {self._size}'
		message = f'{i}. {name} | {price} | {size}'
		return message

	def apply_discount(self, discount_value):
		self.price -= round(self.price * discount_value, 2)
