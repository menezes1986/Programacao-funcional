import flet as ft
import hashlib
import json

# Banco de dados fictício para armazenar credenciais
credenciais = {}

# Função para hash de senha
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função de ordem superior para verificar se o usuário já está cadastrado
def verificar_usuario_existente(verificacao_func):
    def verificar(email):
        return verificacao_func(email)
    return verificar

# Closure para armazenar credenciais
def gerenciar_credenciais():
    credenciais_local = {}
    def listar_usuarios():
        return list(credenciais_local.keys())
    
    def adicionar_usuario(email, senha):
        if email in credenciais_local:
            return "Usuário já cadastrado!"
        credenciais_local[email] = hash_senha(senha)
        return "Usuário cadastrado com sucesso!"
    
    def verificar_usuario(email):
        return email in credenciais_local
    
    return adicionar_usuario, verificar_usuario, listar_usuarios

adicionar_usuario, verificar_usuario, listar_usuarios = gerenciar_credenciais()

verificar_usuario_cadastrado = verificar_usuario_existente(verificar_usuario)

# Interface Flet
def main(page: ft.Page):
    page.title = "Cadastro Seguro"
    page.theme_mode = ft.ThemeMode.LIGHT

    email = ft.TextField(label="Email")
    senha = ft.TextField(label="Senha", password=True)
    mensagem = ft.Text()

    def cadastrar(e):
        resultado = adicionar_usuario(email.value, senha.value)
        mensagem.value = resultado
        page.update()
    
    btn_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    
    # Lista comprehension para mostrar usuários cadastrados
    def listar_usuarios_handler(e):
        usuarios = "\n".join([f"Nome: {nome} | Email: {email}" for nome, email in listar_usuarios()])
        dialog.content = ft.Text(usuarios if usuarios else "Nenhum usuário cadastrado.")
        dialog.open = True
        page.update()
    
    btn_listar = ft.ElevatedButton("Listar Usuários", on_click=listar_usuarios_handler)
    
    page.add(imagem, nome, email, senha, btn_cadastrar, btn_listar, mensagem)

ft.app(target=main)
ft.app(target=main)
