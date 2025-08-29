import customtkinter as ctk
import re

# Definindo aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Função para verificar segurança das senhas
def verificar_senha(senha):
    pontuacao = 0

    # Verificando comprimento da senha
    if len(senha) >= 8:
        pontuacao += 1

    # Verificando se há letras maiúsculas
    if re.search(r'[A-Z]', senha):
        pontuacao += 1

    # Verificando se há letras minúsculas
    if re.search(r'[a-z]', senha):
        pontuacao += 1

    # Verificando se há números
    if re.search(r'[0-9]', senha):
        pontuacao += 1

    # Verificando se há caracteres especiais
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        pontuacao += 1

    # Classificação
    if pontuacao <= 2:
        return "Fraca", pontuacao
    elif pontuacao <= 4:
        return "Média", pontuacao
    else:
        return "Forte", pontuacao

# Função para alternar a visibilidade da senha
def alternar_visibilidade():
    if campo_senha.cget('show') == '•':
        campo_senha.configure(show='')
        botao_mostrar_senha.configure(text="Ocultar")
    else:
        campo_senha.configure(show='•')
        botao_mostrar_senha.configure(text="Mostrar")

# Função para validar a senha na interface
def validar_senha():
    senha = campo_senha.get()
    
    if senha:
        resultado, pontuacao = verificar_senha(senha)
        
        # Atualizar o resultado
        resultado_label.configure(text=f"Força: {resultado}")
        
        # Atualizar a barra de progresso
        progresso = pontuacao / 5  # Convertendo para escala 0-1
        barra_progresso.set(progresso)
        
        # Mudar cor baseada na força
        if resultado == "Fraca":
            barra_progresso.configure(progress_color="red")
            resultado_label.configure(text_color="red")
        elif resultado == "Média":
            barra_progresso.configure(progress_color="orange")
            resultado_label.configure(text_color="orange")
        else:
            barra_progresso.configure(progress_color="green")
            resultado_label.configure(text_color="green")
            
        # Mostrar detalhes
        mostrar_detalhes(senha, pontuacao)
    else:
        resultado_label.configure(text="Digite uma senha primeiro!")

# Função para mostrar detalhes da senha
def mostrar_detalhes(senha, pontuacao):
    detalhes = ""
    
    # Comprimento
    if len(senha) >= 8:
        detalhes += "✓ Comprimento adequado (8+ caracteres)\n"
    else:
        detalhes += "✗ Comprimento insuficiente (<8 caracteres)\n"
    
    # Maiúsculas
    if re.search(r'[A-Z]', senha):
        detalhes += "✓ Contém letras maiúsculas\n"
    else:
        detalhes += "✗ Não contém letras maiúsculas\n"
    
    # Minúsculas
    if re.search(r'[a-z]', senha):
        detalhes += "✓ Contém letras minúsculas\n"
    else:
        detalhes += "✗ Não contém letras minúsculas\n"
    
    # Números
    if re.search(r'[0-9]', senha):
        detalhes += "✓ Contém números\n"
    else:
        detalhes += "✗ Não contém números\n"
    
    # Caracteres especiais
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        detalhes += "✓ Contém caracteres especiais\n"
    else:
        detalhes += "✗ Não contém caracteres especiais\n"
    
    detalhes_label.configure(text=detalhes)

# Criar a janela principal
app = ctk.CTk()
app.title("Verificador de Segurança de Senhas")
app.geometry("500x550")

# Título
titulo = ctk.CTkLabel(app, text="Verificador de Força de Senhas", 
                     font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

# Campo de senha
frame_senha = ctk.CTkFrame(app)
frame_senha.pack(pady=10)

label_senha = ctk.CTkLabel(frame_senha, text="Digite sua senha:", 
                          font=ctk.CTkFont(size=14))
label_senha.pack(pady=5)

# Frame para campo de senha e botão de mostrar/ocultar
frame_campo_senha = ctk.CTkFrame(frame_senha, fg_color="transparent")
frame_campo_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(frame_campo_senha, placeholder_text="Sua senha...", 
                          show="•", width=250, height=40,
                          font=ctk.CTkFont(size=14))
campo_senha.pack(side="left", padx=(0, 5))

botao_mostrar_senha = ctk.CTkButton(frame_campo_senha, text="Mostrar Senha", 
                                   width=80, height=40,
                                   command=alternar_visibilidade)
botao_mostrar_senha.pack(side="left")

# Botão de verificação
botao_verificar = ctk.CTkButton(app, text="Verificar Segurança", 
                               command=validar_senha,
                               height=40, width=200,
                               font=ctk.CTkFont(size=14))
botao_verificar.pack(pady=10)

# Barra de progresso
barra_progresso = ctk.CTkProgressBar(app, width=300, height=20)
barra_progresso.set(0)
barra_progresso.pack(pady=10)

# Label de resultado
resultado_label = ctk.CTkLabel(app, text="Digite uma senha para verificar", 
                              font=ctk.CTkFont(size=16, weight="bold"))
resultado_label.pack(pady=10)

# Frame para detalhes
frame_detalhes = ctk.CTkFrame(app)
frame_detalhes.pack(pady=20, padx=20, fill="both", expand=True)

detalhes_titulo = ctk.CTkLabel(frame_detalhes, text="Detalhes da Análise:", 
                              font=ctk.CTkFont(size=14, weight="bold"))
detalhes_titulo.pack(pady=5)

detalhes_label = ctk.CTkLabel(frame_detalhes, text="", 
                             font=ctk.CTkFont(size=12),
                             justify="left")
detalhes_label.pack(pady=10, padx=10)

# Dica de segurança
dica_label = ctk.CTkLabel(app, 
                         text="Dica: Use pelo menos 8 caracteres com maiúsculas, minúsculas, números e símbolos",
                         font=ctk.CTkFont(size=10),
                         text_color="gray")
dica_label.pack(pady=10)

# Iniciar a aplicação
app.mainloop()