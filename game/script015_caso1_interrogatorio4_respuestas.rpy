label int4f0:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿No saliste en ningún momento del salón?"
    show marissa normal
    mar "Nope."
    mar "Y tampoco me he alejado de mi bolso."
    # mar "En todo ese tiempo libre, he estado hablando solo con mis amigas."
    show marissa:
        ease.5 mleft
    show alice normal at mright with dissolve
    ali "[pla_name], creo que no hay posibilidades de que la carta haya llegado a su bolso en ese momento..."
    pla "Eso parece."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $fraseInterr[0]=True
    jump caso1_testimonio4_inicio

label int4f1:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    show marissa:
        ease.5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿Una llamada?"
    pla "¿Quién te llamó?"
    show alice normal
    show marissa normal
    mar "Era uno de los miembros del club."
    mar "Me habían llamado por un problema, {amarillo}el horno se había dañado.{/amarillo}"
    mar "Y teníamos ese día algunos encargos por cumplir."
    show marissa preocupada
    mar "Así que me alarmé al escuchar esa noticia..."
    show alice sorprendida
    ali "¿Encargos?"
    show marissa alegre hablando
    mar "¡Sí!"
    mar "Nuestro club prepara postres para algunos eventos."
    show marissa alegre
    mar "Desde nuestra página web nos contactan."
    ali "Eh... eso es genial..."
    if not fraseInterr[1]:
        $removeNote("¿Problemas en el club?")
    "Uhm... es algo curioso, pero no hay mucho misterio en eso..."

    # if not fraseInterr[1]:
    #     $addNote("Llamada para Marissa","Minutos antes de que Marissa se tropezara con la profesora Harrow, Marissa recibió una llamada:\nEl horno del club de cocina se había dañado.\nAlarmada, ella se fue corriendo del salón, pero terminó chocando con la profesora de matemáticas.")
    #     "Solo por si acaso, lo apuntaré."
    #sitio web. las actividades no solo se limitan al club
    # "También esto..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $fraseInterr[1]=True
    jump caso1_testimonio4_inicio

label int4f2:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "Exactamente, ¿donde ocurrió este choque?"
    pla "¿{amarillo}Adentro{/amarillo}, o {amarillo}afuera{/amarillo} del salón?"
    show marissa normal
    mar "Uhm..."
    extend " {amarillo}afuera.{/amarillo}"
    pla "Entiendo..."
    "Dejaré que siga hablando..."
    $fraseInterr[2]=True
    jump caso1_testimonio4_inicio

label int4f3:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    show marissa:
        ease.5 mleft
    show alice normal at mright with dissolve
    ali "La profesora Harrow suele llevar una carpeta con papeles y folletos..."
    ali "Así que no es nada extraño que al caerse todos esos papeles salieran volando..."
    ali "Pero..."
    ali "Marissa, tú llevabas un bolso. {amarillo}¿Cómo es que se te cayeron los cuadernos?{/amarillo}"
    show marissa normal
    mar "Eh, pues tenía el bolso abierto."
    show alice sorprendida
    ali "¿¡Eeeh!?" with hpunch
    ali "¡Eso es extraño!"
    ali "Seguramente el acosador aprovechó y metió la carta en tu bolso..."
    ali "Y no le dio tiempo para cerrarlo...{w=1.1}{nw}"
    show marissa preocupada sudor
    mar "Eh, perdón por interrumpirte..."
    show marissa normal
    extend " pero no hay nada raro en eso."
    show alice normal
    ali "¿Qué?"
    show marissa alegre hablando
    mar "Cuando recibí la llamada, estaba guardando mi cuaderno en el bolso."
    mar "Como salí apurada, no tuve tiempo ni de cerrarlo bien."
    mar "Ya que la clases no tardarían en empezar, quería ir rápido al club a ver como solucionar el problema por el que me llamaron."
    # $addNote()#nota: el bolso de mary abierto
    ali "Oh... ya veo..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    jump caso1_testimonio4_inicio

