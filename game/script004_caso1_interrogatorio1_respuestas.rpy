label int1f0:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Así que la carta no se te entregó directamente?"
    mar "Así parece..."
    mar "Después de que las clases terminaran, {amarillo}revisé mi bolso y ahí estaba la carta.{/amarillo}"
    if not fraseInterr[0]:
        $addNote("Carta de amor","La carta ya estaba en el bolso de Marissa el día viernes, ¿cómo pudo llegar hasta ahí?{p}{p}La carta es la siguiente:{p}{p}\"Señorita Mar... Le escribo esta carta para expresar el gran amor que siento por usted [...]{p}{p}Desde el primer día que la conocí, me enamoré como un tonto soñador. [...] Me encanta que usted sea tan inteligente y muy responsable con lo que hace.{p}{p}Siendo la persona tan recta y madura que es usted, espero que venga a...\"{p}{p}Después de esto se menciona que la destinataria está invitada a ir al café que queda cerca de la escuela a las cinco de la tarde de ese mismo día.{p}{p}Se me hace extraño que esta carta sea tan formal...","carta",True)
    show marissa:
        ease .4 mleft
    show alice normal at mright with dissolve
    ali "Qué extraño..."
    ali "{amarillo}¿Cómo llegó esa carta a tu bolso?{/amarillo}"
    show marissa apenada
    mar "Ni idea..."
    pla "Habría que ver en qué momento metieron la carta en tu bolso {amarillo}sin que te dieras cuenta...{/amarillo}"
    show marissa normal
    mar "Uhm... eso estará difícil."
    mar "No suelo separarme de mi bolso, ya que ahí llevo mi celular."
    show alice sorprendida
    ali "¿Llevas tu celular en el bolso?"
    show marissa alegre hablando
    mar "Por supuesto, solo mira..."
    show alice normal
    #mostrar celular
    mar "¡La pantalla es enorme! Obviamente no me cabe en el bolsillo de la falda."
    pla "¿Así que {amarillo}no te separas de tu bolso{/amarillo} en todo el día?"
    mar "Yo diría que sí..."
    show marissa preocupada
    mar "No recuerdo que el viernes me haya separado de mi bolso en ningún momento."
    show marissa alegre
    mar "Lo tengo muy vigilado."
    # if not fraseInterr[0]:
    #     $addNote("El bolso de Marissa","Marissa asegura no haberse despegado de su bolso el viernes cuando encontró la carta.")
    show marissa alegre hablando
    mar "Después de lo que pasó con mi hermana, me he vuelto más cautelosa je, je, je."
    pla "Ya veo..."
    ##una variable bandera
    $fraseInterr[0]=True
    hide alice with dissolve
    hide marissa with dissolve
    jump caso1_testimonio1_inicio

label int1f1:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "El café que queda cerca de la escuela, ¿no? ¿Llegaste a la hora acordada?"
    show marissa enojada
    mar "Eso es lo que acabo de decir."
    mar "Normalmente no soy una persona puntual..."
    mar "Pero considerando la situación, estuve muy pendiente del reloj."
    mar "¿Acaso era necesario preguntarme eso?"
    $restCorazones()
    pla "Eh... creo que no..." with hpunch
    jump caso1_testimonio1_inicio

