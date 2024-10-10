import pyautogui
import time

# pyautogui.write -> escreve um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> aperta uma tecla 
# pyautogui.hotkey -> aperta um atalho de teclado (Ctrl, C)
# pythongui.PAUSE - define um tempo de espera para o proximo comando

# Passo 1: Entrar no Sistema da Empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o navegador 
#apertar a tecla win

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=819, y=515)



# Passo 2: Fazer o Login
time.sleep(5)
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=3275, y=476)
pyautogui.write("pythonimpressinador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha aqui")
pyautogui.click(x=3598, y=675)

time.sleep(2)
# Passo 3: Importar base de dados
import pandas


tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar 1 produto



linha = 0

# para cada linha da minha tabela copiar codigo do formulario
# Passo 5 Repetir o processo de cadatro até acabar os produtos
for linha in tabela.index:
    #codigo
    pyautogui.click(x=3464, y=323)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

  


    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")






