label caso1_interrogatorio4_final:

    $fase_titulo.append("Interrogatorio de Marissa 2")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(10)


    $hora=8
    stop music fadeout 5
    $ quick_menu_gameplay = False
    $ hide_gameplay_layout()
    hide screen interrogatorio_btns
    show marissa normal:
        ease .5 mleft
    show alice normal at mright with dissolve
    pla "Creo que eso es todo por ahora."
    show marissa sorprendida
    mar "¿En serio?"
    mar "Entonces, ¿ya tienen algún sospechoso?"
    pla "Algo así..."
    pla "Pero no estamos seguros del todo." with hpunch
    ali "Sí, todavía tenemos que hacer otro interrogatorio..."
    show marissa normal
    mar "Eh... entiendo..."
    mar "Bueno, ya me voy, las clases no tardarán en empezar."
    pla "Sí, nos vemos."
    $estadoj="Libre"
    hide marissa with dissolve
    show alice:
        ease .5 center
    ali "..."
    show alice pensando
    ali "Siento que estamos cerca de terminar este caso..."
    ali "Pero, aún veo muchas cosas extrañas..."
    ali "Hay... algo que no encaja del todo..."
    pla "Yo también siento eso, espero que {amarillo}si logramos hablar con Neil,{/amarillo} él nos aclare todo..."
    ali "Uhm... sí..."
    pla "Me iré a mi salón, nos vemos en la hora de receso."
    show alice sonriendo
    ali "Sí, nos vemos, [pla_name]."
    scene bg negro with slow_dissolve
    "Ese día, me lo pasé distraído."
    "Había tantas cosas que apunté... pero no encontraba una respuesta."
    "Tal como dijo Alice, había algo que no encajaba..."
    "Pero por más que reviso mis apuntes, no logro encontrar esa pieza que falta..."
    "Espero que pronto pueda encontrar una solución..."
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=10
    $quick_menu=True
    window show
    jump caso1_investigacion3