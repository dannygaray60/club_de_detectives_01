label d1r5_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r5_incorrecto_neil:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show neil sonriendo hablando
    nei "[pla_name], me alegra saber que estás de mi parte..."
    show neil serio
    $restCorazones()
    nei "Pero ese argumento no me ayuda en nada." with hpunch
    jump inicio_d1r5

label d1r5_correcto:
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
    show beck serio:
        ease .5 mleft
    show neil serio at mright with dissolve
    pla "Neil, no tienes por qué mentir..."
    pla "Hay una prueba que demuestra que estás interesado en Marissa."
    pla "¿Recuerdas esto?"
    show neil pensativo
    nei "Es mi número de celular..."
    # nei "Eh... ¡Pero si me dijiste que ella estaba interesada en hablarme!"
    # nei "..."
    # nei "¡Ah!"
    show beck guino
    bec "¡Ja! ¡Tú lo has dicho! Ese es tu número de celular..."
    show beck pensando
    bec "..."
    show beck preocupado
    bec "No entiendo... ¿Y eso qué significa?"
    show beck:
        ease .5 center
    show neil:
        ease .5 right
    show marissa normal at left with dissolve
    mar "Yo tampoco... ¿qué tiene de especial ese número?"
    # pla "Es el número de Neil..."
    pla "Cuando estuve hablando con él, le mentí."
    pla "Le dije que estabas interesada en hablar con él, como agradecimiento por haberte ayudado."
    pla "Alice puede confirmarlo."
    hide beck with dissolve
    show alice pensando with dissolve
    ali "... sí... él mismo escribió su número en la libreta..."
    nei "..."
    show neil serio
    nei "Bien... no puedo negarlo..."
    show neil sonriendo hablando at brinquitos
    play sound campana
    nei "Me gusta Marissa." with flashbulb
    show alice sorprendida
    show marissa sorprendida
    ali "¡Lo ha dicho!" with hpunch
    mar "¿¡Eeeehh!?"
    mar "¿¡Yo- yo te gusto!?" with hpunch
    show neil normal
    nei "Sí... me enamoré a primera vista..."
    "Es tan cliché que hasta me cuesta creerlo."
    show neil pensativo
    nei "Pero no te he acosado en ningún momento, y tampoco he escrito ninguna carta."
    show neil serio hablando
    nei "Es más, {amarillo}ni siquiera sabía tu nombre{/amarillo} o de qué salón eras."
    show neil pensativo
    nei "Además, de que me culpen de algo así... solo por qué me gusta ella... Es exagerado."
    show neil normal
    nei "¿O es que {amarillo}tienen otra prueba{/amarillo} de que demuestre que yo sea el culpable?"
    show marissa normal
    "Una prueba más aparte del número que él escribió, veamos..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    "Cuando Neil escribió su número en mi libreta, descubrí algo sobre {amarillo}su forma de escribir...{/amarillo}"
    "Y eso, debe estar conectado con otra cosa en mi bloc de notas..."

    label neilpideotraprueba:
        if cantidad_corazones==0:
            hide screen corazones
            jump d1_gameover
        show screen corazones
        menu:
            "Neil London (perfil)":
                show neil serio
                nei "[pla_name], ¿y eso qué significa?"
                $restCorazones()
                pla "Eh, perdón... lo intentaré de nuevo" with hpunch
                jump neilpideotraprueba
            "Carta de amor":
                show neil serio
                nei "[pla_name], no entiendo a lo que quieres llegar con eso..."
                $restCorazones()
                pla "Eh, perdón... lo intentaré de nuevo" with hpunch
                jump neilpideotraprueba
            "Perfil del sospechoso":
                # $addCorazones()
                # pause 1
                hide screen corazones
                jump neilpideotraprueba_fin
            "Sombra misteriosa":
                show neil serio
                nei "[pla_name], ¿eso es lo mejor que puedes hacer?"
                $restCorazones()
                pla "Eh, perdón... lo intentaré de nuevo" with hpunch
                jump neilpideotraprueba

    label neilpideotraprueba_fin:            
        pla "Después de analizar la carta, Alice y yo concluimos que el autor es zurdo."
        pla "Y tú, al escribir tu número, vi que {amarillo}también eres zurdo.{/amarillo}"
        show neil pensativo
        nei "Eh... sí, soy zurdo, pero..."
        show neil normal
        nei "Sigue siendo flojo."
        nei "¿Esto es todo lo que tiene el club de detectives?"
        show alice enojada
        ali "¡N- no es cierto!" with hpunch
        ali "También sabemos que quien escribió la carta... es alguien que estaba nervioso{nw}"
        show alice pensando
        extend " y no es una persona segura de sí misma."
        play sound campana
        nei "Y claramente {amarillo}yo no soy esa persona.{/amarillo}" with flashbulb
        show alice sorprendida
        ali "¿Eh?"
        nei "Vamos, he admitido ante todos ustedes que de verdad me gusta Marissa."
        nei "No tengo necesidad de declararme por medio de una carta, ni que fuerámos niños de primaria."
        nei "Además, si quieren, pueden revisar mis cuadernos, y comparar mi caligrafía con la de la carta."
    scene bg negro with fade
    stop music fadeout 2
    "Con total confianza, Neil me mostró algunos de sus cuadernos."
    "Los comparé con la carta..."
    "Y al final, la caligrafía de Neil no se parecía en nada a la de la carta."
    "Hemos regresado al punto de inicio..."
    scene bg salon club detectives with fade
    show neil normal with dissolve
    nei "¿Qué pasa con esa cara larga, [pla_name]?"
    nei "¿Decepcionado de que yo no sea el culpable?"
    "Neil se mostró tan tranquilo al decir eso..."
    show neil pensativo
    nei "Vaya, esperaba algo más sólido para basar tu acusación..."
    nei "Creo que estoy perdiendo el tiempo aquí..."
    pla "E- espera, no te vayas todavía." with hpunch
    show neil normal
    nei "Uhm..."
    nei "[pla_name], ¿podrías mostrarme la carta por un momento?"
    pla "¿Eh?"
    "Algo confundido, hice lo que él me pidió."
    "No tardó demasiado y entonces comenzó a murmurar mientras recorría con la vista el salón del club."
    show neil sonriendo hablando
    nei "Je..."
    "Y sonrió con una pizca de malicia."
    "¿Qué está tramando?"
    nei "Creo que podría ayudarles a resolver el misterio..."
    show neil:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿¡En serio!?" with hpunch
    show alice normal
    pla "Ajá... dinos qué es lo que has pensado..."
    show neil normal
    nei "No tan rápido, puedo quedarme si tú, o tu compañera,{nw}"
    play sound campana
    extend " logran resolver {amarillo}otro acertijo.{/amarillo}" with flashbulb
    show alice sorprendida
    ali "¿Eh, otro?"
    show alice enojada
    ali "¡Vamos, [pla_name]! Si dijo que iba ayudar, hay que hacer que se quede y que nos diga qué ha descubierto."
    pla "E- está bien..."
    nei "Bueno, este acertijo se me ocurrió cuando yo estaba estudiando en la noche, y se fue la luz..."
    hide alice with dissolve
    hide neil with dissolve


    $estadoj="Acertijo"
    $acertijo1_txt="En la casa de Neil, se fue la luz en la noche mientras él estaba estudiando. Entonces Neil encendió diez velas para poder seguir estudiando.{p}{p}Una ráfaga de viento que entró por la ventana apagó tres velas.{p}{p}Al cabo de un rato, Neil se dio cuenta de que se apagó otra vela.{p}{p}Para asegurarse de que no se apague otra más, él cerró las ventanas de la habitación.{p}{p}Si damos por hecho de que el viento no apagó otra vela, ¿cuántas velas quedaron al final?"
    $showMinigameTitle(estadoj)
    play music tiempo_muerto2 fadein 2
    show screen corazones

    $numpad_cifra="0000"
    $addCarisma=True
    label puzzle_velas1:
        $quick_menu_bajo=True
        call screen numpad("puzzle_velas1_resp",acertijo1_txt) with dissolve

    label puzzle_velas1_gameover:
        stop music fadeout 3
        hide screen corazones
        $quick_menu_bajo=False
        scene bg salon club detectives with dissolve
        show neil serio with dissolve
        nei "Qué decepción..."
        show neil serio hablando
        nei "Ya les he dado suficiente oportunidades y no han acertado con la respuesta."
        nei "Lo siento, pero tengo que irme."
        jump caso1_gameover

    label puzzle_velas1_resp:
        $quick_menu_bajo=False
        scene bg salon club detectives with dissolve
        if numpad_cifra !="0004":
            show neil serio with dissolve
            nei "¿Esa es tu respuesta?"
            show neil serio hablando
            nei "Ah... qué decepción..."
            $restCorazones()
            if cantidad_corazones==0:
                jump puzzle_velas1_gameover
            else:
                "Agghhh... ¿¡entonces cuál es la respuesta!?" with hpunch
                hide neil with dissolve
                if cantidad_corazones<4 and addCarisma:
                    "Si me cuesta resolver este acertijo... Debería confíar en Alice, después de todo... {amarillo}ella es mi compañera{/amarillo}."
            menu:
                "Pedir ayuda a Alice":
                    if cantidad_corazones<4 and addCarisma:
                        $updateStat("carisma","+",3)
                        $renpy.notify("Carisma +3")
                        $addCarisma=False
                    show alice normal with dissolve
                    pla "Alice... ¿tienes alguna idea de cuál es la respuesta?"
                    ali "Uhm... no."
                    ali "Pero, creo que en ese tipo de acertijos, es mejor {amarillo}imaginárselos como si estuvieran ocurriendo de verdad.{/amarillo}"
                    pla "¿Qué significa eso?"
                    show alice pensando
                    ali "Por ejemplo... {amarillo}¿cómo terminaría una vela encendida?{/amarillo}"
                    ali "O cuál sería {amarillo}la diferencia con una vela que no está encendida.{/amarillo}"
                    ali "Además... esa pregunta al final, creo que ahí está el truco..."
                    pla "Uhm... {amarillo}la pregunta final...{/amarillo}"
                    "Se podría interpretar esa pregunta como... ¿cuántas velas quedaron? Si una vela encendida se deja sola... {amarillo}¿qué pasaría?{/amarillo}"
                    hide alice with dissolve
                "Intentar de nuevo":
                    pass
            jump puzzle_velas1
        else:
            stop music fadeout 3
            hide screen corazones
            show neil normal with dissolve
            pla "La respuesta es...{nw}"
            play sound campana
            extend " {amarillo}¡Cuatro velas!{/amarillo}" with flashbulb
            show neil sonriendo hablando
            nei "Jee... Correcto."
            show neil normal
            nei "Si dejamos que las velas sigan encendidas, se terminarán consumiendo y dejarían de existir."
            nei "Por lo tanto, {amarillo}solo las velas que fueron apagadas quedan al final.{/amarillo}"

    ##agregamos puntos de intelgencia, en base a la cantidad de corazones restantes (no, ya no)
    $updateStat("intel","+",2)
    $renpy.notify("Inteligencia +2")
    $estadoj="Debate"
    nei "Lo han hecho de nuevo..."
    show neil:
        ease .5 mleft
    show beck enojado at mright with dissolve
    bec "Oye, ¡déjate de tonterías!" with hpunch
    bec "Está claro que tú eres el acosador, ¡solo nos estás haciendo perder el tiempo!"
    show neil normal
    nei "Eh... estás equivocado."
    bec "¿Ah?"
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    nei "[pla_name], Alice... en un caso, es un grave problema tener {amarillo}solo a un sospechoso.{/amarillo}"
    pla "¿Eh? ¿Qué quieres decir con eso?"
    show neil sonriendo hablando
    nei "Je, je, je... ya lo verás..."

    jump caso1_debate_rnd6