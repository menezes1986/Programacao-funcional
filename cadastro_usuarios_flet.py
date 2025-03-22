import flet as ft 
import hashlib
import json

#Função para o gerenciador de credenciais de usuario implementado por Miguel Angêlo
def gerenciar_credenciais():   #Funão de Ordem Alta
#criado um banco fake para o armazenamento das credenciais
    credenciais_local = {}
    def adicionar_usuarios(nome, email,senha):
        if email in credenciais_local:
            return "Erro E-mail já cadastrado"
        credenciais_local[email] = {"nome": nome, "senha": hashlib.sha256(senha.encode()).hexdigest()}
        return "Usuário cadastrado com sucesso!"
#Verificação de usuario criado por Estephane Raely usando a função lambda
    verifica_usuario = lambda email: email in credenciais_local 
#listargem de usuarios criado por Mauricio Viana
    def listar_usuarios():
        return [(dados["nome"], email) for email,dados in credenciais_local.items()]
    
    return adicionar_usuarios,verifica_usuario,listar_usuarios

adicionar_usuarios, verificar_usuario, listar_usuarios = gerenciar_credenciais()

#A interface do flet python foi criada e implementada por Inacio Oliveira e Carla Daniele
def main(page:ft.Page):
#titulo da pagina
    page.title = "Cadastro de Usuarios > Grupo"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    #labels da tela inicial
    nome =  ft.TextField(label="Nome")
    Email =  ft.TextField(label="Email")
    senha = ft.TextField(label="Senha", password=True)
    mensagem = ft.Text()
    
    #imagem da janela do projeto
    imagem = ft.Image(src="grupo1_ads_pf.jfif",width=150,height=150)
    
    #fuções da tela do front flet enviadas para back implementada por Inácio Oliveira
    def cadastrar(e):
        if verificar_usuario(Email.value):
            mensagem.value = "Erro email já cadastrado!"
        else:
            resultado = adicionar_usuarios(nome.value,Email.value,senha.value)
            mensagem.value = resultado
            nome.value=""
            Email.value=""
            senha.value=""
        page.update()
    btn_cadastrar = ft.ElevatedButton("Cadastrar", on_click= cadastrar)
    
    def listar_usuarios_handler(e):
        usuarios = [ft.Text(f"Nome: {nome} | Email: {email}") for nome, email in listar_usuarios()]
        page.add(*usuarios)
    
    btn_listar = ft.ElevatedButton("Listar Usuários", on_click=listar_usuarios_handler)
    
    page.add(imagem, nome, Email, senha, btn_cadastrar, btn_listar, mensagem)

ft.app(target=main)
        
            
    
    