label int3f0:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Tu hora habitual de llegar es a las ocho y media?"
    bec "Eso es lo que he dicho."
    show beck pensando
    bec "Minutos más, minutos menos..."
    # pla "..."
    "No veo nada extraño en eso..."
    hide beck with dissolve
    show alice enojada with dissolve
    $restCorazones()
    ali "¡[pla_name]! ¡No hagas preguntas innecesarias!" with hpunch
    pla "Lo sé, lo sé..."
    hide alice with dissolve
    jump caso1_testimonio3_inicio

label int3f1:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "Con que Física..."
    show beck enojado
    bec "Eh, sí. ¿Podrías al menos dejarme continuar?"
    $restCorazones()
    pla "Ah, claro, perdón..." with hpunch
    jump caso1_testimonio3_inicio

label int3f2:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    # if not fraseInterr[2]:
    #     $addCorazones()
    show beck:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Eh... le entiendo..."
    ali "Esas clases me duermen."
    show beck guino
    bec "Je, je, je. Veo que no soy el único."
    show beck serio
    bec "En serio, viejo... {amarillo}no soporto ver formúlas, números, o cosas así.{/amarillo}"
    bec "{amarillo}No se me da bien los números.{/amarillo}"
    bec "Es un alivio cuando esas clases terminan."
    show beck guino
    bec "Menos mal que tengo una beca por deportes."
    bec "Por que para los estudios, {amarillo}soy todo lo opuesto a un estudiante aplicado{/amarillo} ja, ja, ja."
    # if not fraseInterr[2]:
    #     $updateNote("Beck Doran (perfil)",ndesc="\n\nBeck no soporta ver cosas relacionadas a los números.",add=True)
    "No veo que eso sea algo para enorgullecerse..."
    hide alice with dissolve
    show beck:
        ease .5 center
    # $fraseInterr[2]=True
    # #una vez que se encontró la pista, mandamos al tuto de la siguiente etapa
    # if tuto_interr_refutar:
    #     jump interr_3_fin_frases
    jump caso1_testimonio3_inicio

label int3f3:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A qué hora tuvieron tiempo libre?"
    show beck sonriendo
    bec "{amarillo}Creo que a las diez.{/amarillo}"#misma hora de supuesta clase de mates.
    pla "Así que... ¿fuiste a la cancha, no?"
    show beck pensando
    bec "Por supuesto, {amarillo}es el lugar que más frecuento en la escuela.{/amarillo}"
    show beck serio
    bec "Si es de importancia que lo sepas..."
    show beck guino
    bec "Me topé con un par de chicas que querían ser mis \"amigas\" ja, ja, ja."
    bec "Si quieres, te presento a una."
    show beck:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "Eh... debe ser agotador ser popular..."
    pla "..."
    show alice sorprendida
    ali "¿[pla_name]?"
    # "Hay algo extraño con esto..."
    hide alice with dissolve
    show beck:
        ease .5 center
    #una vez que se encontró la pista, mandamos al tuto de la siguiente etapa
    $fraseInterr[3]=True
    if tuto_interr_refutar:
        jump interr_3_fin_frases
    jump caso1_testimonio3_inicio

label int3f4:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    "No sé qué preguntarle..."
    "Seguramente a Beck tampoco le gusta las clases de Historia, {amarillo}¿o tal vez sí?{/amarillo}"
    hide beck with dissolve
    show alice enojada with dissolve
    $restCorazones()
    ali "¡[pla_name]!" with hpunch
    pla "¿¡Ahora, qué!? Si ni siquiera he hablado."
    ali "Pero parecía que estabas a punto de hacer una pregunta innecesaria."
    "Eh... tiene razón."
    hide alice with dissolve
    jump caso1_testimonio3_inicio

label int3f5:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    show beck serio
    pla "¿Supones?"
    pla "¿Seguro que eso todo lo que tienes para contarme?"
    $restCorazones()
    show beck enojado
    bec "Sí. No tengo nada más que contar." with hpunch
    "Debo ir con más cuidado..."
    # bec "¿Entonces? Si no tienes más preguntas..."
    # "Uh... hay algo que no encaja con lo que ha dicho hasta ahora..."
    jump caso1_testimonio3_inicio



#-------- Respuestas cuando se presenta una evidencia de contradiccion

