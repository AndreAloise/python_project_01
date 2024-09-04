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


	def change_state(self):
		self._active = not self._active

	@classmethod
	def get_restaurants(cls):
		for restaurant in cls.restaurants:
			print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} '
			      f'| {str(restaurant.average_rating).ljust(25)} | {restaurant.status}')

	@property
	def average_rating(self):
		if not self._reviews:
			return '-'
		sum_ratings = sum(review.rating for review in self._reviews)
		rating_qtd = len(self._reviews)
		average = round(sum_ratings / rating_qtd, 1)
		return average

	@property
	def status(self):
		return 'active' if self._active else 'inactive'