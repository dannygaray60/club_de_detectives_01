label caso1_investigacion3:
    $estadoj="Libre"
    play music ambiente2 fadein 4
    scene bg escuela corredor with dissolve
    show alice normal with dissolve
    ali "..."
    pla "¿Estás lista?"
    pla "Aprovecharemos esta hora de receso para buscar a nuestro {amarillo}sospechoso...{/amarillo}"
    show alice pensando
    ali "..."
    ali "Estoy algo nerviosa..."
    ali "Creo que no seré de mucha ayuda otra vez..."
    pla "Descuida..."
    pla "Haces lo mejor que puedes, no te preocupes."
    show alice sonrojada
    ali "..."
    pla "En fin, solo debemos no alertarlo..."
    ali "Tienes razón..."
    ali "Bien, andando."
    hide alice with dissolve
    $renpy.choice_for_skipping()
    "Alice y yo fuimos recorriendo la escuela, en busca del estudiante llamado Neil..."
    "Después de algunos minutos..."

    ## cada elemento es el sprite de un personaje
    $ chars=["images/chars/unk1.png","images/chars/claire/normal.png","images/chars/unk2.png","images/chars/neil/normal.png","images/chars/jane/normal.png"]
    ## cada elemento define a qué etiqueta saltar cuando se selecciona el personaje de la lista anterior
    $ chars_labels=["elec_unk1","elec_alice_resp","elec_unk2","elec_neil","elec_alice_resp"]

    label quien_es_neil:
        show screen btnHelpTextBox("¿Quién es Neil London?")
        $ quick_menu_bajo=True
        ## llamamos pantalla de seleccion
        call screen char_select(chars,chars_labels) with dissolve
        
        label elec_alice_resp:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show alice enojada with dissolve
            ali "¿Es una broma, [pla_name]?"
            $updateStat("intel","-",1)
            $renpy.notify("Inteligencia -1")
            pla "Eh... lo siento."
            hide alice with dissolve
            jump quien_es_neil

        label elec_neil:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            $updateStat("intel","+",1)
            $renpy.notify("Inteligencia +1")
            jump eleccion_de_neil_correcta

        label elec_unk1:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show unk1 with dissolve
            pla "Hola, disculpa..."
            pla "¿Eres Neil London?"
            unk "¿Eh? No..."
            hide unk1 with dissolve
            show alice pensando with dissolve
            ali "¿Qué te hizo pensar que él era Neil London?"
            $updateStat("intel","-",1)
            $renpy.notify("Inteligencia -1")
            pla "Ah, no... nada. Mi error..."
            hide alice with dissolve
            jump quien_es_neil

        label elec_unk2:
            hide screen char_select
            pause 1.8
            $ hide_select_chars()
            hide screen btnHelpTextBox
            $ quick_menu_bajo=False
            show unk2 with dissolve
            pla "Hola, disculpa..."
            pla "¿Eres Neil London?"
            unk "¿Eh? No..."
            hide unk2 with dissolve
            show alice pensando with dissolve
            ali "¿Qué te hizo pensar que él era Neil London?"
            $updateStat("intel","-",1)
            $renpy.notify("Inteligencia -1")
            pla "Ah, no... nada. Mi error..."
            hide alice with dissolve
            jump quien_es_neil
        
    label eleccion_de_neil_correcta:
        show neil normal with dissolve
        pla "Hola... ¿eres Neil London?"
        show neil pensativo
        unk "..."

        #agregamos thumb a perfil de neil
        $lstNotepad_thumb[ lstNotepad_titulo.index("Neil London (perfil)") ]="neil"

        nei "Sí... yo soy."
        show neil serio
        nei "¿Te conozco de algún lado?"
        pla "Eh... no."
        pla "Yo soy [pla_name], y ella es Alice."
        show neil:
            ease .5 mleft
        show alice pensando at mright with dissolve
        ali "Ho- hola..."
        show neil sorprendido
        nei "¿Qué quieren?"
        "Neil ahora se mostró a la defensiva."
        pla "Solo venimos a hacerte algunas preguntas."
        show neil pensativo
        # nei "¿Quienes son ustedes?"
        nei "¿¡He hecho algo malo!?" with hpunch
        pla "¡Ah, no! No es nada en serio..."
        "Rayos, ya se ha puesto alerta..."
        show neil serio
        nei "Uh..."
        nei "Creo que tengo que irme."
        show alice sorprendida
        pla "¡E- espera!" with hpunch
        show neil preocupado hablando
        nei "¿Qué?"
        nei "No pueden obligarme a nada."
        show alice normal
        ali "..."
        show alice pensando
        ali "[pla_name]... ¿deberíamos decirle?"
        "Alice detrás de mí, me sujetó de la chaqueta a la vez que me susurraba."
        pla "..."
        "No hay de otra..."
        show alice normal
        pla "Eh, Neil, verás..."
        play sound campana
        pla "{amarillo}Alice y yo somos del club de detectives.{/amarillo}" with flashbulb
        pla "Y necesitamos que nos contestes algunas preguntas..."
        show neil sorprendido
        # pla "Eso es todo."
        # nei "..."
        nei "¿De- detectives?"
        show neil serio hablando
        nei "Uhm... me cuesta creerlo..."
        show alice pensando at decaer
        ali "..."
        ali "Si tan solo fueramos reconocidos como un verdadero club..."
        hide neil with dissolve
        show alice:
            parallel:
                ease .5 center
            parallel:
                reponerse
        pla "¿Qué pasa, Alice?"
        show alice normal
        ali "Si fueramos reconocidos como un club, tendríamos algunas ventajas..."
        ali "Como poder obligar a un estudiante que conteste nuestras preguntas..."
        ali "Siempre y cuando sea relacionado con el caso en investigación."
        pla "Vaya..."
        pla " Qué loco..."
        "De todas formas, no tenemos esa ventaja..."
        show alice:
            ease .5 mright
        show neil serio at mleft with dissolve
        pla "Hey, Neil... en serio necesitamos que nos contestes..."
        pla "Solo son algunas preguntas, no tardaremos mucho."
        nei "..."
        extend " ..."
        extend " ..."
        "Ah... no tiene caso..."
        show neil serio hablando
        nei "Si quieren saber algo por mi parte..."
        stop music fadeout 3
        nei "Podría hablar,{nw}"
        play sound campana
        show alice sorprendida
        extend " {amarillo}pero con una condición...{/amarillo}" with flashbulb
        ali "..."
        show alice pensando
        ali "Está bien..."
        ali "¿Cuánto hay que pagar?"
        show neil sorprendido
        nei "¿Eh?"
        nei "No, no estoy pidiendo dinero..."
        show alice normal
        pla "¿Entonces?"
        show neil sonriendo hablando
        play sound campana
        nei "{amarillo}Un acertijo.{/amarillo}" with flashbulb
        pla "..."
        extend " ¿eh?"
        show neil normal
        show alice sorprendida
        ali "¿Un acertijo?"
        show alice normal
        nei "Sí, la condición es: {amarillo}que ustedes resuelvan un acertijo...{/amarillo}"
        nei "Si logran resolverlo, {amarillo}pueden preguntarme lo que necesitan saber.{/amarillo}"
        show neil sonriendo hablando
        nei "De lo contrario..."
        nei "Si ustedes fallan cinco veces..."
        play sound campana
        nei "Mis labios estarán sellados." with flashbulb
        show neil normal
        pla "Pero qué..."
        show neil sonriendo hablando
        nei "¿Qué pasa?"
        nei "{amarillo}Un acertijo no debe ser ningún problema para los detectives{/amarillo} je, je, je..."
        show neil normal
        ali "Uno de mis superiores era un fanático de los acertijos..."
        show alice pensando
        ali "Lástima que ya se graduó."
        "..."
        extend " Un acertijo..."
        show alice enojada
        ali "¡Lo- lo haremos!" with hpunch
        pla "¿¡Eh!? ¿¡Estás segura, Alice!?"
        ali "No tenemos de otra, hay que jugar su juego..."
        ali " ¡Y demostrarle que de verdad somos del club de detectives!" with hpunch
        show neil sonriendo hablando
        nei "Jee... esa es la actitud."
        nei "Muy bien..."
        play sound campana
        nei "Es hora de jugar." with flashbulb
        hide alice with dissolve
        hide neil with dissolve

        $quick_menu_gameplay=True

        $estadoj="Acertijo"
        # $acertijo1_txt="Los ratones son famosos por su capacidad para multiplicarse a velocidades de vértigo.{p}{p}El tipo de ratón que tenemos aquí pare 12 bebés una vez al mes. Las crías de ratón, a su vez, pueden tener sus propias crías dos meses después de haber nacido.{p}{p}Has comprado una ratoncita en una tienda de mascotas y te lo has llevado a casa el mismo día que ha nacido. ¿Cuántos ratones tendrás dentro de 10 meses?"
        $acertijo1_txt="Los conejos pueden tener entre 4 y 12 crías por cada camada. Como pueden tener varias camadas en el año, el número de crías puede ascender hasta 80 en este tiempo.{p}{p}Considerando estos datos, si compras un conejo hembra en una tienda de mascotas y te lo llevas a tu casa, ¿cuántos conejos tendrías dentro de tres años?"
        $showMinigameTitle(estadoj)
        play music tiempo_muerto2 fadein 2
        $initCorazones()
        show screen corazones

        $numpad_cifra="0000"
        label puzzle_conejos1:
            scene bg conejos1base with slow_dissolve
            show conejos1:
                alpha 0
                ypos 0.2
                xpos 0.370
                linear 0.8 alpha 1
            $quick_menu_bajo=True
            call screen numpad("puzzle_conejos1_resp",acertijo1_txt) with dissolve

        label puzzle_conejos1_gameover:
            stop music fadeout 3
            hide screen corazones
            $quick_menu_bajo=False
            scene bg escuela corredor
            show neil serio with dissolve
            nei "Qué decepción..."
            show neil serio hablando
            nei "Ya les he dado suficiente oportunidades y no han acertado con la respuesta."
            nei "Lo siento, pero tengo que irme."
            pla "¿¡Eh!? ¡Espera!" with hpunch
            hide neil with dissolve
            # "Sin hacerme caso, Neil se fue..."
            "Ah, he fallado..."
            jump caso1_gameover

        label puzzle_conejos1_resp:
            $quick_menu_bajo=False
            scene bg escuela corredor
            if numpad_cifra !="0001":
                show neil serio with dissolve
                nei "¿Esa es tu respuesta?"
                show neil serio hablando
                nei "Ah... qué decepción..."
                $restCorazones()
                if cantidad_corazones==0:
                    jump puzzle_conejos1_gameover
                else:
                    "Agghhh... ¿¡entonces cuál es la respuesta!?" with hpunch
                    if cantidad_corazones==1:
                        show neil sonriendo hablando
                        nei "Jee... ahora {amarillo}solo te queda una oportunidad...{/amarillo} piensa con cuidado lo que vas a contestar..."
                    else:
                        show neil normal
                        nei "Jum... ahora {amarillo}te quedan [cantidad_corazones] oportunidades.{/amarillo}"
                        nei "Veamos si esta vez no te equivocas..."
                    hide neil with dissolve
                menu:
                    "Pedir ayuda a Alice":
                        $updateStat("intel","-",1)
                        $renpy.notify("Inteligencia -1")
                        show alice normal with dissolve
                        pla "Alice... ¿tienes alguna idea de cuál es la respuesta?"
                        show alice pensando
                        ali "Uhmm... no..."
                        show alice normal
                        play sound campana
                        ali "Pero... hay algo que recordé." with flashbulb
                        ali "Uno de mis superiores, que era aficionado a los acertijos, me había dicho que a veces no hay que pensarlo demasiado."
                        pla "¿Eh? ¿Qué significa eso?"
                        ali "Pues... hay una clase de {amarillo}acertijos que son tramposos.{/amarillo}"
                        pla "¿Un acertijo tramposo?"
                        ali "Sí. Antes de resolver un acertijo, es buena idea ver si este no tiene {amarillo}alguna trampa en su enunciado...{/amarillo}"
                        ali "A veces, {amarillo}la respuesta es tan obvia que no la tomamos en cuenta.{/amarillo}"
                        "Para esconder un árbol, lo mejor es un bosque, ¿eh?"
                        show alice pensando at decaer
                        ali "Aunque no sé si la respuesta a este acertijo es obvia... Perdón por no poder ayudarte."
                        pla "No, tranquila, saber eso me ayudará."
                        hide alice with dissolve
                        "Tengo que intentarlo de nuevo..."
                        "¡Esta vez sí leeré con detenimiento ese acertijo!"
                    "Intentar de nuevo":
                        "Debo leer con más calma las pistas del acertijo..."
                jump puzzle_conejos1
            else:

                $fase_titulo.append("Acertijo -Conejos-")
                $fase_tipo_vida.append("cantidad")
                $fase_corazones.append(cantidad_corazones)
                $fase_multiplicador.append(10)

                $quick_menu_gameplay=False
                stop music fadeout 3
                hide screen corazones
                show neil normal with dissolve
                pla "La respuesta es...{nw}"
                play sound campana
                extend " {amarillo}¡Solo un conejo!{/amarillo}" with flashbulb
                show neil sonriendo hablando
                nei "Jee... Correcto."

        ##agregamos puntos de intelgencia, en base a la cantidad de corazones restantes
        $updateStat("intel","+",cantidad_corazones)
        $renpy.notify("Inteligencia +"+str(cantidad_corazones))

        show neil:
            ease .5 mleft

        ## agregamos un elogio si no se ha perdido ningun corazon
        if cantidad_corazones==5:
            show alice sorprendida at mright with dissolve
            ali "¡Wow, [pla_name]!"
            ali "¡Lo has resuelto en un solo intento!" 
            $updateStat("carisma","+",2)
            $renpy.notify("Carisma +2")
            show alice alegre at brinquitos
            ali "¡Eres increíble!"
            show alice sonriendo
        else:
            show alice normal at mright with dissolve

        nei "Je, je, je... encontraron {amarillo}la trampa del acertijo.{/amarillo} Era obvio que no tendrías más conejos sino hay un macho cerca je, je..."
        show neil normal
        nei "Bien, soy un hombre de palabra..."
        nei "¿Qué necesitan saber?"
        pla "Cuéntanos acerca del viernes de la semana pasada..."
        show neil pensativo
        nei "..."
        nei "¿El viernes... de la semana pasada?"
        nei "¿Por qué ese día?"
        pla "No podemos contarte acerca del caso..."
        pla "Pero ese día... hubo un tropiezo entre una estudiante y la profesora Harrow."
        nei "... la profesora Harrow y una estudiante..."
        show neil sorprendido
        nei "Oh... eso..."
        show neil normal
        nei "Entiendo."
        nei "Veamos... por dónde comienzo..."
        hide alice with dissolve
        hide neil with dissolve
        jump caso1_testimonio5
