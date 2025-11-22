import sqlite3

DB_NAME = "floricultura.db"

def get_connection():
    """Cria e retorna uma conexão com o banco."""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Cria a tabela e popula com dados iniciais."""
    conn = get_connection() # Usa a função acima
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cor TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    
    cursor.execute("SELECT count(*) FROM flores")
    if cursor.fetchone()[0] == 0:
        dados_iniciais = [
            ("Rosa", "Vermelha", 50, 5.0),
            ("Rosa", "Branca", 20, 6.0),
            ("Tulipa", "Amarela", 15, 4.5),
            ("Orquídea", "Roxa", 5, 25.0)
        ]
        cursor.executemany("INSERT INTO flores (nome, cor, quantidade, preco) VALUES (?, ?, ?, ?)", dados_iniciais)
        conn.commit()
        print("Banco de dados inicializado.")
    
    conn.close()