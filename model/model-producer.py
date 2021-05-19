from kafka import KafkaProducer
from json import dumps
import tensorflow as tf

producer = KafkaProducer(acks=0,
                         bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8')
)

model = tf.keras.models.load_model('./classifier.h5')
print(model)
json_model = model.to_json()

producer.send('model', json_model)
producer.flush()
print('[end] send producer')
