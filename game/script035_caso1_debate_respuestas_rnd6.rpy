label d1r6_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r6_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r6_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice alegre
    ali "[pla_name], me alegra ver que estás muy metido en el debate..."
    show alice enojada
    $restCorazones()
    ali "Pero ese argumento no ayuda en nada." with hpunch
    jump inicio_d1r6

label d1r6_incorrecto_neil:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show neil serio hablando
    nei "[pla_name], ¿qué quieres demostrar con ese argumento?"
    show neil serio
    $restCorazones()
    nei "Piensa antes de hablar." with hpunch
    jump inicio_d1r6

label d1r6_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("esoescierto")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    pla "¡Alice, eso es!"
    show alice sorprendida
    ali "¿¡Ehhh!? ¿Qué?"
    pla "¡Todo este tiempo... hemos estado equivocados!"
    show alice normal
    ali "[pla_name]... ¿qué pasa? No entiendo..."
    show alice sorprendida
    pla "La carta no pudo haber sido escrita para Marissa, {amarillo}sino para alguien más.{/amarillo}"
    show alice:
        ease .5 mleft
    show marissa sorprendida at mright with dissolve
    mar "¿¡Eeehhh!?" with hpunch
    mar "¿No era para mí la carta?"
    # mar "Pero si ahí está mi nombre..."
    # pla "No, estás en un error..."
    pla "La forma en la que el autor describe a su gran amor {amarillo}no concuerda con tu forma de ser.{/amarillo}"
    show marissa normal
    show alice normal
    mar "..."
    mar "Ahora que lo dices.. Eso tendría sentido..."
    show alice sorprendida at brinquitos
    ali "¡Ah!"
    "Parece que Alice ya terminó de comprenderlo."
    "Gracias a lo que Alice dijo... entendí que la verdadera destinataria es..."

    # show screen corazones

    # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
    # $idevidencia_correcta="Prof. Harrow (perfil)"

    # label mostrar_evidencia2:

    #     show marissa normal

    #     if cantidad_corazones==0:
    #         jump evidencia_mostrada2_gameover

    #     call screen notepad("evidenc",jumpto="evidencia_mostrada2") with dissolve

    # label evidencia_mostrada2:
    #     if idevidencia_mostrar==idevidencia_correcta:
    #         jump evidencia_mostrada2_correcto
    #     else:
    #         mar "No entiendo... ¿eso qué demuestra?"
    #         $restCorazones()
    #         pla "Ah, lo siento... me he equivocado." with hpunch
    #         jump mostrar_evidencia2

    # label evidencia_mostrada2_gameover:
    #     hide screen corazones
    #     stop music fadeout 1
    #     show marissa preocupada
    #     mar "¿Qué estás intentando hacer, [pla_name]?"
    #     pla "La verdad, es que ni yo lo sé..."
    #     stop music
    #     scene bg negro with dissolve
    #     "Game over"
    #     return

    # label evidencia_mostrada2_correcto:
    #     stop music fadeout 2
    #     hide screen corazones
    #     $showplay_excl("esoes")
    #     $addCorazones()
    #     $updateStat("intel","+",1)
    #     $renpy.notify("Inteligencia +1")

    # #presentar evidencia: mary
    # # pla "Mary Harrow... es la profesora Harrow a quien iba dirigida la carta."
    stop music fadeout 2
    play sound campana
    pla "La profesora de matemáticas." with flashbulb
    mar "¿La profesora Harrow?"
    show marissa sorprendida
    play sound campana
    mar "¡Ah!" with flashbulb
    mar "La profesora se llama {amarillo}Mary{/amarillo} Harrow... Así que el nombre manchado, {amarillo}no era el mío.{/amarillo}"
    show alice:
        ease .5 left
    show marissa:
        ease .5 right
    show neil sonriendo hablando with dissolve
    nei "Jee... ¡Muy bien hecho, [pla_name]... ahora estaría claro cómo fue que llegó la carta a la persona equivocada..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    pla "Sí... la carta llegó hasta Marissa..."

    label lacartallegoel:
        if cantidad_corazones==0:
            hide screen corazones
            jump d1_gameover
        show screen corazones
        menu:
            "\"... durante las clases.\"":
                $restCorazones()
                "Nope... no era eso..." with hpunch
                jump lacartallegoel
            "\"... durante el tropiezo.\"":
                # $addCorazones()
                # pause 1
                hide screen corazones
                pass
            "\"... antes del tropiezo.\"":
                $restCorazones()
                "Nope... no era eso..." with hpunch
                jump lacartallegoel
            "\"... el sábado.\"":
                $restCorazones()
                "Nope... no era eso..." with hpunch
                jump lacartallegoel

    pla "Cuando Marissa y la profesora Harrow tropezaron, también se confundieron un papel en especial, la carta."
    hide alice with dissolve
    show beck enojado at left with dissolve
    bec "Eso es muy sospechoso... ¡Neil, tú tuviste algo que ver con eso!" with hpunch
    show neil normal
    nei "Je, je, je... No, para nada fue eso..."
    nei "Simplemente recordé el momento cuando fui a ayudarlas a recoger los papeles..."
    nei "Se me ocurrió que había una alta probalidad de que algún papel se pudo haber confundido de dueña."
    nei "Sabiendo ahora a quién iba dirigida la carta, será más fácil encontrar a un nuevo sospechoso, ¿verdad, [pla_name]?"

    menu:
        "\"Al contrario.\"":
            nei "¿Eh?"
            nei "Bueno, si tú lo dices..."
            jump d1_gameover
        "\"Así es.\"":
            $updateStat("carisma","+",1)
            $renpy.notify("Carisma +1")
        "\"Posiblemente.\"":
            $updateStat("carisma","-",1)
            $renpy.notify("Carisma -1")
            nei "¿Qué pasa con esa poca confianza?"
        "\"Eso no ayuda.\"":
            nei "¿En serio?"
            nei "Supongo que tu cerebro no da para más..."
            jump d1_gameover

    show beck:
        ease .5 center
    show neil:
        ease .5 mleft
    show alice normal at left with dissolve

    ali "Eso explicaría por qué parecía tan confuso el caso... pero entonces..."
    ali "¿Quién sería nuestro nuevo sospechoso?"

    # scene bg salon club detectives
    hide alice
    hide beck
    hide marissa
    hide neil

    ## cada elemento es el sprite de un personaje
    $ chars=["images/chars/alice/normal.png","images/chars/neil/normal.png","images/chars/beck/serio.png","gui/empty.png","images/chars/marissa/normal.png"]
    ## cada elemento define a qué etiqueta saltar cuando se selecciona el personaje de la lista anterior
    $ chars_labels=["nuevosospechoso_incorrecto","nuevosospechoso_incorrecto","elec_beck2",False,"nuevosospechoso_incorrecto"]

    label quien_es_nuevosospechoso:
        if cantidad_corazones==0:
            jump d1_gameover
        show screen btnHelpTextBox("Si la destinataria es la profesora, entonces quien escribió la carta es...")
        $ quick_menu_bajo=True
        ## llamamos pantalla de seleccion
        call screen char_select(chars,chars_labels) with dissolve

    label nuevosospechoso_incorrecto:
        hide screen char_select
        pause 1.8
        $ hide_select_chars()
        hide screen btnHelpTextBox
        $ quick_menu_bajo=False
        show screen corazones
        $restCorazones()
        "No es hora de juegos, ya tengo claro quien pudo escribir la carta..." with hpunch
        hide screen corazones
        jump quien_es_nuevosospechoso

    label elec_beck2:
        # show screen corazones
        # $addCorazones()
        pause .4
        hide screen char_select
        pause 1.4
        $ hide_select_chars()
        hide screen btnHelpTextBox
        $ quick_menu_bajo=False
        hide screen corazones
        play music tiempo_muerto fadein 3
        show marissa normal with dissolve
        pla "Creo que Beck es el autor de la carta..."
        show marissa sorprendida
        mar "¿¡Be- Beck!?" with hpunch
        pla "Él está enamorado de la profesora Harrow."
        mar "¿¡Aaahh!? ¿Beck está enamorado de ella?"
        mar "N- no lo puedo creer..."
        show marissa normal:
            ease .5 mright
        show beck enojado at mleft with dissolve
        bec "Sí, yo tampoco puedo creerlo." with hpunch
        bec "¿Que yo estoy enamorado de una profesora?"
        bec "¡Eso no es posible!"
        "¿Eh? Pero qué le pasa a Beck... ahora piensa negarlo..."
        show beck:
            ease .5 left
        show marissa:
            ease .5 right
        show alice normal with dissolve
        ali "Pero tú hablaste con [pla_name] y él dedujo que..."
        show beck serio
        bec "¿Que lo dedujo? Seguramente solo fue una suposición."
        bec "La profesora es alguien respetable. Y es una gran mujer..."
        show beck pensando
        bec "Pero no estoy interesado en ella."
        show marissa preocupada sudor
        mar "[pla_name], ¿estás seguro de que a Beck le gusta a la profesora Harrow?"
        # "Yo sí estoy seguro... pero no contaba con que Beck lo negara rotundamente."
        $renpy.choice_for_skipping()
        $renpy.save("checkpoint")
        "Debe haber{nw}"
        play sound campana
        extend " {amarillo}algo que demuestre el interés de Beck con la profesora Harrow...{/amarillo}" with flashbulb
        show marissa normal

        # $quick_menu_gameplay=True

        # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
        $idevidencia_correcta="Ayuda en matemáticas"

        label mostrar_evidencia2:
            show screen corazones

            if cantidad_corazones==0:
                jump evidencia_mostrada2_gameover

            call screen notepad("evidenc",jumpto="evidencia_mostrada2") with dissolve

        label evidencia_mostrada2:
            if idevidencia_mostrar==idevidencia_correcta:
                jump evidencia_mostrada2_correcto
            else:
                mar "No entiendo... ¿eso qué demuestra?"
                $restCorazones()
                pla "Ah, lo siento... me he equivocado." with hpunch
                jump mostrar_evidencia2

        label evidencia_mostrada2_gameover:
            hide screen corazones
            stop music fadeout 1
            show marissa preocupada
            mar "¿Qué estás intentando hacer, [pla_name]?"
            pla "La verdad, es que ni yo lo sé..."
            jump d1_gameover

        label evidencia_mostrada2_correcto:
            $showplay_excl("esoes")
            $addCorazones()
            pause 1
            hide screen corazones
            pass

        # $quick_menu_gameplay=False

        pla "No Beck... hay una prueba que demuestra que sí estás interesado en la profesora."
        bec "¿Ah, sí? Lo dudo mucho..."
        # bec "A ver, muestráme esa prueba."
        # pla "No es una prueba física... más bien..."
        stop music fadeout 1
        play sound campana
        pla "Entonces, ¿explícanos {amarillo}por qué pasas mucho tiempo en el salón de maestros{/amarillo}?" with flashbulb
        show beck sorprendido
        bec "¿Eh?"
        pla "Vamos, me refiero a que tú recibes tutoría con la profesora Harrow. Y no solo una vez..."
        show beck pensando
        bec "¿Y eso qué tiene de malo? Solo estoy preocupado por mis notas..."
        pla "También podría ser una excusa para pasar más tiempo con ella..."
        pla "Además, ese sería un momento oportuno para dejarle una carta a la profesora entre sus papeles sin que se diera cuenta."
        show marissa sorprendida
        mar "Beck..."
        show beck sorprendido
        bec "No... están en un error..."
        "Parece que Beck sigue sin querer rendirse..."
        show marissa normal
        show beck serio
        bec "Marissa, no es lo que piensas..."
        show beck pensando
        bec "Yo de ninguna manera escribí esa carta..."
        mar "Pero Beck..."
        mar "Ahora que lo pienso... Tú eres zurdo. Como la persona que escribió la carta."
        bec "¿Y eso qué? No demuestra nada..."
        mar "Además, vi al acosador el sábado y..."
        show beck serio
        bec "¡Ni siquiera estuve en la escuela ese día!" with hpunch
        "¿Beck no estuvo en la escuela el sábado?"
        "Hay algo que demuestra lo contrario..."
        show alice enojada
        $showplay_excl("esonoescierto")
        play music debate fadein 4
        "¿Eh?"
        show marissa sorprendida
        ali "E- eso... no es cierto..."
        ali "Los fines de semana siempre hay partidos de fútbol."
        show beck pensando
        show marissa normal
        bec "Ah... bueno, eso..."
        show beck preocupado
        bec "Solo fue una casualidad."
        pla "No hay por qué seguir negándolo, Beck..."
        show beck enojado
        bec "Lo niego porque no es cierto."
        pla "¿Y qué me dices de {amarillo}tu encuentro con Marissa en la cafetería el viernes?{/amarillo}"
        bec "¿Qué con eso?"
        show beck pensando
        bec "Solo fue una casualidad."
        show marissa preocupada sudor
        mar "Pero ese café no es un lugar al que frecuentes ir."
        $renpy.choice_for_skipping()
        $renpy.save("checkpoint")
        bec "Ya te lo dije..."
        play sound campana
        bec "{amarillo}Me llamaron al celular algunos amigos,{/amarillo} para ir al café a conversar un rato." with flashbulb
        bec "{amarillo}Estuvimos hablando sobre el partido del sábado.{/amarillo}"
        "No, eso no es cierto..."
        pla "¿Estás seguro de eso?"
        show marissa preocupada
        show alice normal
        show beck serio
        bec "Sí."
        pla "Qué raro, porque..."
        "¡Hay algo que demuestra su contradicción!"

        # $quick_menu_gameplay=True

        # ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
        $idevidencia_correcta="Problemas en red de telefonía"

        label mostrar_evidencia3:
            show screen corazones

            if cantidad_corazones==0:
                jump evidencia_mostrada2_gameover

            call screen notepad("evidenc",jumpto="evidencia_mostrada3") with dissolve


        label evidencia_mostrada3:
            if idevidencia_mostrar==idevidencia_correcta:
                jump evidencia_mostrada3_correcto
            else:
                mar "No entiendo... ¿qué quieres dar a entender con eso?"
                $restCorazones()
                pla "Ah, lo siento... me he equivocado." with hpunch
                jump mostrar_evidencia3

        label evidencia_mostrada3_correcto:
            stop music fadeout 1
            $showplay_excl("esoes")
            $addCorazones()
            pause 1
            hide screen corazones
            pass

        # $quick_menu_gameplay=False
        play music tiempo_muerto fadein 1
        
        pla "Eso es muy extraño... El viernes, que fue cuando Marissa llegó al café, {amarillo}la red de telefonía estaba caída.{/amarillo}"
        play sound campana
        pla "Ese viernes, no se podía llamar, ni enviar mensajes desde el celular."
        show marissa sorprendida
        mar "Ah, cierto..."
        show beck enojado
        bec "No... no... Eso no es suficiente para acusarme..." with hpunch
        "¡Aaaah qué terco es!" with vpunch
        show marissa normal
        "¿Ahora qué mentira va a decir?"
        stop music fadeout 1
        play sound campana
        bec "{amarillo}Si yo fuera el acosador, Marissa me hubiera identificado desde un principio.{/amarillo}" with flashbulb
        pla "¿Qué?"
        show alice sorprendida
        show marissa sorprendida

        mar "E- es... es cierto..."
        mar "No pude identificar al acosador..."
        mar "A Beck lo hubiera reconocido rápidamente..."
        show beck serio
        bec "¿Lo ves ahora?"
        bec "Todo ha sido una serie de casualidades."
        show beck guino
        bec "No soy el acosador. Y tampoco escribí esa carta de amor."

        menu:
            "Tiene razón":
                jump caso1_gameover
            "Hay algo más...":
                show alice enojada
                ali "¡[pla_name]! No podemos dejar pasar esta oportunidad." with hpunch
                ali "El caso está a punto de ser resuelto."
                show alice pensando
                pla "Pero... ¿cómo explicaríamos el hecho de que Marissa no pudo identificar al acosador?"
                $renpy.choice_for_skipping()
                $renpy.save("checkpoint")
                show alice enojada
                ali "¡Debe haber algo que usó el acosador para evitar ser identificado!" with hpunch
                show alice pensando
                ali "Pero no logro averiguar qué podría ser..."
                "Uhm..."
                "Algo que el acosador usó..."
                "Podría ser..."
                $hora=16
                $ruleta2_mas_facil=False

    label ruleta2_inicio:

        #-----Inicia minijuego

        $estadoj="Ruleta Incóg."
        $ruleta_porcentaje=100
        $ruleta_id=2

        #palabra a descubir
        $palabra_ruleta="CAPUCHA"

        #posicion de la letra a averiguar en palabra
        $posicionenpalabra=0

        python:
            #lo que se mostrara en el panel derecho
            lstLetrasActuales=[]
            #agregamos varios guiones bajos
            for x in xrange(0,len(palabra_ruleta)):
                lstLetrasActuales.append("_")

        if not ruleta2_mas_facil:
            $letras1=["G","P","S","Y","H","E","R","A","J","U","E","R","O"]
            $letras2=["I","T","Z","K","R","Ñ","U","M","W","C","P","H","B"]
        else:
            $letras1=["C","S","P","X","U","H"]
            $letras2=["A","S","P","C","A","H"]

        $showMinigameTitle("Ruleta de la incógnita")
        # $quick_menu_gameplay=True
        $quick_menu_bajo=True
        window hide
        play music deduccion fadein 3
        $change_cursor("target")
        scene bg salon club detectives
        $renpy.show_screen("temporizador",185)#185
        
        call screen ruleta_incognita(letras1,letras2,"Para no ser identificado, el acosador usó la...",palabra_ruleta) with dissolve

        label ruleta2_gameover:
            $quick_menu_bajo=False
            stop music fadeout 3
            $change_cursor()
            if not ruleta2_mas_facil:
                pla "No... no sé..."
                show alice enojada
                ali "¡[pla_name]!" with hpunch
                ali "¡No puedes rendirte! Estamos cerca de resolver el caso."
                show alice sorprendida
                pla "¿Es que no lo has escuchado? ¿Por qué Marissa no pudo identificar al acosador?"
                pla "No encuentro explicación a eso..."
                show alice enojada
                ali "[pla_name], no estás solo..."
                show alice pensando
                ali "Yo no quiero ser ninguna carga."
                pla "Alice..."
                ali "Solo hay que pensar con calmas las cosas."
                show alice enojada
                ali "Una buena deducción {amarillo}parte de las preguntas correctas.{/amarillo}"
                pla "¿Y qué debo preguntarme entonces?"
                show alice normal
                ali "Bueno... ¿el problema es que Marissa no identificó a Beck, no?"
                play sound campana
                ali "Entonces, hay que preguntarse, {amarillo}¿qué usarías para evitar que algún conocido te identifique?{/amarillo}" with flashbulb
                pla "Ehm... ¿Un disfraz?"
                show alice:
                    ease .5 mright
                show beck enojado at mleft with dissolve
                bec "No irás a pensar que he usado un disfraz, ¿verdad?"
                bec "Eso es ridículo."
                show beck sorprendido
                play sound campana
                ali "Tal vez {amarillo}algo que haga lo mismo que un disfraz.{/amarillo}" with flashbulb
                "Uhm... un disfraz... algo parecido... disfraz... ropa... algo para cubrir..."
                show alice sorprendida
                show sherinford pequeño with dissolve:
                    ypos .300
                    xoffset 10
                    xpos 0.650
                she "¡Pío, pío, pío!" with hpunch
                ali "¿Sherinford?"
                hide sherinford with dissolve
                she "¡Pío, pío, pío!" with hpunch
                bec "¿De donde ha salido ese pollo?"
                "Sherinford apareció de repente, sacudió sus alas enérgicamente y luego comenzó a escalar por mi cuerpo, hasta posarse en mi cabeza."
                ali "Sherinford... ¿También quieres ayudar?"
                she "¡Pío!" with hpunch
                show alice alegre
                ali "¡Muy bien! ¡Sherinford también estará apoyándote, [pla_name]!"
                ali "Seguramente él te pasará un poco de su inteligencia."
                "¿Que tendré más inteligencia por tener a este pollo encima de mi cabeza?"
                "No creo que eso funcione..."
                "Bien, una vez más..."
                $ruleta2_mas_facil=True
                $quick_menu_bajo=True
                jump ruleta2_inicio
            else:
                jump ruleta1_gameover

    label ruleta2_fin:
        $showplay_excl("esoes")
        stop music fadeout 3
        $estadoj="Debate"
        $quick_menu_gameplay=False
        $quick_menu_bajo=False
        window show
        show alice sorprendida with dissolve
        play sound campana
        pla "¡El acosador usó una capucha!" with flashbulb

    pla "Beck usó {amarillo}la capucha del suéter{/amarillo} que trae puesto para ocultar su identidad."
    if ruleta2_mas_facil:
        pla "Gracias Sherinford, supongo que algo de tu inteligencia se me debió haber pegado."
        show sherinford grande behind alice at left with dissolve:
            xoffset -300
            on show:
                linear 1 xoffset 20
        she "Pío."
        hide sherinford with dissolve
    show alice normal:
        ease 1 right
    show marissa sorprendida at center with dissolve
    show beck pensando at left
    mar "Eh..."
    "Marissa se acercó atónita hacia Beck, y con la confianza que una amistad da, le puso la capucha encima de la cabeza..."
    mar "¡Es él! ¡Es la sombra que miré! ¡Su silueta es idéntica!" with hpunch
    "Beck se retiró la capucha, pero no dijo una sola palabra."
    mar "Por qué... por qué pasó todo esto..."
    pla "Creo poder explicarlo todo."
    show alice enojada
    ali "¡Así se habla, [pla_name]!"

    $fase_titulo.append("Debate + Acertijo + Ruleta de la incógnita")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(20)

    $quick_menu_gameplay=False
    show marissa preocupada
    show alice normal

    play music tiempo_muerto fadein 3

    pla "El viernes, Beck estaba en el salón de maestros con la profesora Harrow."
    pla "Ya que él está enamorado de ella, le escribió una carta, algo cursi..."
    pla "Pero él estaba consciente que no era alguien a quien podría impresionarla."
    pla "Un alumno, declarándose a una profesora... Obviamente eso acarreaba mucha inseguridad y presión..."
    pla "Por eso es que Beck seguramente dejó la carta entre los papeles de la profesora cuando estaban en el salón de maestros."
    pla "Ese mismo día, la profesora Harrow se tropezó con Marissa."
    pla "En medio de la confusión, la carta que era de la profesora, llegó a parar a Marissa sin que ella se diera cuenta..."
    # pla "Sino hasta a final de las clases."
    pla "Beck presenció parte de la escena, pero no estaba consciente todavía de lo que realmente pasó."
    pla "Entonces cuando Beck y Marissa se encontraron en el café, es cuando beck lo entendió, la carta llegó a la persona equivocada."
    $quick_menu_gameplay=True
    pla "El sábado, que es cuando Beck y Marissa estaban en la escuela..."
    
    label beckfinal:
        pla "Beck quiso forzar el casillero de Marissa..."
        mar "¿Por qué Beck haría algo así?"
        pla "Bueno..."
        menu:
            "Quería dejarle una carta":
                mar "¿Eh? ¿Por qué Beck quería dejarme una carta?"
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                pla "Ehm... perdón, me he equivocado..." with hpunch
                jump beckfinal
            "Quería recuperar la carta":
                pass
            "Quería el celular de Marissa":
                mar "¿Mi celular? ¿Para qué Beck querría mi celular?"
                pla "Está claro que..."
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                extend " me he equivocado." with hpunch
                jump beckfinal
            "No sé":
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                play sound golpe
                ali "¡[pla_name]!" with hpunch
                pla "Perdón... ahora lo tengo claro..."
                jump beckfinal
    $quick_menu_gameplay=False
    pla "Creo que Beck pensó que habías guardado la carta en tu casillero."
    pla "Beck quería recuperar la carta, sin que te dieras cuenta, seguramente él se sentía demasiado avergonzado como para confesar la verdad."
    pla "Eso también explicaría que te sintieras acosada."
    pla "Y cuando lo viste, no lo pudiste identificar porque él llevaba su suéter con la capucha puesta."
    pla "Al final, llegaste a nuestro club pensando que esa carta era para ti, pero simplemente era el nombre de la profesora Harrow manchado con tinta."
    show beck preocupado
    stop music fadeout 2
    play sound campana
    bec "Tienes razón... es tal como lo has dicho... ya no puedo seguir negándolo." with flashbulb
    bec "Perdón Marissa, por haberte hecho pasar un mal momento..."
    mar "Beck..."
    mar "Si tan solo me lo hubieras dicho..."
    show beck pensando
    bec "Lo siento, en serio... estaba tan nervioso y avergonzado... No pensé con claridad."
    "Marissa respiró hondo, dejando ir un peso que llevaba encima..."
    "Entonces, sacó la carta de su bolso y se lo entregó a Beck."
    show marissa alegre
    mar "Toma, tendrás que trabajar en tu falta de confianza si quieres intentarlo de nuevo..."
    show beck sonrojado
    bec "... sí..."
    $estadoj="Libre"
    play music ambiente fadein 4
    #marisa se dirige a neil
    mar "Este... ¿Neil?"
    hide beck with dissolve
    show neil sorprendido at left with dissolve
    nei "¿¡S- sí!?" with hpunch
    mar "¿En serio te gusto?"
    show neil sonriendo hablando
    nei "¡Sí! ¡Me enamoré de ti a primera vista!" with hpunch
    "Wow... qué directo."
    show marissa sonrojada
    mar "Entiendo."
    mar "Pero, lo siento, no estoy interesada en tener un novio."
    show neil sorprendido
    nei "¿¡Eeeeh!?" with hpunch
    # nei "Ya veo..."
    show marissa alegre hablando at brinquitos
    play sound campana
    mar "Pero podríamos ser amigos, y también podemos conocernos mejor..." with flashbulb
    nei "¿E- en... serio?"
    "Eso significa esperanza."
    show neil sonriendo hablando
    nei "Je, je, je..."
    "Y ahí va, Neil empezó a sonreír como idiota de nuevo."
    hide neil with dissolve
    show marissa:
        ease .5 mleft
    show alice:
        ease .5 mright
    mar "[pla_name], Alice..."
    show marissa at brinquitos
    mar "¡Gracias por ayudarme!"
    show marissa sonrojada
    mar "Aunque al final solo fue un error mío..."
    show alice sorprendida
    ali "¡No- no te preocupes!" with hpunch
    ali "Es lo que el club hace, ¡este club está para ayudar a las personas!"
    show marissa alegre
    mar "Je, je, je. Es un gran club."
    show marissa alegre hablando
    mar "Ya verán, les contaré a mis amigos que ustedes son geniales."
    mar "Si alguien tiene un problema, ¡les diré que vengan a este club!"
    ali "¿En serio?"
    show alice alegre at brinquitos
    ali "¡Eso sería genial!"
    hide marissa with dissolve
    show alice normal
    show beck preocupado at mleft with dissolve
    bec "Oye, [pla_name], quiero disculparme por haberme comportado como un tonto."
    show beck pensando
    bec "Me siento mal por pedirlo, pero..."
    show beck preocupado
    bec "¿Podrían mantener esto en secreto?"
    pla "Claro, no le diremos a nadie de esto..."
    ali "Yo- yo tampoco diré nada."
    show beck sonrojado
    bec "En serio, gracias..."
    hide alice with dissolve
    show neil pensativo at mright with dissolve
    show beck pensando
    bec "A ti también te debo una disculpa..."
    bec "Perdón por querer echarte la culpa de todo."
    nei "Descuida."
    bec "Espero que no le digas a nadie lo que ha pasado..."
    nei "Pues yo no soy miembro de este club, así que no tengo ninguna obligación de guardar tu secreto..."
    show beck:
        ease .5 left
    show neil:
        ease .5 right
    show marissa normal with dissolve
    mar "Neil..."
    show neil sorprendido
    nei "¡Aaahh! ¡Era una broma!" with hpunch
    nei "No le diré a nadie, confía en mí."
    show marissa alegre
    mar "Es bueno saberlo."
    hide neil with dissolve
    hide beck with dissolve
    show marissa alegre hablando
    mar "Bueno, es hora de irme."
    mar "Y no crean que es una despedida."
    mar "¿Todavía podemos ser amigos?"
    show marissa:
        ease .5 mleft
    show alice pensando at mright with dissolve
    ali "¿Eh? Un amigo..."
    show alice sonrojada
    "Alice sonrió levemente, mientras su cara se ruborizaba."
    pla "Claro, seremos amigos después de todo."
    show marissa alegre at brinquitos
    mar "¡Genial, nos vemos, Alice, [pla_name]!"
    hide marissa with dissolve
    show beck pensando at mleft with dissolve
    show alice normal
    bec "Yo también me voy."
    show beck guino
    bec "Ah, yo también les hablaré a mis amigos del club. Siempre y cuando ustedes mantengan su palabra."
    pla "Claro, nuestros labios estarán sellados."
    bec "Eso espero, adiós."
    hide beck with dissolve
    show neil pensativo at mleft with dissolve
    nei "Ah... bien hecho."
    show neil sonriendo hablando
    nei "Han demostrado que de verdad pertenecen a un club de detectives."
    nei "Bien, yo también me voy."
    hide neil with dissolve
    show alice normal:
        ease .5 center
    "Y sin decir nada más, Neil se retiró."
    "Nos quedamos Alice y yo en silencio."
    "Yo por mi parte me tumbé a un banquillo, cansado de todo el trabajo hecho."
    pla "Ah... me duele la cabeza."
    ali "Has pensado mucho... es normal..."
    pla "Pues espero no pensar más en lo que resta de la semana."
    $quick_menu_btn_notepad=False
    "Después dejé mi libreta en la mesa."
    pla "Bien, es todo por hoy, me iré a casa."
    show alice alegre
    ali "Sí, buen trabajo, [pla_name]."
    hide alice with dissolve
    "Fui en busca de mi mochila, y cuando ya me estaba dirigiendo a la puerta..."
    stop music fadeout 3
    show katherine normal with dissolve
    "..."
    extend " ¿eh?"
    "No... lo que faltaba... otro caso..."
    unk "¿Tú eres miembro de este club?"
    pla "Eh, sí... soy [pla_name]."
    unk "Ya veo."
    show katherine:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿Eh?" with hpunch
    show alice pensando at temblor
    extend " ... uh..."
    pla "¿Alice, qué te pasa?"
    "De repente, ella se puso a temblar, claramente nerviosa."
    pla "Disculpa, ¿quién eres?"
    unk "Vaya, qué decepcionante, ni siquiera sabes quién soy..."
    unk "Como se esperaba de este club tan inútil."
    pla "¿Eh?" with hpunch
    "Pero... ¿qué ha dicho?"
    hide alice
    show alice pensando at mright
    ali "[pla_name],{nw}"
    play sound campana
    extend " ella es la presidenta del co- comité estudiantil..." with flashbulb
    play music investigacion fadein 4
    pla "¿¡La- la pre- presidenta del co- comité estudiantil!?" with hpunch
    unk "¿Acaso es costumbre tartamudear en este club?"
    kat "Soy, {amarillo}Katherine Hyde.{/amarillo}"
    show katherine enojada
    kat "Grábate ese nombre en eso que llamas cerebro."
    "Pero qué rayos le pasa..."
    pla "¿Y a qué vino la presidenta del comité estudiantil a este club?"
    "Dije eso mostrandome serio, no podía ser amable con ella."
    kat "¿Acaso no es obvio?{nw}"
    play sound campana
    show alice sorprendida
    extend " {amarillo}Voy a cerrar este club.{/amarillo}" with flashbulb
    pla "¿¡Eh!?" with hpunch
    pla "Pero si todavía falta mucho tiempo..."
    show katherine normal
    kat "¿Para qué dejar para mañana lo que puedes hacer hoy?"
    kat "El anterior presidente era muy suave con los clubes, pero eso se ha acabado."
    "¿¡Acaso este es el nacimiento de una dictadura!?" with hpunch
    # kat "Desde mi primer año en este cargo, pondré mano dura a aquellos que no se atienen al reglamento."
    show alice pensando:
        ease .5 right
    show katherine:
        ease .5 center
    show henry sonriendo at left with dissolve
    play sound campana
    "¿Y ahora qué?" with flashbulb
    "Otra persona se apareció en el club."
    pla "Eh, usted es el de la otra vez..."
    unk "Hey, ¿qué tal chico?"
    play sound campana
    kat "{amarillo}Director Okamoto{/amarillo}..." with flashbulb
    pla "¿¡Di- Director!?"
    kat "¿Qué? ¿Acaso no sabías que él es el director?"
    pla "Ehm... no..."
    "Me da verguenza, admitirlo. Vaya, me he perdido de tanto en el primer día de clases..."
    "Primero, conozco a la nueva presidenta del comité estudiantil."
    "Y ahora me voy enterando que este hombre es el nuevo director de la escuela..."
    show henry tranquilo
    hen "Henry Okamoto, mucho gusto, chico, ya me suponía que no sabías quién era yo."
    "Henry... ¿Okamoto?"
    show henry alegre
    hen "Ah, y si te lo estás preguntando, mi padre es japonés, pero yo crecí y nací en este país."
    "¿Eh? Parece que me ha leído la mente..."
    show henry tranquilo
    hen "Y señorita Hyde... me preguntaba a dónde iba con tanta prisa..."
    hen "Y parece que he acertado."
    kat "Supongo que debe de estar enterado que este no es ningún club reconocido por la escuela."
    hen "Sí, no tiene los miembros suficientes."
    kat "Entonces no hay nada más que hablar, hay que desocupar este salón para otros clubes que sí lo necesitan."
    pla "¡E- espera!" with hpunch
    show katherine enojada
    kat "¿Alguna objeción?"
    pla "Eh... bueno..."
    "Mientras balbuceaba, noté que Alice seguía sin hablar..."
    show henry sonriendo
    hen "Ya, ya, tampoco hay que ser rudos."
    show henry tranquilo
    hen "Ellos todavía tienen dos meses para conseguir los miembros suficientes."
    hen "No veo razón para apresurar las cosas."
    kat "Pero director... ellos no hacen más que perder el tiempo..."
    hen "¿Cómo puedes estar segura de eso?"
    kat "Bueno... yo..."
    show henry sonriendo
    play sound campana
    hen "¿Los has estado vigilando?" with flashbulb
    pla "¿Qué?"
    show katherine enojada
    kat "Yo- yo- solo estaba haciendo mi trabajo."
    hen "¿Acaso ellos han faltado al reglamento en algún momento?"
    kat "..."
    kat "No."
    show henry tranquilo
    hen "Ahí lo tienes, ¿ahora quién ha estado perdiendo el tiempo?"
    "Uh, eso debió doler."
    kat "..."
    kat "Como sea."
    kat "En cuanto vea que algunos de ustedes hace algo indebido..."
    kat "¡Cerraré este club inmediatamente!" with hpunch
    hide katherine with dissolve
    show henry:
        ease .5 mleft
    show alice:
        ease .5 mright
    pla "Pero qué rayos le pasa a esa chica..."
    show henry serio
    play sound campana
    hen "Creo que tiene algo contra el club." with flashbulb
    pla "¿Eh?"
    show henry alegre
    hen "Oh, no me hagas caso, solo estaba hablando conmigo mismo je, je, je."
    show henry tranquilo
    hen "Bien, tengo que irme."
    hen "Espero que logren mantener este club a flote."
    hide henry with dissolve
    show alice:
        ease .5 center
    "Y con una leve reverencia, el director se retiró del salón..."
    "Han pasado tantas cosas en tan poco tiempo..."
    "Ah... creo que este dolor de cabeza está empeorando..."
    pla "¿Alice?"
    ali "Pe- perdón... me quedé paralizada..."
    show alice at decaer
    ali "En cuanto pienso que el club podría cerrar..."
    ali "Me pongo muy nerviosa..."
    show alice at reponerse
    pause .7
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 60
    she "Pío..."
    pla "Bah, no le pongas mente a esa engreída presidenta."
    pla "Hagamos nuestro mejor esfuerzo, y ya verás que tendremos los miembros suficientes para el club."
    show alice sonrojada
    ali "[pla_name]..."
    show alice sonriendo
    ali "Gracias por seguir en el club."
    scene bg negro with slow_dissolve
    "Aunque logramos resolver nuestro primer caso juntos..."
    "Alice y yo seguíamos siendo los únicos miembros del club de detectives."
    "Y tenemos dos meses para cambiar la situación."
    "Lo he pasado bien en este club, y ahora me he comprometido a ayudar."
    "¡No voy a dejar que este club cierre!"

    $noInteract()

    stop music fadeout 3
    hide screen quick_menu
    $quick_menu=False
    window hide
    $ renpy.pause(3,hard=True)

    # show text "{size=70}Fin del primer caso.{/size}" at truecenter
    # with dissolve
    # pause 3
    # hide text
    # with dissolve

    $renpy.choice_for_skipping()
    play sound caso_resuelto
    show text "{size=70}¡Primer caso resuelto!{/size}":
        center
        ypos .9
    show alice chibi:
        center
        ypos .7
        zoom .6
    # with dissolve
    $ renpy.pause(4,hard=True)
    hide text
    with dissolve
    hide alice with dissolve

    if _return:
        $persistent.hikikomoriholmes_unlocked=True
    $persistent.extras_unlocked = True

    call screen casoFinDetalles()
    if persistent.skipcredits:
        show screen btnSkipCredits()
    
    #inicio creditos
    $renpy.music.play(audio.creditos, channel='music', loop=False, fadeout=2.0, synchro_start=False, fadein=1.5, tight=None, if_changed=False)

    $ renpy.pause(3,hard=True)

    show text "{size=30}Concepto y guion{/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30}Arte de personajes (sprites){/size}{p}{size=70}Tokudaya{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30}Ilustraciones adicionales{/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30}Escenarios{/size}{p}{size=50}loo.sakura.ne.jp{p}Pixabay.com{p}LindaHicks{p}Wokandapix{p}Ajalfalro{p}Uncle Mugen{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(4,hard=True)
    hide text

    show text "{size=30}Música de fondo{/size}{p}{size=50}Amacha{p}Kevin Macleod{p}Eric Matyas{p}Vibe Mountain{p}Asher Fulero{p}Dead Seed{p}Silent Partner{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(4,hard=True)
    hide text

    show text "{size=30}Efectos de sonido{/size}{p}{size=60}Freesound.org{p}Taira Komori{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(3,hard=True)
    hide text

    show text "{size=30}Progamación y diseño{/size}{p}{size=70}Danny Garay{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    show text "{size=30}Jugadores beta (sin ningún orden en particular){/size}{p}{size=40}Pablo Canché, Alexis Sánchez, Marcos Lopez, Davar Osorio, Danny Huerta, Iván Medina, Bill García, Williams Chia, Deivid Navarro, Juan Cruz, Matías Barraza, Jeremy Garrido, Sebas BZ, José Veintimilla, Daniel Castro, Juan Vicente, Michel Hernández, Juan Manuel, Ramiro Segovia.{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(6,hard=True)
    hide text

    show text "{size=30}Motor de juego{/size}{p}{size=70}Ren'Py{/size}" at truecenter with dissolve:
        xalign .5
    $ renpy.pause(2,hard=True)
    hide text

    $ renpy.pause(1,hard=True)

    label fin_creditos:
        if persistent.skipcredits:
            hide screen btnSkipCredits with dissolve
        show logo at truecenter with dissolve
        $ renpy.pause(1,hard=True)
        show text "{size=70}¡Gracias por jugar!{/size}" with dissolve:
            xalign .5
            ypos .8
        $ renpy.pause(5,hard=True)
        hide logo with dissolve
        hide text with dissolve
        stop music fadeout 3
        $ renpy.pause(4,hard=True) 

        $noInteract(False)

    $persistent.skipcredits=True
    return



