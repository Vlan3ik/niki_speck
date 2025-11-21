screen main_menu():
    tag menu
    add "bg menu"
    add "logo" xpos 0.5 ypos 0.2 anchor (0.5, 0.5)

    vbox xpos 0.5 ypos 0.6 anchor (0.5, 0.5) spacing 30:
        textbutton "Новая игра" action Start() text_size 48
        textbutton "Загрузить"   action ShowMenu("load") text_size 48
        textbutton "Настройки"  action ShowMenu("preferences") text_size 48
        textbutton "Выход"      action Quit(confirm=False) text_size 48