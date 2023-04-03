                                                        #PROGRAMMING FOR ENGINEERS - SENG 207
                                                        # SAMUEL DANQUAH ANKAPONG 
                                                        #           10982880
                                                        #          PROJECT 2 - PART 1



import PySimpleGUI as sg
import pyttsx3

engine_MAIN = pyttsx3.init()
voiceSelect = engine_MAIN.getProperty('voices')

font = ('Monaco',10)

layout = [    [sg.Text('Enter text to speak:',text_color='#030008',background_color='#ADEFD1', font = font)],
    [sg.InputText(key='input'),sg.Button('Speak',button_color='#00203F')],
    [sg.Text('Select voice type:',text_color='#030008',background_color='#ADEFD1'),sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='#00203F'),sg.Radio('Female', 'RADIO1', key='female',background_color='#00203F')],
    [sg.Text("Volume:",text_color= '#030008',background_color='#ADEFD1')],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="vol")],
    [sg.Text("Rate:",text_color= '#030008',background_color='#ADEFD1')],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="Rate")], 
]

window = sg.Window('Damz Text-To-Speech', layout,background_color='#ADEFD1')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        if values['male']:
            engine_MAIN.setProperty('voice', voiceSelect[0].id)
        elif values['female']:
           engine_MAIN.setProperty('voice', voiceSelect[1].id)


        text = values['input']
        user_volume = values["vol"]
        user_rate = values["Rate"]
        engine_MAIN.setProperty('volume', user_volume)
        engine_MAIN.setProperty("rate", user_rate)
        engine_MAIN.say(text)
        engine_MAIN.runAndWait()

window.close()

