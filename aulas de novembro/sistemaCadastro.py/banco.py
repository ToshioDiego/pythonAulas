import mysql.connector

class BancoDados:
    def __init__(self):
        self.cadastrar = mysql.connector.connect(
            user='Toshio', 
            password='DiegoToshio.2003',
            host='10.28.1.135', 
            database="cadastrar"
        )
        if self.cadastrar.is_connected():
            database_informacao = self.cadastrar.get_server_info()
            print(f"Conectado ao Banco de Dados = {database_informacao}")
            
        self.cursor = self.cadastrar.cursor()

    def Registrar_valores(self, nome, email, senha):
        today = "insert into TelaDeCadastro (nome, email, senha) values (%s, %s, %s)"
        values = (nome, email ,senha)

        self.cursor.execute(today, values)
        self.cadastrar.commit()
        print(self.cursor.rowcount, "registro(s) inserido(s).")
        
        
    def Editar_valores(self, nome,email,senha,id_nome):
        editarsalve = 'update TelaDeCadastro set nome =%s, email =%s, senha=%s where id_nome=%s'
        cadastroedit=(nome,email,senha,id_nome)
        try :
            self.cursor.execute(editarsalve,cadastroedit)
            self.cadastrar.commit()
            print("Usuário editado com sucesso!")
        except Exception as e:
            self.cadastrar.rollback()
            print(f"Erro ao editar usuário: {e}")
        finally:
            self.cursor.close()

        print(self.cursor.rowcount, "registro(s) editado(s).")  
        
    def Excluir_valores(self, id_nome):
        deletecadastro=f"DELETE FROM TelaDeCadastro WHERE id_nome={id_nome}"
        try:
            self.cursor.execute(deletecadastro)
            self.cadastrar.commit()
            print("Usuário excluido com sucesso!")
        except Exception as e:
            self.cadastrar.rollback()
            print(f"Erro ao excluir usuário: {e}")
        finally:
            self.cursor.close()

        print(self.cursor.rowcount, "registro(s) excluido(s).") 
        
        '''delete_query = "delete from TelaDeCadastro where id_nome = %s;"
        delete_data = (id,)

        self.cursor.execute(delete_query, delete_data)
        self.cadastrar.commit()'''
        
    def lista_valores(self):

        consulta_mysql = "select * from TelaDeCadastro"
        self.cursor.execute(consulta_mysql)
        linhas = self.cursor.fetchall()

        for linha in linhas:
                print("-="*20)
                print(f"Id = {linha[0]}")
                print(f"nome = {linha[1]}")
                print(f"email = {linha[2]}")
                
        self.cadastrar.commit()
        
    def fechar_conexao(self):
        if self.cadastrar.is_connected():
            self.cadastrar.close()
            print("Conexão encerrada")
            print("-=" * 20)

        