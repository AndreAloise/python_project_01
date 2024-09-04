from models.restaurant_menu.menu_item import MenuItem


class Dish(MenuItem):
	def __init__(self, name, price, description):
		super().__init__(name, price)
		self._description = description

	def show_item(self, i):
		name = f'Name: {self.name.ljust(25)}'
		price = f'Price: R${str(self.price).ljust(15)}'
		description = f'Description: {self._description}'
		message = f'{i}. {name} | {price} | {description}'
		return message
