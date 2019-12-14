label int5f0:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A la biblioteca?"
    pla "¿Qué irías a hacer a la biblioteca, si a esa hora todavía había clases?"
    show neil pensativo
    nei "Resulta que me habían encargado traer algunos libros de la biblioteca, así que por casualidad pasé por el corredor en ese momento."
    "Uhm... No hay nada relevante en lo que ha dicho..."
    jump caso1_testimonio5_inicio

label int5f1:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    # pla "Oye Neil..."
    pla "¿De casualidad, no conocías a aquella chica?"
    nei "..."
    nei "Bueno... no."
    show neil sonriendo hablando
    nei "{amarillo}Fue la primera vez que la vi...{/amarillo}"
    hide neil with dissolve
    show alice normal with dissolve
    ali "..."
    pla "¿Qué pasa, Alice?"
    show alice pensando
    ali "No sé si fueron ideas mías..."
    show alice normal
    play sound campana
    ali "Pero le {amarillo}brillaron los ojos cuando mencionaste a Marissa.{/amarillo}" with flashbulb
    pla "Tienes razón..."
    hide alice with dissolve
    show neil normal with dissolve
    # nei "¿Qué pasa? ¿De qué están hablando?"
    # pla "Neil..."
    # nei "¿Sí?"
    # pla "Sabes, esa chica a la que ayudaste,{nw}"
    # play sound campana
    # extend " {amarillo}se llama Marissa.{/amarillo}" with flashbulb
    # show neil sorprendido
    # nei "¡...!"
    # nei "¿Ma- Marissa?"
    # show neil sonriendo hablando
    # nei "Es un lindo nombre... je, je, je..."
    # pla "Dime, ¿qué opinas de ella?"
    # show neil pensativo
    # nei "¿De esa chica?"
    # nei "Pues no la conozco..."
    # show neil sonriendo hablando at brinquitos
    # nei "Pero ella es realmente linda... je, je..."
    # "Esto afirma lo que tengo apuntado..."
    jump caso1_testimonio5_inicio

label int5f2:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Qué hiciste exactamente?"
    show neil sorprendido
    nei "¿Qué pregunta es esa?"
    nei "¿Qué más iba a hacer? Obvio que fui a ayudarlas."
    show neil normal
    nei "Estuve recogiendo todos los papeles del suelo."
    nei "No creo que se necesite mayor explicación."
    # nei "Tanto para la profesora Harrow, así también ayudé a aquella chica."
    $restCorazones()
    pla "No debí preguntar algo tan obvio..." with hpunch
    jump caso1_testimonio5_inicio

label int5f3:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Te fuiste a donde?"
    nei "¿Acaso has olvidado lo que he dicho?"
    show neil serio hablando
    nei "Pues a la biblioteca. ¿Es el trabajo de un detective hacer preguntas tan obvias?"
    hide neil with dissolve
    show alice enojada
    ali "¡[pla_name]!"
    $restCorazones()
    pla "Lo sé... error mío..." with hpunch
    hide alice with dissolve
    jump caso1_testimonio5_inicio

label int5f4:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Es eso cierto?"
    show neil pensativo
    nei "Eh... ¿me estás diciendo mentiroso?"
    if not interr_frase4_refutada:
        pla "¡No, no! No me malinterpretes." with vpunch
        pla "Solo quise decir que... Tal vez sí viste a alguien más en ese momento..."
        nei "¿En serio?"
        show neil sonriendo hablando
        nei "Pues si estás tan seguro... {amarillo}demuestrámelo.{/amarillo}"
        show neil normal
        nei "Yo por mi parte, no recuerdo nada más."
        "Debería tener {amarillo}algo para demostrar...{/amarillo} Neil {amarillo}tuvo haber visto a otra persona...{/amarillo}"
    else:
        "No tiene caso, aquí no hay nada más que preguntar."
    jump caso1_testimonio5_inicio

label int5f5:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿En serio nadie te llamó la atención?"
    nei "Pues, es lo que he dicho."
    $restCorazones()
    nei "Siguiente pregunta." with hpunch
    "Debo ser más directo..."
    "{amarillo}Neil se tuvo que interesar en alguien{/amarillo} cuando sucedió el tropiezo, ¿pero en quién?"
    jump caso1_testimonio5_inicio


## respuestas cuando se refuta una frase

label int5f0_refutado:
    jump int5_incorrecto
label int5f1_refutado:
    jump int5_incorrecto
label int5f2_refutado:
    jump int5_incorrecto
label int5f3_refutado:
    jump int5_incorrecto


