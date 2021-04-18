import PySimpleGUI as sg
import random, pyperclip
from datetime import datetime

global time

layout = [[sg.Text('Dice Roller')], [sg.Spin([i for i in range(1,11)], key='many'), sg.T('Dices will be rolled')],
          [sg.T('This will choose from 1-6\nClick here to roll\n\\/')], [sg.Button('ROLL'), sg.Exit('EXIT')], [sg.T('', size=(25,1),key='random')],
          [sg.Button('COPY SEED')]]
window = sg.Window('Dice Roll', layout, margins=(30,30))

while True:
    now = datetime.now()
    time = now.strftime('%m%D%h%Y%H%M%S%M').replace('/', '')
    event, values = window.read(timeout=500)
    if event in ('EXIT', sg.WIN_CLOSED):
        break
    if event == 'ROLL':
        random.seed(time)
        images = []
        total = 0
        try:
            if int(values['many']) <= 10:
                for i in range(int(values['many'])):
                    num = str(random.randint(1, 6))
                    images.append(sg.Image(f'diceassets/{num}.png'))
                    total = total+int(num)
                layout2 = [images, [sg.T(f'Total value : {total}')], [sg.Button('OK')], [sg.T(f'Seed used : {time}'), sg.Button('COPY')]]
                window2 = sg.Window('DICE', layout2, margins=(10,10))
                while True:
                    event2, values2 = window2.read()
                    if event2 in ('OK', sg.WIN_CLOSED):
                        break
                    if event2 == 'COPY':
                        pyperclip.copy(time)
                        sg.PopupAutoClose('Copied to clipboard', auto_close_duration=1)
                window2.close()
            else:
                sg.Popup('Choose from 1 - 10')
        except ValueError:
            sg.Popup('Bruh!')
    if event == 'COPY SEED':
        pyperclip.copy(time)
        sg.PopupAutoClose('Copied to clipboard', auto_close_duration=1)
    window['random'].update(time)
window.close()
