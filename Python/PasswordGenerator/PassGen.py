import random, pyperclip, time
import PySimpleGUI as sg

layout = [[sg.T('Password Generator')],
          [sg.T('Characters : '), sg.Spin([i for i in range(9, 31)], key='length')],
          [sg.T('Password   : '), sg.T(key='output', size=(35, 1))],
          [sg.Button('COPY'), sg.Button('GENERATE'), sg.Exit('EXIT')]]
window = sg.Window('Password Generator', layout, margins=(10,10))

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '-', '_']

passw = ''

while True:
    event, values = window.read()
    if event in ('EXIT', sg.WIN_CLOSED):
        break
    if event == 'GENERATE':
        length = values['length']
        passw = ''
        for i in range(int(length)):
            passw = passw + random.choice(chars)
        if len(passw) > 30:
            window['output'].update('Password too long, already copied')
            pyperclip.copy(passw)
        else:
            window['output'].update(str(passw))

    if event == 'COPY':
        if passw == '':
            pyperclip.copy('Hello people i am an innocent man.')
            window['output'].update('Copied nothing')
        else:
            pyperclip.copy(passw)
            window['output'].update('Copied!')

window.close()