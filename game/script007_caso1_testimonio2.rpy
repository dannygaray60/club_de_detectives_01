label caso1_testimonio2:
    $estadoj="Testimonio"
    $interrogatorio_activo=False
    $initInterrVars()
    #intro testimonio
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio2_inicio:

        if estadoj=="Interrogatorio":
            show screen interrogatorio_btns
            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[1] and fraseInterr[2] and fraseInterr[3]:
                jump caso1_iterrogatorio2_final

        if cantidad_corazones==0 or timeup:
            hide screen interrogatorio_btns
            jump int2_gameover   

        $renpy.block_rollback()
        show mary normal with dissolve
        $ interr_fraseid=0
        mary "{amarillo}El viernes de la semana pasada{/amarillo}, después de haber hablado {amarillo}con un alumno{/amarillo} en el salón de maestros..."
        $ interr_fraseid=1
        mary "{amarillo}Siguiendo con mi horario,{/amarillo} fui al salón de la señorita Morstan a impartir clases."
        $ interr_fraseid=2
        show mary pensando
        mary "Pero al acercarme a la entrada, {amarillo}fue cuando ella se tropezó conmigo.{/amarillo}"
        $ interr_fraseid=3
        show mary hablando
        mary "{amarillo}Papeles salieron volando{/amarillo}, fue un desastre. Menos mal que {amarillo}alguien vino a ayudar.{/amarillo}"
        $ interr_fraseid=4
        show mary pensando
        mary "Después de haber recogido mis documentos. Le impuse a Marissa un castigo."
        $ interr_fraseid=5
        show mary normal
        mary "Luego, {amarillo}di mis clases con normalidad.{/amarillo}"
        $ interr_fraseid=6
        mary "{amarillo}Eso es todo.{/amarillo}"
        $ renpy.block_rollback()

        hide screen interrogatorio_btns

        if estadoj=="Testimonio":
            stop music fadeout 2

            mary "Bien, suelta tus preguntas."
            mary "No tengo todo el tiempo del mundo."
            mary "Te daré {amarillo}cinco minutos{/amarillo} para aclarar todas tus dudas."
            pla "¿¡Eh!?" with hpunch
            "¿Cinco minutos?"
            "¡Debo darme prisa!"

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $quick_menu_gameplay = True

            $estadoj="Interrogatorio"
            $interrogatorio_activo=True

            ## variables del interrogatorio
            $interr_id=2
            ##para establecer cual es la última frase y así desactivar el botón de siguiente
            $interr_frasefinal=6

            #en este interrogatorio, como no se necesita refutar, se desactiva el botón
            $interr_btn_refutar_disabled=True

            #variables bandera
            $fraseInterr={0:0,1:1,2:2,3:3,4:4}
            $fraseInterr[0]=False
            $fraseInterr[1]=False
            $fraseInterr[2]=False
            $fraseInterr[3]=False
            $fraseInterr[4]=False

            #establecemos cantidad de corazones a 5
            $initCorazones()

            #intro interrogatorio
            $showMinigameTitle(estadoj)

            #mostramos panel de corazones y temporizador en 300 segundos
            $show_gameplay_layout(300)
            #botones de interrogatorio
            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio2_inicio

        else:
            $checkTimeAndJump("int"+str(interr_id)+"_gameover")
            "Por alguna razón, siento que hay algo aquí que podría ser importante en la investigación..."
            "¡Necesito hacer las preguntas correctas!" with hpunch
            jump caso1_testimonio2_inicio