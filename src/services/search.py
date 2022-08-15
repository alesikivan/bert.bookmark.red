from top2vec import Top2Vec
from pathlib import Path

# BERT Model init
bert_model_file = Path('src/data/top2vec_vis_ngram_model')
BERT_MODEL = Top2Vec.load(bert_model_file)

class Search:
    @staticmethod
    def bert_search(params):
        query = params.get('query') or ''
        documents_amount = 50

        [text, scores, ids] = BERT_MODEL.query_documents(query, num_docs=documents_amount)

        return ids.tolist()
