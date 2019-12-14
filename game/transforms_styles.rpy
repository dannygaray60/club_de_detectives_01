init:

## posiciones para personajes
###############################
    transform left:
        yanchor 1.0
        ypos 1.0
        xanchor 0.5
        xpos 0.2
    transform mleft:
        yanchor 1.0
        ypos 1.0
        xanchor 0.5
        xpos 0.350
    transform mright:
        yanchor 1.0
        ypos 1.0
        xanchor 0.5
        xpos 0.650
    transform right:
        yanchor 1.0
        ypos 1.0
        xanchor 0.5
        xpos 0.8



###################
## para el "objetion"
    transform excl:
        xalign 0.5
        yalign 0.5
        yoffset 400
        linear 0.3 yoffset -200
        linear 0.1 yoffset 0
        pause 1.5
        linear 0.3 yoffset 700

    transform notaaparecer:
        xanchor 1.0
        ypos 0.480
        on show:
            xpos 2900
            linear 0.9 xpos 1280
        on hide:
            linear 5 xpos 2900

###############################
## animaciones para personajes
######################################

    transform temblor():
        # xcenter x 
        yoffset 0 yanchor 1.0 ypos 1.0 alpha 1.00 subpixel True
        parallel:
            ease 0.250 yoffset 3
            ease 0.250 yoffset 0
            repeat
        parallel:
            easein .050 xoffset 2
            ease .150 xoffset -2
            easeout .050 xoffset 0
            repeat

    transform acercarse:
        parallel:
            ease 1 zoom 1.5
        parallel:
            ease 1 yoffset 300
    transform alejarse:
        parallel:
            ease 1 zoom 1
        parallel:
            ease 1 yoffset 0

    #hacer que el sprite baje un poco de altura
    #esto es para indicar tristeza en un personaje
    transform decaer:
        linear 1 yoffset 60
    #y este es para regresar a la posicion inicial
    transform reponerse:
        linear 1 yoffset 0

    transform reponerse_rapido:
        linear 0.2 yoffset 0

    # #para hacer que un personaje se eche a correr a la izquierda
    # transform correr_izquierda:
    #     linear 0.6 xoffset -900

    # #para hacer que un personaje se eche a correr a la derecha
    # transform correr_derecha:
    #     linear 0.6 xoffset 900   
        
    transform asentir:
        linear .2 yoffset 50
        #regresamos "y" a posicion normal
        linear .3 yoffset 0

    transform brinquitos:
        easein .2 yoffset 80
        easein .1 yoffset 0
        ease .2 yoffset 50
        ease .1 yoffset 0
        easein .2 yoffset 20
        easein .1 yoffset 0

    transform smolchar_random_move:
        rotate_pad True
        rotate 0
        #brinquitos
        choice:
            easein .2 yoffset -100
            easein .1 yoffset 0
            ease .2 yoffset -50
            ease .1 yoffset 0
            easein .2 yoffset -30
            easein .1 yoffset 0
        #girar un poco
        choice:
            #ver abajo
            choice:
                linear .5 rotate -20 
                pause .7 
                linear .5 rotate 0
            #ver arriba
            choice:
                linear .5 rotate 20 
                pause .7 
                linear .5 rotate 0
        #un salto
        choice:
            easein .2 yoffset -60
            easein .2 yoffset 5
        #saltito lateral
        choice:
            #hacia la derecha
            choice:
                block:
                    parallel:
                        easein .2 yoffset -70
                        easein .2 yoffset 0
                    parallel:
                        easein .4 xoffset 100
                pause .8
                block:
                    parallel:
                        easein .2 yoffset -70
                        easein .2 yoffset 0
                    parallel:
                        easein .4 xoffset 0
            #hacia la izquierda
            choice:
                block:
                    parallel:
                        easein .2 yoffset -70
                        easein .2 yoffset 0
                    parallel:
                        easein .4 xoffset -100
                pause .8
                block:
                    parallel:
                        easein .2 yoffset -70
                        easein .2 yoffset 0
                    parallel:
                        easein .4 xoffset 0  
        pause 1
        repeat

    transform smolchar2_random_move:
        #brinquitos
        choice:
            easein .2 yoffset -80
            easein .1 yoffset 0
            ease .2 yoffset -50
            ease .1 yoffset 0
            easein .2 yoffset -30
            easein .1 yoffset 0
        #un salto
        choice:
            easein .2 yoffset -50
            easein .2 yoffset 0
        #saltito lateral
        choice:
            block:
                parallel:
                    easein .2 yoffset -50
                    easein .2 yoffset 0
                parallel:
                    easein .4 xoffset 40
            pause .8
            block:
                parallel:
                    easein .2 yoffset -50
                    easein .2 yoffset 0
                parallel:
                    easein .4 xoffset 0   
        pause 1
        repeat

    transform smolsherinford_random_move:
        rotate_pad True
        rotate 0
        #brinquitos
        choice:
            easein .2 yoffset -50
            easein .1 yoffset 0
            ease .2 yoffset -30
            ease .1 yoffset 0
            easein .2 yoffset -10
            easein .1 yoffset 0
        #girar un poco
        choice:
            linear .5 rotate 20
            pause 1 
            linear .5 rotate 0
        #un salto
        choice:
            easein .2 yoffset -5
            easein .2 yoffset 5
        #saltito lateral
        choice:
            parallel:
                easein .2 yoffset -5
                easein .2 yoffset 5
            parallel:
                easein .4 xoffset 7
            pause .6
            choice:
                parallel:
                    easein .2 yoffset -5
                    easein .2 yoffset 5
                parallel:
                    easein .4 xoffset -7
            choice:
                pass    
        pause 1
        repeat

