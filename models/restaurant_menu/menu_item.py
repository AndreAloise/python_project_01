from abc import ABC, abstractmethod


class MenuItem(ABC):
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@abstractmethod
	def show_item(self, i):
		pass

	@abstractmethod
	def apply_discount(self, discount_value):
		"""
			Apply discount to item's price\n
			discount_value : float (Ex: 0.05)
		"""
		pass
