import random, time
from datetime import datetime
import PySimpleGUI as sg

default = [[
     {"pos": (0, 0), "name": 1, "neartile": [(0, 1), (1, 0)]},
     {"pos": (0, 1), "name": 2, "neartile": [(0, 0), (1, 1), (0, 2)]},
     {"pos": (0, 2), "name": 3, "neartile": [(0, 1), (1, 2)]}],
    [{"pos": (1, 0), "name": 4, "neartile": [(2, 0), (1, 1), (0, 0)]},
     {"pos": (1, 1), "name": 5, "neartile": [(0, 1), (1, 0), (2, 1), (1, 2)]},
     {"pos": (1, 2), "name": 6, "neartile": [(1, 1), (2, 2), (0, 2)]}],
    [{"pos": (2, 0), "name": 7, "neartile": [(1, 0), (2, 1)]},
     {"pos": (2, 1), "name": 8, "neartile": [(2, 0), (1, 1), (2, 2)]},
     {"pos": (2, 2), "name": 0, "neartile": [(1, 2), (2, 1)]}]]

solved = [[
     {"pos": (0, 0), "name": 1, "neartile": [(0, 1), (1, 0)]},
     {"pos": (0, 1), "name": 2, "neartile": [(0, 0), (1, 1), (0, 2)]},
     {"pos": (0, 2), "name": 3, "neartile": [(0, 1), (1, 2)]}],
    [{"pos": (1, 0), "name": 4, "neartile": [(2, 0), (1, 1), (0, 0)]},
     {"pos": (1, 1), "name": 5, "neartile": [(0, 1), (1, 0), (2, 1), (1, 2)]},
     {"pos": (1, 2), "name": 6, "neartile": [(1, 1), (2, 2), (0, 2)]}],
    [{"pos": (2, 0), "name": 7, "neartile": [(1, 0), (2, 1)]},
     {"pos": (2, 1), "name": 8, "neartile": [(2, 0), (1, 1), (2, 2)]},
     {"pos": (2, 2), "name": 0, "neartile": [(1, 2), (2, 1)]}]]

def swap(kosong, chosen):
    kosong_pos = kosong["pos"]
    chosen_pos = chosen["pos"]
    temp = kosong["name"]
    default[kosong_pos[0]][kosong_pos[1]]["name"] = chosen["name"]
    default[chosen_pos[0]][chosen_pos[1]]["name"] = temp
    return chosen



def shuffle():
    kosong = default[2][2]
    last_piece = kosong["pos"]
    for i in range(1000):
        near_tiles = kosong["neartile"]
        try:
            near_tiles.remove(last_piece)
        except ValueError:
            pass
        random.seed(datetime.now().strftime('%m%D%h%Y%H%M%S%M%F%f').replace('/', ''))
        chosen = random.choice(near_tiles)
        chosen = default[chosen[0]][chosen[1]]
        kosong = swap(kosong, chosen)
        last_piece = kosong["pos"]


def printt(position):
    return default[position[0]][position[1]]['name']


sg.theme_background_color('white')
sg.theme_button_color(('white', 'blue'))

layout = [[sg.T('', size=(23, 1), font='bold 20', key='time')],
          [sg.Button(printt((0, 0)), font='bold', key='00', size=(10, 5)), sg.Button(printt((0, 1)), font='bold', key='01', size=(10, 5)), sg.Button(printt((0, 2)), font='bold', key='02', size=(10, 5))],
          [sg.Button(printt((1, 0)), font='bold', key='10', size=(10, 5)), sg.Button(printt((1, 1)), font='bold', key='11', size=(10, 5)), sg.Button(printt((1, 2)), font='bold', key='12', size=(10, 5))],
          [sg.Button(printt((2, 0)), font='bold', key='20', size=(10, 5)), sg.Button(printt((2, 1)), font='bold', key='21', size=(10, 5)), sg.Button(printt((2, 2)), font='bold', key='22', size=(10, 5))],
          [sg.T(background_color='white')], [sg.Button('SHUFFLE', font='bold', size=(10,2), button_color=('black', 'lime')), sg.Button('SOLVE', font='bold', size=(10,2), button_color=('black', 'lime')), sg.Button('EXIT', font='bold', size=(10,2), button_color='red')]]