## Otros transforms
    transform atlLogo:
        alpha 0
        zoom 1.5
        xpos 0.090 ypos 0.010
        # on start:
        linear .9 alpha 1 zoom 0.8
    transform atlMainMenuBtns(x):
        # aparecer
        zoom 0
        on start:
            linear x zoom 1.2
            linear .3 zoom 1
    ##panel detras del nombre de juego en mainmenu
    transform panelMainMenuTitle:
        zoom 1.4
        xanchor 1.0 xpos 0.670 ypos 0.035 yanchor 0.0
        fliped_h
        leftpanelMainMenu
        aparecer

    transform aliceMainMenu:
        on start:
            alpha 0
            parallel:
                linear 1 alpha 1
            parallel:
                linear 1 xoffset -50
    transform leftpanelMainMenu:
        on start:
            xoffset -300
            linear 1 xoffset 0

    transform fliped_h:
        xzoom -1.0
    transform fliped_v:
        yzoom -1.0
    #lista de argumentos en debate
    transform debateArgsList:
        zoom zoomqckmenu
        xanchor choice_args_xanchor
        on show:
            xoffset 800
            linear 0.2 xoffset 0
        on hide:
            linear 0.2 xoffset 800
    ## para mostrar temporalmente titulo de un minijuego
    transform minigame_title:
        centro_pantalla
        xoffset 1200
        on show:
            linear 0.5 xoffset 0
        on hide:
            linear 0.5 xoffset -1200
    #panel que se muestra arriba
    transform panelMinigameTop:
        yoffset -100
        on show:
            linear 0.5 yoffset 0
        on hide:
            linear 0.5 yoffset -100
    #panel que muestra corazones arriba
    transform panelHearts:
        xanchor 0.5 yanchor 0 xpos 0.5 ypos 0
        panelMinigameTop
    #para cuadro de dialogo
    transform windowDialogo:
        pass
        # yoffset 400
        # on show:
        #     yoffset 400
        #     linear 0.5 yoffset 0
        # on hide:
        #     linear 0.5 yoffset 400

    transform atlhbox_chibis_gamemenu:
        xanchor .5
        yanchor 1.0
        zoom .3
        ypos .880
        xpos .1
    transform atlhbox_chibis_gamemenu_ingame:
        zoom .140
        xalign 1.0
        yoffset -110
        xoffset -70




############################################
## Estilos generales
############################################
    style frase_button_text:
        color "#ffffff"
        font "gui/fonts/FjallaOne.otf"
        size 65
        line_spacing -10
        outlines [ (1, "#000000", 0, 0) ]
        xalign 0.5
    style frase_text:
        color "#ffffff"
        font "gui/fonts/FjallaOne.otf"
        size 65
        line_spacing -10
        outlines [ (1, "#000000", 0, 0) ]
        xalign 0.5
    style murmullo_button_text:
        color "#ffffff"
        font "gui/fonts/FjallaOne.otf"
        size 45
        line_spacing -10
        outlines [ (1, "#000000", 0, 0) ]
        xalign 0.5
    style murmullo_text:
        color "#ffffff"
        font "gui/fonts/FjallaOne.otf"
        size 45
        line_spacing -10
        outlines [ (1, "#000000", 0, 0) ]
        xalign 0.5
    #######################################