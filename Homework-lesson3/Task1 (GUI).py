"""
Task 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
"""
import PySimpleGUI as sg

layout = [[sg.Text("Введіть слово: ")],
          [sg.Input(key='-WORD-')],
          [sg.Text("Введіть номер символу у слові починаючи відлік з 1: ")],
          [sg.Input(key='-SYMBOL_NUMBER-')],
          [sg.Text(size=(40, 2), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
window = sg.Window('Window Title', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    word = values['-WORD-']
    symbol_number = values['-SYMBOL_NUMBER-']
    if not word.strip(" "):
        window['-OUTPUT-'].update("Слово не може бути пустим")
    elif not symbol_number.isdigit() or symbol_number.startswith("0"):
        window['-OUTPUT-'].update("Номер символу має бути цілою цифрою починаючи з 1")
    else:
        int_symbol_number = int(symbol_number)
        if len(word) < int_symbol_number:
            last_symbol = word[-1]
            window['-OUTPUT-'].update(f"Довжина слова менша за {int_symbol_number}, останній символ: \"{last_symbol}\"")
        else:
            symbol = word[int_symbol_number - 1]
            window['-OUTPUT-'].update(f"The selected symbol in word is \"{symbol}\" ")

window.close()
