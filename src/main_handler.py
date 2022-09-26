from src.services.search import Search
from src.services.visualizer import Visualizer

class MainHandler:
	@staticmethod
	def search(params):
		return Search.bert_search(params)
		
	@staticmethod
	def find_clusters(params):
		return Visualizer.find_clusters(params)
