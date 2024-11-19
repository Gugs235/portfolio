import customtkinter as ctk

# .place(x= , y=) - a posição que vc quer que o objeto fique
# .get() - Para salvar um input para usar em outra tela 
# .destry() - Para fechar a tela


# criando a tela
janela = ctk.CTk()

# tamanho da tela
janela.geometry("500x500")

# Mudando a cor da tela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# mostrando texto
txt1 = ctk.CTkLabel(janela , text = "Bem-vindo")
txt1.pack()
txt1.place(x=225, y=100)

# input
input1 = ctk.CTkEntry(janela, placeholder_text="Qual é o seu nome?")
input1.pack()
# input1.place(x= ,y=)

# botao
btn1 = ctk.CTkButton(janela, text="Entrar", command = None)
btn1.pack()
# btn1.place(x= ,y=)








































































# para manter a janela aberta
janela.mainloop()