label int3f0_refutado:
    jump int3_incorrecto
label int3f1_refutado:
    jump int3_incorrecto
label int3f2_refutado:
    jump int3_incorrecto
label int3f4_refutado:
    jump int3_incorrecto
label int3f5_refutado:
    jump int3_incorrecto


label int3f3_refutado:
    hide screen interrogatorio_btns

    if interr_item_notepad_select==interr_item_notepad_correcto:
        hide screen interrogatorio_btns
        $quick_menu_gameplay = False
        $hide_gameplay_layout()
        stop music fadeout 1
        $showplay_excl("esonoescierto")
        pla "¿Estás seguro de que hubo tiempo libre a esa hora?"
        show beck sorprendido
        bec "¿Eh?"
        show beck pensando
        extend " Creo estar seguro de que así fue..."
        show beck:
            ease .5 mleft
        show alice normal at mright with dissolve
        ali "Qué frase tan contradictoria..."
        show beck serio
        pla "Estás en un error, Beck."
        pla "A esa hora, y en ese día..."
        play sound campana
        pla "No pudiste ir a la cancha a jugar." with flashbulb
        show beck sorprendido
        bec "¿Eh? ¿Por qué no?"
        pla "Por lo que tengo apuntado, no pudo haber tiempo libre en ese momento, y más aún cuando tocaba clases de matemáticas."
        bec "¡Ah! ¡Es cierto!"
        # bec "Me he confundido..."
        show beck pensando
        bec "Creo que he confudido las cosas, pero ya recuerdo bien."
        pla "También sé que fuiste al salón de maestros a pedir ayuda a la profesora Harrow."
        pla "Y que además hubo un tropiezo entre la profesora y Marissa."
        show beck sorprendido
        bec "¿¡Eeeeh!? ¿¡También sabías de todo eso!?" with hpunch
        $updateNote("Beck Doran (perfil)",ndesc="\n\nBeck estuvo en el corredor en los momentos finales al tropiezo de la profesora con Marissa, así que es algo así como un testigo.",add=True)
        pla "Somos del club de detectives."
        show beck:
            ease .5 mleft
        show alice sonriendo at mright with dissolve
        ali "¡Bien dicho, [pla_name]!"

        # show beck serio
        # pla "Hablé con la profesora Harrow..."
        # pla "Y ella me dijo que estabas en el salón de maestros en ese momento."
        # pla "Además, también me comentó que a esa hora se dirigía a tu salón."
        # show beck pensando
        # bec "..."
        # bec "Eh... yo..."
        # show beck preocupado
        # bec "Uh... ahora que lo dices, sí..."
        # bec "Creo que me he confundido de día..."
        # bec "Ese día había ido al salón de maestros para pedir ayuda a la profesora Harrow..."
        # show beck serio
        # bec "¿Y qué con eso?"
        # "..."
        # pla "Beck... ese día... Marissa se tropezó con la profesora Harrow."
        # show alice sorprendida
        # ali "¡Ah! Cómo lo he dejado pasar..."
        # ali "A esa hora no hubo tiempo libre en el salón..."
        # pla "Exactamente. En el salón de Marissa a las diez, ellos tenían clases de matemáticas."
        # show beck pensando
        # bec "Eh... si es cierto... lo había olvidado..."
        # pla "Ahora que sacamos ese tema, ¿podrías contarnos lo que viste?"
        # show beck serio
        # bec "Está bien..."
        # $addCorazones()
        jump caso1_interrogatorio3_final
    else:
        jump int3_incorrecto

label int3_incorrecto:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    ##agregar respuestas random
    bec "¿Qué?"
    bec "¿Y eso qué demuestra?"
    pla "Eh... bu- bueno... yo..."
    $restCorazones()
    "¡Debo pensar muy bien antes de hablar!" with hpunch
    jump caso1_testimonio3_inicio

label int3_gameover:
    hide screen interrogatorio_btns
    $hide_gameplay_layout()
    stop music fadeout 1.0
    show beck pensando
    bec "Ya se me está haciendo tarde, no seguiré hablando del tema."
    pla "¿¡Eh!? ¡Pero si no hemos terminado todavía!" with hpunch
    show beck preocupado
    bec "Pues yo sí he terminado, suerte con la investigación."
    hide beck with dissolve
    jump caso1_gameover