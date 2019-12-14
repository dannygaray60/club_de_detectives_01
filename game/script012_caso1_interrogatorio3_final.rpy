label caso1_interrogatorio3_final:

    $fase_titulo.append("Interrogatorio de Beck")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(10)

    stop music fadeout 5
    # pla     necestio preguntarte algo

    # bec     jum... que cosa?

    # menu:
    # Sobre el castigo de Marissa
    # -menos inteligencia
    # Sobre lo que pasó despues
    # -menos inteligencia
    # Sobre el chico
    # --correcto
    show beck sonriendo
    show alice normal
    bec "Lo siento por eso, pero ya lo tengo claro..."
    bec "Ese día sí tuvimos un tiempo libre, pero fue antes de que nos tocara Matemáticas."
    bec "Así como dices, {amarillo}yo estuve en el salón de maestros.{/amarillo}"
    bec "Después la profesora Harrow se fue al salón."
    bec "Yo en cambio tardé un poco más, ya que algunas chicas llegaron para hablar conmigo."
    show beck pensando
    bec "Creo que tardé como tres o cinco minutos para llegar al salón."
    show beck guino
    bec "Fui corriendo... ya sabes, no hay que hacer enojar a la profesora Harrow..."
    show beck preocupado
    bec "Pero al llegar... {amarillo}la encontré en el suelo, junto a Marissa recogiendo algunos papeles.{/amarillo}"
    show beck pensando
    bec "Ahora que lo recuerdo..."
    play sound campana
    extend " {amarillo}había un chico que no era de nuestra sección.{/amarillo}" with flashbulb
    show beck serio
    bec "Cuando llegué, ya habían recogido la mayoría de papeles."
    bec "Al parecer, ese chico estuvo ayudándolas."
    bec "Y la profesora Harrow no perdió tiempo para castigar a Marissa."
    bec "Yo me enteré de todos los detalles de lo que pasó, después de que mandaran a Marissa a la biblioteca."
    "Bien, es hora de preguntarle lo que necesito saber..."
    $addintel=True
    label saber_mas_de_chico_o_castigo:
        show beck sonriendo
        show alice normal
        menu:
            "Sobre el castigo de Marissa":
                pla "¿Qué clase de castigo recibió Marissa?"
                show beck sorprendido
                bec "Eh... bueno... si no me equivoco, la mandaron a resolver cien ejercicios de álgebra en la biblioteca."
                show alice pensando
                ali "Eso debió ser terrible..."
                show beck preocupado
                bec "Ni que lo digas... yo apenas aguanto resolviendo unos cuatro o menos... Al menos trato de resolverlos..."
                # -menos inteligencia
                $addintel=False
                jump saber_mas_de_chico_o_castigo
            "Después del tropiezo...":
                pla "Después de que Marissa se tropezó con la profesora Harrow..."
                pla "Ellas recogieron las cosas que se les había caído..."
                pla "Y la profesora Harrow después no tardó en castigar a Marissa..."
                pla "¿Qué pasó después de eso?"
                show beck pensando
                bec "No mucho... recibimos clases de matemáticas como si nada hubiera pasado."
                bec "Marissa llegó hasta después de que la profesora Harrow se fue del salón."
                pla "Entiendo..."
                # -menos inteligencia
                $addintel=False
                jump saber_mas_de_chico_o_castigo
            "Sobre el chico":
                if addintel:
                    $updateStat("intel","+",1)
                    $renpy.notify("Inteligencia +1")
                $addintel=False
                play sound campana
                "Eso era a lo que quería llegar..." with flashbulb
                pla "Hey, Beck, ¿conoces a ese chico?"
                show beck pensando
                bec "Uh... no. {amarillo}No lo conozco para nada...{/amarillo}"
                pla "¿Podrías describirnos a esta persona?"
                bec "Solo sé que era alguien que se miraba muy delgado y pálido..."
                show beck guino
                bec "Algo así como un cerebrito, de esos que son muy malos en los deportes ja, ja, ja."
                pla "Oh... entiendo..."
                show alice pensando
                ali "[pla_name]... Pregúntale si no notó nada raro con ese chico..."
                pla "Ehm... bueno..."
                pla "Beck, ¿y notaste algo fuera de lugar con esa persona que llegó a ayudar?"
                show beck pensando
                bec "..."
                show beck sorprendido
                show alice sorprendida
                play sound campana
                bec "¡Ah!" with flashbulb
                pla "¿Has recordado algo?"
                show beck pensando
                show alice normal
                bec "Creo..."
                "Beck miró a los lados, como asegurándose de que nadie lo escuchara a parte de nosotros."
                show beck preocupado
                bec "No sé si eran ideas mías..."
                play sound campana
                bec "{amarillo}Pero ese chico no dejaba de ver a Marissa.{/amarillo}" with flashbulb
                bec "Estaba como embobado viéndola..."
                $updateNote("Neil London (perfil)",ndesc="\n\nSegún lo que ha dicho Beck, Neil parecía \"embobado\" viendo a Marissa.",add=True)
                pla "¿¡Ehh!?"
                show alice pensando
                ali "Uhm... habrá que investigar más sobre ese chico."
                pla "Eso parece..."

    hide alice with dissolve
    show beck sonriendo:
        ease .5 center
    bec "Bien, creo que ya he contestado muchas preguntas..."
    stop music fadeout 5
    bec "Déjame ahora hacerte una..."
    show beck serio
    bec "El caso que ustedes están investigando... ¿tiene que ver con Marissa?"
    # pla "..."
    pla "Eh... sí..."
    show beck sorprendido
    bec "¿Y qué le pasó a ella?"
    pla "No puedo decirte nada más..."
    show beck pensando
    bec "Uh... ella no ha dicho nada..."
    bec "Pero, sabes..."
    show beck serio
    bec "No estaré tranquilo si uno de mis amigos está en problemas..."
    bec "Mira, si necesitas ayuda en algo, solo dímelo."
    bec "¿Te parece bien si intercambiamos números?"
    pla "Uh, claro..."
    show beck sonriendo
    bec "¡Genial!"
    bec "Bueno, creo que ya tengo que irme."
    show beck guino
    bec "Suerte con la investigación je, je, je."
    hide beck with dissolve
    "Dicho esto, después de intercambiar números, Beck se fue de buen humor."
    if pla_stat["carisma"]>1:
        show alice alegre with dissolve
        ali "Oh... [pla_name], te viste genial."
        ali "¡¡¡Ya pareces todo un detective!!!"
        pla "Eh... tampoco es para tanto..."
        # "Vaya, me dejado llevar en esta investigación..."
        "Qué bien se siente ser halagado..."
        pla "Aunque hubiera sido más rápido contar con tu ayuda..."
        show alice sonrojada at decaer
        ali "Eh... lo siento..."
        pla "Descuida, ya obtuvimos varias pistas interesantes..."
        show alice sonriendo at reponerse
    else:
        show alice normal with dissolve
    ali "Y ahora, ¿qué hacemos?"
    pla "¿Que qué hacemos? Pues a descansar. Ya se ha hecho demasiado tarde."
    show alice pensando
    ali "Uh... Cierto..."
    show alice sonriendo
    ali "Al menos hemos avanzado bastante..."
    pla "Claro. Ya el lunes podremos buscar a ese tal Neil, y hacerle algunas preguntas."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=7
    $dia="Lun."
    $fecha="Febrero 24"
    $estadoj="Libre"
    $quick_menu=True
    window show
    jump caso1_investigacion2
