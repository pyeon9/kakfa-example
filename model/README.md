# Pub/Sub a TF 2.0 model file(.h5) via kafka-python

## Producer
Producer dumps `.h5` file with encoding 'utf-8' via json.

![model-producer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-17-kafka-model/model-producer.png?raw=true)

## Consumer
Consumer decodes and load json file. Then reconstruct model via `tensorflow.keras.models.model_from_json()` function. 

![model-consumer](https://github.com/pyeon9/images-for-github-page/blob/main/kafka-hdfs/2021-05/05-17-kafka-model/model-consumer.png?raw=true)
