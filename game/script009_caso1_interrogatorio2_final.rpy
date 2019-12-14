label caso1_iterrogatorio2_final:

    $fase_titulo.append("Interrogatorio de Prof. Harrow")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(10)

    stop music fadeout 2
    hide screen interrogatorio_btns
    $quick_menu_gameplay = False
    $hide_gameplay_layout()
    $estadoj="Libre"
    pla "Muchas gracias profesora Harrow."
    $addNote("Prof. Harrow (perfil)","Una persona estricta y muy responsable con su trabajo, así es la profesora Mary Harrow. Además, le gusta el orden y la eficiencia.{p}{p}Cuando se enoja, da mucho miedo. La conozco desde hace un buen tiempo ya que ella es una amiga de mi familia, por lo cual, me he acostumbrado a su mirada intimidadora.","mary")
    pla "Creo que eso era todo lo que necesitaba saber."
    show mary pensando
    mary "Entiendo."
    show mary hablando
    mary "Bien, te puedes retirar. Ahora tengo que hablar con Marissa..."
    show mary:
        ease .5 mleft
    show marissa apenada at mright with dissolve
    mar "Uuuaaaahh... Noooooo..." with hpunch
    "Pobre Marissa..."
    scene bg escuela edificio principal corredor with fade
    "Cada vez, esto se vuelve más confuso..."
    "Ahora, han aparecido nuevos detalles... y {amarillo}un sospechoso...{/amarillo}"
    "¿Podremos resolver este misterio?"
    if numero_alice_obtenido:
        "Por cierto..."
        "¿Cómo le habrá ido a Alice?"
        "No he tenido noticias suyas."
        "Le envié un mensaje diciéndole que encontré nuevas pistas sobre el caso, pero no me ha contestado..."
    "El receso no tardará en terminar..."
    "Después de clases iré al club."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=14
    $quick_menu=True
    window show
    scene bg escuela corredor clubes dia with dissolve
    pause 2
    "Para mi sorpresa, encontré el salón del club de detectives completamente cerrado."
    if numero_alice_obtenido:
        "Estuve golpeando la puerta, pero nadie ha respondido."
        "También le he marcado a Alice pero no ha contestado."
    "¿Donde podría estar?"
    show hatty sonriendo with dissolve
    pause 1
    "..."
    play music ambiente fadein 4
    hat "¿¡Ehh!? Tú eres..."
    hat "El chico de la otra vez."
    pla "Hola."
    show hatty alegre
    hat "¡Hey qué tal! ¿Qué haces frente al club de literatura?" with hpunch
    pla "¿Qué?"
    show hatty pensando
    hat "¿Qué pasa con esa cara de confusión?"
    pla "Ehm... Hatty, este es el club de detectives..."
    show hatty asustada
    hat "¿¡Eh!?" with hpunch
    hat "Me... he equivocado..."
    show hatty pensando at decaer
    hat "Donde puede estar..."
    show hatty at reponerse
    pla "¿Qué estás buscando? Si se puede saber..."
    hat "Estoy buscando a mi hermana..."
    hat "Me había dicho que iba al club de literatura a llenar un formulario..."
    "Uh..."
    hat "Ah... qué molestia, solo tengo que decirle que llegaré tarde a la casa..."
    "Hatty comenzó a murmurar para sí misma, mientras miraba su celular."
    hat "Justamente hoy también tuvo que{nw}"
    play sound campana
    extend " {amarillo}caerse la red de telefonía...{/amarillo}" with flashbulb 
    "¿Eh?"
    show hatty sonriendo
    hat "¿Qué pasa, [pla_name]?"

    menu:
        "\"No es nada\"":
            $updateStat("intel","-",1)
            $renpy.notify("Inteligencia -1")
            pla "No es nada."
            hat "Uhm... ya..."

        "\"¿La red de telefonía está caída?\"":
            $updateStat("intel","+",1)
            $renpy.notify("Inteligencia +1")
            pla "¿La red de telefonía está caída?"
            hat "Así es..."

    show hatty pensando
    hat "¿No te parece curioso?"
    play sound campana
    hat "{amarillo}El viernes de la semana pasada también estaba la red caída.{/amarillo}" with flashbulb
    pla "Con que el viernes de la semana pasada..."
    pla "Entonces, ¿no puedes llamar a tu hermana?"
    show hatty molesta
    hat "Sí... aunque suena el tono, las llamadas no conectan, tampoco sirve la red de internet, ni puedo enviar mensajes de texto..."
    pla "¿Entonces tampoco se podía llamar o enviar mensajes el viernes pasado?"
    hat "Sí... por eso es curioso, hoy también es viernes..."
    hat "Y el problema duró todo el día, seguramente hoy sea igual..."
    $addNote("Problemas en red de telefonía","El viernes de la semana pasada (cuando Marissa recibió la carta), y también el viernes 21, la red de telefonía se ha caído. Por lo tanto ha sido imposible llamar o enviar mensajes desde el celular en esos días.")
    pla "Ya veo... no me había dado cuenta."
    show hatty sonriendo
    hat "¿Eh? ¿Por qué estás apuntando eso?"
    pla "Ah, bueno... estoy en medio de una investigación..."
    hat "¿Una investigación?"

    # pla "¿Estás buscando a tu hermana?"
    # hat "Sí. Ella se unió al club de literatura, y pensé que este era el salón."
    # pla "Sí estás buscando ese club, está allá..."
    # "Le señalo a Hatty a donde tiene que ir."
    # hat "Oh, ya veo... gracias."
    # hat "..."
    # hat "Así que este es el club de detectives..."
    # hat "¿Qué pasa? ¿No hay nadie adentro?"
    # pla "Eso parece..."
    # hat "¿Y qué me cuentas del club?"
    # "¿Eh? Parece que ella está interesada en el club..."
    # pla "Uhm... bueno..."
    # pla "Estamos en medio de una investigación."
    # hat "Ooohhh..."

    hat "¿Y a quién estás investigando?"
    pla "No puedo decírtelo. Es información confidencial."
    show hatty molesta
    hat "Uhh..."
    extend " ahora estaré con la curiosidad."
    pla "Bueno, si estás deseosa de saberlo, siempre serás bienvenida al club."
    pla "Estamos en busca de nuevos miembros."
    hat "Eh..."
    show hatty alegre at brinquitos
    hat "Interesante. Lo tendré en cuenta. Je, je."
    show hatty pensando
    hat "..."
    hat "Hey... [pla_name]... me averguenza decirlo... pero..."
    hat "¿Dónde está el club de literatura?"
    "Vaya, su sentido de la orientación está terriblemente mal..."
    pla "Bueno, el club de literatura está en el primer salón de este corredor..."
    hat "Oh, me he pasado entonces..."
    show hatty alegre
    hat "Bueno, nos vemos [pla_name]."
    hide hatty with dissolve
    # "Y al final, Hatty se fue con los ánimos decaídos..."
    "Esa chica necesita tener un mapa todo el día..."
    # "..."
    "Uhm... qué debería hacer..."
    if numero_alice_obtenido:
        "Ya que Alice no me ha contestado, no tengo nada que hacer aquí..."
    "Todavía hay tiempo."
    "Y con lo que he descubierto hasta ahora..."
    play sound campana
    "Sería buena idea hablar con {amarillo}Beck Doran.{/amarillo}" with flashbulb
    "Si alguien sabe de acosadores, seguramente es él."
    $quick_menu_btn_notepad=False
    $addstate=True
    label beck_esta_en_club_de:
        "Si no me equivoco... Beck está en el club de..."
        menu:
            "Deportes":
                "No... está claro que es eso, pero de un deporte en específico..."
                $addstate=False
                jump beck_esta_en_club_de
            "Beisból":
                "No... ese no es..."
                $addstate=False
                jump beck_esta_en_club_de
            "Fútbol":
                if addstate:
                    $updateStat("intel","+",1)
                    $renpy.notify("Inteligencia +1")
                $quick_menu_btn_notepad=True
                "El club de fútbol..."

    "Entonces... seguramente a esta hora... Beck podría estar en la cancha de la escuela..."
    "Bien, vamos para allá..."
    stop music fadeout 5
    scene bg escuela campo deporte tarde with slow_dissolve
    "Al llegar a la cancha de la escuela, noté que había un partido en juego..."
    play music partido_futbol fadein 6
    "..."
    "¿¡Eh!?" with hpunch
    "Al examinar el lugar, vi que alguien se escondía detrás de un árbol."
    "Uh..."
    "Con pasos cautelosos, me acerqué a aquel árbol..."
    "Y la sorpresa fue..."
    stop music fadeout 2
    show alice sorprendida
    ali "¡...!" with hpunch
    pla "¿Alice?"
    ali "¡Aaaahh!" with hpunch
    play music ambiente3 fadein 3
    ali "¿[pla_name]? ¿Qu- qué haces aquí?"
    pla "Es lo que yo debería preguntar..."
    pla "¿Qué estás haciendo escondida aquí? Pareces una acosadora..."
    show alice asustada
    ali "¡Ah! ¡Cla- claro que no!" with hpunch
    ali "¡Estoy investigando!" with hpunch
    pla "¿Investigando qué?"
    show alice pensando
    ali "A todas estas personas..."
    show alice normal
    ali "Marissa había dicho que el sábado vino a la escuela, ¿no?"
    show alice pensando
    play sound campana
    ali "{amarillo}Pues ese día hubo un partido de fútbol.{/amarillo}" with flashbulb
    show alice normal
    pla "¿En serio? No tenía idea..."
    show alice pensando
    ali "Sí... recordé que uno de mis superiores era fánatico del fútbol, y había dicho que aquí juegan partidos de ligas escolares en los fines de semana."
    show alice normal
    ali "Así que pensé que el acosador posiblemente frecuente venir a la cancha..."
    $addNote("Cancha en fin de semana","En los fines de semana, se juegan partidos de ligas escolares en la escuela, eso es lo que me dijo Alice.")
    pla "..."
    pla "Nada mal..."
    ali "¿Y tú por qué viniste acá?"
    # pla "¿No has recibido mi mensaje? Te lo envié en la hora de receso."
    # ali "Uhm... no... no he recibido nada."
    # "Me lo imaginaba, entonces la red telefónica realmente está fallando..."
    pla "En mi caso, vine para tratar de hablar con un experto en acosadores."
    show alice sorprendida
    ali "¿¡Eh!?" with hpunch
    ali "¿Un experto en acosadores?"
    pla "¿Has visto a todas esas chicas entre el público?"
    unk "¡Eso, vamos! ¡Hay que ganar!"
    unk "¡Aaahh! ¡Beck! ¡Mete otro gol!"
    show alice normal
    ali "Uh... sí..."
    "A pesar de que esto parecía ser un partido de práctica, había varias chicas haciendo de porristas..."
    pla "Pues cuando fui al salón de Marissa, descubrí que uno de sus compañeros suele ser acosado por mujeres."
    show alice sorprendida
    ali "¿¡En serio!?" with hpunch
    pla "Sí, se llama Beck Doran... ese mismo que tiene la pelota..."
    pla "Pensé que sería buena idea hablar con él sobre el caso."
    ali "¿Estás seguro?"
    ali "Marissa no quería que muchas personas se enteraran de su problema..."
    pla "Lo sé... Pero creo que podemos tener más información si hablamos con él."
    show alice normal
    ali "Uh... bueno, está bien."
    "..."
    ali "..."
    show alice sorprendida
    pla "¿Piensas quedarte allí?"
    ali "Pues... sí..."
    pla "Déjame decirte que eso te hace ver muy sospechosa."
    pla "Vamos, veamos el partido un rato."
    ali "..."
    show alice sonrojada
    ali "... Está bien..."
    if not numero_alice_obtenido:
        pla "Oye, Alice... creo que deberíamos intercambiar números."
        show alice sorprendida
        ali "¿¡Eh!?"
        show alice sonrojada
        ali "La verdad... es que yo también estaba pensando en eso..."
        pla "Genial."
        "Alice y yo intecambiamos números."
        "Aunque la red de telefonía esté fallando hoy, siempre es bueno tener el número de tus compañeros."
    stop music fadeout 4
    scene bg negro with dissolve
    pause 1.4
    $hora=15
    scene bg escuela corredor afuera tarde with dissolve
    pause 1
    "Después de que el partido terminó, Alice y yo estuvimos muy atentos de a donde se dirigía Beck."
    "Esperamos el momento oportuno para hablar con él."
    "Beck había ya había salido de unos vestidores que quedaban cerca de la cancha."
    "Y cuando Beck ya no estaba cerca de nadie, fue entonces cuando nos acercamos."
    show beck serio with dissolve
    pause 1
    show beck sorprendido
    bec "¿Eh?"
    pla "Hola, Beck..."
    bec "Tú eres... el chico que estaba hablando con Marissa..."
    bec "¿Cómo te llamabas? Este..."
    pla "[pla_name]. Y esta chica que me está acompañando es Alice Baskerville."
    bec "¿Quién?"
    show alice pensando at right with dissolve
    "Vi que Alice estaba escondida detrás de mí."
    bec "¿Qué pasa? Parece que le doy miedo..."
    pla "Alice... vamos, deja de esconderte..."
    ali "Uh..."
    show beck:
        ease .5 mleft
    pause .5
    show alice:
        ease .5 mright
    ali "{size=25}H- hola...{/size}"
    show beck pensando
    bec "¿Entonces? ¿Qué querían?"
    show beck guino
    bec "No me digas... ¿te arrepentiste y ahora quieres unirte al club de fútbol?"
    pla "Eh... no. Ya tengo un club."
    play sound campana
    pla "Alice y yo somos del club de detectives." with flashbulb
    show beck sorprendido
    bec "¿¡Eeeeh!?" with hpunch
    bec "Pe- pero... ¿no estabas a punto de meterte en el club de Marissa?"
    pla "Era solo una excusa para investigar."
    bec "¿Investigar?"
    bec "¿Qu- qué están investigando?"
    pla "No podemos decírtelo. Es algo confidencial con quien pidió nuestra ayuda."
    hide alice with dissolve
    show beck pensando:
        ease .5 center
    bec "Uh... bueno, yo no me he metido en algún problema, así que adiós..."
    pla "¡Espera!" with hpunch
    pla "No es un caso que te involucra a ti. Pero podrías haber sido {amarillo}testigo de algo...{/amarillo}"
    show beck sorprendido
    bec "¿Eh?"
    pla "Queremos saber lo que pasó {amarillo}el viernes de la semana pasada.{/amarillo}"
    bec "¿El viernes?"
    pla "Solo necesito hacerte algunas preguntas, no será mucho tiempo."
    bec "..."
    show beck pensando
    bec "Bueno... ¿y qué quieren saber?"
    pla "Para empezar, ¿podrías relatarnos lo que pasó ese día?"
    bec "Uh... no me siento cómodo con esto..."
    show beck preocupado
    bec "¿Me meteré en problemas si digo algo indebido?"
    pla "Lo dudo... solo queremos saber más de ese día."
    show beck pensando
    bec "..."
    extend " está bien."
    pla "Muchas gracias."
    bec "Bien... veamos..."
    jump caso1_testimonio3