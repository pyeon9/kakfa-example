from kafka import KafkaConsumer
from json import loads
import tensorflow as tf

consumer = KafkaConsumer('model',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='model-group',
                         consumer_timeout_ms=1000,
                         value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print('[begin] get consumer list')
for message in consumer:
    print("Topic: %s, Offset: %d, Value: %s" % \
            (message.topic, message.offset, message.value)
    )
    json_model = message.value
print('[end] get consumer list')

model = tf.keras.models.model_from_json(json_model)
print(model)

