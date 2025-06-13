from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPICO = 'meu-topico'

print("Enviando mensagens para o Kafka...")

while True:
    mensagem = {
        'nome': fake.first_name(),  # Procurar por nome de pessoas
        'acao_feita': random.choice(['inseriu dado', 'deletou coluna', 'atualizou tabela']),
        'sistema': random.choice(['Azure Databricks']),
        'momento': fake.date_time().strftime('%d/%m/%Y %H:%M')
    }

    print("Enviando:", mensagem)
    producer.send(TOPICO, mensagem)
    time.sleep(1)  # 1 segundo entre cada mensagem
