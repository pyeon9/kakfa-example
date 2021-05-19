from kafka import KafkaConsumer
import numpy as np

consumer = KafkaConsumer('pickle',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='pickle-group',
                         consumer_timeout_ms=1000,
                         value_deserializer=lambda x: np.frombuffer(x)
)

print('[begin] get consumer list')
for message in consumer:
    print("Topic: %s, Offset: %d, Value: %s" % \
            (message.topic, message.offset, message.value)
    )
print('[end] get consumer list')

