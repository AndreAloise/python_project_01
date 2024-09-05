from models.restaurant_menu.menu_item import MenuItem


class Drink(MenuItem):
	def __init__(self, name, price, size):
		super().__init__(name, price)
		self._size = size

	def show_item(self, i):
		name = f'Name: {self.name.ljust(self.NAME_LEFT_PADDING_ADJUST_SPACE)}'
		price = f'Price: R${str(self.price).ljust(self.PRICE_LEFT_PADDING_ADJUST_SPACE)}'
		size = f'Size: {self._size}'
		message = f'{i}. {name} | {price} | {size}'
		return message
