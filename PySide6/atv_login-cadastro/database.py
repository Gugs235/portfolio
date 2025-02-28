# database.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='atv_Mauricio_cadastro',
            user='suporte',
            password='suporte'
        )
        if connection.is_connected():
            print("Conexão bem-sucedida com o banco de dados!")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def insert_user(nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro, foto=None, senha=None):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = '''
                INSERT INTO usuarios (nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro, foto, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            valores = (nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro, foto, senha)
            print("Valores recebidos:", valores)
            cursor.execute(query, valores)
            connection.commit()
            print("Cadastro realizado com sucesso!")
        except Error as e:
            print(f"Erro ao inserir usuário: {e}")
            raise
        finally:
            cursor.close()
            connection.close()
            print("Conexão fechada.")
    else:
        print("Não foi possível conectar ao banco de dados.")

def get_user(nome, senha):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT nome, foto FROM usuarios WHERE nome = %s AND senha = %s"
            cursor.execute(query, (nome, senha))
            result = cursor.fetchone()
            if result:
                print(f"Usuário encontrado: {result}")
                return {"nome": result[0], "foto": result[1]}
            else:
                print("Nenhum usuário encontrado com esse nome e senha.")
                return None
        except Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
            print("Conexão fechada.")
    return None