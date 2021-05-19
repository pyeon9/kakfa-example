from kafka import KafkaProducer
import time

producer = KafkaProducer(acks=0, compression_type='gzip', \
			bootstrap_servers=['localhost:9092'], \
			value_serializer=lambda x: x.encode('utf-8')
)

start = time.time()
for i in range(10):
    data = str(i)
    producer.send('poll', value=data)
    producer.flush()
print('elapsed :', time.time() - start)
