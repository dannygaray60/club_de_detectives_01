label caso1_iterrogatorio1_final:

    $fase_titulo.append("Interrogatorio de Marissa")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(10)

    stop music fadeout 2
    hide screen interrogatorio_btns
    $quick_menu_gameplay = False
    $hide_gameplay_layout()
    scene bg negro with dissolve
    pause 1.5
    $estadoj="Libre"
    play music ambiente2 fadein 4
    scene bg salon club detectives with dissolve
    $hora=16 #4pm
    pla "Bien... creo que ahora sí hemos hecho todas las preguntas debíamos hacer."
    show alice normal with dissolve
    ali "Así parece, [pla_name]."
    show alice:
        ease .5 mright
    show marissa sorprendida at mleft with dissolve
    mar "Vaya... ya se ha hecho tarde..."
    show marissa alegre hablando
    mar "Bueno, en serio muchas gracias por aceptar mi petición, me tengo que ir."
    if numero_marissa_obtenido:
        mar "Por cualquier cosa... [pla_name], puedes llamarme je, je, je."
        show alice sorprendida
        ali "¿¡Eh!?" with hpunch
        ali "[pla_name]... ¿Tienes el número de Marissa?"
        pla "Eh... sí... ¿hay algo malo con eso?"
        show alice sonrojada
        ali "N- no... nada..."
        show marissa alegre at brinquitos
        mar "Je, je, je, estás sonrojada."
        show alice asustada
        ali "¡Cla- claro que no!" with hpunch
        show alice sonrojada
        mar "Si quieres, también podemos intercambiar números."
        mar "De todas formas, debe ser importante tener a donde llamarme, ¿no?"
        ali "Su- supongo..."
        "¿Qué pasa con la reacción de Alice?"
    else:
        show marissa sorprendida
        mar "Ah, casi lo olvido..."
        mar "Creo que es importante que intercambiemos números."
        ali "Cierto..."
        "Me mostré de acuerdo con la idea de Marissa, entonces Alice y yo intercambiamos números con ella."

    show alice normal
    show marissa preocupada
    mar "Ah, otra cosa..."
    show alice sorprendida
    ali "¿Qué pasa?"
    mar "Este... quería pedirles otro favor..."
    mar "Les estaría muy agradecida de que {amarillo}no hablen mucho del caso con otras personas...{/amarillo}"
    mar "No quisiera que se extendieran rumores..."
    pla "Entiendo... aunque eso complicaría las cosas..."
    mar "Lo sé..."
    mar "Pero en la medida de lo posible, sean cautelosos, por favor."
    show marissa apenada
    mar "No me gustaría que todo el mundo sepa que fui plantada por un acosador."
    show alice alegre at brinquitos
    ali "¡Claro! ¡Cuenta con nosotros!"
    show marissa alegre
    mar "En serio... gracias..."
    mar "Y pensar que aparte de mi hermana, yo también necesitaría la ayuda de este club..."
    show alice normal
    show marissa alegre hablando
    show sherinford pequeño at mright with dissolve:
        ypos .450
        xoffset 70
    she "Pío."
    mar "¿Eh?"
    mar "Ese pollito, ¿es tuyo?"
    ali "S- sí... se llama Sherinford."
    show marissa alegre
    mar "Awwww qué lindo."
    show marissa alegre hablando
    mar "Bueno, me voy."
    mar "Estaremos en contacto."
    show marissa alegre at brinquitos
    mar "¡Bye, bye!"
    hide marissa with dissolve
    show alice:
        ease .5 center
    show sherinford pequeño:
        ypos .450
        xoffset 70
        ease .5 xpos .5
    pla "Qué caso tan curioso..."
    show alice alegre at brinquitos
    show sherinford pequeño at brinquitos
    ali "Je, je... ¿ahora no estás arrepentido de haberte unido al club?"
    pla "..."
    extend " solo espero no meterme en problemas con esto..."
    stop music fadeout 2
    scene bg negro with slow_dissolve
    pause 1.5
    jump caso1_investigacion1