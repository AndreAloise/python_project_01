from abc import ABC, abstractmethod


class MenuItem(ABC):
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@abstractmethod
	def show_item(self, i):
		pass

	def apply_discount(self, discount_value):
		"""
			Apply discount to item's price\n
			discount_value : float (Ex: 0.05)
		"""
		if 0 < discount_value < 1:
			self.price -= round(self.price * discount_value, 2)
		else:
			print(f'Invalid discount value: {discount_value}. No discount for item: {self.name}\n')