window = sg.Window('8puzzle', layout)
shuffle()
pop = False
start = datetime.now()
while True:
    event, values = window.read(timeout=5)
    if event in ('EXIT', sg.WIN_CLOSED):
        break

    if event == 'SHUFFLE':
        shuffle()
        window['11'].update(button_color='green')
        window.read(timeout=100)
        for i in ['00', '01', '02', '10', '12', '20', '21', '22']:
            window[i].update(button_color='green')
        window.read(timeout=100)
        window['11'].update(button_color='lime')
        window['11'].update(printt((1,1)))
        window.read(timeout=100)
        for i in ['00', '01', '02', '10', '12', '20', '21', '22']:
            window[i].update(button_color='lime')
            pos = (int(i[0]), int(i[1]))
            window[i].update(printt(pos))
        window.read(timeout=100)
        window['11'].update(button_color='blue')
        window.read(timeout=100)
        for i in ['00', '01', '02', '10', '12', '20', '21', '22']:
            window[i].update(button_color='blue')
        for i in range(3):
            for i2 in range(3):
                window[f'{i}{i2}'].update(printt((i, i2)))
                if printt((i, i2)) != 0:
                    window[f'{i}{i2}'].update(button_color='blue')
                elif printt((i, i2)) == 0 and pop == False:
                    window[f'{i}{i2}'].update(button_color='gray')
        window.read(timeout=0)
        pop = False
        for i in range(5):
            window['time'].update(f'{5-i}')
            window.read(timeout=1000)
        start = datetime.now()

    if event == 'SOLVE':
        for i in ['11', '12', '02', '01', '00', '10', '20', '21', '22']:
            window[i].update(button_color='green')
            pos = (int(i[0]), int(i[1]))
            default[pos[0]][pos[1]]['name'] = solved[pos[0]][pos[1]]['name']
            window[i].update(printt((pos[0], pos[1])))
            window.read(timeout=100)
            window[i].update(button_color='lime')
            window.read(timeout=75)
        for i in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
            window[i].update(button_color='blue')
            window.read(timeout=50)
        pop = True
        window['time'].update('Solved by Machine')

    if event in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
        try:
            target = None
            pos = (int(event[0]), int(event[1]))
            for i in default[pos[0]][pos[1]]["neartile"]:
                if default[i[0]][i[1]]["name"] == 0:
                    target = default[i[0]][i[1]]
                    break
            swap(target, default[pos[0]][pos[1]])
        except TypeError:
            pass
        pop = False

    col = default[0]
    stat = True
    if not col[0]['name'] == 1 or not col[1]['name'] == 2 or not col[2]['name'] == 3:
        stat = False
    col = default[1]
    if not col[0]['name'] == 4 or not col[1]['name'] == 5 or not col[2]['name'] == 6:
        stat = False
    col = default[2]
    if not col[0]['name'] == 7 or not col[1]['name'] == 8 or not col[2]['name'] == 0:
        stat = False
    if stat and pop == False:
        for i in range(3):
            for i2 in range(3):
                window[f'{i}{i2}'].update(printt((i, i2)))
                if printt((i, i2)) != 0:
                    window[f'{i}{i2}'].update(button_color='blue')
                else:
                    window[f'{i}{i2}'].update(button_color='gray')
        window.read(timeout=0)
        for i in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
            window[i].update(button_color='green')
            window.read(timeout=100)
        sg.PopupQuickMessage(f'Passed!\n{minutes}:{seconds}:{microsec}')
        for i in ['00', '01', '02', '10', '11', '12', '20', '21', '22']:
            window[i].update(button_color='blue')
            window.read(timeout=100)
        pop=True
        window['time'].update(f'Solved ({minutes}:{seconds}:{microsec})')

    for i in range(3):
        for i2 in range(3):
            window[f'{i}{i2}'].update(printt((i, i2)))
            if printt((i,i2)) != 0:
                window[f'{i}{i2}'].update(button_color='blue')
            elif printt((i,i2)) == 0 and pop == False:
                window[f'{i}{i2}'].update(button_color='gray')

    if pop == False:
        now = datetime.now()
        remain = now - start
        microsec = remain.microseconds
        seconds = remain.seconds
        hours = seconds // 3600
        minutes = (seconds // 60) % 60
        seconds = seconds % 60
        if len(str(seconds)) == 1:
            seconds = f'0{seconds}'
        window['time'].update(f'{minutes}:{seconds}:{microsec}')

window.close()
exit(0)
