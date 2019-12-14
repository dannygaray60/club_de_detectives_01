label caso1_debate_rnd1:
    stop music fadeout 1
    hide marissa with dissolve
    hide alice with dissolve
    

    $ quick_menu_gameplay = True
    $ estadoj="Debate"      
    $ initDebateVars()

    
    $ debate_args.append(1)## id del debate
    $ debate_args.append(1)## id de la ronda del debate
    $ debate_args.append(1)## cual id de frase es la correcta
    $ debate_args.append(3)## cual id de argumento es el correcto
    $ argumentos = ["Carta de amor","Papel y casillero","Beck Doran (perfil)","Perfil del sospechoso","Tropiezo"]  
    $ show_gameplay_layout(600)
    play music debate


label inicio_d1r1:
    if cantidad_corazones==0:
        jump d1_gameover

    $ frase_args=[]
    $ change_cursor("target")
    show screen debateArgumento
    $ quick_menu_bajo=True 
    
    ## aqui comienzan a hablar los participantes

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa normal with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(0)## el id de la frase (desde cero)
    $ frase_args.append("Mi pregunta es...")
    $ frase_args.append("frase")## el tipo (frase o murmullo)
    $ frase_args.append(d1r1f0)## qué animacion usar
    $ frase_args.append(False)## si es clickeable (True o False)
    $ frase_args.append(False)##label de char para resp incorrecta, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1.5,hard=True)

    $ frase_args.append(1)##el id de la frase
    $ frase_args.append("{azul}¿Hay otra pista acerca del autor?{/azul}")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f1)##qué animacion usar
    $ frase_args.append(True)##clickeable (True o False)
    $ frase_args.append("marissa")##si es clickeable, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice normal with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(2)##el id de la frase
    $ frase_args.append("¿Otra pista?")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f2)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    show alice pensando

    $ frase_args.append(3)##el id de la frase
    $ frase_args.append("{amarillo}Cre- creo que sí...{/amarillo}")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f3)##qué animacion usar
    $ frase_args.append(True)##clickeable (True o False)
    $ frase_args.append("alice")##si es clickeable, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 0
        linear 0.5 xpan 60
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show marissa alegre hablando with fast_dissolve
    show screen debateCharPanel("marissa")

    $ frase_args.append(4)##el id de la frase
    $ frase_args.append("¡Genial! ¿Y cuál es?")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f4)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(2,hard=True)

    hide screen debateText1

    $ frase_args.append(5)##el id de la frase
    $ frase_args.append("{azul}¿Hay un mensaje secreto en la carta?{/azul}")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f2)##qué animacion usar
    $ frase_args.append(True)##clickeable (True o False)
    $ frase_args.append("marissa")##si es clickeable, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1.8,hard=True)

    $ frase_args.append(6)##el id de la frase
    $ frase_args.append("{amarillo}¿Hay alguien con la misma letra?{/amarillo}")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r0f5)##qué animacion usar
    $ frase_args.append(True)##clickeable (True o False)
    $ frase_args.append("marissa")##si es clickeable, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(2,hard=True)

    show marissa at brinquitos

    $ frase_args.append(7)##el id de la frase
    $ frase_args.append("{azul}¿El nombre de esa persona sí estaba en la carta?{/azul}")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f7)##qué animacion usar
    $ frase_args.append(True)##clickeable (True o False)
    $ frase_args.append("marissa")##si es clickeable, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $renpy.choice_for_skipping()
    $ renpy.pause(3,hard=True)

    $clearDebateText()

    scene bg salon club detectives:
        xpan 60
        linear 0.5 xpan 0
    $ renpy.pause(0.5,hard=True)

    ## informacion del hablante
    show alice pensando with fast_dissolve
    show screen debateCharPanel("alice")

    $ frase_args.append(8)##el id de la frase
    $ frase_args.append("Eh...")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f8)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1,hard=True)

    $ frase_args.append(9)##el id de la frase
    $ frase_args.append("Ahm...")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f9)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText2(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1,hard=True)

    $ frase_args.append(10)##el id de la frase
    $ frase_args.append("Pues...")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f10)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText3(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1,hard=True)

    $ frase_args.append(11)##el id de la frase
    $ frase_args.append("Yo- este...")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f11)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText4(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(1.3,hard=True)
    $renpy.choice_for_skipping()
    hide screen debateText1
    hide screen debateText2
    hide screen debateText3
    hide screen debateText4

    show alice asustada

    $ frase_args.append(12)##el id de la frase
    $ frase_args.append("¡[pla_name]! ¡Ayuuuda!")
    $ frase_args.append("frase")##(frase o murmullo)
    $ frase_args.append(d1r1f12)##qué animacion usar
    $ frase_args.append(False)##clickeable (True o False)
    $ frase_args.append(False)##si es clickeable, nombre de char o False
    show screen debateText1(debate_args,frase_args)## mostramos la frase
    $ frase_args=[]## reiniciamos variable
    $ renpy.pause(3,hard=True)


    hide alice with dissolve
    $clearDebateText()
    $change_cursor()
    $ quick_menu_bajo=False
    hide screen debateArgumento
    hide screen debateArgs
    $renpy.choice_for_skipping()
    "Vaya, Marissa tiene muchas ideas..."
    "Pero sí hay algo más que descubrimos..."
    jump inicio_d1r1