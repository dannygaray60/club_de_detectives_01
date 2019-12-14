label caso1_testimonio3:

    $estadoj="Testimonio"
    $interrogatorio_activo=False
    $initInterrVars()
    #intro testimonio
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio3_inicio:

        if estadoj=="Interrogatorio":
            show screen interrogatorio_btns

            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[3]:

                if interr_3_arreglado:
                    jump caso1_interrogatorio3_final

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int3_gameover
        
        $renpy.block_rollback()
        show beck sonriendo with dissolve
        $interr_fraseid=0
        bec "{amarillo}El viernes llegué a la hora habitual{/amarillo} a la escuela, como a las ocho y media."
        show beck pensando
        $interr_fraseid=1
        bec "Recuerdo que {amarillo}la primera clase fue Física.{/amarillo}"
        show beck preocupado
        $interr_fraseid=2
        bec "Ah... {amarillo}en serio que es aburrida...{/amarillo}"
        $interr_fraseid=3
        bec "{amarillo}Después de eso tuvimos tiempo libre,{/amarillo} así que me fui a la cancha a jugar un rato."
        show beck sonriendo
        $interr_fraseid=4
        bec "Más tarde regresé al salón para {amarillo}la siguiente clase que era Historia.{/amarillo}"
        show beck sonriendo
        $interr_fraseid=5
        bec "Eso fue todo... {amarillo}supongo...{/amarillo}"
        hide beck with dissolve
        $renpy.block_rollback()
        hide screen interrogatorio_btns

        ##creamos un label, en donde dirigiremos al jugador en caso de que todavía no se ha activado el tuto para presentar contradicciones
        label interr_3_fin_frases:

            if estadoj=="Testimonio":
                stop music fadeout 2

                show alice normal with dissolve
                ali "Bu- buena suerte, [pla_name]..."
                pla "¿No piensas ayudarme?"
                show alice pensando at decaer
                ali "Lo- lo siento..."
                hide alice with dissolve

                ## desactivamos opciones irrelevantes del quick menu, y el menu normal
                $quick_menu_gameplay = True

                $estadoj="Interrogatorio"
                $interrogatorio_activo=True

                ##por alguna razón, al iniciar por primera vez el interrogatorio, el codigo actúa como si se hubiera acabado el tiempo, por el momento, mejor establecemos manualmente las variables a False.
                $timeup=False
                $timeup2=False

                ##con esta variable, establecemos si en un interrogatorio, este ha sido refutado correctamente o no, con esto, logramos obtener nueva informacion
                $interr_3_arreglado=False
                ##y con esta, mostramos un tutorial para indicar una contradiccion, y mostrarla solo una vez
                $tuto_interr_refutar=True

                ##item del notepad que es el correcto para refutar
                ##convertimos ese titulo en su posicion del array
                $interr_item_notepad_correcto=lstNotepad_titulo.index("Horario de Prof. Harrow")

                ## variables del interrogatorio
                $interr_id=3
                ##para establecer cual es la última frase y así desactivar el botón de siguiente
                $interr_frasefinal=5

                #en este interrogatorio, como no se necesita refutar, se desactiva el botón
                $interr_btn_refutar_disabled=True

                #variables bandera
                $fraseInterr={3:3}
                $fraseInterr[3]=False

                #establecemos cantidad de corazones a 5
                $initCorazones()

                #intro interrogatorio
                $showMinigameTitle(estadoj)

                #mostramos panel de corazones y temporizador en 700 segundos
                $show_gameplay_layout(700)
                
                #botones de interrogatorio
                show screen interrogatorio_btns

                play music tiempo_muerto2 fadein 3

                jump caso1_testimonio3_inicio

            else:
                $checkTimeAndJump("int"+str(interr_id)+"_gameover")
                if fraseInterr[3] and not interr_3_arreglado:
                    hide beck with dissolve
                    "Uhm..."
                    show alice normal with dissolve
                    ali "¿Qué pasa, [pla_name]?"
                    pla "No estoy seguro... pero creo hay algo que no encaja con lo que ha dicho Beck hasta ahora."
                    show alice sorprendida
                    ali "Oh, entonces {amarillo}hay una contradicción en lo que ha dicho Beck.{/amarillo}"
                    pla "Eso quiere decir que {amarillo}Beck ha mentido...{/amarillo}"
                    show alice normal
                    ali "Una contradicción {amarillo}no necesariamente significa que alguien ha mentido a propósito.{/amarillo}"
                    ali "Tal vez ha olvidado algo o se ha confundido con los hechos."
                    # ali "Oh, has encontrado una {amarillo}contradicción.{/amarillo}"
                    pla "Entiendo, tengo que ver en donde Beck se está contradiciendo con lo que tengo apuntado..."
                    hide alice with dissolve
                    show beck sonriendo with dissolve
                    bec "¿Qué pasa? ¿Qué están murmurando entre ustedes?"
                    if tuto_interr_refutar:
                        tuto "A continuación, se te habilitará la opción de {amarillo}refutar{/amarillo}."
                        tuto "Si encuentras una contradicción en una frase, sitúate en esta, {amarillo}y presiona el botón de refutar.{/amarillo}"
                        tuto "Luego presentas la evidencia que demostrará {amarillo}la contradicción del interrogado.{/amarillo}"
                        play sound campana
                        tuto "{amarillo}Presentar una evidencia incorrecta, restará un corazón.{/amarillo}" with flashbulb
                        $tuto_interr_refutar=False
                        $interr_btn_refutar_disabled=False
                    pla "No, nada... por favor, continúa."
                    bec "Bueno..."
                    jump caso1_testimonio3_inicio

                # elif not fraseInterr[2] and interr_3_arreglado:
                #     "Ya he encontrado la contradicción de Beck, pero todavía necesito una pista más..."
                #     "Necesito hacer la pregunta correcta."
                #     jump caso1_testimonio3_inicio

                else:
                    show alice normal with dissolve
                    ali "Esto no es suficiente..."
                    pla "¿En serio?"
                    ali "Hay que seguir preguntando..."
                    show alice sonriendo
                    ali "Mis superiores me decían que {amarillo}no se puede razonar sin tener suficientes datos.{/amarillo}"
                    pla "Lo entiendo... bien, veamos qué más información podemos sacar..."
                    hide alice with dissolve
                    jump caso1_testimonio3_inicio