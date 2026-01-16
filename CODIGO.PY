# passo a passo do programa

# (cadastro de produtos - automação)

#bibliotecas
import pyautogui as py
import time

py.alert("A automação vai começar. Não mexa no mouse/teclado!")

#colinha

#py.click -> clica                         
#py.write -> escreve
#py.press -> aperta tecla
#py.hotkey -> aperta atalho (hotkey)

#passo 1: Entrar no sistema
#abrir navegador

link='https://dlp.hashtagtreinamentos.com/python/intensivao/login'

py.PAUSE = 0.5
py.press('win')
py.write('chrome')
py.press('enter')

py.write(link)
py.press('enter')
# fazer uma pausa para carregar o site
time.sleep(3)

# passo 2: Fazer login

#click no campo (login)
py.click(x=769, y=408)
py.write('login') # escreve o login
py.press('tab') #passa para o prox. campo
py.write('senhadificilantihack') #escreve a senha
py.press('tab') #passa para o botão (enter)
py.press('enter')
#fazer uma pausa para carregar o site
time.sleep(3)

# Passo 3: Abrir base de dados e importar o arquivo csv
import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    # passo 4: cadastrar um produto
    #código do produto

    py.click(x=855, y=292) #clica no campo (cod do produto)
    codigo = str(tabela.loc[linha, 'codigo'])
    
    py.write(codigo)
    py.press('tab') #passa para o prox campo
    
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    py.write(marca)
    py.press('tab')
   
     #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    py.write(tipo)
    py.press('tab')
   
    #categoria
    categoria  = str(tabela.loc[linha, 'categoria'])
    py.write(categoria)
    pyi.press('tab')
   
    #preco
    preco = str(tabela.loc[linha, 'preco_unitario'])
    py.write(preco)
    py.press('tab')
   
    #custo
    custo = str(tabela.loc[linha, 'custo']) 
    py.write(custo)
    py.press('tab')
   
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs!= 'nan': # se obs !=(diferente) de nan (vazio) -(pula obs)
         py.write(obs)
    py.press('tab') #passa para o botão enviar

    py.press('enter') #clica em enviar
    
    # voltar para o inicio da tela (topo do site)
    py.scroll(5000)


# passo 5: Repetir os cadastros (passo 4) até acabar a lista
