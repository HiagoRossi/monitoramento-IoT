from kafka import KafkaConsumer
import json
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'dados', 'dados_sensores.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Conexão com o SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Cria a tabela caso não exista 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        acao_feita TEXT,
        sistema TEXT,
        momento TEXT
    )
''')
conn.commit()

# Kafka consumer
consumer = KafkaConsumer(
    'meu-topico',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-santander'
)

print("📡 Aguardando mensagens do Kafka...")

for mensagem in consumer:
    try:
        dado = mensagem.value
        print(f"📥 Mensagem recebida 👉 Nome: {dado['nome']} | Ação: {dado['acao_feita']} | Sistema: {dado['sistema']} | Momento: {dado['momento']}")

        cursor.execute('''
            INSERT INTO sensores (nome, acao_feita, sistema, momento)
            VALUES (?, ?, ?, ?)
        ''', (dado['nome'], dado['acao_feita'], dado['sistema'], dado['momento']))
        conn.commit()
        
    except Exception as e:
        print("⚠️ Erro ao processar a mensagem:", e)
        print("🧾 Conteúdo cru da mensagem:", mensagem.value)