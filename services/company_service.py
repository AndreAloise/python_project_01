import json

from models.dtos.company_raw_data_dto import CompanyRawDataDto


class CompanyService:
	def __init__(self):
		pass

	@staticmethod
	def convert_json_to_list_dto(json_data: json):
		"""
	        Converte uma lista de dicionários JSON em uma lista de objetos CompanyRawDataDto.

	        :param json_data: Lista de dicionários JSON contendo dados das empresas.
	        :return: Lista de objetos CompanyRawDataDto.
		"""
		dto_list = []
		for entry in json_data:
			dto = CompanyRawDataDto(
				company=entry.get("company"),
				item=entry.get("item"),
				price=entry.get("price"),
				description=entry.get("description")
			)
			dto_list.append(dto)
		return dto_list
