label caso1_debate_rnd0:
    stop music fadeout 1
    
    ##ocultamos quickmenu
    $ quick_menu_gameplay = True
    #cambiamos estado de juego
    $ estadoj="Debate"
    ## mostramos titulo
    $ showMinigameTitle(estadoj,2)

    ##inicializamos variables          
    $ initDebateVars()
    $ initCorazones()

    ## id del debate
    $ debate_args.append(1)
    ## ronda:
    #########
    ## id de la ronda del debate (desde cero)
    $ debate_args.append(0)
    ## cual id de frase es la correcta
    $ debate_args.append(10)
    ## cual id de argumento es el correcto
    $ debate_args.append(1)
    ## lista de argumentos
    $ argumentos = ["Neil London (perfil)","Perfil del sospechoso","Carta de amor","Sombra misteriosa"]  

    #establecemos temporizador en segundos
    $ show_gameplay_layout(600)

    play music debate


label inicio_d1r0:
    # $ keymapDebate()
    if cantidad_corazones==0 or timeup:
        jump d1_gameover

    $ frase_args=[]
    ## cambiamos el cursor a un apuntador personalizado
    $ change_cursor("target")
    ## mostramos argumentos
    show screen debateArgumento
    ## bajamos el quickmenu
    $ quick_menu_bajo=True 
    

    ## aqui comienzan a hablar los participantes

    ## movemos escenario
    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    ## pausamos el tiempo necesario hasta que el escenario deje de moverse
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    ## el id de la frase (desde cero)
    $ frase_args.append(0)
    ## la frase
    $ frase_args.append("Yo sugiero que...")
    ## el tipo (frase o murmullo)
    $ frase_args.append("frase")
    ## qué animacion usar
    $ frase_args.append(d1r0f0)
    ## si es clickeable (True o False)
    $ frase_args.append(False)
    ## label de char para resp incorrecta, nombre de char o False
    $ frase_args.append(False)
    ## mostramos la frase
    show screen debateText1(debate_args,frase_args)
    ## reiniciamos variable
    $ frase_args=[]

    $ renpy.pause(0.8,hard=True)

    ## el id de la frase
    $ frase_args.append(1)
    ## la frase
    $ frase_args.append("hay que establecer...")
    ## el tipo (frase o murmullo)
    $ frase_args.append("frase")
    ## qué animacion usar
    $ frase_args.append(d1r0f1)
    ## si es clickeable (True o False)
    $ frase_args.append(False)
    ## label de char para resp incorrecta, nombre de char o False
    $ frase_args.append(False)
    ## mostramos la frase
    show screen debateText2(debate_args,frase_args)
    ## reiniciamos variable
    $ frase_args=[]

    $ renpy.pause(2,hard=True)

    show alice normal

    ## el id de la frase
    $ frase_args.append(2)
    ## la frase
    $ frase_args.append("la {amarillo}personalidad del autor{/amarillo} de la carta.")
    ## el tipo (frase o murmullo)
    $ frase_args.append("frase")
    ## qué animacion usar
    $ frase_args.append(d1r0f2)
    ## si es clickeable (True o False)
    $ frase_args.append(False)
    ## label de char para resp incorrecta, nombre de char o False
    $ frase_args.append(False)
    ## mostramos la frase
    show screen debateText3(debate_args,frase_args)
    ## reiniciamos variable
    $ frase_args=[]

    $renpy.choice_for_skipping()
    ## tiempo en el que el personaje está hablando
    $ renpy.pause(3.8,hard=True)
    ## escondemos todas las frases (y/o murmullos)
    $ clearDebateText()
    ## escondemos personaje
    hide alice with fast_dissolve
    hide screen debateCharPanel

    ## movemos escenario
    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    ## pausamos el tiempo necesario hasta que el escenario deje de moverse
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(3) ## el id de la frase (desde cero)
    $ frase_args.append("¿La personalidad?") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f3) ## qué animacion usar
    $ frase_args.append(False) ## si es clickeable (True o False)
    $ frase_args.append(False) ## label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(4) ## el id de la frase (desde cero)
    $ frase_args.append("Uhm... pues {amarillo}parece un chico romántico.{/amarillo}") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f4) ## qué animacion usar
    $ frase_args.append(False) ## si es clickeable (True o False)
    $ frase_args.append(False) ## label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(4,hard=True)

    hide screen debateText1
    hide screen debateText2

    show marissa apenada

    $ frase_args.append(5) ## el id de la frase (desde cero)
    $ frase_args.append("Si tan solo me hubiera dado la carta...") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f5) ## qué animacion usar
    $ frase_args.append(False) ## si es clickeable (True o False)
    $ frase_args.append(False) ## label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(5,hard=True)

    hide screen debateText1
    hide screen debateCharPanel

    ## movemos escenario
    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    ## pausamos el tiempo necesario hasta que el escenario deje de moverse
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice normal with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(6) ## el id de la frase (desde cero)
    $ frase_args.append("Bueno, apartando el hecho del acoso...") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f6) ## qué animacion usar
    $ frase_args.append(False) ## si es clickeable (True o False)
    $ frase_args.append(False) ## label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    hide screen debateText1
    hide screen debateCharPanel

    ## movemos escenario
    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    ## pausamos el tiempo necesario hasta que el escenario deje de moverse
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(7) ## el id de la frase (desde cero)
    $ frase_args.append("En ese caso...") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f7) ## qué animacion usar
    $ frase_args.append(False) ## si es clickeable (True o False)
    $ frase_args.append(False) ## label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $ renpy.pause(2,hard=True)

    show marissa alegre hablando

    $ frase_args.append(8) ## el id de la frase (desde cero)
    $ frase_args.append("Tal vez sea un {azul}chico nervioso...{/azul}") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f8) ## qué animacion usar
    $ frase_args.append(True) ## si es clickeable (True o False)
    $ frase_args.append("marissa") ## label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(9) ## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}O inseguro de sí mismo...{/amarillo}") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f9) ## qué animacion usar
    $ frase_args.append(True) ## si es clickeable (True o False)
    $ frase_args.append("marissa") ## label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $renpy.choice_for_skipping()

    $ frase_args.append(10) ## el id de la frase (desde cero)
    $ frase_args.append("{azul}O un poco de los dos{/azul},{p}consecuencias de estar{p}enamorado supongo...") ## la frase
    $ frase_args.append("frase") ## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f10) ## qué animacion usar
    $ frase_args.append(True) ## si es clickeable (True o False)
    $ frase_args.append("marissa") ## label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args) ## mostramos la frase
    $ frase_args=[] ## reiniciamos variable

    $ renpy.pause(1,hard=True)

    show marissa alegre at brinquitos

    $ renpy.pause(3.3,hard=True)

    hide marissa with dissolve

    if cantidad_corazones==0 or timeup:
        jump d1_gameover
    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    $renpy.choice_for_skipping()
    hide screen debateArgumento
    hide screen debateArgs
    "La primera cosa a aclarar, es sobre la personalidad del autor de la carta..."
    "Debo revisar mis apuntes, y demostrar si Alice o Marissa {amarillo}se equivocaron en algo...{/amarillo}"
    "O si una de ellas {amarillo}ha dicho algo acertado.{/amarillo}"

    jump inicio_d1r0