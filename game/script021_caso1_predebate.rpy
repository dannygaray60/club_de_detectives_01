label caso1_predebate:
    "Al llegar al salón del club, me encontré con Alice, quien estaba sacando una pizarra acrílica."
    pla "¿Y esa pizarra?"
    show alice sonriendo with dissolve
    ali "Ah, [pla_name]. Te quería mostrar esto, en la hora de receso hice un{nw}"
    play sound campana
    extend " {amarillo}diagrama de correlación.{/amarillo}" with flashbulb
    pla "¿Un diagrama de correlación?"
    ali "Mira..."

    hide screen quick_menu
    $quick_menu=False
    window hide
    scene caso1_diagrama1 with dissolve
    pause 6
    $quick_menu=True
    window show

    pla "Oh... ¿eso tú lo dibujaste?"
    ali "Je, je."
    "Alice sonrió con orgullo al mostrarme su trabajo."
    "Si ella no estuviera en el club de detectives, no le iría mal en el club de arte..."
    pla "Uhm... Así que {amarillo}Neil no es conocido de Marissa o de Beck...{/amarillo}"
    pla "No está nada mal... aunque le falta algo..."

    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 1
    scene caso1_diagrama2 with dissolve
    pause 3
    $quick_menu=True
    window show

    ali "¿Eh?"
    ali "¿¡Beck está enamorado de la profesora Harrow!?" with hpunch 
    pla "Sí, ayer en la tarde me lo encontré, y descubrí eso..."
    pla "Claro que no me lo dijo directamente, pero estaba claro que Beck tiene gustos {amarillo}peligrosos.{/amarillo}"
    $addNote("Diagrama de correlación","Un diagrama de correlación dibujado por Alice. No le quedó nada mal.{p}{p}En este se resume que Marissa y Beck son compañeros, Neil parece estar interesado en Marissa, Marissa y la profesora Harrow tropezaron afuera del salón de clases. Además, Beck seguramente está enamorado de la profesora Harrow.","diagrama",True)
    ali "Oh... no me imaginaba que a él le gustara a alguien así..."
    ali "Las chicas que lo siguen seguramente se decepcionarían al saber eso..."
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    ali "Al final llegamos..."
    show alice sonriendo
    ali "Estoy segura de que hoy daremos con la solución del caso."
    pla "Sí, eso espero..."
    show alice pensando
    ali "Es tan nostálgico... esta vez estaré en un debate, ahora sin mis superiores..."
    show alice asustada at temblor
    ali "Qué nervios."
    hide alice
    show alice sorprendida
    show sherinford pequeño at center with dissolve:
        ypos .200
        xoffset 10
    she "¡Pío, pío, pío!"
    ali "Sherinford..."
    show alice sonriendo
    ali "Gracias por animarme."
    pla "No hay por que estar nerviosa, ¿acaso no se han hecho muchos debates aquí?"
    show alice normal 
    ali "Claro que sí."
    show alice alegre
    ali "Mis superiores se veían geniales demostrando contradicciones, presentando pruebas o atrapando al culpable aquí mismo."
    show alice pensando
    ali "Y por eso, es que hasta se formaba algún escándalo o discusión..."
    pla "Me lo imagino..."
    show alice normal
    ali "Sí, menos mal que teníamos a algún profesor para mantener el orden."
    pla "Espero que ese no sea nuestro caso..."
    show alice:
        ease .5 mright
    show sherinford pequeño :
        ypos .200
        xoffset 10
        ease .5 xpos 0.650
    show marissa normal at mleft with dissolve
    pause .6
    show marissa alegre hablando at brinquitos
    mar "¡Hooola!"
    show marissa alegre
    mar "¿He llegado puntual, no?"
    pla "Ah, hola Marissa."
    stop music fadeout 2
    pla "Bien, creo que con nosotros tres, podemos comenzar."
    ali "Así es."
    hide sherinford with dissolve
    show alice sonriendo
    ali "Quedate aquí, Sherinford, sé un buen chico."
    play music tiempo_muerto fadein 3
    show marissa normal
    mar "¿Y qué vamos a hacer exactamente?"
    show alice normal
    ali "Veamos..."
    ali "Lo primero, sería tener claro un resumen de los hechos."
    ali "Mis superiores siempre decían que hay que tener bases sólidas para resolver un caso."
    # ali "¿[pla_name]?"
    # pla "Sí..."
    "Con que un resumen... Solo por si acaso, {amarillo}debería darle una ojeada a mis apuntes...{/amarillo}"
    $quick_menu_gameplay=True
    ali "Bien [pla_name]. Lo primero es..."

    label predebate1_preg1:

        ali "¿Quién es nuestro cliente?"

        menu:
            "Alice Baskerville":
                show alice enojada
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                ali "¿Estás bromeando?" with hpunch
                ali "[pla_name], te lo preguntaré de nuevo..."
                jump predebate1_preg1
            "Marissa Doran":
                show marissa normal
                mar "Ehm... ¿Doran?"
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                ali "[pla_name], eres un olvidadizo..." with hpunch
                ali "¿Podrías al menos leer bien tus apuntes?"
                jump predebate1_preg1
            "Neil London":
                show alice enojada
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                ali "[pla_name], ese no es nuestro cliente." with hpunch
                ali "Una vez más..."
                jump predebate1_preg1
            "Marissa Morstan":
                pla "Pues obvio es {amarillo}Marissa Morstan.{/amarillo}"
                show marissa alegre at brinquitos
                play sound campana
                mar "{amarillo}¡Din, din!{/amarillo} ¡Correcto!" with flashbulb
                show marissa normal
                mar "Pero... ¿era necesario preguntar esto?"
                $updateStat("intel","+",1)
                $renpy.notify("Inteligencia +1")
                show alice asustada at temblor
                ali "Eh- eh sí... ¡Si- siempre es bueno tener claro las cosas básicas!"
                hide alice
                show alice pensando at mright
                show marissa normal
                mar "Entiendo..."

    show alice sonriendo
    ali "Bien, [pla_name], siguiente pregunta..."

    label predebate1_preg2:

        ali "¿Cuál es el problema de nuestra cliente?"
        
        menu:
            "Encontrar el amor de su vida":
                show marissa alegre at brinquitos
                mar "Je, je, je."
                show marissa enojada
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                mar "[pla_name], puedes ser un bromista en otro momento." with hpunch
                pla "Pe- perdón..."
                jump predebate1_preg2
            "Tiene bajas calificaciones":
                show marissa enojada
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                mar "¿Así que el chico listo pretende también echarme en cara mis bajas calificaciones?" with hpunch
                pla "¡Ah! Pe- perdón..."
                jump predebate1_preg2
            "Está siendo acosada por un fan":
                show alice normal
                ali "Uhm... ¿qué pistas tenemos para deducir que el acosador es un fan de Marissa?"
                pla "Ehm... ninguna..."
                show alice enojada
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                ali "¿Entonces?" with hpunch
                ali "Vamos, te haré de nuevo la pregunta..."
                jump predebate1_preg2
            "Está siendo acosada por alguien":
                show alice alegre
                play sound campana
                $updateStat("intel","+",1)
                $renpy.notify("Inteligencia +1")
                ali "Exacto." with flashbulb
            "El horno de su club se ha dañado":
                show marissa sorprendida
                mar "Eh... bueno, sí, se ha dañado el horno de mi club..."
                show marissa normal
                mar "Pero no por eso he venido a pedirles ayuda."
                play sound golpe
                $updateStat("intel","-",1)
                $renpy.notify("Inteligencia -1")
                pla "Cierto, cierto..." with hpunch
                jump predebate1_preg2

    show alice pensando
    ali "Y ese acosador seguramente sea la misma persona que escribió la carta."
    show alice normal
    ali "Y nuestro trabajo consiste en {amarillo}descubrir la identidad de esa persona.{/amarillo}"
    show alice pensando
    ali "Ahora... es momento de comenzar el debate."
    show marissa alegre at brinquitos
    mar "Qué emoción je, je, je."
    stop music fadeout 1
    hide marissa with dissolve
    hide alice with dissolve
    $quick_menu_gameplay=False
    $ argumentos = ["Argumento #1","Argumento #2","Argumento #3"]
    tuto "Ahora, pasaremos al {amarillo}debate escolar.{/amarillo}"
    tuto "En este minijuego, los participantes estarán hablando uno por uno..."
    if renpy.variant("small"):
        tuto "Y lo que estén diciendo se mostrará como {amarillo}frases flotantes.{/amarillo} que puedes tocar."
    else:
        tuto "Y lo que estén diciendo se mostrará como {amarillo}frases flotantes {/amarillo} a las que puedes {amarillo}disparar.{/amarillo}"
    show screen debateArgumento
    tuto "A la derecha tendrás un {amarillo}botón de argumento.{/amarillo}"
    tuto "Si lo tocas, se desplegará una serie de argumentos que puedes intercambiar."
    hide screen debateArgumento
    tuto "Las frases de los participantes tendrán {amarillo}palabras resaltadas{/amarillo} en amarillo o azul."
    tuto "Si una frase está resaltada en {amarillo}amarillo{/amarillo}, eso quiere decir que puedes {amarillo}señalar una contradicción{/amarillo} con el argumento que tengas seleccionado."
    tuto "En cambio, si la frase está resaltada en {amarillo}azul{/amarillo}, entonces {amarillo}estarás reafirmando la frase.{/amarillo}"
    tuto "Si te equivocas al contradecir, o reafirmar, entonces perderás un corazón."
    tuto "Asegúrate de enfocarte en las frases que te parezcan importantes, ya que {amarillo}algunas te restarán segundos si las tocas{/amarillo}, así que ten cuidado."
    tuto "Si aciertas con la respuesta, {amarillo}recuperarás un corazón.{/amarillo}"
    tuto "Un debate consta de varias rondas, y tendrás que pasar a través de todas estas rondas, {amarillo}con los corazones que te queden.{/amarillo}"
    tuto "Buena suerte."

    jump caso1_debate_rnd0