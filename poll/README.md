# Subsribe messages via `consumer.poll()` method

## Producer
Producer sends strings encoded in 'utf-8'.

## Consumer
Consumer polls topic periodically. If consumes some messages, consumer prints them. But if if fails to consume, prints 'No messages' and sleeps for 3 seconds. 

![consumer-first-poll](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-18-kafka-poll/02-consumer-fisrt-poll.png?raw=true)

![consumer-second-poll](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-18-kafka-poll/03-consumer-second-poll.png?raw=true)