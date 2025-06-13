# monitoramento-IoT

## Projeto: Monitoramento de Sensores IoT com Kafka
Este projeto simula o monitoramento de sensores de uma área de engenharia de dados, utilizando um fluxo com Kafka e SQLite.

## Objetivo:
Criar um sistema de envio (Producer) e recebimento (Consumer) de dados simulados de sensores, com salvamento local em um banco SQLite. Conceitos de streaming de dados, mensageria com Kafka e armazenamento no Banco.

## Tecnologias utilizadas: 
Python, Kafka (via Docker), Kafka-Python, Faker, SQLite3

## Para rodar o projeto é preciso:
Subir o Kafka via Docker: docker-compose up -d

## Instale as dependências Python: 
pip install kafka-python faker

## Rode o Producer:  
python3 producer.py

## Rode o Consumer (em outro terminal): 
python3 consumer.py

## Para visualizar os dados salvos (opcional):
python3 dados_sensores.py
