from abc import ABC, abstractmethod


class MenuItem(ABC):
	def __init__(self, name, price):
		self.name = name
		self.price = price

	@abstractmethod
	def show_item(self, i):
		pass
