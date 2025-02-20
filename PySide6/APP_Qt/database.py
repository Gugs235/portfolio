# database.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # ou o endereço do seu servidor MySQL
            database='atv_Mauricio_cadastro',
            user='suporte',  # substitua pelo seu usuário do MySQL
            password='suporte'  # substitua pela sua senha do MySQL
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def insert_user(nome, email, cpf, telefone, endereco, data_nascimento, sexo):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = '''
            INSERT INTO usuarios (nome, email, cpf, telefone, endereco, data_nascimento, sexo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (nome, email, cpf, telefone, endereco, data_nascimento, sexo))
        connection.commit()
        cursor.close()
        connection.close()