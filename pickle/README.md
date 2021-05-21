# Pub/Sub a python pickle file via kafka-python

## Producer
Producer transforms pickle file which contains numpy array instance to bytes.

![pickle-producer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-16-kafka-pickle/pickle-producer.png?raw=true)

## Consumer
Consumer reconstructs bytes to numpy array.

![pickle-consumer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-16-kafka-pickle/pickle-consumer.png?raw=true)

A shape of numpy array may differ from the original one because of the operation of `tobytes()` and `numpy.frombuffer()`. You ought to change its shape if you need. 