# database.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Verifique se este é o host correto
            database='atv_Mauricio_cadastro',
            user='suporte',  # Substitua pelo usuário correto
            password='suporte'  # Substitua pela senha correta
        )
        if connection.is_connected():
            print("Conexão bem-sucedida com o banco de dados!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def insert_user(nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
                INSERT INTO usuarios (nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            print("Valores recebidos:")  # Para verificar os dados recebidos
            valores = (nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro)
            cursor.execute(query, valores)
            connection.commit()
            print("Cadastro realizado com sucesso!")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()
            connection.close()
            print("Conexão fechada.")
    else:
        print("Não foi possível conectar ao banco de dados.")
