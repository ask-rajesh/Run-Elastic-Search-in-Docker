from elasticsearch import Elasticsearch, helpers
from faker import Faker
import random

# Initialize Elasticsearch client
es = Elasticsearch("http://localhost:9200")

# Create the student index with the required mappings
def create_index():
    index_mapping = {
        "mappings": {
            "properties": {
                "roll_number": {
                    "type": "keyword"
                },
                "name": {
                    "type": "text"
                },
                "age": {
                    "type": "integer"
                },
                "grade": {
                    "type": "keyword"
                },
                "email": {
                    "type": "keyword"
                }
            }
        }
    }

    es.indices.create(index="student_index", body=index_mapping, ignore=400)  # ignore 400 errors (index already exists)

# Generate 1000 fake student records
def generate_students(num_students=1000):
    fake = Faker()
    students = []

    for i in range(1, num_students + 1):
        student = {
            "_index": "student_index",
            "_source": {
                "roll_number": str(i),
                "name": fake.name(),
                "age": random.randint(18, 25),
                "grade": random.choice(["A", "B", "C", "D", "E"]),
                "email": fake.email()
            }
        }
        students.append(student)

    return students

# Insert the student records into the index
def insert_students(students):
    helpers.bulk(es, students)

if __name__ == "__main__":
    create_index()  # Create the index
    students = generate_students()  # Generate student records
    insert_students(students)  # Insert records into Elasticsearch
    print("1000 student records inserted successfully.")
