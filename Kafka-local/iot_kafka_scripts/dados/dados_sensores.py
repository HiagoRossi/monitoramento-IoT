import sqlite3

conn = sqlite3.connect('dados_sensores.db')  
cursor = conn.cursor()

# Consulta os últimos registros com limite de 10 
cursor.execute("SELECT * FROM sensores ORDER BY id DESC LIMIT 10")
linhas = cursor.fetchall()

print("📊 Últimos 10 dados recebidos:")
for linha in linhas:
    print(f"🧾 ID: {linha[0]} | Nome: {linha[1]} | Ação: {linha[2]} | Sistema: {linha[3]} | Momento: {linha[4]}")

conn.close()
