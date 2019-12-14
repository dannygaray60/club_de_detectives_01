init python:
    if not persistent.gameover_counter_set:
        persistent.gameover_counter_set=True
        persistent.gameover_counter={}
    change_cursor() 
    define_images("images/bg")


label splashscreen:
    ##establecemos volumen para canal de audio txt (nombre del mixer)
    python:
        if not persistent.set_volumes:
            persistent.set_volumes=True
            _preferences.volumes["txt"]*=.50
    if not config.debug:
        scene bg blanco with dissolve
        play audio moneda
        show splashs at truecenter with dissolve 
        $ renpy.pause(3,hard=True)
    return

# El juego comienza aquí.
label start:

    ## Antes de cada nueva partida, reiniciamos variables
    $ resetVar()
    if not config.debug:
        # Inicio de la historia
        jump inicio
    else:
        jump dev_room
        
    ## Finaliza el juego:
    return
