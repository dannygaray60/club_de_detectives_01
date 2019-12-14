label caso1_testimonio4:
    $estadoj="Testimonio"
    $interrogatorio_activo=False
    $initInterrVars()
    #intro testimonio
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio4_inicio:

        if estadoj=="Interrogatorio":
            show screen interrogatorio_btns
            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[2] and fraseInterr[4]:
                jump caso1_interrogatorio4_final

        if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int4_gameover

        $renpy.block_rollback()
        show marissa alegre hablando with dissolve
        $ interr_fraseid=0
        mar "Antes de la clase de matemáticas, {amarillo}estuve charlando con mis amigas en el salón.{/amarillo}"
        show marissa normal
        $ interr_fraseid=1
        mar "Casi al final de la hora, {amarillo}recibí una llamada.{/amarillo}"
        $ interr_fraseid=2
        show marissa normal
        mar "Entonces, salí a toda prisa y {amarillo}fue cuando choqué con la profesora...{/amarillo}"
        $ interr_fraseid=3
        show marissa apenada
        mar "{amarillo}Los papeles de la profesora Harrow salieron volando{/amarillo}, y a mí se me {amarillo}cayeron algunos cuadernos.{/amarillo}"
        $ interr_fraseid=4
        show marissa at decaer
        mar "No tardé en empezar a recoger las cosas, esa profesora es aterradora, {amarillo}poco después vino alguien a ayudar.{/amarillo}"
        $ interr_fraseid=5
        show marissa enojada at reponerse
        mar "A pesar de haberme disculpado, la profesora {amarillo}me castigó.{/amarillo}"
        $ interr_fraseid=6
        show marissa normal
        mar "No regresé al salón {amarillo}hasta que las clases de matematicas terminaron.{/amarillo}"
        $ renpy.block_rollback()

        hide screen interrogatorio_btns

        if estadoj=="Testimonio":
            stop music fadeout 2
            hide marissa with dissolve

            show alice normal with dissolve
            ali "Vaya, ella debió pasarlo terrible..."
            ali "Me siento afortunada de no haber visto a la profesora Harrow molesta..."
            pla "Sí... Como sea, veamos qué podemos averiguar..."
            show alice sonriendo
            ali "¡Sí!"
            hide alice with dissolve

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $quick_menu_gameplay = True

            $estadoj="Interrogatorio"
            $interrogatorio_activo=True

            ## variables del interrogatorio
            $interr_id=4
            ##para establecer cual es la última frase y así desactivar el botón de siguiente
            $interr_frasefinal=6

            #en este interrogatorio, como no se necesita refutar, se desactiva el botón
            $interr_btn_refutar_disabled=True

            #variables bandera
            $fraseInterr={0:0,1:1,2:2,4:4}
            $fraseInterr[0]=False
            $fraseInterr[1]=False
            $fraseInterr[2]=False
            $fraseInterr[4]=False

            #establecemos cantidad de corazones a 5
            $initCorazones()

            #intro interrogatorio
            $showMinigameTitle(estadoj)

            #mostramos panel de corazones y temporizador en 300 segundos
            $show_gameplay_layout(400)
            
            #botones de interrogatorio
            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio4_inicio

        else:
            $checkTimeAndJump("int"+str(interr_id)+"_gameover")
            hide marissa with dissolve
            "Marissa me ha contado algunas cosas que ya sabía..."
            "Pero, hay otras de las que necesito más información."
            "¡Necesito hacer las preguntas correctas!" with hpunch
            jump caso1_testimonio4_inicio