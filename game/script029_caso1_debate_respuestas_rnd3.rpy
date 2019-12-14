label d1r3_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r3_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice sonriendo
    ali "[pla_name], me alegra que quieras estar de acuerdo conmigo..."
    $restCorazones()
    show alice enojada
    ali "¡Pero ese argumento no me ayuda en nada!" with hpunch
    jump inicio_d1r3

label d1r3_incorrecto_beck:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    $randomnum = renpy.random.randint(1, 3)
    if randomnum==1:
        show beck pensando
        bec "Vale... tampoco es yo me luzca a la hora de pensar..."
        show beck enojado
        $restCorazones()
        bec "Pero tú ahora no pareces más listo que yo." with hpunch
    elif randomnum==2:
        show beck serio
        bec "Hey [pla_name]..."
        show beck guino
        $restCorazones()
        bec "Creo que te iría mejor estar en el club de deportes." with hpunch
        "Uh... ¿qué me habrá querido decir?"
    elif randomnum==3:
        show beck serio
        bec "¿Y cómo explica todo ese argumento?"
        $restCorazones()
        pla "Ehm... error mío..." with hpunch
    $renpy.jump("inicio_d"+str(debate_args[0])+"r"+str(debate_args[1]))

label d1r3_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("esonoescierto")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    
    pla "Te equivocas Beck"
    bec "Ohh vamos... ¿otra vez?"
    show beck preocupado
    bec "¿Y ahora en qué me he equivocado?"
    pla "Alice podría responder esa pregunta..."
    show beck:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿¡Ehh!? ¿¡Y- yo!?" with hpunch
    pla "¿Cuántas Alice tenemos en el club entonces?"
    show alice enojada
    ali "..."
    show alice normal
    ali "Ahora que lo dices..."
    ali "Yo también pensé en eso..."
    ali "Cuando fuimos al casillero de Marissa, traté de meter un papel ahí."
    ali "Pero no pude, {amarillo}ni por las rejillas{/amarillo}, ni alrededor de la puerta..."
    ali "Por más delgado que sea el papel no pudo entrar al casillero."
    ali "A menos que envolvieras la hoja en un palillo..."
    pla "Pero el papel no tenía ningún rasgo de haber sido enrollado o doblado más de lo necesario."
    pla "Solo presenta un doblez a la mitad."
    show beck pensando
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    bec "Uh... debe haber alguna respuesta a eso..."
    bec "Supongo que eso es lo importante del asunto."

    jump caso1_debate_rnd4