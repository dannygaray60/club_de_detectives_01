label caso1_testimonio5:
    $estadoj="Testimonio"
    $interrogatorio_activo=False
    $initInterrVars()
    #intro testimonio
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    $interr_frase4_refutada=False

    label caso1_testimonio5_inicio:

        if estadoj=="Interrogatorio":
            show screen interrogatorio_btns

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int5_gameover
        
        $renpy.block_rollback()
        show neil normal with dissolve
        $interr_fraseid=0
        nei "Ese día, a las diez, {amarillo}iba de camino a la biblioteca.{/amarillo}"
        show neil pensativo
        $interr_fraseid=1
        nei "Entonces, encontré a la profesora Harrow y {amarillo}a una chica en el suelo...{/amarillo}"
        show neil normal
        $interr_fraseid=2
        nei "También vi que había montones de papeles regados por el suelo, {amarillo}así que ayudé a recogerlos.{/amarillo}"
        show neil sonriendo hablando
        $interr_fraseid=3
        nei "Después de eso, {amarillo}me fui.{/amarillo}"
        show neil serio hablando
        $interr_fraseid=4
        if not interr_frase4_refutada:
            nei "Y como {amarillo}no vi a nadie más en el camino,{/amarillo} no tengo nada más que contar."##refutar con perfil de beck o interrogar, de todas formas no activa bandera, pero aumenta inteligencia en 2
        else:
            nei "Y sí, vi a esa persona que se llama Beck, {amarillo}aunque no hablé con él.{/amarillo}"
        if interr_frase4_refutada:
            show neil serio hablando
            $interr_fraseid=5
            nei "Pero eso es todo, aparte de la gran altura de ese tal Beck, {amarillo}nadie más me llamó particularmente la atención{/amarillo} como para seguir hablando al respecto."#refutar con perfil de marissa
        hide neil with dissolve
        $renpy.block_rollback()
        hide screen interrogatorio_btns

        if estadoj=="Testimonio":
            stop music fadeout 2
            show alice normal with dissolve
            ali "Uhm..."
            ali "Eso fue rápido..."
            pla "Sí... casi todo lo que ha dicho ya lo sabemos..."
            "¿Pero, estará diciendo toda la verdad?"
            hide alice with dissolve

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $quick_menu_gameplay = True

            $estadoj="Interrogatorio"
            $interrogatorio_activo=True

            ## variables del interrogatorio
            $interr_id=5
            ##para establecer cual es la última frase y así desactivar el botón de siguiente
            $interr_frasefinal=4

            #en este interrogatorio, solo es necesario refutar correctamente
            $interr_btn_refutar_disabled=False

            #establecemos cantidad de corazones a 5
            $initCorazones()

            #intro interrogatorio
            $showMinigameTitle(estadoj)

            #mostramos panel de corazones y temporizador en 720 segundos
            $show_gameplay_layout(720)
            
            #botones de interrogatorio
            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio5_inicio

        else:
            $checkTimeAndJump("int"+str(interr_id)+"_gameover")
            
            if not interr_frase4_refutada:
                show alice normal with dissolve
                ali "Esto no es suficiente..."
                ali "¿Qué hacemos, [pla_name]?"
                "¿Qué hacemos? Yo estoy haciendo la mayoría del trabajo..."
                "Pero... En serio, ¿qué podría hacer?"
                "¿Seguir {amarillo}preguntando{/amarillo} o señalar una {amarillo}contradicción{/amarillo}?"
                hide alice with dissolve
            else:
                "Muy bien, ya he demostrado una contradicción..."
                "¡Pero hay otra más importante!" with hpunch
            jump caso1_testimonio5_inicio