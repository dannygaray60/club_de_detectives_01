################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Pantallas internas a juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

## agregamos el custom_namebox, que en el objeto Character() comienza con "show_"
screen say(who, what, custom_namebox=None):
    style_prefix "say"

    if quick_menu_bajo==False:
        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"

                    text who id "who"
                    ## si hay un argumento en custom_namebox establecemos un background sacado del argumento
                    if custom_namebox is not None:
                        background Frame(custom_namebox, gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                    at atlNamebox()

            text what id "what"
            if who is not None:
                add "chat_icon" at atlNameboxChatIcon
                add "chat_icon_dot" at atlNameboxChatIcon

    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

transform atlNamebox():
    zoom zoomqckmenu
    yoffset nameboxyoff
    xoffset -300
    on start:
        linear .1 xoffset 0
# if renpy.variant("small"):
#     transform atlNamebox:
#         zoom 1.3
#         yoffset -16
#         xoffset -300
#         on start:
#             linear .1 xoffset 0

transform atlNameboxChatIcon:
    parallel:
        atlNamebox
    parallel:
        xpos 14
        ypos 10

init:
    image chat_icon:
        "gui/chat_icon.png"
    image chat_icon_dot:
        "gui/chat_icon_dot_a.png"
        pause .5
        "gui/chat_icon_dot_b.png"
        pause .5
        "gui/chat_icon_dot_c.png"
        pause .5
        repeat

## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    frame:
        if not renpy.variant("small"):
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            xsize 500
        else:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.2
            xsize 500
        vbox:
            xalign 0.5            
            text prompt style "input_prompt"
            input id "input" color "#BB7900"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    color "#660066"
    text_align 0.5

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    text_align 0.5


## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    style_prefix "choice"

    vbox:
        for i in items:
            if i.chosen:
                textbutton "{font=gui/fonts/fontawesome.ttf}{/font} "+i.caption action i.action
            else:
                textbutton i.caption action i.action


## Cuando es 'True', el encabezamiento será dicho por el narrador. Si es
## 'False', será presentado como un botón inactivo. 
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Pantalla de menú rápido #####################################################
##
## El menú rápido es presentado en el juego para ofrecer fácil acceso a los
## menus externos al juego.

screen quick_menu():
    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100
    if quick_menu:
        #posicion y del quickmenu horizontal
        if quick_menu_bajo==False:
            $ quick_menu_ypos=0.85
        else:
            $ quick_menu_ypos=1.0

        ####################################
        ## Quickmenu vertical a la izquierda
        ####################################
        vbox spacing -40 at atl_quick_menu_ver_izq:
            #menu principal
            imagebutton auto "gui/quickmenu/home_%s.png" action MainMenu() focus_mask True
            #skip
            imagebutton:
                auto "gui/quickmenu/skip_%s.png"
                action Skip() alternate Skip(fast=True, confirm=True) focus_mask True
            ##opciones
            imagebutton auto "gui/quickmenu/settings_%s.png" action ShowMenu('preferences') focus_mask True

        ####################################
        ## Quickmenu vertical a la derecha
        ####################################
        if quick_menu_timescr:
            ## boton para ver el estado general del juego y jugador
            imagebutton auto "gui/quickmenu/statusbtn_%s.png" action ShowMenu('status') xanchor 1.0 yanchor 0 xpos 1282 ypos 0.158 focus_mask True at atl_quick_menu_ver_der_btn
            fixed xalign 1.0 yalign 0.0 at atl_quick_menu_ver_der:
                add "gui/day_icons/day_status.png" xalign 1.0
                ## de 6 a 11 (6am a 11am) es mañana
                ## de 12 a 17 (12pm a 5pm) es tarde
                ## de 18 a 5 (de 6pm a 5am) es noche 
                if hora>5 and hora<12:
                    add "gui/day_icons/morning.png" xalign 1.0
                elif hora>11 and hora<18:
                    add "gui/day_icons/afternoon.png" xalign 1.0
                else:
                    add "gui/day_icons/night.png" xalign 1.0

                # hora y dia
                text dia+" "+convertHH(hora) xalign 0.5 size 38 xpos 0.839 yoffset -2
                #estado del juego
                text estadoj xalign 0.5 size 32 xpos 0.840 yoffset 35
                # fecha actual
                text fecha xalign 0.5 size 27 xpos 0.850 yoffset 75

        ##########################
        ## Quickmenu horizontal
        ##########################

        ## quickmenu normal
        if not quick_menu_gameplay:
            
            hbox xanchor 1.0 yanchor 1.0 xpos 1.0 ypos quick_menu_ypos spacing -38 at atl_quick_menu_hor(zoomqckmenu):

                ## autoFW
                imagebutton:
                    action Preference("auto-forward", "toggle") 
                    focus_mask True
                    ## si está activado el auto avance, ponemos el boton activo
                    if _preferences.afm_enable==True:
                        auto "gui/quickmenu/auto_enabled_%s.png"
                    else:
                        auto "gui/quickmenu/auto_%s.png" 

                ##historial
                imagebutton auto "gui/quickmenu/textlog_%s.png" action ShowMenu('history') focus_mask True

                #bloc de notas
                if quick_menu_btn_notepad:
                    imagebutton auto "gui/quickmenu/notepad_%s.png" action ShowMenu('notepad') focus_mask True
                else:
                    add "gui/quickmenu/notepad_disabled.png"

                #cargar
                imagebutton auto "gui/quickmenu/load_%s.png" action ShowMenu('load') focus_mask True

                #guardar
                imagebutton auto "gui/quickmenu/save_%s.png" action ShowMenu('save') focus_mask True

                #ocultar interfaz
                imagebutton auto "gui/quickmenu/hide_%s.png" action HideInterface() focus_mask True

            ## lugar donde aparecerá circulo de notificacion para el block de notas
            if notepad_notificacion:
                add "gui/quickmenu/circle_notify.png" xpos 0.757 ypos quick_menu_ypos-0.04 xoffset notepadnotifyxoffset

        ## un quickmenu para juegos como debate e interrogatorio, donde la opcion de guardado,carga y salto de texto dan resultados inesperados, así que mejor los desactivamos
        else:
            hbox xanchor 1.0 yanchor 1.0 xpos 1.0 ypos quick_menu_ypos spacing -38 xoffset 97 at atl_quick_menu_hor(zoomqckmenu):
                imagebutton auto "gui/quickmenu/textlog_%s.png" action ShowMenu('history') focus_mask True
                imagebutton auto "gui/quickmenu/notepad_%s.png" action ShowMenu('notepad') focus_mask True
                    ##solo para rellenar
                add "gui/quickmenu/notepad_idle.png"

transform atl_quick_menu_ver_izq:
    xoffset -500
    on start:
        pause 0.4
        easein 0.4 xoffset 0
    on hide:
        easein 0.4 xoffset -500
transform atl_quick_menu_ver_der:
    xoffset 500
    on start:
        pause 0.7
        easein 0.4 xoffset 0
    on hide:
        pause 0.3
        easein 0.4 xoffset 500
transform atl_quick_menu_ver_der_btn:
    yoffset -300
    zoom zoomqckmenu
    on start:
        pause 0.9
        easein 0.4 yoffset 0
    on hide:
        easein 0.4 yoffset -300



transform atl_quick_menu_hor(varzoom):
    zoom varzoom
    xoffset 500
    on start:
        easein 0.4 xoffset 0
    on hide:
        easein 0.4 xoffset 500
      
## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

## Pantalla de block de notas #####################################################

# pantalla de botones scroll
screen notepad_scrollbtns():
    frame style_prefix "btnScrollNotepad":
        vbox:
            textbutton "" action Scroll(id="barra_notepad", direction="vertical decrease", amount=u'step')
            textbutton "" action Scroll(id="barra_notepad", direction="vertical increase", amount=u'step')
style btnScrollNotepad_frame:
    background None
    yalign .5
    ypos .6
    xanchor 1.0
    xpos .770
style btnScrollNotepad_vbox:
    spacing 10
style btnScrollNotepad_button_text:
    color "#ffffff"
    hover_color gui.hover_color
    font "gui/fonts/fontawesome.ttf"
    size 80

screen notepad(para=False,jumpto=False):
    #la variable "para", indicará para qué se utilizará el bloc de notas, por ejemplo, en un dialogo se usaría para presentar alguna evidencia, o usar el bloc en un debate o interrogatorio

    zorder 120
    modal True

    ## quitamos el icono de notificacion del bloc de notas
    on "show" action [SetVariable("notepad_notificacion",False),Stop(channel="text")]

    #El action Return() funciona bien solo cuando estamos en un dialogo normal, pero a la hora de colocar otros screen o en un minijuego, este no oculta el bloc de notas, para eso utilizar Hide("notepad")
    if not para:
        imagebutton idle "gui/semi_dark_screen.png" action [Return(),Hide("notepad")]
        frame:
            background "gui/notes_close.png"
            xalign 0.0 yalign 0.5
            xpos 0.640
            ypos 0.800
            style_prefix "btnCloseNotepad"
            textbutton "Cerrar" action [Return(),Hide("notepad",dissolve)] xpos 0.450 yanchor 0.5 ypos 0.790
    elif para=="evidenc":
        #como se tiene que presentar una evidencia si o si, inhabilitamos la opcion de ocultar el notepad
        add "gui/semi_dark_screen.png"
        #un boton de historial
        hbox xanchor 1.0 yanchor 1.0 xpos 1.0 ypos 1.0 spacing -38 xoffset 97 at atl_quick_menu_hor(zoomqckmenu):
            imagebutton auto "gui/quickmenu/textlog_%s.png" action ShowMenu('history') focus_mask True
            ##solo para rellenar
            add "gui/quickmenu/notepad_idle.png"
    elif para=="interr":
        imagebutton idle "gui/semi_dark_screen.png" action [Hide("notepad",dissolve)]
        frame:
            background "gui/notes_close.png"
            xalign 0.0 yalign 0.5
            xpos 0.640
            ypos 0.800
            style_prefix "btnCloseNotepad"
            textbutton "Cerrar" action [Hide("notepad",dissolve)] xpos 0.450 yanchor 0.5 ypos 0.790

    add "gui/note.png" xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.510

    viewport:
        id "barra_notepad"
        style_prefix "notepad"
        xsize 440
        xpos 0.34
        ypos 0.090
        scrollbars "vertical"
        draggable True
        mousewheel True
        arrowkeys True
        ysize 600
        ## aqui se mostrarian las notas desde un array
        vbox:
            if lstNotepad_titulo==[]:
                text "Todavía no hay notas."
            else:
                $ i=1
                for nota_t in lstNotepad_titulo:
                    if para=="interr" or para=="evidenc":
                        textbutton "{b}[i]. [nota_t]{/b}" action ShowMenu('notepad_text',lstNotepad_desc[i-1],nota_t,lstNotepad_thumb[i-1],lstNotepad_img[i-1],"interr") top_margin 20
                        button top_padding 0:
                            if para=="interr":
                                action [ Hide("notepad"), SetVariable("interr_item_notepad_select",i-1),Jump( "int"+str(interr_id)+"f"+str(interr_fraseid)+"_refutado") ]
                            elif para=="evidenc":
                                action [SetVariable("idevidencia_mostrar",nota_t),Return(),Jump(jumpto)]
                            xalign 1.0
                            text "{font=gui/fonts/fontawesome.ttf}{/font} Presentar" size 35 hover_color gui.hover_color
                            
                    else:
                        textbutton "{b}[i]. [nota_t]{/b}" action ShowMenu('notepad_text',lstNotepad_desc[i-1],nota_t,lstNotepad_thumb[i-1],lstNotepad_img[i-1])
                    $i+=1

    if renpy.variant("small"):
        use notepad_scrollbtns

screen notepad_text(nota_desc,nota_t,notethumb=False,noteimg=False,para=False):

    zorder 121
    modal True

    if para:
        imagebutton idle "gui/semi_dark_screen.png" action Return()
    else:
        imagebutton idle "gui/semi_dark_screen.png" action Hide('notepad_text',dissolve) 
    
    add "gui/note_item_title.png" xanchor 1.0 yanchor 0.5 ypos 0.5 xpos 0.330

    if notethumb:
        if noteimg:
            frame yanchor 0.5 xpos 0.882 ypos 0.3:
                button:
                    text "{font=gui/fonts/fontawesome.ttf}{/font}" style "btnampliar"
                    action ShowMenu("noteImgFull",noteimg,para)
        add "images/notes_img/"+notethumb+"_thumb.jpg" xanchor 0.5 yanchor 0.5 xpos 0.787 ypos 0.3
        add "gui/notes_img_panel/tape.png" xanchor 0.5 yanchor 0.5 xpos 0.880 ypos 0.3
    
    add "gui/note.png" xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.510 

    frame:
        background "gui/notes_close.png"
        xalign 0.0 yalign 0.5
        xpos 0.640
        ypos 0.800
        button:
            text "Atrás" style "btnCloseNotepad_button_text" xpos 0.700 yanchor 0.5 ypos 0.790
            if para:
                action Return()
            else:
                action Hide('notepad_text',dissolve) 

    viewport:
        id "barra_notepad"
        scrollbars "vertical"
        draggable True
        mousewheel True
        arrowkeys True
        style_prefix "notepad"
        xsize 440
        ysize 600
        xpos 0.34
        ypos 0.090
        text nota_desc

    viewport at rotar_m_90:
        draggable True
        mousewheel True
        arrowkeys True
        xsize 510
        ysize 75
        xanchor 0.5 yanchor 0.5
        xpos 0.288 ypos 0.5
        vbox xsize 510 xanchor 0.5 xpos 0.5 xalign 0.5:
            vbox:
                xalign 0.5
                style_prefix "notepad_item_title"
                text nota_t text_align 0.5

    if renpy.variant("small"):
        use notepad_scrollbtns

style scrollbar:
    unscrollable "hide"
style vscrollbar:
    unscrollable "hide"

style btnampliar:
    color "#A366A3"#gui.selected_color
    hover_color gui.hover_color
    size 50


## pantalla para mostrar la imagen del bloc de notas a pantalla completa
screen noteImgFull(imagen,para=False):
    zorder 122
    modal True
    add "images/notes_img/"+imagen+"_img.jpg"
    frame xanchor 0.0 yanchor 1.0 xpos 0 ypos 1.0:
        button:
            if para:
                action Return()
            else:
                action Hide('noteImgFull')
            text "{font=gui/fonts/fontawesome.ttf}{/font}" style "btnampliar"



screen interrogatorio_btns():

    ## desactivamos la posibilidad de avanzar con space o click en cualquier lado
    # key "dismiss" action NullAction()

    fixed at atlInterrBtns(interrbtnyoff,zoomqckmenu):

        hbox yanchor 1.0 ypos 0.784 xpos 0.086:
            add "gui/interrogatory/base.png"

        hbox yanchor 1.0 ypos 0.707 xpos -1 spacing -40:
            ## int + idinterrogatorio + fraseid
            ## boton para interrogar
            imagebutton auto "gui/interrogatory/interrogar_%s.png" action  [ Function(checkTimeAndJump,"int"+str(interr_id)+"_gameover"), Jump( "int"+str(interr_id)+"f"+str(interr_fraseid) ) ] focus_mask True
            ##botón de refutar
            if not interr_btn_refutar_disabled:
                imagebutton auto "gui/interrogatory/refutar_%s.png" action [Function(checkTimeAndJump,"int"+str(interr_id)+"_gameover"), Show("notepad",para="interr",transition=dissolve) ] focus_mask True
            else:
                imagebutton idle "gui/interrogatory/refutar_insensitive.png" action NullAction() focus_mask True


        hbox yanchor 1.0 ypos 0.780 spacing -40:
            #boton para retroceder texto
            if interr_fraseid!=0:
                imagebutton auto "gui/interrogatory/prev_%s.png" action Rollback() focus_mask True
            else:
                imagebutton idle "gui/interrogatory/prev_insensitive.png" action NullAction() focus_mask True
            #y el boton para avanzar
            if interr_fraseid!=interr_frasefinal:
                imagebutton auto "gui/interrogatory/next_%s.png" action renpy.curry(renpy.end_interaction)(True) focus_mask True
            else:
                imagebutton idle "gui/interrogatory/next_insensitive.png" action NullAction() focus_mask True

transform atlInterrBtns(interrbtnyoff,zoomqckmenu):
    xoffset -300
    yoffset interrbtnyoff
    zoom zoomqckmenu
    on start:
        easein 0.6 xoffset 0
    on hide:
        easein 0.6 xoffset -300
# if renpy.variant("small"):
#     transform atlInterrBtns:
#         yoffset -220
#         zoom 1.3
#         xoffset -300
#         on start:
#             easein 0.6 xoffset 0
#         on hide:
#             easein 0.6 xoffset -300
# else:
#     transform atlInterrBtns:
#         xoffset -300
#         on start:
#             easein 0.6 xoffset 0
#         # on show:
#         #     easein 0.6 xoffset 0
#         on hide:
#             easein 0.6 xoffset -300


#######################################
## Estilos para block de notas
#######################################

## rotar -90
transform rotar_m_90:
    rotate 270 rotate_pad False

style notepad_button_text:
    font "gui/fonts/IndieFlower.ttf"
    color "#7F7F7F"
    hover_color gui.hover_color
    size 35
    line_spacing -20

style notepad_text:
    size 30
    line_spacing -10
    font "gui/fonts/IndieFlower.ttf"
    color "#000000"
style notepad_text:
    variant "small"
    size 40
style notepad_button_text:
    variant "small"
    color "#555555"
    

style notepad_item_title_text:
    size 45
    font "gui/fonts/IndieFlower.ttf"
    color "#000000"
    line_spacing -20

style btnCloseNotepad_button_text:
    color "#000000"
    hover_color gui.hover_color
    font "gui/fonts/playtime.ttf"
    size 60


## Pantalla de estado general del juego (tiempo jugado, estadisticas, etc) #####################################################

screen status():

    on "show" action Stop(channel="text")

    $ horas_jugados = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutos_jugados = convertSeconds( renpy.get_game_runtime() )[1]
    $ seen = renpy.count_seen_dialogue_blocks()
    $ dialogue = renpy.count_dialogue_blocks()
    $ porcentaje_gameplay = seen * 100 / dialogue

    add "gui/semi_dark_screen.png"

    frame xpos 50 ypos 50 padding 10,10:
        vbox:
            text "Jugador: "+pla_name color "#000000"
            text "Tiempo jugado: [horas_jugados] horas, [minutos_jugados] minutos." color "#000000"
            text "Juego completado al [porcentaje_gameplay]%" color "#000000"
            text "Puntos de Inteligencia: "+str(pla_stat["intel"]) color "#000000"
            text "Puntos de Carisma: "+str(pla_stat["carisma"]) color "#000000"
        
    frame:
        xalign 1.0
        yalign 1.0
        style_prefix "btnCloseNotepad"
        textbutton "Cerrar" action Return()  


###############################
## Pantalla de frase de debate
#############################
screen debateCharPanel(personaje):
    add "images/debate_panels/"+personaje+"_panel.png" at deb_panel

screen debateText(debate_args,frase_args,num):

    ## comprobamos si no se ha acabado el tiempo
    on "show" action Function(checkTimeAndJump,"d"+str( debate_args[0] )+"_gameover")

    # on "hide" action Function(callable=focus_target_cursor)

    $ iddebate = debate_args[0]
    $ idronda = debate_args[1]
    $ idfrasecorrecta = debate_args[2]
    $ idargcorrecto = debate_args[3]
  
    $ idfraseactual = frase_args[0]
    $ texto = frase_args[1]
    $ tipo = frase_args[2]
    $ animacion = frase_args[3]
    $ btn = frase_args[4]
    $ personaje = frase_args[5]

    ## creamos una etiqueta para donde saltar si el texto es clickeable
    $ etiqueta_actual = "d"+str(iddebate)+"r"+str(idronda)

    # if personaje and tipo=="frase":
    #     ## añadir imagen en la esquina inferior izquierda
    #     add "images/debate_panels/"+personaje+".png" xpos 0 ypos 1.0 xanchor 0.0 yanchor 1.0 at deb_panel

    hbox:
        style_prefix tipo

        if btn:
            textbutton texto:
                hovered Function(callable=focus_target_cursor,fcs=True)
                unhovered Function(callable=focus_target_cursor)
                if (debate_arg_seleccionado==idargcorrecto) and idfraseactual==idfrasecorrecta:
                    action [ Jump(etiqueta_actual+'_correcto') ]
                    activate_sound audio.correcto
                else:
                    action Jump(etiqueta_actual+'_incorrecto_'+personaje)
                    activate_sound audio.incorrecto

        else:
            textbutton texto:
                hovered Function(callable=focus_target_cursor,fcs=True)
                unhovered Function(callable=focus_target_cursor)
                action Function(callable=restTimer) #NullAction()
                activate_sound audio.incorrecto

        at animacion

transform deb_panel:
    yalign 1.0
    xalign 0.0
    zoom .8
    yoffset 2
    xpos -300
    on show:
        linear .3 xpos 0

## Pantallas para poder usar la misma pantalla varias veces

screen debateText1(debate_args,frase_args):
    use debateText(debate_args,frase_args,1)

screen debateText2(debate_args,frase_args):
    use debateText(debate_args,frase_args,2)

screen debateText3(debate_args,frase_args):
    use debateText(debate_args,frase_args,3)

screen debateText4(debate_args,frase_args):
    use debateText(debate_args,frase_args,4)

## los estilos están en transform_styles.rpy

###################################################################
## boton con el argumento actual, para abrir la lista de argumentos
###################################################################

screen debateArgumento():
    if quick_menu_bajo:
        $yp=0.880
    else:
        $yp=0.730

    style_prefix "choice_args"
    vbox ypos yp at debateArgsList:
        button:
            text "{font=gui/fonts/fontawesome.ttf}{/font} "+argumentos[debate_arg_seleccionado]
            action [Show("debateArgs"),SelectedIf(1==1)]
            activate_sound audio.ctc


###############################################
## lista de argumentos para usarse en un debate
###############################################

screen debateArgs():

    zorder 120
    on "show" action Hide("debateArgumento")

    style_prefix "choice_args"

    imagebutton idle "gui/semi_dark_screen.png" action [Hide("debateArgs"),Show("debateArgumento")] at aparecer

    vbox at debateArgsList:
        $ i=0
        for arg in argumentos:
            button:
                if debate_arg_seleccionado == i:
                    text "{font=gui/fonts/fontawesome.ttf}{/font} "+arg
                else:
                    text "{font=DejaVuSans.ttf}○{/font} "+arg
                action [Hide("debateArgs"),SetVariable("debate_arg_seleccionado",i),Show("debateArgumento")]
                activate_sound audio.ctc
            $ i=i+1        

style choice_args_vbox:
    ypos 0.5
    xpos 1.0
    xanchor 1.0
    yanchor 0.5
    spacing 40
    xoffset 95
style choice_args_vbox:
    variant "small"
    yoffset -20
style choice_args_button is default:
    properties gui.button_properties("choice_button")
    right_padding 120
    xsize None
    xalign 1.0
style choice_args_button_text is default:
    size 38
    xalign 1.0


################################################
## Boton para mostrar un mensaje
################################################

screen btnHelpTextBox(msj):
    imagebutton auto "gui/interrogatory/interrogar_%s.png" xanchor 0.0 yanchor 0.5 ypos 0.7 xpos -0.010:
        action Notify(message=msj)
        # action Show("TextBoxPopup",message=msj)

##despues de cerrar la caja de texto, automaticamente avanza el script, lo cual no debe ser asi, esto solo pasa a la hora de seleccionar personaje
screen TextBoxPopup(message="Null"):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 20
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            textbutton "- OK -" action [Return(),Hide("TextBoxPopup")] xalign .5 top_padding -15 bottom_padding -20

################################################
## Mostrar el nombre de un minijuego
################################################
screen minigame_title(msj="Vacío",vers=1):
    if vers==1:
        $ hidetimer=3
        on "show" action Play('sound', audio.intro_minigame)
    elif vers==2:
        $ hidetimer=6
        on "show" action Play('sound', audio.intro_minigame2)
    timer hidetimer action Return()# Hide('minigame_title')
    timer hidetimer-0.3 action Play('sound', audio.flash)
    hbox at minigame_title:
        add "gui/header_ingame_bg.png"
    hbox at minigame_title:
        text "- [msj] -" color "#ffffff" size 90

#########################################################
## mostrar corazones a la hora de debate o interrogatorio
#########################################################

screen corazones():
    hbox at panelHearts:
        add "gui/superior_panel.png"
    hbox at panelHearts:
        spacing 5
        yoffset 9
        for x in xrange(0,cantidad_corazones):
            if cantidad_corazones<3:
                if cantidad_corazones==2:
                    add anim.Blink("gui/heart_full.png") 
                else:
                    add anim.Blink("gui/heart_full_danger.png")
            else:
                add "gui/heart_full.png"

## para mostrar un mensaje al lado del panel de corazones
screen notifyCorazones(msj="-1",pos_neg="pos"):

    #he dejado de usar esta pantalla ya que a veces en los interrogatorios la notificacion no desaparece luego de hacer rollback y en su lugar utilizo la pantalla de notify normal

    hbox at atlnotifyCorazones xanchor 0.5 yanchor 0.5 xpos 0.6 ypos 0.038:
        if pos_neg=="neg":
            text msj color "#FF0000" size 50 outlines [ (absolute(1.5), "#ffffff", absolute(0), absolute(0)) ]
        elif pos_neg=="pos":
            text msj color "#00AA00" size 50 outlines [ (absolute(1.5), "#ffffff", absolute(0), absolute(0)) ]



transform atlnotifyCorazones:
    yoffset -30
    parallel:
        notify_appear
    parallel:
        on show:
            linear .3 yoffset 0
            pause 2
            linear .3 yoffset -30
#####################################
## temporizador en la parte superior
#######################################

screen temporizador(cd_time):
    add "gui/superior_panel.png" xanchor 0.5 yanchor 0 xpos 0.3 ypos 0 at panelMinigameTop
    hbox at panelMinigameTop:
        xanchor 0.5 yanchor 0.013 xpos 0.3 ypos 0.013
        #icono_reloj
        add "gui/timer_icon.png" xanchor 1.0 yanchor 0.5 xpos 0.5 ypos 0.280
        add DynamicDisplayable(countdown, cd_time) xanchor 1.0 yanchor 0.5 xpos 1.0 ypos 0.3

## para mostrar un texto que indica si se agregó o restó tiempo, este
## texto estará arriba del mouse
screen mouseText(mx,my,txt="-10 sec"):
    hbox at notify_appear xanchor 0.5 yanchor 0.5 xpos mx-40 ypos my-60:
        text txt color "#FF0000" size 60 outlines [ (absolute(1.5), "#ffffff", absolute(0), absolute(0)) ]
    timer 1 action Hide('mouseText')

### Para mostrar personajes al hacer click, realizar accion

screen char_select(chars,chars_label):
    on "show" action Show("char1_select", char=chars,labels=chars_label)
    on "show" action Show("char2_select", char=chars,labels=chars_label)
    on "show" action Show("char3_select", char=chars,labels=chars_label)
    on "show" action Show("char4_select", char=chars,labels=chars_label)
    on "show" action Show("char5_select", char=chars,labels=chars_label)

screen char1_select(char=False,labels=False):
    if char:
        imagebutton idle char[0] xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 0.5 focus_mask True at char1_at:
            action [Hide("char1_select"),Show("char2_select", char=char, labels=labels),Show("char3_select", char=char, labels=labels),Show("char4_select", char=char, labels=labels),Show("char5_select", char=char, labels=labels),Jump(labels[0])] activate_sound audio.moneda

screen char2_select(char=False,labels=False):
    if char:
        imagebutton idle char[1] xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 0.5 focus_mask True at char2_at:
            action [Hide("char2_select"),Show("char1_select", char=char, labels=labels),Show("char3_select", char=char, labels=labels),Show("char4_select", char=char, labels=labels),Show("char5_select", char=char, labels=labels),Jump(labels[1])] activate_sound audio.moneda

screen char3_select(char=False,labels=False):
    if char:
        imagebutton idle char[2] xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 0.5 focus_mask True at char3_at:
            action [Hide("char3_select"),Show("char1_select", char=char, labels=labels),Show("char2_select", char=char, labels=labels),Show("char4_select", char=char, labels=labels),Show("char5_select", char=char, labels=labels),Jump(labels[2])] activate_sound audio.moneda

screen char4_select(char=False,labels=False):
    if char:
        imagebutton idle char[3] xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 0.5 focus_mask True at char4_at:
            action [Hide("char4_select"),Show("char1_select", char=char, labels=labels),Show("char2_select", char=char, labels=labels),Show("char3_select", char=char, labels=labels),Show("char5_select", char=char, labels=labels),Jump(labels[3])] activate_sound audio.moneda

screen char5_select(char=False,labels=False):
    if char:
        imagebutton idle char[4] xanchor 0.5 yanchor 1.0 ypos 1.0 xpos 0.5 focus_mask True at char5_at:
            action [Hide("char5_select"),Show("char1_select", char=char, labels=labels),Show("char2_select", char=char, labels=labels),Show("char3_select", char=char, labels=labels),Show("char4_select", char=char, labels=labels),Jump(labels[4])] activate_sound audio.moneda


transform char1_at:
    left
    char_click

transform char2_at:
    mleft
    char_click

transform char3_at:
    center
    char_click

transform char4_at:
    mright
    char_click

transform char5_at:
    right
    char_click
    
transform char_click:  
    alpha 1 
    zoom 1.2
    # aparecer
    on hide:
        parallel:
            brinquitos
        parallel:
            linear 0.5 xzoom -1.0 yzoom 1.0
            linear 0.5 xzoom 1.0 yzoom 1.0
            linear 0.4 alpha 0
    on replace:
        pause 1.4
        linear 0.4 alpha 0
        # pause 0.9
        # alpha 1


screen ruleta_incognita(letras1,letras2,pista,palabra):

    #las letras con las que esta formada la palabra
    $lstLetras=list(palabra)
    #obtenemos total de letras
    $totalpalabralet=len(palabra)

    frame xanchor 0.5 yanchor 0.5 xpos 370 ypos 385 xpadding 10 ypadding 10:
        vbox:
            text "{font=gui/fonts/fontawesome.ttf}{/font} [ruleta_porcentaje]%" color "#660066" size 50 text_align 0.5 xalign 0.5
            text "[totalpalabralet] letras" color "#660066" size 50 text_align 0.5 xalign 0.5

    vbox xanchor 1.0 xpos 0.950 yalign 0.5 spacing 10:

        frame xsize 500 xpadding 5 ypadding 5 xalign 0.5:
            text pista color "#555555" size 50 line_spacing -10 text_align 0.5 xalign 0.5

        frame xsize None xpadding 5 ypadding 5 xalign 0.5:
            text [c for c in lstLetrasActuales] color "#660066" size 60 line_spacing -10 text_align 0.5 xalign 0.5 kerning 15
    
    $totalet1=len(letras1)
    $totalet2=len(letras2)

    $gradoslet1plus=360/totalet1
    $gradoslet2plus=360/totalet2

    fixed style_prefix "letragrande":

        $gradoslet1=0
        for let in letras1:
            textbutton let at mov( gradoslet1,300 )  action Function(callable=checkLetraRuleta,letra_elegida=let,lstPalabra=lstLetras)
            $gradoslet1+=gradoslet1plus

        $gradoslet2=0
        for let in letras2:
            textbutton let at mov2( gradoslet2,200 ) action Function(callable=checkLetraRuleta,letra_elegida=let,lstPalabra=lstLetras)
            $gradoslet2+=gradoslet2plus


transform mov(ang,rad):
    alpha 0
    anchor (0.5, 0.5)
    around (370, 385)
    parallel:
        linear 4 alpha 1.0
    parallel:
        easein 4 radius rad clockwise circles 1 angle ang
    parallel:
        pause 3.5
        block:
            linear 9 clockwise circles 1
            repeat

transform mov2(ang,rad):
    alpha 0
    anchor (0.5, 0.5)
    around (370, 385)
    radius 0
    parallel:
        linear 4 alpha 1.0
    parallel:
        easein 4 radius rad clockwise circles 1 angle ang
    parallel:
        pause 3.5
        block:
            linear 10 clockwise circles -1
            repeat

style letragrande_button_text:
    color "#ffffff"
    hover_color "#E09915"
    font "gui/fonts/FjallaOne.otf"
    size 70
    line_spacing -10
    outlines [ (1, "#000000", 0, 0) ]


############################################
## Pantalla de teclado numerico
############################################

screen numpad(lbl=False,pista=False):

    if pista:
        frame xsize 400 ysize 600 yalign 0.5 xpos 100:
            viewport:
                scrollbars "vertical"
                draggable True
                mousewheel True
                arrowkeys False
                frame:
                    background None
                    padding [10,10]
                    text pista color "#555555" line_spacing -10 justify True adjust_spacing True

    ##teclado numerico
    fixed xpos 0.8 ypos 0.4:
        add "gui/numpad/base.png"
        frame xsize 216:
            background None
            hbox xalign 0.5:
                text numpad_cifra color "#56743A" font "gui/fonts/DS-DIGIB.TTF" size 100 yoffset -17
        grid 3 4 spacing -2 yoffset 73:
            for x in xrange(1,10):
                imagebutton auto "gui/numpad/"+str(x)+"_%s.png" action Function(numpadCifra,"add",x) focus_mask True activate_sound audio.numpad_hover
            imagebutton auto "gui/numpad/del_%s.png" action Function(numpadCifra,"del") focus_mask True activate_sound audio.ctc
            imagebutton auto "gui/numpad/0_%s.png" action Function(numpadCifra,"add",0) focus_mask True activate_sound audio.numpad_hover
            imagebutton auto "gui/numpad/ok_%s.png" action Jump(lbl) focus_mask True activate_sound audio.numpad_select

# style numpad_button:
#     zoom 3

screen btnSkipCredits():
    textbutton "Saltar créditos" action Jump("fin_creditos"):
        xalign 1.0
        yalign 1.0
        yoffset -10
        xoffset -10

screen casoFinDetalles():
    $ horas_jugados = convertSeconds( renpy.get_game_runtime() )[0]
    $ minutos_jugados = convertSeconds( renpy.get_game_runtime() )[1]
    $cor="{font=gui/fonts/fontawesome.ttf}{/font}" #icon_corazon
    $intel=pla_stat["intel"]
    $carisma=pla_stat["carisma"]
    $intel_total=intel*5
    $carisma_total=carisma*5

    add "images/bg/bg salon club detectives.jpg"
    frame:
        xmargin 10
        ymargin 10
        padding [10,5]
        text "Resultados de "+pla_name size 70 color "#660066"
    frame:
        xalign 1.0
        xmargin 10
        ymargin 10
        padding [10,5]
        vbox spacing -5:
            # text "Puntos de inteligencia: "+str(pla_stat["intel"]) size 25 color "#660066"
            # text "Puntos de carisma: "+str(pla_stat["carisma"]) size 25 color "#660066"
            text "Tiempo jugado: [horas_jugados] horas, [minutos_jugados] minutos." size 25 color "#660066"
    frame:
        ysize 450
        xalign .5
        yalign .5
        padding [20,20,20,20]
        # background "#FFFFFF"
        viewport:
            scrollbars "vertical"
            draggable True
            mousewheel True
            arrowkeys True
            vbox:
                $total=0
                $ i=0
                $countgm=persistent.gameover_counter[id_partida]
                for x in fase_titulo:
                    $title=x
                    $tipo=fase_tipo_vida[i]
                    $mult=fase_multiplicador[i]
                    $cant=fase_corazones[i]
                    if tipo=="cantidad":
                        $puntos=cant*mult
                    else:
                        $puntos=(cant/10)*mult
                    $total+=puntos

                    hbox spacing 30 xalign 1.0:
                        text title color "#404040"
                        if tipo=="cantidad":
                            text "{color=#FF0000}[cor]{/color}0[cant] X [mult] =" color "#404040"
                        else:
                            text "[cant]% X 0[mult] =" color "#404040"
                        text "[puntos] Ptos." color "#106885"              
                    $i+=1
                hbox spacing 30 xalign 1.0:
                    text "Puntos de inteligencia" color "#404040"
                    text "[intel] X 5 =" color "#404040"
                    text "[intel_total] Ptos." color "#106885"
                hbox spacing 30 xalign 1.0:
                    text "Puntos de carisma" color "#404040"
                    text "[carisma] X 5 =" color "#404040"
                    text "[carisma_total] Ptos." color "#106885"
                #para evitar una division entre cero
                $total=total+carisma_total+intel_total
                if countgm==0:
                    $total_final=total
                else:
                    $total_final=total/countgm
                hbox spacing 30 xalign 1.0:

                    text "Total: [total] Ptos." color "#AB7510"
                    if countgm==0:
                        text "(sin game over) =" color "#AB7510"
                    else:
                        text "/ [countgm] \"Game overs\" =" color "#AB7510"
                    text "[total_final] Ptos." color "#AB7510"

    #obtener rango
    # S 130-alto
    # A 90-129
    # B 60-89
    # C 30-59
    # D 0-29
    if total_final>=130:
        $rango="S - Dupin"
        $hiki_unlock=True
    elif total_final>=90 and total_final<130:
        $rango="A - Holmes"
        $hiki_unlock=True
    elif total_final>=60 and total_final<90:
        $rango="B - Kogoro"
        $hiki_unlock=True
    elif total_final>=30 and total_final<60:
        $rango="C - Watson"
        $hiki_unlock=False
    elif total_final<30:
        $rango="D - Lestrade"
        $hiki_unlock=False

    frame:
        xmargin 10
        ymargin 10
        padding [10,5]
        yalign 1.0
        xalign .5
        text "Rango "+rango size 70 color "#660066"
    hbox:
        xalign 1.0
        yalign 1.0
        imagebutton auto "gui/numpad/ok_%s.png" action Return(hiki_unlock) at atlGameResultsBtn

transform atlGameResultsBtn:
    zoom 1.3#zoomqckmenu


screen credits():
    text gui.about at creditstext

transform creditstext:
    xalign .5
    yoffset 900
    on show:
        linear 70  yoffset -12500

################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if not main_menu:

            textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action MainMenu()

            textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action ShowMenu("history")
                
            textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action ShowMenu("save")

            textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action ShowMenu("load")

            textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action ShowMenu("preferences")

            if not renpy.ios :
                textbutton "{font=gui/fonts/fontawesome.ttf}{/font}" action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")


style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    size 60
    xalign 0.5
    line_spacing 10


## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    on "show" action Function(callable=change_cursor)

    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    tag menu

    style_prefix "main_menu"

    add "fondoMainMenu"#gui.main_menu_background

    # add "gui/overlay/main_menu_1.png" yanchor 1.0 ypos 723 xoffset -3 at leftpanelMainMenu

    add "images/alice_objection_gorro.png" yalign 1.0 xpos 0.100 at aliceMainMenu

    add "images/logo.png" at atlLogo

    vbox xanchor .5 xpos .8 yanchor .5 ypos .550 spacing 10 at aparecer:
        vbox xalign .5 spacing -3 xoffset -3 at atlMainMenuBtns(1):
            imagebutton auto "gui/main_menu_btns/inicio_%s.png" action Start() focus_mask True
            imagebutton auto "gui/main_menu_btns/cargar_%s.png" action ShowMenu("load") focus_mask True
        hbox spacing 20:
            imagebutton auto "gui/main_menu_btns/opciones_%s.png" action ShowMenu("preferences") focus_mask True at atlMainMenuBtns(1)
            imagebutton auto "gui/main_menu_btns/acerca_%s.png" action ShowMenu("about") focus_mask True at atlMainMenuBtns(1)
        imagebutton auto "gui/main_menu_btns/ayuda_%s.png" action ShowMenu("help") focus_mask True xalign .5

    hbox yoffset -50 spacing 40 at aparecer:
        yanchor 1.0 ypos 0.950 xpos 0.030
        imagebutton auto "gui/main_menu_btns/donar_%s.png" action OpenURL("http://dannygaray60.blogspot.com/p/donaciones-por-paypal.html") focus_mask True at atlMainMenuBtns(1)
        if persistent.extras_unlocked:
            imagebutton auto "gui/main_menu_btns/extras_%s.png" action ShowMenu("extras") focus_mask True at atlMainMenuBtns(1)
        else:
            imagebutton idle "gui/main_menu_btns/extras_insensitive.png" action NullAction() focus_mask True at atlMainMenuBtns(1)

    imagebutton auto "gui/main_menu_btns/salir_%s.png" action Quit(confirm=not main_menu) focus_mask True yalign 1.0 xoffset -2 yoffset 2 at leftpanelMainMenu



    ## Este marco vacío oscurece el menu principal.
    # frame:
    #     pass

    ## La sentencia 'use' incluye otra pantalla dentro de esta. El contenido
    ## real del menú principal está en la pantalla de navegación.
    # vbox at leftpanelMainMenu:
    #     style_prefix "main_menu_navigation"

    #     xpos 20
    #     yalign 1.0

    #     spacing gui.navigation_spacing

    #     textbutton _("Comenzar") action Start()
    #     textbutton _("Cargar") action ShowMenu("load")
    #     textbutton _("Extras") action ShowMenu("extras")
    #     textbutton _("Opciones") action ShowMenu("preferences")
    #     textbutton _("Acerca de") action ShowMenu("about")

    #     if renpy.variant("pc"):
    #         ## La ayuda no es necesaria ni relevante en dispositivos móviles.
    #         textbutton _("Ayuda") action ShowMenu("help")
    #     ## El botón de salida está prohibido en iOS y no es necesario en
    #     ## Android.
    #     if not renpy.ios and not renpy.variant("ios") :
    #         textbutton "Salir" action Quit(confirm=not main_menu)

    

    if gui.show_name:
        add "gui/button/choice_hover_background.png" xanchor 0.0 xpos 0.780 ypos 1.0 yanchor 1.0
        text "Versión: [config.version] ([version_state])" xanchor 1.0 xpos 0.990 yanchor 1.0 ypos 1.0 color "#ffffff" size 25

    if config.debug:
        add "gui/button/choice_hover_background.png" xanchor 0.0 xpos 0.700 ypos 0.0 yanchor 0.0 at fliped_v
        text "Modo desarrollador activado" xanchor 1.0 xpos 0.990 yanchor 0.0 ypos 0.005 color "#ffffff" size 25


    # add "gui/button/choice_selected_background.png" at panelMainMenuTitle

    # hbox ypos 0.030 xpos 0.010 at leftpanelMainMenu:#aparecer:
    #     text "[config.name!t]":
    #         color "#ffffff"
    #         size 55
    #         # style "main_menu_title"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

# style main_menu_navigation_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

style main_menu_navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    size 50
    xalign 0.0
    hover_color "#ffffff"
    line_spacing -20


# style main_menu_frame:
#     xsize 280
#     yfill True

#     background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Cuando se usa
## esta pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

screen game_menu(title, scroll=None, yinitial=0.0,chibi=0):

    on "show" action Stop(channel="text")

    #add "gui/semi_dark_screen.png"

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background


    frame:
        style "game_menu_outer_frame"
        if main_menu:
            hbox at atlhbox_chibis_gamemenu:
                if chibi==1:
                    add "images/chibipixel_alice.png" at smolchar_random_move
                elif chibi==2:
                    add "images/chibipixel_marissa.png" at smolchar_random_move
        else:
            hbox spacing 90 at atlhbox_chibis_gamemenu_ingame:
                add "images/chibipixel_alice.png" at smolchar2_random_move
                add "images/chibipixel_marissa.png" at smolchar2_random_move
        hbox:

            ## Reservar espacio para la sección de navegación.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if main_menu:
        textbutton "Regresar {font=gui/fonts/fontawesome.ttf}{/font}":
            style "main_return_button"

            action Return()
    else:
        textbutton "{font=gui/fonts/fontawesome.ttf}{/font}":
            style "return_button"
            action Return()

            

    label title

    # if main_menu:
    #     key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 20
    right_margin 20
    top_margin 10

style game_menu_content_frame:
    variant "small"
    left_margin -30

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size 60
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style main_return_button:
    xpos 10
    yalign 1.0
    yoffset -30
style main_return_button_text:
    size 50


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Acerca de"), scroll="viewport",chibi=2):

        style_prefix "about"

        vbox:
            text "[config.name!t]" color gui.accent_color size 40
            text _("{i}Versión [config.version!t] ([version_state]){/i}\n")

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n" text_align 0.5

            text _("Programado en {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]. Código fuente del juego disponible en {a=https://github.com/dannygaray60/club_de_detectives_01}Github.{/a}\n\n[renpy.license!t]")


## Esto se redefine en 'options.rpy' para añadir texto a la pantalla 'acerca
## de'.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


####################################################
### pantalla de extras
####################################################

screen extras():

    tag menu


    use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Extras"), scroll="viewport",chibi=1):

        style_prefix "extras"

        vbox:
            textbutton "{font=gui/fonts/fontawesome.ttf}{/font} ¿Quieres la secuela del juego?" action Start("palabras_autor")
            # textbutton "{font=gui/fonts/fontawesome.ttf}{/font} Leer \"Hikikomori Holmes\"" action Start("hikikomoriholmes")
            textbutton "{font=gui/fonts/fontawesome.ttf}{/font} Soundtrack" action ShowMenu("music_room")
            # textbutton "{font=gui/fonts/fontawesome.ttf}{/font} Rangos obtenidos" action ShowMenu("rangos")
        null height 90
        text "Otras obras del autor." color gui.selected_color size 60 xalign .5 text_align .5
        null height 40
        grid 3 2:
            imagebutton idle "images/covers_ln/1.jpg" action OpenURL("http://dannygaray60.blogspot.com/2017/11/end-of-melancholy-novela-ligera.html") at atlNovelsCover(0.3)
            imagebutton idle "images/covers_ln/2.jpg" action OpenURL("http://dannygaray60.blogspot.com/2018/11/ikigai-academy-novela-web-18-leer-online.html") at atlNovelsCover(0.350)
            imagebutton idle "images/covers_ln/3.png" action OpenURL("http://dannygaray60.blogspot.com/2018/10/hasta-que-vuelvas-sonreir-novela-ligera.html") at atlNovelsCover(0.400)
            imagebutton idle "images/covers_ln/4.jpg" action OpenURL("http://dannygaray60.blogspot.com/2018/02/una-mirada-ausente-relato-lectura-online.html") at atlNovelsCover(0.200)
            imagebutton idle "images/covers_ln/5.jpg" action OpenURL("http://dannygaray60.blogspot.com/2018/10/hikikomori-holmes-novela-ligera.html") at atlNovelsCover(0.290)
            null

        imagebutton idle "images/covers_ln/collage.jpg" action OpenURL("http://dannygaray60.blogspot.com"):
            xalign .5
 
transform atlNovelsCover(z):
    zoom z
    on hover:
        alpha 0.6
    on idle:
        alpha 1.0
    


style extras_button_text:
    color gui.accent_color 
    hover_color gui.interface_text_color
    size 70
    hover_underline True


screen game_over():
    timer 0.5 action Play('sound', audio.game_over2)
    timer 3.5 action Play('sound', audio.ctc)
    # text "Reintentos: "+str(persistent.gameover_counter[id_partida]) at atlReintentosTxt size 30
    add "gui/game_over_screen/foco.png" at atlGameOverFoco
    add "images/alice_chibi_cry.png" at atlGameOverChibi
    add "gui/game_over_screen/texto.png" at atlGameOverText
    hbox at atlGameOverBtns:
        spacing 100
        imagebutton auto "gui/game_over_screen/si_%s.png" action Function(callable=loadCheckPoint) hover_sound audio.txtbip
        imagebutton auto "gui/game_over_screen/no_%s.png" action Return() hover_sound audio.txtbip
transform atlReintentosTxt:
    xalign 1.0
    xoffset -10
    yoffset 10
transform atlGameOverText:
    yoffset -500
    xanchor 1.0
    xpos .970
    ypos .2
    on show:
        ease 1 yoffset 100
        ease .5 yoffset 0
transform atlGameOverBtns:
    alpha 0
    xanchor .5
    xpos .7
    yanchor 1.0
    ypos .9
    on show:
        pause 2
        linear .5 alpha 1.0
transform atlGameOverChibi:
    alpha .050
    zoom .7
    xanchor .5
    xpos .220
    ypos .150
    on show:
        pause 3.5
        alpha 1.0
transform atlGameOverFoco:
    alpha 0
    on show:
        pause 3.5
        alpha 1

# screen rangos():
#     tag menu

#     use game_menu("Rangos obtenidos", scroll="viewport"):

#         vbox:
#             hbox:
#                 if persistent.rango_s:
#                     add "gui/window_icon - copia.png"
#                 else:
#                     add "gui/window_icon - copia2.png"
#                 vbox:
#                     text "S - Dupin" color "#660066"
#                     text "Consigue 130 puntos o más." color "#555555"
#             hbox:
#                 if persistent.rango_a:
#                     add "gui/window_icon - copia.png"
#                 else:
#                     add "gui/window_icon - copia2.png"
#                 vbox:
#                     text "A - Holmes" color "#660066"
#                     text "Consigue 90 puntos o más." color "#555555"
#             hbox:
#                 if persistent.rango_b:
#                     add "gui/window_icon - copia.png"
#                 else:
#                     add "gui/window_icon - copia2.png"
#                 vbox:
#                     text "B - Kogoro" color "#660066"
#                     text "Consigue 60 puntos o más." color "#555555"
#             hbox:
#                 if persistent.rango_c:
#                     add "gui/window_icon - copia.png"
#                 else:
#                     add "gui/window_icon - copia2.png"
#                 vbox:
#                     text "C - Watson" color "#660066"
#                     text "Consigue 30 puntos o más." color "#555555"
#             hbox:
#                 if persistent.rango_d:
#                     add "gui/window_icon - copia.png"
#                 else:
#                     add "gui/window_icon - copia2.png"
#                 vbox:
#                     text "D - Lestrade" color "#660066"
#                     text "Consigue 29 puntos o menos." color "#555555"

# Step 3. Create the music room screen.
screen music_room():

    tag menu

    on "replaced" action Play('music', audio.tema_principal)

    use game_menu("Soundtrack", scroll="viewport"):

        style_prefix "music_room"

        # The buttons that play each track.
        textbutton "Poofy Reel" action mr.Play("audio/bgm/poofy_reel.ogg")
        textbutton "Careless Summer" action mr.Play("audio/bgm/careless_summer.ogg")
        textbutton "Operatic 3" action mr.Play("audio/bgm/operatic_3.ogg")
        textbutton "Pug too sanpo" action mr.Play("audio/bgm/pugtoosanpo.ogg")
        textbutton "Comical Pizzicato" action mr.Play("audio/bgm/comical_pizzicato.ogg")
        textbutton "Ionic Magnet" action mr.Play("audio/bgm/ionic_magnet.ogg")
        textbutton "Destiny" action mr.Play("audio/bgm/destiny.ogg")
        textbutton "Bacteria" action mr.Play("audio/bgm/bacteria.ogg")
        textbutton "Texture 2" action mr.Play("audio/bgm/texture2.ogg")
        textbutton "First in line" action mr.Play("audio/bgm/first_in_line.ogg")
        textbutton "Retro Party" action mr.Play("audio/bgm/retroparty.ogg")

        null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()
        # Restore the main menu music upon leaving.
        # on "replaced" action Play("music", "track1.ogg")

style music_room_button_text:
    color gui.accent_color 
    hover_color gui.interface_text_color
    size 70

## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    if not quick_menu_gameplay:

        use file_slots("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Guardar"))

    else:
        use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Guardar")):

            # vbox :
            text "La opción de guardado ha sido desactivada, posiblemente hay un minijuego en transcurso." color gui.accent_color size 40 xalign 0.5

            add "images/sherinford.png" xalign 0.5 yalign 1.0 ypos .9


