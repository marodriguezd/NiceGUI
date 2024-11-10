from nicegui import ui
from nicegui.elements.mixins.color_elements import color


def lesson_01():
    ui.label('Welcome to NiceGUI Playlist!')

    ui.run()

def lesson_02():
    ui.label('Welcome to NiceGUI Playlist!')

    ui.link('Go to this Amazing Web',
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    ui.chat_message('Hello Nigga',
                    name='Tetona y culona',
                    stamp='now',
                    avatar='https://i.pinimg.com/564x/5d/0b/4c/5d0b4c42d4650653fe5054cd3f4dae2b.jpg')

    ui.markdown('This is **Markdown**.')

    ui.mermaid('''
    graph LR;
        A --> B;
        A --> C;
                ''')

    ui.html('This is <strong>HTML</strong>')

    ui.run()

def lesson_03():
    ui.button('Click me!', color='red',
              on_click=lambda : ui.label('You clicked me!'))

    ui.button('Show link!', color='blue',
              on_click=lambda : ui.link('Super Duper Web',
                                        'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

    ui.button('Click me!', color='green',
              on_click=lambda : ui.notify('You clicked me!'))

    ui.run()