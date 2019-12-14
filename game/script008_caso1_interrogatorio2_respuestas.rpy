label int2_gameover:
    hide screen interrogatorio_btns
    $hide_gameplay_layout()
    stop music fadeout 1.0
    mary "Sabes, [pla_name], te recomiendo que busques otro club."
    show mary hablando
    mary "No estás haciendo más que perder el tiempo."
    mary "No hablaré más, ahora retírate. Tengo que hablar con cierta alumna problemática."
    pla "Eh, profesora Harrow..." 
    mary "¿Te lo tengo que repetir?" with hpunch
    pla "No..."
    jump caso1_gameover
    
label int2f0:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    "¿El viernes de la semana pasada?"
    "Marissa dijo que ese día encontró la carta en su bolso..."
    pla "Espere, profesora Harrow..."
    pla "¿Con quién estuvo hablando en el salón de maestros?"
    # mary "..."
    play sound campana
    mary "Con Beck Doran." with flashbulb
    pla "¿¡Ehhh!?"
    show mary hablando
    mary "¿Por qué te sorprendes? ¿Acaso también lo conoces?"
    pla "Eh... algo así..."
    show mary normal
    pla "Como sea, después de que estuvo hablando con Beck en el salón de maestros..."
    pla "Usted iba en dirección al salón de Marissa, ¿no?"
    mary "Así es."
    show mary:
        ease .5 mleft
    show marissa normal at mright with dissolve
    mar "Con que Beck estaba... ¿hablando con la profesora Harrow?"
    mar "Qué raro... {nw}"
    play sound campana
    extend "{amarillo}él no es alguien al que le guste las clases de matemáticas.{/amarillo}" with flashbulb
    show mary hablando
    mary "..."
    show marissa sorprendida
    mar "¡Iiiiihhhh!" with hpunch
    mar "¡Ya- ya me callo! ¡Pe- perdón por interrumpir!" with hpunch
    show marissa preocupada
    show mary hablando
    mary "Él ha ido a verme varias veces, lo que demuestra que Beck sí hace un esfuerzo por aprender."
    show mary pensando
    mary "No como otras personas..."
    "Vaya, qué indirecta tan directa..."
    if not fraseInterr[0]:
        $addNote("Ayuda en matemáticas","El día del tropiezo (viernes), Beck estuvo con la profesora Harrow en el salón de maestros, por una pequeña tutoría de matemáticas; según he oído de la profesora, Beck ha ido varias veces a buscar ayuda. Aunque... Marissa había dicho que él odia esa clase... ¿Entonces para qué va a hablar con la profesora?")
        "No sé si este hecho es importante... pero nada pierdo con anotarlo."
        $updateNote("Beck Doran (perfil)",ndesc="\n\nAl parecer, a Beck no le gusta las clases de matemáticas.",add=True)
        pla "Y también esto..."
    pla "¿Acaso a Marissa le ha ido mal en clases?"
    "Sin querer hice esta pregunta, motivado por la curiosidad."
    show mary normal
    mary "Decir que le va mal es poca cosa..."
    mary "Aunque ella sea una chica muy carismática..."
    mary "Es una completa olvidadiza, despreocupada, siempre anda con la cabeza en las nubes..."
    mary "No entrega sus tareas a tiempo, y si lo hace, sus trabajos dejan que desear."
    show marissa apenada at decaer
    mar "Ya pareeeee..."
    if not fraseInterr[0]:
        $updateNote("Marissa Morstan (perfil)",ndesc="\n\nEs una chica carismática, pero la profesora Harrow me ha hecho ver que esta chica es también despreocupada, olvidadiza, no entrega tareas a tiempo, es mala en matemáticas...",add=True)
        pla "Interesante..."
        show marissa sorprendida at reponerse_rapido
        mar "¡Oye, [pla_name]! No anotes cosas innecesarias." with hpunch
    hide marissa with dissolve
    show mary:
        ease .5 center
    $fraseInterr[0]=True
    jump caso1_testimonio2_inicio

label int2f1:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A qué hora exactamente fue al salón?"
    mary "A las diez en punto."
    mary "Los jueves y viernes doy clases de matemáticas en ese salón a esa hora."
    if not fraseInterr[1]:
        $addNote("Horario de Prof. Harrow","Los jueves y viernes a las diez de la mañana, la profesora Harrow imparte clases de matemáticas en el salón de Marissa.")
    pla "Entiendo..."
    $fraseInterr[1]=True
    jump caso1_testimonio2_inicio