screen load():

    tag menu

    use file_slots("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title,chibi=1):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.4

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        if renpy.get_screen("load"):
                            action [FileAction(slot),Function(callable=change_cursor)]
                        else:
                            action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action [FilePagePrevious(),Play('sound', audio.ctc)]

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}R") action FilePage("quick")

                ## range(1, 10) da los numeros del 1 al 9.
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)

                # textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action FilePageNext()
                textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action If ( int(FileCurrentPage())>4, true=None, false=[FilePageNext(),Play('sound', audio.ctc)] )


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    size 40
    # ypos 0.0

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    size 60

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    size 20


## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.variant("pc"):
        $ xps_box=0.8
    else:
        $ xps_box=0.0

    use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Opciones"), scroll="viewport",chibi=1):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action Preference("display", "window")
                        textbutton _("Pant. completa") action Preference("display", "fullscreen")

                vbox xpos xps_box:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action Preference("skip", "toggle")
                    # textbutton _("Tras opciones") action Preference("after choices", "toggle")
                    # textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

                ## Aquí se pueden añadir 'vboxes' adicionales del tipo
                ## "radio_pref" o "check_pref" para nuevas preferencias.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Velocidad de texto")

                    bar value Preference("text speed")

                    label _("Velocidad de autoavance")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volumen de música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volumen de sonido")

                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action Play("sound", config.sample_sound)

                        label _("Volumen de texto")

                        hbox:
                            bar value MixerValue('txt')
                            textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action Play("text", audio.txtbip,selected=False)
                            textbutton _("{font=gui/fonts/fontawesome.ttf}{/font}") action Stop(channel="text")


                    if config.has_voice:
                        label _("Volumen voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Prueba") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("{font=gui/fonts/fontawesome.ttf}{/font} Silenciar todo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0
    size 40

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10
    top_padding -2

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
    predict False

    use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Esto distribuye los elementos apropiadamente si
                ## 'history_height' es 'None'.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Toma el color del texto 'who' de 'Character', si ha
                        ## sido establecido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text "\n"+what:
                    substitute False

        if not _history_list:
            label _("El historial está vacío.")


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xpos -30
    xfill True
    ysize gui.history_height
    

style history_window:
    variant "small"
    xpos -60

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    size 40
    xalign 0.0

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    size 35

    xoffset -155

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    if renpy.variant("large"):
        default device = "keyboard"
    else:
        default device = "general"

    use game_menu("{font=gui/fonts/fontawesome.ttf}{/font} "+_("Ayuda"), scroll="viewport",chibi=2):

        style_prefix "help"
        # if renpy.variant("large"):
        vbox:
            spacing 15
            hbox:
                if renpy.variant("small"):
                    textbutton _("General") action SetScreenVariable("device", "general")
                textbutton _("Rangos") action SetScreenVariable("device", "rangos")
                if renpy.variant("large"):
                    textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                    textbutton _("Ratón") action SetScreenVariable("device", "mouse")
                    if GamepadExists():
                        textbutton _("Mando") action SetScreenVariable("device", "gamepad")
        null height 50
        if device == "general":
            use general_help
        elif device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help
        elif device == "rangos":
            use rangos_help
    # else:
    #     use general_help

screen general_help():
    #solo se mostrara en version movil
    hbox:
        label _("Toque en pantalla")
        text _("Avanzar el diálogo.")
    hbox:
        label _("Botón atrás")
        text _("Mostrar el historial de diálogo.")        
    hbox:
        text "Para cerrar el juego se recomienda usar el botón de salir del menú principal."

screen rangos_help():
    vbox:
        vbox:
            text "S - Dupin" color "#660066"
            text "Consigue 130 puntos o más." color "#555555"

        vbox:
            text "A - Holmes" color "#660066"
            text "Consigue 90 puntos o más." color "#555555"

        vbox:
            text "B - Kogoro" color "#660066"
            text "Consigue 60 puntos o más." color "#555555"

        vbox:
            text "C - Watson" color "#660066"
            text "Consigue 30 puntos o más." color "#555555"

        vbox:
            text "D - Lestrade" color "#660066"
            text "Consigue 29 puntos o menos." color "#555555"

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Avanzar el diálogo y activar la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanzar el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navegar en la interfaz.")

    hbox:
        label _("Escape")
        text _("Acceder al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Saltar el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activar/desactivar el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Mostrar el historial de diálogo.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Ocultar la interfaz.")

    hbox:
        label "S"
        text _("Captura de pantalla.")

    hbox:
        label "A"
        text _("Activar/desactivar el auto avance de texto.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanzar el diálogo y activar la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Ocultar la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Acceder al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba\nClic en lado de retroceso")
        text _("Mostrar el historial de diálogo.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanzar hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanzar el diálogo y activa la interfaz.")

    # hbox:
    #     label _("Gatillo izquierdo\nBotón sup. frontal izq.")
    #     text _("Retrocede al diálogo anterior.")

    # hbox:
    #     label _("Botón sup. frontal der.")
    #     text _("Avanza hacia el diálogo siguiente.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Comenzar, Guía")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Asegura que otras pantallas no reciban entrada mientras se muestra esta
    ## pantalla.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton "{font=gui/fonts/fontawesome.ttf}{/font} "+_("Sí") action yes_action
                textbutton "{font=gui/fonts/fontawesome.ttf}{/font} "+_("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    size 40

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 50

## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    xpos gui.skip_xpos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "{font=gui/fonts/fontawesome.ttf}{/font} [message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    xpos gui.notify_xpos
    right_padding 50
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    font "gui/fonts/playtime.ttf"


## Pantalla para mostrar una imagen de evidencia
screen noteImg(imagen,autohide=True):
    add "images/notes_img/"+imagen+"_thumb.jpg" at notaaparecer
    if autohide:
        timer 4 action Hide('noteImg')


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True',
        ## como lo es más arriba.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Variantes móviles
################################################################################

# style pref_vbox:
#     variant "medium"
#     xsize 450

## Ya que puede carecer de ratón, se reempleza el menú rápido con una versión
## con menos botones y más grandes, más fáciles de tocar.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu:

#         hbox:
#             style_prefix "quick"

#             xalign 0.5
#             yalign 1.0

#             textbutton _("Atrás") action Rollback()
#             textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Menú") action ShowMenu()


# style window:
#     variant "small"
#     background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu.png"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size+20
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size+25
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    xoffset 8

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
