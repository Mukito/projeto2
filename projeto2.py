import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

#-----------------------------------------------------------------------------------------------
# Aqui vc adciona o Codigo da Ação para a analise (Ex. BBAS3.SA, PETR4.SA)
ticker = input("Digite o codigo da ação desejada: ")

# Aqui vc Digita a Data inicial
inicio = input("Digite a Data Inicial: (Ano) XXXX- (Mes) XX- (Dia) XX:\n")

# Aqui vc Digita a Data Final
fim = input('Digite a Data Final:(Ano) XXXX- (Mes) XX- (Dia) XX:\n')

dados = yfinance.Ticker(ticker).history(start=inicio, end=fim)
fechamento = dados.Close
#-----------------------------------------------------------------------------------------------

# Aqui vc adciona o Codigo da Ação para a analise (Ex. BBAS3.SA, PETR4.SA)
# ticker = input("Digite o codigo da ação desejada: ")

#dados = yfinance.Ticker(ticker).history(start="2020-12-01", end="2021-01-01")
#fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)



destinatario1 = "mukito100@gmail.com"
#destinatario2 = "mukitoprograma@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f"""

Prezado gestor,

Segue as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação Mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atenciosamente
Fabiano Santos Ramos
Analista de Sistemas
(61)98646-2326

"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botao escrever
pyautogui.click(x=-1834, y=189)

# digitar o email do destinatario e teclar TAB
pyperclip.copy(destinatario1)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# clicando para enviar
pyautogui.click(x=-602, y=1006)

#---------------------------------------------------------------
# Fechar o Gmail
pyautogui.hotkey("ctrl", "f4")


print(f"""\n
-----------------------------------\n      
Codigo: {ticker}\n
inicio: {inicio}\n 
Fim: {fim}\n
------------------------------------\n
""")
print("OPERAÇÃO REALIZADA COM SUCESSO!!!")