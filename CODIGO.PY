# passo a passo do programa

# (cadastro de produtos - automação)

#bibliotecas
import pyautogui
import time

pyautogui.alert("A automação vai começar. Não mexa no mouse/teclado!")

#colinha

#pyautogui.click -> clica                         
#pyautogui.write -> escreve
#pyautogui.press -> aperta tecla
#pyautogui.hotkey -> aperta atalho (hotkey)

#passo 1: Entrar no sistema
#abrir navegador

link='https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
# fazer uma pausa para carregar o site
time.sleep(3)

# passo 2: Fazer login

#click no campo (login)
pyautogui.click(x=769, y=408)
pyautogui.write('login') # escreve o login
pyautogui.press('tab') #passa para o prox. campo
pyautogui.write('senhadificilantihack') #escreve a senha
pyautogui.press('tab') #passa para o botão (enter)
pyautogui.press('enter')
#fazer uma pausa para carregar o site
time.sleep(3)

# Passo 3: Abrir base de dados e importar o arquivo csv
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    # passo 4: cadastrar um produto
    #código do produto

    pyautogui.click(x=855, y=292) #clica no campo (cod do produto)
    codigo = str(tabela.loc[linha, 'codigo'])
    
    pyautogui.write(codigo)
    pyautogui.press('tab') #passa para o prox campo
    
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
   
     #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
   
    #categoria
    categoria  = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
   
    #preco
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
   
    #custo
    custo = str(tabela.loc[linha, 'custo']) 
    pyautogui.write(custo)
    pyautogui.press('tab')
   
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs!= 'nan': # se ob !=(diferente) de nan (vazio) -(pula obs)
         pyautogui.write(obs)
    pyautogui.press('tab') #passa para o botão enviar

    pyautogui.press('enter') #clica em enviar
    
    # voltar para o inicio da tela (topo do site)
    pyautogui.scroll(5000)


# passo 5: Repetir os cadastros (passo 4) até acabar a lista
