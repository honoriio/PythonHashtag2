import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
           "Server=localhost;"
           "Database=Sql/chinook.db")


conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM artists WHERE name = ?", ("BackBeat",))
resultado = cursor.fetchall()
cursor.commit()
print(resultado)

cursor.close()
conexao.close()