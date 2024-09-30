from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")

# result = es.count(index="student_index", body={})
# print(result)
#
#
# # Get cluster information
# # cluster_info = es.info()
# # print("Cluster Info:", cluster_info)

result = es.search(index="student_index", body={"query": {"match_all": {}}})
for ele in result['hits']['hits']:
    print("Search Result:", ele["_source"])