label int4f4:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    show marissa:
        ease.5 mleft
    show alice normal at mright with dissolve
    ali "¿Vino alguien a ayudar?"
    "Eso es lo que nos han dicho la profesora Harrow, y Beck..."
    pla "Marissa... ¿Conoces a ese chico que vino a ayudarlas?"
    show marissa normal at reponerse
    mar "..."
    extend " nope."
    mar "No creo haberlo visto antes, {amarillo}no lo conozco de nada.{/amarillo}"
    pla "Uh..."
    pla "¿Y qué hizo exactamente esta persona?"
    mar "Pues lo normal, lo que cualquiera haría en esa situación, {amarillo}nos ayudó a recoger todos los papeles que habían en el suelo...{/amarillo}"
    show marissa apenada
    mar "Había muchos, parecía un mar de papeles..."
    if not fraseInterr[4]:
        $updateNote("Neil London (perfil)",ndesc="\n\nAl parecer, no es un conocido de Marissa o Beck.",add=True)
    pla "Y... ¿no has notado algo extraño en ese chico?"
    show marissa normal
    mar "..."
    mar "Ahora que lo dices..."
    mar "Creo que{nw}"
    play sound campana
    extend " {amarillo}sí había algo raro.{/amarillo}" with flashbulb
    show alice sorprendida
    ali "¡Dinos mas!" with hpunch
    show alice normal
    show marissa preocupada
    mar "Bueno, esa persona {amarillo}se veía muy servicial conmigo.{/amarillo}"
    show marissa alegre hablando
    mar "{amarillo}Estuvo interesado{/amarillo} en saber si me había lastimado."
    show marissa at brinquitos
    mar "Era algo así... {amarillo}como alguien caballeroso{/amarillo} je, je, je."
    show alice sorprendida
    ali "Eh..."
    ali "¿Y si la profesora Harrow se enojó contigo porque ese chico fue caballeroso solo contigo?"
    show marissa alegre
    mar "Ja, ja, ja."
    mar "Qué cosas dices."
    if not fraseInterr[4]:
        $updateNote("Neil London (perfil)",ndesc="\n\nMarissa a corroborado que Neil parece estar interesado en ella.",add=True)
        "Apuntado..."
    hide alice with dissolve
    show marissa:
        ease .5 center
    $fraseInterr[4]=True
    jump caso1_testimonio4_inicio

label int4f5:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Qué clase de castigo te dio?"
    show marissa apenada
    mar "Me mandó a realizar un montón de ejercicios en la biblioteca..."
    pla "Interesante..."
    hide marissa with dissolve
    show alice enojada
    ali "..."
    $restCorazones()
    pla "Ah, lo sé... es una pregunta innecesaria..." with hpunch
    hide alice with dissolve
    # pla "Uhm... ¿y en tu camino a la biblioteca no pasó nada?"
    # show marissa sorprendida
    # mar "¿Eh? ¿A qué te refieres?"
    # pla "Por ejemplo, {amarillo}¿te encontraste con alguien?{/amarillo}"
    # show marissa normal
    # mar "Uhm. No. Nada de nada."
    jump caso1_testimonio4_inicio

label int4f6:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Y no pasó nada más?"
    show marissa sorprendida
    mar "¿Eh? ¿No recuerdas que solo querías saber lo que pasó relacionado al choque?"
    $restCorazones()
    pla "Ah, cierto..." with hpunch
    jump caso1_testimonio4_inicio
    

label int4_gameover:
    hide screen interrogatorio_btns
    $hide_gameplay_layout()
    stop music fadeout 1.0
    show marissa preocupada
    mar "Uhm... creo que ha sido un error venir a pedirles ayuda."
    mar "Parece que no estamos llegando a ningún lado con esta investigación."
    mar "Lo- lo siento... Mejor iré a hablar con algún maestro."
    show marissa apenada
    mar "Gracias de todas formas..."
    jump caso1_gameover