label int5f4_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==lstNotepad_titulo.index("Marissa Morstan (perfil)") and not interr_frase4_refutada:
        $showplay_excl("espera")
        "No, espera..."
        "Neil dijo que no vio a nadie más en el camino, pero {amarillo}es obvio que se encontró con Marissa{/amarillo} y la profesora Harrow, porque les fue a ayudar."
        "Así que tiene que haber {amarillo}una tercera persona...{/amarillo}"
        "Uf, menos mal Alice no me ha regañado."
        hide neil with dissolve
        show alice enojada with dissolve
        $restCorazones()
        ali "[pla_name]..." with hpunch
        "No hay que cantar victoria antes de tiempo..."
        hide alice with dissolve
        jump caso1_testimonio5_inicio

    elif interr_item_notepad_select==lstNotepad_titulo.index("Beck Doran (perfil)") and not interr_frase4_refutada:
        $showplay_excl("esonoescierto")
        pla "¿Estás seguro de eso?"
        show neil pensativo
        nei "Ehm... sí..."
        pla "¿Y qué me dices de Beck?"
        show neil serio
        nei "¿Beck? ¿Quién es ese?"
        "Ah, cierto... no lo conoce..."
        pla "Es un chico que estudia en el mismo salón que la chica que ayudaste..."
        pla "Y esa persona, {nw}"
        play sound campana
        extend "{amarillo}estaba en el corredor cuando tú fuiste a ayudar a recoger los papeles.{/amarillo}" with flashbulb
        show neil sorprendido
        nei "¿¡Eh!?"
        show neil pensativo
        nei "Uhmm... {amarillo}¿es un chico alto y de cabello café?{/amarillo}"
        $checkTimeAndJump("int"+str(interr_id)+"_gameover")
        menu:
            "Sí":
                pla "Sí..."
                nei "Eh..."
                show neil serio hablando
                nei "No, espera... la única persona que conozco que es alta y {amarillo}de cabello café{/amarillo} no fue ese día a la escuela."
                nei "Y no se llama \"Beck\"."
                $restCorazones()
                "Ah... he metido la pata... Debería revisar mi bloc de notas, {amarillo}creo que entendí mal su pregunta.{/amarillo}" with hpunch
            "No":
                if not interr_frase4_refutada:
                    $updateStat("intel","+",1)
                    $renpy.notify("Inteligencia +1")
                pla "No, la persona de la que te estoy hablando es alta, pero es de cabello rojo."
                show neil serio
                nei "Uhm... alguien alto y pelirrojo..."
                play sound campana
                show neil sorprendido
                nei "¡Ah! ¡Ya lo recuerdo!" with flashbulb
                show neil normal
                nei "Ahora que he hecho esfuerzo en recordar..."
                nei "Sí, creo haber visto a esa persona en ese momento."
                play sound campana
                nei "¿Pero qué importancia tiene eso?" with flashbulb
                nei "No hablé con él para nada, yo solo seguí mi camino."
                # pla "..."
                # pla "Tienes razón..."
                show neil sonriendo hablando
                nei "Je, je, je... creo que no tardará en terminarse el receso..."
                nei "Debería irme ya..."
                pla "¡Ah! ¡Espera!" with hpunch
                pla "Todavía hay algo más..."
                $checkTimeAndJump("int"+str(interr_id)+"_gameover")
                nei "Bien... ¿qué más necesitas saber?"
                if not interr_frase4_refutada:
                    tuto "Las frases del interrogado han sido actualizadas. {amarillo}Ha aparecido otra contradicción.{/amarillo}"
                $interr_frase4_refutada=True
                $interr_frasefinal=5
        jump caso1_testimonio5_inicio
    else:
      jump int5_incorrecto  


label int5f5_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==lstNotepad_titulo.index("Marissa Morstan (perfil)") or interr_item_notepad_select==lstNotepad_titulo.index("Neil London (perfil)"):
        $quick_menu_gameplay = False
        $hide_gameplay_layout()
        stop music fadeout 1
        $showplay_excl("esonoescierto")
        jump caso1_interrogatorio5_final
    else:
      jump int5_incorrecto 



label int5_incorrecto:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    ##agregar respuestas random
    show neil serio
    nei "¿Y eso qué demuestra?"
    $restCorazones()
    "¡Ah, me he equivocado!" with hpunch
    jump caso1_testimonio5_inicio

label int5_gameover:
    hide screen interrogatorio_btns
    $hide_gameplay_layout()
    stop music fadeout 1.0
    show neil pensativo
    nei "Pensándolo bien..."
    show neil normal
    nei "Ustedes de todas formas no lograrían resolver el caso. Así que esto es una pérdida de tiempo."
    pla "¡Pero resolvimos tu acertijo!"
    show neil pensativo
    nei "¿Y eso qué?"
    nei "Tal vez fue pura suerte."
    nei "Además era un acertijo que hasta un niño podría resolver."
    show neil normal
    nei "Lo siento, me tengo que ir."
    hide neil with dissolve
    "No... no... ¡No!" with hpunch
    jump caso1_gameover