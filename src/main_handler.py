from src.services.search import Search

class MainHandler:
	@staticmethod
	def search(params):
		return Search.bert_search(params)
