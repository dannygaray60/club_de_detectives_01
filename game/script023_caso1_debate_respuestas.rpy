label d1r0_correcto:
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
    pla "Lo que Alice y yo deducimos a partir de la carta..."
    pla "Es que hay una alta probabilidad de que, al menos al momento de que fue escrita, {amarillo}esta persona estaba nerviosa.{/amarillo}"
    show marissa sorprendida
    mar "¿Eh? ¿Y cómo lo supieron?"
    pla "{amarillo}El ligero temblor en la caligrafía{/amarillo} de la carta..."
    pla "Incluso, se ve lugares donde la punta del bolígrafo estuvo sobre el papel demasiado tiempo."
    show marissa normal:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Además... el no haber escrito su nombre..."
    ali "Y declararse por medio de una carta..."
    ali "Demuestra que {amarillo}esa persona es alguien insegura de sí misma.{/amarillo}"
    show marissa normal
    mar "¿En serio?"
    show marissa preocupada
    mar "Vaya... No me imaginaba eso..."
    mar "Ya que soy una persona muy sociable, no pensé que alguien se sentía de esa manera..."
    mar "Tampoco es que yo fuera alguien inalcanzable, o algo por el estilo..."
    show marissa normal
    mar "Está bien, ¿y eso es todo lo que han averiguado?"
    show alice sorprendida
    ali "¿¡Eh!? ¿A- a qué te- te refieres?"
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    mar "Vamos, que el autor de la carta sea alguien que estaba nervioso y que se sentía inseguro de sí mismo..."
    mar "¿En qué ayudaría a identificarlo?"
    jump caso1_debate_rnd1


label d1r0_incorrecto_marissa:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    $randomnum = renpy.random.randint(1, 4)
    if randomnum==1:
        show marissa normal
        mar "No entiendo a qué quieres llegar con eso, pero..."
    elif randomnum==2:
        show marissa alegre
        mar "A veces dices cosas muy raras ja, ja, ja."
        mar "[pla_name]..."
    elif randomnum==3:
        show marissa apenada
        mar "Sabes, creo que estoy empezando a dudar si fue buena idea pedirles ayuda..."
    elif randomnum==4:
        show marissa normal
        mar "¿Y eso qué demuestra?"
        pla "Eh... creo que nada..."
    $restCorazones()
    show marissa enojada
    mar "¡No vine a perder el tiempo!" with hpunch
    $renpy.jump("inicio_d"+str(debate_args[0])+"r"+str(debate_args[1]))

label d1_gameover:
    hide screen debateArgumento
    hide screen debateArgs
    stop music fadeout 3
    $hide_gameplay_layout()
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    scene bg negro with slow_dissolve
    "Estuvimos dando vueltas en círculos con lo que estabamos discutiendo."
    "Todos daban su opinión sin parar y siempre terminamos con muchas contradicciones, pero ninguna respuesta."
    jump caso1_gameover

