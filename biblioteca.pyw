import PySimpleGUI as sg
import os
from random import randint, choice

file_name = randint(10000000, 99999999)
files = [file for file in os.listdir("./") if file.endswith(".flok")]
text_size = sum([len(open(file, "r").read()) for file in files])
pages = len(files)

sg.theme('DarkGrey9')  

layout = [    [sg.Menu([['Configurações', ['Fechar', 'Apagar Dados', 'Sobre-mim']]], background_color='#ffffff', text_color='#000000')],
    [sg.Column(        [[sg.Text(f'Caracteres Escritos: {text_size}', font=(None, 12), text_color='White')],
         [sg.Text(f'Paginas Escritas: {pages}', font=(None, 12), text_color='White')],
         [sg.Button('Salvar', size=25)],
         [sg.Button('Abrir Aleatorio', size=25)]], pad=(25,0), element_justification='center'),
     sg.Column(
        [[sg.Multiline(size=(999, 999), font=(None, 18), no_scrollbar=True, pad=0, key='text', text_color='white')]], element_justification='right', pad=0)]
]

window = sg.Window(file_name, margins=(0,0), size=(800, 400), resizable=True).Layout(layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Fechar'):
        break

    if event == 'Apagar Dados' and sg.popup_yes_no('Você tem certeza?\nVocê tem certeza mesmo?', background_color='#ffffff', button_color='#ff4444', text_color='#000000') == 'Yes':
        [os.remove(delete) for delete in files]
        break

    if event == 'Sobre-mim':
        sg.popup('Opa, Meu nome é Gabriel e eu quero ser um programador, esse programa foi feito no intuito de aprender, ou seja, no futuro farei um bem melhor!', background_color='#ffffff', button_color='#eeeeee', text_color='#000000', title='Sobre-mim')

    if event == 'Salvar' and sg.popup_yes_no('Você tem certeza? Ao salvar o programa será fechado', background_color='#ffffff', button_color='#dddddd', text_color='#000000') == 'Yes':
        with open(f'{file_name}.flok', 'w') as f:
            f.write(values['text'])
            break
    
    if event == 'Abrir Aleatorio':
        if not files:
            sg.popup_quick_message('Ainda não existe paginas.', background_color='#ffffff', text_color='#000000')
        else:
            arquivo = choice(files)
            sg.popup_quick_message(f'{arquivo} aberto.', background_color='#ffffff', text_color='#000000')

            with open(arquivo, 'r') as f:
                content = f.read()
                window['text'].update(content)
            file_name = arquivo.replace('.flok', '')
            window.TKroot.title(arquivo)

window.close()
