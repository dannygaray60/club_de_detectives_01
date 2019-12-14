label caso1_testimonio1:
    scene bg salon club detectives with dissolve
    
    $estadoj="Testimonio"
    $interrogatorio_activo=False
    $initInterrVars()
    #intro testimonio
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 3

    label caso1_testimonio1_inicio:

        if estadoj=="Interrogatorio":
            show screen interrogatorio_btns

            ## si se realizaron todas las preguntas necesarias...
            if fraseInterr[0] and fraseInterr[2] and fraseInterr[4] and fraseInterr[8] and fraseInterr[9]:
                jump caso1_iterrogatorio1_final

            if cantidad_corazones==0 or timeup:
                hide screen interrogatorio_btns
                jump int1_gameover
        
        $renpy.block_rollback()
        show marissa normal with dissolve
        $interr_fraseid=0
        mar "{amarillo}El viernes{/amarillo} de la semana pasada, {amarillo}encontré una carta en mi bolso.{/amarillo}"
        show marissa alegre hablando
        $interr_fraseid=1
        mar "Considerando ese bonito gesto, de escribir una carta de amor, {amarillo}fui al lugar y a la hora mencionada.{/amarillo}"
        show marissa apenada
        $interr_fraseid=2
        mar "{amarillo}Esperé un tiempo{/amarillo} afuera del café..."
        $interr_fraseid=3
        mar "Aunque me molestó un poco haber sido plantada, {amarillo}no le di mayor importancia al asunto, así que me fui.{/amarillo}"
        show marissa normal
        $interr_fraseid=4
        mar "No sé si es importante... pero noté {amarillo}algo raro en mi casillero{/amarillo} cuando llegué a la escuela {amarillo}el sábado.{/amarillo}"
        $interr_fraseid=5
        mar "{amarillo}A parte de eso...{/amarillo}"
        show marissa alegre
        $interr_fraseid=6
        mar "El domingo me lo pasé en mi casa, {amarillo}no salí a ningún lugar.{/amarillo}"
        show marissa preocupada
        $interr_fraseid=7
        mar "Pero el lunes... Es cuando empecé a sentir que {amarillo}alguien me observaba{/amarillo} constantemente..."
        $interr_fraseid=8
        mar "En el salón de clases, en los corredores, incluso afuera de la escuela... {amarillo}esa sensación seguía ahí.{/amarillo}"
        $interr_fraseid=9
        mar "Incluso, llegué a ver una {amarillo}sombra{/amarillo} escondiéndose en una esquina."
        hide marissa with dissolve
        $renpy.block_rollback()
        hide screen interrogatorio_btns

        if estadoj=="Testimonio":
            stop music fadeout 2
            show alice normal with dissolve
            ali "Uhm..."
            ali "Ciertamente hay muchos misterios sobre el asunto... ¿Verdad, [pla_name]?"
            pla "Ah, sí..."
            ali "[pla_name], es hora de hacer las preguntas."
            show alice alegre
            ali "¡Vamos a ello!" with hpunch
            hide alice with dissolve
            tuto "Hola de nuevo."
            tuto "Recién has escuchado el {amarillo}testimonio{/amarillo} de una persona."
            tuto "Ahora, realizarás un {amarillo}interrogatorio.{/amarillo}"
            tuto "En un interrogatorio, podrás {amarillo}avanzar o retroceder{/amarillo} las frases del interrogado {amarillo}cuantas veces quieras.{/amarillo}"
            tuto "Para {amarillo}realizar una pregunta{/amarillo}, solo úbicate en una frase, y presiona el botón con el símbolo de interrogación."
            tuto "Pero ten cuidado..."
            tuto "Si realizas preguntas innecesarias..."
            tuto "{amarillo}Se te penalizará{/amarillo} con un corazón menos."
            tuto "Tendrás cinco corazones, si los pierdes todos, será un {amarillo}game over.{/amarillo}"
            tuto "También hay que estar pendiente del {amarillo}tiempo...{/amarillo}"
            tuto "Una persona no siempre será tan paciente para estar todo el rato respondiendo tus preguntas."
            tuto "Una cosa más, cuando estés en medio de un minijuego, {amarillo}no podrás guardar tu partida.{/amarillo}"
            tuto "Así que asegúrate de guardar de vez en cuando."
            tuto "Buena suerte."
            $estadoj="Interrogatorio"
            $interrogatorio_activo=True

            ## variables del interrogatorio
            $interr_id=1
            ##para establecer cual es la última frase y así desactivar el botón de siguiente
            $interr_frasefinal=9

            #en este interrogatorio, como no se necesita refutar, se desactiva el botón
            $interr_btn_refutar_disabled=True

            #variables bandera
            $fraseInterr={0:0,2:2,4:4,8:8,9:9}
            $fraseInterr[0]=False
            $fraseInterr[2]=False
            $fraseInterr[4]=False
            $fraseInterr[8]=False
            $fraseInterr[9]=False

            #establecemos cantidad de corazones a 5
            $initCorazones()

            ## desactivamos opciones irrelevantes del quick menu, y el menu normal
            $quick_menu_gameplay = True

            #intro interrogatorio
            $showMinigameTitle(estadoj)

            #mostramos panel de corazones y temporizador en 600 segundos
            $show_gameplay_layout(600)
            
            #botones de interrogatorio
            show screen interrogatorio_btns

            play music tiempo_muerto2 fadein 3

            jump caso1_testimonio1_inicio

        else:
            $checkTimeAndJump("int"+str(interr_id)+"_gameover")
            show alice normal with dissolve
            ali "Esto no es suficiente..."
            pla "¿En serio?"
            ali "Hay que seguir preguntando..."
            show alice sonriendo
            ali "Mis superiores me decían que {amarillo}no se puede razonar sin tener suficientes datos.{/amarillo}"
            pla "Lo entiendo... bien, veamos qué más información podemos sacar..."
            hide alice with dissolve
            jump caso1_testimonio1_inicio