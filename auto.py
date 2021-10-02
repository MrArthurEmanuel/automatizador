from tkinter import font
from tkinter.constants import CENTER, LEFT, RIGHT
from tkinter.ttk import Style
import PySimpleGUI as sg
import os 

class Automacao:
    def __init__(self):
        sg.theme('DarkBlack')


        layout = [
            
            [sg.Text('                          Automatizador Transmissão PIB',font=('Impact', '15'))],
            [sg.Text('Operador:',font=('Impact', '17'), size=(10,1)), sg.Input(key='user')],
            [sg.Button('Abrir Programas e Páginas', font=('Impact', '15'), expand_x=True, border_width='7')],
            [sg.Button('Tutorial de uso',font=('Impact', '15'), expand_x=True, border_width='7')],
            

        ]

        self.janela = sg.Window('Automatizador PIB', layout)




    def Iniciar(self):
        while True:
            eventos,valores = self.janela.read()

            
            if eventos == 'Abrir Programas e Páginas':
                
                sg.popup(f"Bom Culto {valores['user']}\nAperte Ok para continuar", font=('Arial', '15'), title='Aviso')
                #os.startfile('https://www.facebook.com/live/producer/?entry_point=pages_feed&target_id=255088104520467')
                #os.startfile('https://studio.youtube.com/channel/UCtLCyrfDtjKtZJtiu-ECErQ/livestreaming/dashboard')
                
                break
        
            if eventos == 'Tutorial de uso':
                sg.popup('''1 - ESSE É O PROGRAMA MAIS SIMPLES DE USAR.
                \n2 - Coloque seu nome ali no campo "Operador" (É só um charminho)
                \n3 - Depois, basta clicar no botão "Abrir Programas e Páginas e esperar os programas e as páginas carregarem.
                \n4 - Irá abrir automaticamente a página do Facebook e do YouTube (Ambas na parte das transmissões)
                \n5 - O programa irá fechar automaticamente depois de ter iniciado tudo, não se assuste.
                \n6 - NÃO CLIQUE MAIS DE UMA VEZ NO BOTÃO DE ABRIR PELO AMOR DE GOD. Tenha fé, ele vai abrir''', title='Tutorial do programa')


            if eventos == sg.WINDOW_CLOSED:
                break


auto = Automacao()
auto.Iniciar()
