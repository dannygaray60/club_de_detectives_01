label d1r1_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r1_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice enojada
    ali "[pla_name]..."
    $restCorazones()
    ali "No me contradigas, sé que hay otra cosa que averiguamos acerca del autor de la carta..." with hpunch
    show alice pensando
    ali "Pero no sé exactamente qué es..."
    jump inicio_d1r1

label d1r1_correcto:
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
    pla "Sí, descubrimos otra pista."
    play sound campana
    pla "{amarillo}El autor de la carta es zurdo.{/amarillo}" with flashbulb
    show marissa preocupada sudor
    mar "¿Es... zurdo? Vaya, eso sí ayuda a identificarlo..."
    mar "Tengo curiosidad, ¿cómo lo supiste?"
    show marissa normal
    pla "Me fijé en la inclinación de la letra."
    pla "Y cualquier diestro no dejaría ese tipo de inclinación al escribir."
    show marissa:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¡Ah, cierto!"
    ali "Se me había olvidado decirlo..."
    show alice pensando
    ali "Es que Marissa empezó a decir muchas cosas y me puse nerviosa..."
    show marissa preocupada sudor
    mar "¿¡Eh!? Pe- perdón..."
    show marissa preocupada
    mar "Estaba algo emocionada..."
    ali "..."
    pla "En fin, si el autor de la carta es zurdo, eso también explicaría las manchas en el papel."
    mar "La mano con la que escribe pasaría sobre la tinta fresca..."
    show marissa alegre hablando at brinquitos
    show alice normal
    mar "¡Wow! ¡Eso es increíble! ¡Tal como se esperaba del club de detectives!"
    show alice sonrojada
    ali "..."
    "Por un momento, vi una ligera mueca de sonrisa en Alice..."
    show alice normal
    pla "Y con esta pista, se reduciría bastante la lista de sospechosos..."
    "Aunque eso no es suficiente..."
    show marissa normal
    mar "Bueno, ya está claro sobre la personalidad y una característica especial de esa persona..."
    mar "Pero... no entiendo."
    mar "Cómo una persona que escribió la carta con nervios y además se sentía inseguro..."
    mar "¿Llegó hasta el punto de acosarme?"
    show alice pensando
    ali "..."
    pla "La verdad, eso es algo que no podemos llegar a entender..."
    pla "Marissa, cuando nos pediste ayuda, dijiste que fueramos discretos en este caso..."
    show alice normal
    show marissa preocupada
    mar "Así es, no me gustaría esto vaya a propagarse como un rumor..."
    pla "Eh, sí... pero creo que necesitamos involucrar a otras personas."
    show alice normal
    mar "¿Ah, sí?"
    pla "Sabes, creo que Beck podría ayudarnos a entender mejor a este acosador."
    mar "..."
    stop music
    play sound campana
    show marissa preocupada sudor
    mar "¡Ah! ¡Beck tiene {amarillo}experiencia lidiando con acosadoras{/amarillo}!" with flashbulb
    mar "..."
    show marissa alegre
    mar "¡No hay problema!"
    show marissa alegre hablando
    mar "Conozco a Beck desde el año pasado, y estoy segura que no es alguien de los que va iniciando rumores."
    mar "Y él puede entender cómo me siento al respecto..."
    pla "Perfecto entonces, lo mandaré a llamar."
    $quick_menu_gameplay=False
    scene bg negro with dissolve
    "Corrí hacia la cancha de la escuela, no tardé en encontrar a Beck, quien estaba a un lado de la cancha charlando con unos amigos."
    "Le dije que necesitábamos de su ayuda para resolver el problema de Marissa."
    "Y él aceptó ir conmigo al salón del club."
    play music ambiente fadein 3
    scene bg salon club detectives with dissolve
    show beck preocupado with dissolve
    pause 1
    show beck:
        ease .5 mleft
    show marissa alegre hablando at mright with dissolve
    mar "Hola Beck."
    bec "Hey, Marissa..."
    bec "[pla_name] me estuvo contando en el camino..."
    bec "Sobre lo de que recibiste una carta de amor, y después de eso empezaste a ser acosada..."
    show marissa normal
    mar "Eh... así es..."
    show beck pensando
    bec "Marissa, me hubieras pedido ayuda."
    bec "Puede ser peligroso lidiar con un acosador."
    mar "Lo sé..."
    mar "Pero por eso, es que pedí ayuda al club de detectives."
    mar "Sé por experiencia que ellos son discretos, además..."
    mar "Solo he pedido que identificaran al acosador."
    mar "Con las pruebas suficientes pediré ayuda a un maestro, incluso al director."
    bec "..."
    bec "No... incluso llegar a ese punto..."
    show beck preocupado
    bec "¿Y tienen a algún sospechoso?"
    "Las miradas de Marissa y Beck se dirigieron a mí, y luego pasaron a Alice, en busca de respuestas..."
    show beck sorprendido
    show marissa sorprendida
    pla "Eh... pues sí tenemos un sospechoso..."
    bec "¿¡En serio!?"
    bec "¿Quién es?"
    show beck preocupado
    show marissa normal
    pla "Preferiría no decirlo por ahora, no hasta tener información suficiente."
    pla "Y por eso es que te he llamado."
    show beck:
        ease .5 left
    show marissa:
        ease .5 center
    show alice pensando at right with dissolve
    ali "E- estoy de acuerdo con [pla_name]..."
    ali "Lo mejor, es no lanzar acusaciones si una base sólida..."
    ali "E- eso es lo que me enseñaron mis superiores..."
    bec "Uhm..."
    show alice normal
    bec "Bien... ¿y qué necesitan saber?"
    pla "Sobre tu experiencia."
    show beck sorprendido
    bec "¿Mi experiencia?"
    pla "Todos conocemos que eres alguien muy popular."
    pla "Una persona que constantemente está en compañía de otras personas..."
    pla "Creo que en este salón, tú eres el único quien tiene experiencia lidiando con acosadoras."
    show beck pensando
    bec "..."
    # bec "¡Ah, cierto!"
    bec "Con que yo soy el experto en ser acosado..."
    bec "No me gusta como suena..."
    show beck guino
    bec "Pero tienes razón."
    $quick_menu_gameplay=True
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    bec "Bien, es hora de que la voz de la experiencia hable."
    jump caso1_debate_rnd2