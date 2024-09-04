from models.review import Review


class Restaurant:

	restaurants = []

	def __init__(self, name, category):
		self._name = name
		self._category = category
		self._active = False
		self._reviews = []
		Restaurant.restaurants.append(self)

	def receive_reviews(self, client, rating):
		if 0 < rating <= 5:
			review = Review(client, rating)
			self._reviews.append(review)