label caso1_debate_rnd6:
    stop music fadeout 1
    hide neil with dissolve
    hide beck with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    $ debate_args.append(1)## id del debate
    $ debate_args.append(6)## id de la ronda del debate
    $ debate_args.append(15)## cual id de frase es la correcta
    $ debate_args.append(3)## cual id de argumento es el correcto
    $ argumentos = ["Neil London (perfil)","Diagrama de correlación","Cancha en fin de semana","Prof. Harrow (perfil)","Papel y casillero","Tropiezo"]  
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r6:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    #0-neil 20-beck 50-marissa 60-alice

    scene bg salon club detectives:
        xpan 30
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil normal with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("Primero, recomiendo que...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r2f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.4,hard=True)

    $ frase_args.append(1)## el id de la frase (desde cero)
    $ frase_args.append("le den un nuevo vistazo a la carta.")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.2,hard=True)

    $ frase_args.append(2)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}Tal vez puede haber nuevas pistas ahí.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("neil")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice normal with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(3)## el id de la frase (desde cero)
    $ frase_args.append("{azul}Pero no hay nada más en la carta...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 50
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(4)## el id de la frase (desde cero)
    $ frase_args.append("Además, han dicho que {p}{amarillo}fue una persona zurda...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f4)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $ frase_args.append(5)## el id de la frase (desde cero)
    $ frase_args.append("Sino fue Neil, ¿quién escribió la carta?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f5)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 50
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show neil normal with fast_dissolve
    show screen debateCharPanel("neil")

    $ frase_args.append(6)## el id de la frase (desde cero)
    $ frase_args.append("Sería mejor...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f6)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(7)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}enfocarse en el contenido de la carta.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f7)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("neil")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 50
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(8)## el id de la frase (desde cero)
    $ frase_args.append("¿Qué podría haber{p}escondido en el {p}contenido?")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(9)## el id de la frase (desde cero)
    $ frase_args.append("{azul}¿Tal vez un código secreto?{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("marissa")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 20
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show beck serio with fast_dissolve
    show screen debateCharPanel("beck")

    $ frase_args.append(10)## el id de la frase (desde cero)
    $ frase_args.append("Viendo la forma en la que fue escrita...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f10)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2.5,hard=True)

    hide screen debateText1

    $ frase_args.append(11)## el id de la frase (desde cero)
    $ frase_args.append("Tal vez el autor {amarillo}es un poeta...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f8)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.5,hard=True)

    $ frase_args.append(12)## el id de la frase (desde cero)
    $ frase_args.append("Ya que no tiene un físico destacado...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r4f4)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    $ frase_args.append(13)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}Esa es su única manera{p} para ligar con chicas.{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f13)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("beck")##label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 20
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(14)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}Hay algo en la carta que no concuerda...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f1)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    $ frase_args.append(15)## el id de la frase (desde cero)
    $ frase_args.append("{azul}Es como si se tratara de otra persona...{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f2)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)

    show alice normal

    $ frase_args.append(16)## el id de la frase (desde cero)
    $ frase_args.append("{azul}¿Neil no es el acosador?{/azul}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r0f0)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2.7,hard=True)

    show alice pensando

    $ frase_args.append(17)## el id de la frase (desde cero)
    $ frase_args.append("{amarillo}Todo es tan confuso...{/amarillo}")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r6f5)## qué animacion usar
    $ frase_args.append(True)## si es clickeable (True o False)
    $ frase_args.append("alice")##label de char para resp incorrecta, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    hide alice with dissolve
    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "Tal como dijo Neil, debería leerme de nuevo la carta y {amarillo}entender mejor el contenido{/amarillo} de esta."
    "No quiero confiar en él, pero si dice que hay algo más en la carta... ¡Debo confirmarlo!"
    jump inicio_d1r6