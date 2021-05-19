from kafka import KafkaProducer
import gzip
import pickle

producer = KafkaProducer(acks=0,
                         bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: x.tobytes()
)

with gzip.open('./label', 'rb') as f:
    label = pickle.load(f)
print(label)

producer.send('pickle', label)
producer.flush()
print('[end] send producer')
