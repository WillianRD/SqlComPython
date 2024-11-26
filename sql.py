import sqlite3

from App import Produto

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("meu_banco.db")
cursor = conn.cursor()

# Criar a tabela, se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        desc TEXT NOT NULL,
        date TEXT
    )
''')

# Criando um objeto Produto
produto = Produto(name="Hardware", desc="Intel ")

# Inserindo dados na tabela
cursor.execute("INSERT INTO produtos (name, desc) VALUES (?, ?)", (produto.name, produto.desc))
conn.commit()  # Commitando as alterações

# Deletando dados
nome_produto = "Produto X"
cursor.execute("DELETE FROM produtos WHERE name = ?", (nome_produto,))
conn.commit()

# Selecionando todos os dados
cursor.execute("SELECT * FROM produtos")
for exibirDados in cursor.fetchall():
    print(exibirDados)

# Fechando a conexão
cursor.close()
conn.close()
