# kakfa-example
A simple example code of producer &amp; consumer for kafka-python.
Both producer and consumer works on local machine. 
If you want to consume messages on other machine, change `localhost` in line 4 of `consumer.py` to the IP of kakfa server.


1. Execute producer.py
```
  $ python producer.py
```
You can see the result like below. About 0.63s was taken to send 1,000 messages.

![producer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-04/04-21-kafka-example/02-producer.png?raw=true)

2. Execute consumer.py
```
  $ python consumer.py
```
You can see the messages like below. 

![consumer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-04/04-21-kafka-example/03-consumer.png?raw=true)


For more information, visit [my GitHub Page post](http://127.0.0.1:4000/blog/kafka-hdfs/2021-04-21-kafka-example/) written in Korean.