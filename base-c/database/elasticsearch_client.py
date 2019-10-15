import uuid

import singletons
from elasticsearch import Elasticsearch

from core.redis_wrapper import cache


@singletons.GlobalFactory
class ElasticsearchClient:

    def __init__(self):
        self.elastic_client = Elasticsearch()

    def insert(self, index, document):
        id = uuid.uuid4()
        self.elastic_client.index(index=index, id=id, body=document)
        return id

    @cache()
    def get_id(self, index, id):
        return self.elastic_client.get(index=index, id=id)

    @cache()
    def get_all(self, index):
        return self.elastic_client.search(index=index)['hits']['hits']
