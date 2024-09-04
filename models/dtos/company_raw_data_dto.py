class CompanyRawDataDto:
	def __init__(self, company, item, price, description):
		self.company = company
		self.item = item
		self.price = price
		self.description = description

	def __repr__(self):
		return (f"CompanyRawDataDto(company={self.company!r}, item={self.item!r}, "
		        f"price={self.price}, description={self.description!r})")
