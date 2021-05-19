from kafka import KafkaConsumer
from time import sleep

consumer = KafkaConsumer('poll',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='pickle-group',
                         consumer_timeout_ms=1000,
                         value_deserializer=lambda x: x.decode('utf-8')
)

while True:
    batch = consumer.poll(timeout_ms=1000)
    if len(batch.items()) > 0:
        print('## Message Received!')
        for partition, messages in batch.items():
            for message in messages:
                print("Topic: %s, Offset: %d, Value: %s" % \
                    (message.topic, message.offset, message.value)
                )
    else:
        print('No messages')
        sleep(3)