label int1f2:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    # if not fraseInterr[2]:
    #     $addCorazones()
    pla "¿Cuánto tiempo esperaste en el café?"
    show marissa preocupada sudor
    mar "Uhm... creo que {amarillo}media hora...{/amarillo}"
    pla "Así que podemos descartar que esa persona haya llegado tarde..."
    show marissa:
        ease .5 mleft
    show alice normal at mright with dissolve
    ali "¿Y si se trató de una broma?"
    pla "¿Una broma?"
    show marissa apenada
    mar "Entonces esto sería una de muy mal gusto..."
    show marissa normal
    mar "Pero no lo creo, {amarillo}mis amigos no son de los que dan bromas...{/amarillo}"
    pla "¿Pero qué tal si la persona que te envió esa carta {amarillo}es alguien al que no le caigas bien?{/amarillo}"
    show alice sorprendida
    ali "Oh... ¡Un enemigo!"
    pla "Yo no le diría así tampoco..."
    show marissa preocupada
    mar "Uhm... podría ser..."
    mar "{amarillo}Aunque no conozco a nadie con el que haya tenido problemas.{/amarillo}"
    show alice normal
    ali "..."
    play sound campana
    ali "{amarillo}¿Tal vez esa persona se arrepintió de la carta?{/amarillo}" with flashbulb
    pla "¿A qué te refieres, Alice?"
    ali "Estaba pensando... Si alguien estaba {amarillo}tan enamorado{/amarillo}, hasta el punto de escribir una carta de amor..."
    ali "Eso quiere decir que {amarillo}no tuvo el valor de decírselo en persona...{/amarillo}"
    ali "Además, {amarillo}no escribió su nombre...{/amarillo} Creo que eso fue por que tal vez no estaba seguro de ir a la cafetería."
    mar "..."
    show alice sorprendida
    pla "..."
    ali "¿Q- qué? ¿Dije algo extraño?"
    pla "No... es que..."
    play sound campana
    pla "Podrías estar en lo correcto." with flashbulb
    ali "¿¡Eeeh!?" with hpunch
    show alice alegre at brinquitos
    ali "Eh... ju, ju, ju..."
    "Alice soltó una pequeña risa en tono triunfal, y de repente..."
    show alice enojada
    ali "¡Oye! ¡Tampoco es para sorprenderse!" with hpunch
    show alice normal
    show marissa preocupada
    mar "Pero... si eso fuera así..."
    mar "¿Por qué llegar hasta el punto de acosarme?"
    ali "... cierto..."
    # pla "Tal vez realmente esa persona esté algo mal de la cabeza, pero también está enamorada de ti..."
    if not fraseInterr[2]:
        $addNote("Perfil del sospechoso","Podría ser alguien que es muy inseguro, y que demuestre estar locamente enamorado de Marissa. Aunque este nerviosismo quizás se deba únicamente por estar enamorado...")
    show marissa apenada
    mar "Uh... qué miedo... menos mal que{nw}"
    play sound campana
    extend " {amarillo}Beck estaba cerca...{/amarillo}" with flashbulb
    pla "¿Beck?"
    show marissa alegre hablando
    mar "Ah, es un amigo, estudia en el mismo salón que yo."
    "Uhm... un amigo..."
    hide marissa with dissolve
    hide alice with dissolve
    $fraseInterr[2]=True
    jump caso1_testimonio1_inicio

label int1f3:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A donde te fuiste?" 
    show marissa normal
    mar "A mi casa."
    mar "Había cumplido con los deberes del club y tenía tarea pendiente."
    mar "Así que {amarillo}no salí de mi casa por el resto del día.{/amarillo}"
    pla "¿Y no has recibido alguna llamada o mensaje extraño?"
    mar "Nope."
    show marissa enojada
    mar "Si hubiera recibido aunque sea un mensaje extraño, obvio que les hubiera contado."
    hide marissa with dissolve
    show alice enojada with dissolve
    ali "No sigas, [pla_name]."
    ali "No hay pistas para sacar de esa información."
    $restCorazones()
    ali "¡Hay que hacer las preguntas correctas!" with hpunch
    pla "S- sí..."
    hide alice with dissolve
    jump caso1_testimonio1_inicio

label int1f4:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "Espera, Marissa..."
    pla "Es mejor que también nos cuentes lo que pasó ese día..."
    show marissa sorprendida
    mar "¿¡Eh!? Pe- pero tal vez solo era ideas mías... no creo que sea importante..."
    pla "Si es importante o no para el caso, eso lo decidiremos nosotros."
    show marissa:
        ease .5 mleft
    show alice alegre at mright with dissolve
    ali "¡Bien dicho, [pla_name]!"
    ali "¡Mis superiores siempre me decían que cualquier pista es importante, {amarillo}aunque parezca irrelevante!{/amarillo}"
    ali "Un buen detective luego sabrá cuales pistas descartar."
    mar "E- entiendo..."
    show alice normal with slow_dissolve
    show marissa normal
    mar "Bueno..."
    mar "Como he dicho, {amarillo}el sábado fui a la escuela, por actividades del club.{/amarillo}"
    play sound campana
    mar "Entonces, al ir a mi casillero noté que {amarillo}la cerradura tenía varios añarazos...{/amarillo}" with flashbulb
    pla "¿Arañazos?"
    show alice sorprendida at brinquitos
    ali "¡Oh, ya sé! {amarillo}¡Tal vez alguien quería forzar la cerradura!{/amarillo}"
    pla "Eso parece obvio..."
    pla "La cuestión sería, {amarillo}cuándo sucedieron aquellos arañazos{/amarillo}."
    ali "¿Uh?"
    show alice normal
    pla "Marissa, ¿esos arañazos tú los hiciste?"
    mar "No creo... Eran arañazos demasiado evidentes..."
    # mar "Puede que sí sean arañazos por mi culpa, o puede que no..."
    # mar "No estoy segura."
    pla "{amarillo}¿El sábado fue la primera vez que viste esos arañazos?{/amarillo}"
    mar "Eh... sí..."
    pla "¿A qué hora los viste?"
    mar "Desde que llegué a la escuela a las {amarillo}tres de la tarde{/amarillo}, no revisé mi casillero hasta irme..."
    mar "{amarillo}Salí de la escuela a las cinco.{/amarillo}"
    if not fraseInterr[4]:
        $ addNote("Arañazos en el casillero","Marissa afirmó haber visto arañazos en su casillero desde el sábado de la semana pasada a las cinco de la tarde. Esto podría darnos alguna pista acerca de cuándo estuvo el acosador en la escuela.")
    pla "Entiendo... Puedes continuar."
    hide marissa with dissolve
    hide alice with dissolve
    $fraseInterr[4]=True
    jump caso1_testimonio1_inicio

