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

    with ui.button('Click me!', color='pink',
                   on_click=lambda : badge.set_text(int(badge.text)+1)):
        badge = ui.badge('0', color='red').props('floating')

    ui.run()

def lesson_04():
    label = ui.label('Crotetas')

    toggle_text = ui.toggle(['text-1', 'text-2'], value='text-1',
                            on_change=lambda : label.set_text(f'You clicked {toggle_text.value}'))

    image = ui.image('JavaScript.png').classes('w-64')

    toggle_image = ui.toggle(['JavaScript', 'Python'],
                             on_change=lambda : image.set_source(f'{toggle_image.value}.png'))

    ui.run()

def lesson_05():
    gender_image = ui.image('').classes('w-48')
    radio_image = ui.image('').classes('w-48')

    toggle_gender = ui.toggle(['WOMAN', 'MAN'],
                              on_change=lambda : gender_image.set_source(f'{toggle_gender.value}.png'))

    radio_country = ui.radio(['England', 'USA'],
                             on_change=lambda : radio_image.set_source((f'{radio_country.value}.png')))

    ui.run()