label int2f2:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Cómo ocurrió exactamente ese choque entre usted y Marissa?"
    mary "No tiene misterio..."
    mary "Al momento de llegar a la entrada, Marissa apareció de repente."
    mary "Al parecer, ella estaba corriendo."
    show mary:
        ease .5 mleft
    show marissa normal at mright with dissolve
    pla "Uhm... ¿Marissa?"
    mar "Eh... salí corriendo del salón por problemas en el club..."
    pla "Ya veo..."
    if not fraseInterr[2]:
        $addNote("¿Problemas en el club?","¿Qué clase de problemas tenía el club de Marissa para que ella saliera corriendo del salón?")
        "Tendré que preguntarle más tarde sobre esto."
    $fraseInterr[2]=True
    hide marissa with dissolve
    show mary:
        ease .5 center
    jump caso1_testimonio2_inicio

label int2f3:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "Así que... los papeles que usted llevaba, ¿se cayeron al suelo?"
    mary "Así es."
    mary "..."
    show mary:
        ease .6 mleft
    show marissa normal at mright with dissolve
    "La profesora Harrow dirigió una breve y amenazadora mirada a Marissa."
    show marissa sorprendida
    mar "¡Iiiihh!" with hpunch
    "¡La profera Harrow usó intimidación!"
    "¡Es muy efectivo!"
    show marissa preocupada
    mar "A mi también se me cayeron algunas cosas."
    pla "¿En serio?"
    mar "Uh... sí... llevaba la mochila abierta y se me cayeron los cuadernos."
    show marissa apenada
    mar "Fue aterrador estarlos recogiendo teniendo a la profesora tan cerca."
    show marissa normal
    pla "Por cierto..."
    play sound campana
    extend " {amarillo}¿Así que alguien vino a ayudarlas?{/amarillo}" with flashbulb
    pla "¿Me podría decir de quien se trataba?"
    show mary sorprendida
    # mary "Eh..."
    mary "Se trataba de {amarillo}Neil London.{/amarillo} Es un chico del tercer año B."
    show mary normal
    pla "¿Neil London? ¿Marissa, lo conoces?"
    mar "No... nunca había escuchado ese nombre antes."
    pla "Uhm..."
    if not fraseInterr[3]:
        pla "¿Podría describírmelo?"
        "Voy a tener que hablar con ese chico..."
        mary "Es alguien de aspecto tranquilo, piel clara, al igual que su cabello."
        $addNote("Neil London (perfil)","Es alguien de aspecto tranquilo, piel clara, al igual que su cabello.")
        pla "Muchas gracias."
        $addNote("Tropiezo","La profesora Harrow y Marissa chocaron entre ellas en la entrada del salón de Marissa, aproximadamente a las diez de la mañana. Papeles salieron volando, y Neil London fue a ayudarlas a recoger sus papeles.")
        "También anotaré todo lo que sé sobre este tropiezo entre Marissa y la profesora."
    hide marissa with dissolve
    show mary:
        ease .5 center
    $fraseInterr[3]=True
    jump caso1_testimonio2_inicio

label int2f4:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A qué castigo se refiere?"
    show mary:
        ease .6 mleft
    show marissa apenada at mright with dissolve
    mar "Fue horrible, [pla_name]..."
    show marissa at decaer
    mar "La profe me mandó a resolver cien ejercios de álgebra en la biblioteca."
    # if not fraseInterr[4]:
    #     $addNote("Castigo de Marissa","Debido al tropiezo que tuvo Marissa con la profesora de Matemáticas, ella recibió un castigo. Tuvo que ir a la biblioteca a resolver ejercicios de álgebra")
    mar "Fue toda una tortura..."
    show marissa at reponerse
    show mary pensando
    mary "Ah... si tan solo fueras aplicada en tus estudios, no te parecería un castigo serio."
    hide marissa with dissolve
    show mary:
        ease .5 center
    # $fraseInterr[4]=True
    jump caso1_testimonio2_inicio

label int2f5:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿No pasó nada más?"
    show mary hablando
    mary "Por algo he dicho que di mis clases con normalidad."
    pla "Ah, cierto..."
    $restCorazones()
    mary "Te sugiero que no me hagas perder el tiempo..." with hpunch
    pla "¡Pe- pe- perdón!"
    jump caso1_testimonio2_inicio

label int2f6:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Eso es todo?"
    mary "Eso es todo."
    show mary hablando
    mary "¿Algún problema con eso?"
    $restCorazones()
    pla "¡Eh! No- no..." with hpunch
    jump caso1_testimonio2_inicio