label int1f5:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿A parte de eso?"
    show marissa enojada
    $restCorazones()
    mar "A eso voy, ¡no me interrumpas!" with hpunch
    pla "Pe- perdón..."
    jump caso1_testimonio1_inicio

label int1f6:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Podrías contarnos acerca de ese día?"
    show marissa apenada
    mar "¿Por qué?"
    mar "Fue un día aburrido y no salí de mi casa."
    hide marissa with dissolve
    show alice enojada with dissolve
    $restCorazones()
    ali "¡[pla_name]! ¡No interrumpas a cada rato a Marissa!" with hpunch
    ali "¡Concéntrate en hacer las preguntas correctas!" with hpunch
    pla "Pe- perdón... Marissa, puedes continuar."
    hide alice with dissolve
    show marissa normal with dissolve
    mar "Claro..."
    jump caso1_testimonio1_inicio

label int1f7:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "Entonces fue el lunes cuando comenzó de verdad el acoso..."
    pla "¿Qué te hizo pensar que comenzaste a ser acosada?"
    mar "No sabría ponerlo en palabras..."
    mar "Es como un sexto sentido..."
    "No creo que un sexto sentido nos ayude..."
    "Debería dejar que Marissa siga hablando."
    jump caso1_testimonio1_inicio

label int1f8:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    pla "¿Y qué me dices acerca del club?"
    show marissa sorprendida
    mar "¿Eh? ¿A qué te refieres con eso?"
    pla "Has dicho que ese sentimiento de estar siendo observada..."
    pla "Lo has experimentado en {amarillo}el salón de clases, los corredores e incluso afuera de la escuela...{/amarillo}"
    pla "¿Pero también eso pasa en el salón de tu club? Ya que no lo mencionaste..."
    show marissa:
        ease .5 mleft
    show alice alegre at mright with dissolve
    ali "¡Oh! ¡Esa es una buena pregunta, [pla_name]!"
    show marissa preocupada
    mar "Ahora que lo mencionas..."
    play sound campana
    mar "En el salón del club {amarillo}es el único lugar donde puedo sentirme segura.{/amarillo}" with flashbulb
    if not fraseInterr[8]:
        $addNote("Sensación de ser observada","Marissa declaró que se siente observada (por el posible acosador) en varios lugares de la escuela, a exepción del salón del club... ¿por qué no mencionó el club?{p}{p}Ella dijo que el salón es el único lugar donde puede sentirse segura.")
    pla "Interesante..."
    hide marissa with dissolve
    hide alice with dissolve
    # ali "¿Eso es algo importante, [pla_name]?"
    # ali "Mis superiores me habían enseñado que un buen detective no debe ser influenciado por corazonadas."
    # pla "Lo sé, pero no está de más anotarlo."
    # ali "Ya..."
    $fraseInterr[8]=True
    jump caso1_testimonio1_inicio

label int1f9:
    hide screen interrogatorio_btns
    $showplay_excl("espera")
    show marissa:
        ease .5 mleft
    show alice sorprendida at mright with dissolve
    ali "¿¡U- una sombra!?" with hpunch
    pla "¿Cómo que una sombra? Sé más específica."
    show marissa apenada
    mar "Uh... Eso quisiera yo..."
    mar "La verdad, es la única forma que encontré para describirlo..."
    show marissa preocupada
    mar "Es que fue tan rápido, sé que era la silueta de una persona."
    mar "Pero cuando me di la vuelta, esa persona se escondió muy rápido."
    mar "No pude identificar el rostro, ni su cabello... nada."
    show alice normal
    show marissa apenada at decaer
    mar "Perdón por no poder ayudar con más información..."
    pla "Descuida."
    if not fraseInterr[9]:
        $addNote("Sombra misteriosa","Marissa dijo que se topó con la silueta de una persona que rápidamente se escondió, posiblemente se trate del acosador. ¿Qué le impidió a Marissa haber identificado a esa persona?")
    ali "Eso es demasiado raro..."
    $fraseInterr[9]=True
    # if not fraseInterr[9]:
    #     $addNote("Resumen del caso","Resumen, sombra misteriosa. hechos principales")
    hide marissa with dissolve
    hide alice with dissolve
    jump caso1_testimonio1_inicio


label int1_gameover:
    hide screen interrogatorio_btns
    $hide_gameplay_layout()
    stop music fadeout 1.0
    hide alice
    hide marissa
    show marissa normal
    mar "Uhm... creo que ha sido un error venir a pedirles ayuda."
    mar "Lo- lo siento... Mejor iré a hablar con algún maestro."
    show marissa apenada
    mar "Gracias de todas formas..."
    jump caso1_gameover
