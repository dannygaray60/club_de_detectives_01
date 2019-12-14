init -2 python:

    import datetime

    #con esto se puede obtener fecha actual, con $today.month $today.year etc
    # today=datetime.date.today()
    # today_time=datetime.time.today()

    if renpy.variant("android"):
        zoomqckmenu=1.2
        interrbtnyoff=-170
        nameboxyoff=-11
        notepadnotifyxoffset=-60
        choice_args_xanchor=0.950
    else:
        zoomqckmenu=1
        interrbtnyoff=-50
        nameboxyoff=0
        notepadnotifyxoffset=0
        choice_args_xanchor=1.0

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)
    # Step 2. Add music files.
    mr.add("audio/bgm/poofy_reel.ogg", always_unlocked=True)
    mr.add("audio/bgm/careless_summer.ogg", always_unlocked=True)
    mr.add("audio/bgm/operatic_3.ogg", always_unlocked=True)
    mr.add("audio/bgm/pugtoosanpo.ogg", always_unlocked=True)
    mr.add("audio/bgm/comical_pizzicato.ogg", always_unlocked=True)
    mr.add("audio/bgm/ionic_magnet.ogg", always_unlocked=True)
    mr.add("audio/bgm/destiny.ogg", always_unlocked=True)
    mr.add("audio/bgm/bacteria.ogg", always_unlocked=True)
    mr.add("audio/bgm/texture2.ogg", always_unlocked=True)
    mr.add("audio/bgm/first_in_line.ogg", always_unlocked=True)
    mr.add("audio/bgm/retroparty.ogg", always_unlocked=True)

    #para impedir que el jugador haga pausa, scroll, avanzar texto, o cualquier otra interaccion:
    def noInteract(val=True):
        if val:
            config.allow_skipping = False
            config.keymap['game_menu']=[]
            config.keymap['help']=[]
            config.keymap['history']=[]
            renpy.clear_keymap_cache()
        else:
            config.keymap['game_menu']=[ 'K_ESCAPE', 'K_MENU', 'mouseup_3' ]
            config.keymap['help']=[ 'K_F1', 'meta_shift_/' ]
            config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]
            renpy.clear_keymap_cache()
            config.allow_skipping = True


    ## para actualizar el numer de la cifra del teclado numerico virtual
    def numpadCifra(act="add",num=0):
        global numpad_cifra
        if act=="del":
            ##removemos la ultima cifra
            numpad_cifra=numpad_cifra[:-1]
            ##agregamos un cero al inicio de la cifra
            numpad_cifra="0"+numpad_cifra
        elif act=="add":
            ##removemos la primera cifra
            numpad_cifra=numpad_cifra[1:]
            ##agregamos el numero al final de la cifra
            numpad_cifra=numpad_cifra+str(num)

    def loadCheckPoint():
        renpy.load("checkpoint")

    def checkLetraRuleta(letra_elegida,lstPalabra):
        global ruleta_id
        global posicionenpalabra
        global ruleta_porcentaje
        global lstLetrasActuales
        global timeup
        mouse_x= renpy.get_mouse_pos()[0]
        mouse_y= renpy.get_mouse_pos()[1]

        if not timeup and ruleta_porcentaje>0:

            if lstPalabra[posicionenpalabra]==letra_elegida:
                renpy.play(audio.correcto,channel="sound")
                lstLetrasActuales[posicionenpalabra]=letra_elegida
                posicionenpalabra+=1
                if len(lstLetrasActuales)==posicionenpalabra:
                    renpy.hide_screen("ruleta_incognita")
                    renpy.hide_screen("temporizador")
                    change_cursor()
                    renpy.jump("ruleta"+str(ruleta_id)+"_fin")
            else:
                renpy.play(audio.incorrecto,channel="sound")
                if ruleta_porcentaje<=10:
                    renpy.hide_screen("ruleta_incognita")
                    renpy.hide_screen("temporizador")
                    change_cursor()
                    renpy.jump("ruleta"+str(ruleta_id)+"_gameover")
                else:
                    renpy.show_screen('mouseText',mouse_x,mouse_y,"-10 %")
                    ruleta_porcentaje-=10
                

        elif timeup:
            renpy.hide_screen("ruleta_incognita")
            renpy.hide_screen("temporizador")
            change_cursor()
            renpy.jump("ruleta"+str(ruleta_id)+"_gameover")


    def updateStat(nvar,tipo="set",valor=0):
            global pla_stat

            if tipo=="set":
                pla_stat[nvar]=valor
            elif tipo=="+":
                pla_stat[nvar]+=valor
            elif tipo=="-":
                pla_stat[nvar]-=valor

            if pla_stat[nvar]<0:
                pla_stat[nvar]=0


    ## reiniciar variables que se utilizarán a lo largo del juego
    def resetVar():
        from datetime import datetime
        initNotepadVars()
        initDebateVars()
        initInterrVars()
        initEvidencVars()
        initCorazones()
        clearNotepad()
        timeUpFalse()

        #variable para activar desactivar el cartel de la hora y fecha de quick_menu
        global quick_menu_timescr
        quick_menu_timescr=True

        ## Datos del jugador
        global pla_name
        global pla_stat
        pla_stat={1:"intel",2:"carisma"}
        pla_name = "Yo"
        pla_stat["intel"]=0
        pla_stat["carisma"]=0

        ## menu rapido especial para debates
        global quick_menu_bajo
        quick_menu_bajo=False

        ## boton bloc de notas
        global quick_menu_btn_notepad
        quick_menu_btn_notepad=False

        ## quickmenu para debate,interrogatorio... o cualquier otro evento donde se prohiba guardar, cargar...
        global quick_menu_gameplay
        quick_menu_gameplay=False

        ## boton del quickmenu para saltar texto
        # global skip_btn_disabled
        # skip_btn_disabled=False

        ## Tiempo y día
        ###############
        ## la hora en formato de 24 (22,12,3...)
        global hora
        hora=8
        # el estado del juego, (libre, investigacion, debate, testimonio, escuela...)
        global estadoj
        estadoj = "Libre"
        ## la fecha
        global fecha
        fecha="Enero 01"
        ##dia actual (Lun,Mar,Mié,Jue,Vie,Sáb,Dom)
        global dia
        dia="Lun."

        #contador de gameovers
        now = datetime.now()
        global id_partida
        id_partida=now.strftime("%d%m%Y_%H%M%S")
        persistent.gameover_counter[id_partida]=0 

        #minijuegos fases
        #en listas
        global fase_titulo
        global fase_corazones
        #cantidad o porcentaje
        global fase_tipo_vida
        global fase_multiplicador
        fase_titulo=[]
        fase_corazones=[]
        fase_tipo_vida=[]
        fase_multiplicador=[]
        

    ## inicializar variables para interrogatorio
    def initInterrVars():
        global interr_id
        interr_id=0
        ## id de la frase en el interrogatorio
        global interr_fraseid
        interr_fraseid=0
        ## para desactivar los botones de refutar e interrogar
        global interr_btns_disable
        interr_btns_disable=False
        ## para definir cual es el item del block de notas que es correcto para refutar una frase de interrogatorio
        global interr_item_notepad_correcto
        interr_item_notepad_correcto=0
        ## y cual es el seleccionado
        global interr_item_notepad_select
        interr_item_notepad_select=0
        ## cual es el id de la frase final (contamos desde 0)
        global interr_frasefinal
        interr_frasefinal=0
        ## botones
        global interr_btn_refutar_disabled
        interr_btn_refutar_disabled=False
        ##variable bandera, que determina si una frase fue interrogada.
        # global frase_interrogada
        # frase_interrogada=[]


    ## inicializar variables para mostrar una evidencia
    def initEvidencVars():
        global idevidencia_mostrar
        idevidencia_mostrar=0
        global idevidencia_correcta
        idevidencia_correcta=0
        global evidencia_mostrada
        evidencia_mostrada=False

    #################################
    ## Funciones para el notepad
    ####################################

    def initNotepadVars():
        global lstNotepad_titulo
        global lstNotepad_desc
        global lstNotepad_thumb
        global lstNotepad_img
        lstNotepad_titulo=[]
        lstNotepad_desc=[]
        lstNotepad_thumb=[]
        lstNotepad_img=[]


    ## reproducir sonido notificacion y mostrarla encima del icono del block de notas
    def notepad_notify():
        global notepad_notificacion
        notepad_notificacion=True
        renpy.play(audio.notificacion,channel="sound")

    ## añadir elemento al notepad
    def addNote(titulo,descripcion,imagen=False,ampliable=False):
        global lstNotepad_titulo
        global lstNotepad_desc
        global lstNotepad_thumb
        global lstNotepad_img
        lstNotepad_titulo.append(titulo)
        lstNotepad_desc.append(descripcion)
        lstNotepad_thumb.append(imagen)
        if ampliable:
            lstNotepad_img.append(imagen)
        else:
            lstNotepad_img.append(False)
        if imagen:
            renpy.show_screen("noteImg",imagen)
        renpy.notify('"'+titulo+'" agregado al bloc de notas.')
        notepad_notify()

    ## remover nota en base a un numero de array
    def removeNote(numarg):
        global lstNotepad_titulo
        global lstNotepad_desc
        global lstNotepad_thumb
        global lstNotepad_img

        #si el id no es un entero, entonces obtendremos la posicion en el array
        if not isinstance(numarg,int):
            numarg=lstNotepad_titulo.index(numarg)

        titulonote=lstNotepad_titulo[numarg]

        lstNotepad_titulo.pop(numarg)
        lstNotepad_desc.pop(numarg)
        lstNotepad_thumb.pop(numarg)
        lstNotepad_img.pop(numarg)

        renpy.play(audio.notificacion,channel="sound")
        renpy.notify('"'+titulonote+'" eliminado del bloc de notas.')

    ## actualizar un elemento en base a un numero array
    def updateNote(numarg,ntit=False,ndesc=False,nthu=False,nimg=False,add=False):
        global lstNotepad_titulo
        global lstNotepad_desc
        global lstNotepad_thumb
        global lstNotepad_img

        #si el id no es un entero, entonces obtendremos la posicion en el array
        if not isinstance(numarg,int):
            numarg=lstNotepad_titulo.index(numarg)

        if ntit:
            lstNotepad_titulo[numarg]=ntit
        if ndesc:
            #si add es true, entonces añadimos texto a la descripción
            if add:
                lstNotepad_desc[numarg]+=ndesc
            else:
                lstNotepad_desc[numarg]=ndesc
        if nthu:
            lstNotepad_thumb[numarg]=nthu
            renpy.show_screen("noteImg",nthu)
        if nimg:
            lstNotepad_img[numarg]=nimg
        if not ntit:
            renpy.notify('"'+lstNotepad_titulo[numarg]+'" actualizado.')
        else:
            renpy.notify('"'+ntit+'" actualizado.')
        notepad_notify()

    ## Eliminar todos los items del bloc de notas
    def clearNotepad():
        ## para mostrar circulo de notificacion en block de notas
        global notepad_notificacion
        notepad_notificacion=False
        ##limpiamos variables
        global lstNotepad_titulo
        lstNotepad_titulo=[]
        global lstNotepad_desc
        lstNotepad_desc=[]
        global lstNotepad_thumb
        lstNotepad_thumb=[]
        global lstNotepad_img
        lstNotepad_img=[]
   
    

    ###############################
    ## funciones para los corazones
    ###############################
    def initCorazones():
        global cantidad_corazones
        cantidad_corazones = 5
    #he dejado de usar esta pantalla ya que a veces en los interrogatorios la notificacion no desaparece luego de hacer rollback y en su lugar utilizo la pantalla de notify normal
    def addCorazones(cnt=1):
        global cantidad_corazones
        if cantidad_corazones<5:
            renpy.hide_screen("corazones")
            renpy.play(audio.moneda,channel="sound")
            cantidad_corazones=cantidad_corazones+cnt
            renpy.show_screen("corazones")
        elif cantidad_corazones>5:
            cantidad_corazones=5
    def restCorazones(cnt=1):
        global cantidad_corazones
        if cantidad_corazones<0:
            cantidad_corazones=0
        else:
            renpy.hide_screen("corazones")
            renpy.play(audio.golpe,channel="sound")
            cantidad_corazones=cantidad_corazones-cnt
            renpy.show_screen("corazones")


    def showMinigameTitle(msj,vers=1):
        renpy.choice_for_skipping()
        renpy.save("checkpoint")
        renpy.call_screen("minigame_title",msj,vers)
        # if vers==1:
        #     renpy.pause(3.5,hard=True)
        # elif vers==2:
        #     renpy.pause(6.3,hard=True)        


    ########################################
    ## Funciones para el momento del debate
    #########################################

    ## inicializar variables para debate
    def initDebateVars():
        global frase_args
        global debate_args
        global debate_arg_seleccionado
        frase_args=[]
        debate_args=[]
        ## cual id de argumento está seleccionado por defecto
        debate_arg_seleccionado = 0

    ## esconder textos de personajes
    def clearDebateText():
        renpy.hide_screen("debateCharPanel")
        renpy.hide_screen("debateText1")
        renpy.hide_screen("debateText2")
        renpy.hide_screen("debateText3")
        renpy.hide_screen("debateText4")

    ###########################
    ## Funciones para eventos
    ###########################

    def show_gameplay_layout(t):
        renpy.show_screen("corazones")
        renpy.show_screen("temporizador",t)
    ## y para ocultarlas
    def hide_gameplay_layout():
        renpy.hide_screen("corazones")
        renpy.hide_screen("temporizador")

    def hide_select_chars():
        renpy.hide_screen("char1_select")
        renpy.hide_screen("char2_select")
        renpy.hide_screen("char3_select")
        renpy.hide_screen("char4_select")
        renpy.hide_screen("char5_select")    
    ##############################
    ## otras funciones
    #################################

    ## comprobamos si un texto es valido para ser un nombre de persona
    def checkNamePlayer(txt):
        ## comprobamos si al menos tiene una letra, o contiene caracteres alfabeticos
        ## y si tiene más de 2 caracteres o menos de 21
        if len(txt)>2 and len(txt)<16 and txt.replace(" ", "").isalpha():
            return True
        else:
            return False  

    ## reproducir sonido y mostrar imagen de "objection"
    def showplay_excl(nam):
        global quick_menu_bajo
        quick_menu_bajo = True
        renpy.play(audio.correcto,channel="sound")
        renpy.show(name=nam, at_list=[excl])
        renpy.pause(2.5,hard=True)
        renpy.hide(name=nam)
        quick_menu_bajo = False

    ## establecer que el tiempo se acabó
    def timeUpFalse():
        global timeup
        timeup = False
        global timeup2
        timeup2 = False

    ## Reproducir sonido al dar al siguiente texto en el dialogo
    ## ademas reproducira un bip cuando el texto se está mostrando, estilo ace attorney, este sonido estará en el canal txt definidio en options.rpy
    def sound_txt(txt, **kwargs):
        if txt == "show":
            renpy.music.play(audio.txtbip, channel="text", loop=True)
        elif txt == "slow_done" or txt == "end":
            renpy.music.stop(channel="text")
    def sound_ctc(ctc, **kwargs):
        if ctc == "end":
            renpy.play(audio.ctc,channel="text")

    def change_cursor(ctype=False):
        if renpy.variant("pc"):
            if ctype=="target":
                config.mouse={"default":[("gui/target.png",31,31)]}
            else:
                config.mouse={"default":[("gui/cursor.png",0,0)]}

    ## para mostrar un cuadro alrededor de un cursor target
    ## desactivado por ahora, causa un bucle infinito
    def focus_target_cursor(fcs=False):
        if renpy.variant("pc"):
            pass
        #     if fcs:
        #         config.mouse={"default":[("gui/target_focus.png",31,31)]}
        #     else:
        #         config.mouse={"default":[("gui/target.png",31,31)]}

    ## para crear etiquetas personalizadas como {amarillo}texto{/amarillo}
    def amarillo(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#FFBB3E")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]
    def azul(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"color={}".format("#48B5E3")),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]

    config.custom_text_tags["amarillo"] = amarillo
    config.custom_text_tags["azul"] = azul

    ## comprobar si el tiempo se ha acabado, si es así saltamos a un label
    def checkTimeAndJump(label):
        global timeup
        global timeup2
        if timeup or timeup2:
            renpy.jump(label)

    ## recibe un parametro entero, el cual retornara un texto tipo "2 PM"
    def convertHH(hora=0):
        ampm = "AM"
        ## Lo que siga despues de 12 es PM y a partir de 1 es AM
        tiempo_usuario = "Nada"
        tiempo_modificado = hora

        if hora>12 and hora<=24:
            ampm="PM"
            if hora == 24:
                ampm="AM"              
            hora = hora - 12
        else:
            if hora == 12:
                ampm="PM"
        #para agregar un cero a los numero del 1 al 9
        if hora>0 and hora<10:
            hora= "0"+str(hora)
            
        tiempo_usuario = str(hora)+" "+ampm

        return tiempo_usuario

    ## convertir segundos a horas y minutos
    def convertSeconds(scs):
        ##convertimos los segundos a entero
        scs = round(scs)

        ##ahora este valor pasará a ser un hh:mm:ss
        scs = str(datetime.timedelta(seconds=scs))
        ##se convierte ahora en un array
        scs = scs.split(":")

        return scs

    ## funcion para restarle tiempo al countdown
    def restTimer(secs=10):
        global minutes
        global seconds
        #creo que no resta exactamente 10 segundos...
        tiempoactual=((minutes*60)+seconds)-secs
        # renpy.hide_screen("temporizador")
        renpy.show_screen("temporizador",tiempoactual)
        mouse_x= renpy.get_mouse_pos()[0]
        mouse_y= renpy.get_mouse_pos()[1]
        renpy.show_screen('mouseText',mouse_x,mouse_y)

    # This function will run a countdown of the given length. It will
    # be white until 5 seconds are left, and then red until 0 seconds are
    # left, and then will blink 0.0 when time is up.
    def countdown(st, at, length=0.0):
        global timeup
        global timeup2
        global minutes
        global seconds
        time_remaining = length - st
        minutes = (int) (length - st) / 60
        seconds = (int) (length - st) % 60
        if time_remaining > 2.0:
            timeup=False
            return Text("%02d:" % minutes + "%02d" % seconds, color="#fff", size=47), .1
        elif time_remaining > 0.0:
            timeup=False
            return Text("%02d:" % minutes + "%02d" % seconds, color="#f00", size=47), .1
        else:
            timeup=True
            ##un timeup adicional para los debates...
            timeup2=True
            return anim.Blink(Text("00:00", color="#f00", size=47)), None