label caso1_inicio:

    $dia="Jue."
    $fecha="Febrero 20"
    $hora=16#4pm
    $quick_menu=True
    window show
    # pause 1
    scene bg salon club detectives with dissolve
    play music ambiente2 fadein 4
    "Ha pasado un día desde que entregamos los volantes..."
    "Y todavía no ha llegado nadie..."
    "Para matar el tiempo, me he dedicado a leer algunas novelas sobre detectives."
    "En este salón, hay algunas novelas interesantes..."
    show alice normal with dissolve
    pla "Uhm... ¿Entonces, {amarillo}el asesino es el mayordomo{/amarillo}?"
    "Después de haber llegado al clímax de la historia, le di a conocer mi conclusión a Alice."
    "Según ella, yo necesitaba{nw}"
    play sound campana
    extend " {amarillo}\"entrenamiento deductivo\"{/amarillo}." with flashbulb
    "Y Alice es quien me estaba enseñando..."
    show alice sonriendo
    ali "Ju, ju, ju... Es un error común pensar eso."
    pla "¿Un error? Pero si está claro que el mayordomo es el culpable..."
    show alice alegre
    ali "Esa era la intención del escritor."
    play sound campana
    ali "{amarillo}No hay que dejarse guiar por pistas falsas.{/amarillo}" with flashbulb
    show alice sonriendo
    pla "¿Pistas falsas?"
    ali "Sí, los autores de misterio {amarillo}suelen ser muy tramposos.{/amarillo}"
    ali "A las pistas verdaderas no se le dan demasiado enfásis en las historias..."
    ali "Y cuando menos te lo esperes..."

    scene bg alice_objection with dissolve
    show alice_objection with dissolve

    ali "¡El detective señala a la persona menos sospechosa!"

    pla "Eh... ¿Con que es así?"
    pla "Eso suena injusto..."
    ali "Bueno..."
    ali "Es que una historia de detectives en donde sepas quién es el culpable, se tornaría aburrida..."
    ali "Aunque pensándolo bien..."
    ali "La gracia de una novela de misterio, {amarillo}es el misterio en sí mismo{/amarillo}. No siempre es algo relevante saber quien es el culpable..."
    pla "Entiendo..."
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    pla "..."
    ali "Esto ha estado muy calmado..."
    pla "Sí, así es."
    ali "..."
    show alice pensando
    ali "No ha habido ningún delito..."
    pla "Tampoco hay que alegrarse porque ocurra uno."
    show alice normal
    ali "Pero... esto no es lo que quiero para el club..."
    ali "¿Crees que lo de los volantes no funcionó?"
    pla "Bueno, tampoco tenía muchas esperanzas en eso..."
    show alice sorprendida
    ali "¿¡Eeeehh!?" with hpunch
    pla "Solo mira..."
    show alice normal
    pla "Varios clubes tienen muchas actividades por ofrecer, sin tener que depender de nadie, como parece ser el caso aquí."
    pla "Este es un club demasiado pasivo..."
    pla "Creo que estamos al mismo nivel que el club de literatura en cuanto a popularidad."
    pla "No... quizás debajo de ellos todavía."
    show alice pensando
    ali "Ehh..."
    ali "Eso es decepcionante..."
    pla "Es lo que hay."
    pla "Tenemos que pensar en una actividad para el club..."
    pla "No sé... algo que tenga que ver con la temática... eso de las deducciones y cosas así..."
    ali "Uhm..."
    ali "Uhhmmmm..."
    show alice asustada
    ali "UHHHMMMM...."
    show alice sorprendida
    play sound campana
    ali "¡Ah! ¡Una {amarillo}{i}escape room{/i}!{/amarillo}" with flashbulb
    show alice normal
    pla "¿Escape room? ... Una sala de escape..."
    pla "¿Qué es eso?"
    ali "Es un juego, donde pones a un grupo de personas en una habitación o sala grande..."
    ali "Y solo podrán salir si resuelven los acertijos que se encuentran."
    pla "Oh, eso es interesante..."
    pla "Me recuerda a una película..."
    "Aunque esa película era gore..."
    ali "Aunque lo complicado, es la creación de los acertijos..."
    show alice pensando
    ali "Lo he intentado... pero no soy buena en crear uno que sea desafiante."
    pla "Uh, yo tampoco..."
    pla "Si tuvieramos a {amarillo}una persona a la que le gusten los acertijos...{/amarillo}"
    show alice pensando
    ali "Y si... {w=1}{nw}"
    show alice sorprendida
    pla "Denegado."
    pla "Ya te he dicho que no debemos cometer un delito y luego fingir resolverlo."
    ali "¡Wuuaah! ¡Me has leído la mente!" with hpunch
    pla "Eres tan fácil de entender..."
    show alice normal
    ali "..."
    ali "¡Oh!"
    ali "¿Y si solamente es un show?"
    ali "Podríamos dejar que los participantes resuelvan un crimen fingido, mientras nosotros les ayudamos con pistas."
    pla "Dene... oh... no es una mala idea..."
    show alice sonriendo
    ali "Je, je, je. ¿Verdad que sí?"
    pla "Pero hay un problema."
    pla "Si fuera un crimen fingido..."
    pla "Tendría que haber sospechosos, ¿no?"
    show alice normal
    ali "Sí. Eso es obvio."
    show alice sorprendida
    pla "¡Y también es obvio que solo somos dos personas!" with hpunch
    ali "..."
    show alice pensando
    ali "Ah..."
    ali "Necesitaríamos a más personas para hacerlo bien..."
    pla "Así es..."
    pla "Pero eso es mejor que nada... hay que hacer el esfuerzo."
    pla "No podemos quedarnos de brazos cruzados esperando que un caso nos caiga del cielo..."
    show alice normal
    unk "Disculpen... ¿hay alguien aquí?"
    pla "¿Eh?"
    hide alice
    show marissa normal with slow_dissolve
    "..."
    show marissa alegre
    mar "¡Ah! ¡[pla_name], aquí estás!"
    pla "¿¡Marissa!?"
    show marissa:
        linear .5 mleft
    show alice normal at mright with dissolve
    ali "¿La conoces, [pla_name]?"
    pla "Eh, sí... la conocí cuando fui al club de cocina..."
    show marissa normal
    mar "Hola... este... ¿Alice?"
    show alice sorprendida
    ali "¿¡Ah!?" with hpunch
    show marissa alegre hablando
    mar "Soy Marissa, ¿no te acuerdas? Creo que nos vimos aquí hace un año."
    mar "El club ayudó a mi hermana mayor por el caso de un robo..."
    show alice pensando
    ali "..."
    show alice sorprendida
    ali "¡Oh! ¡El caso del collar de oro!"
    show marissa alegre:
        mleft
        brinquitos
    mar "¡Sí, ese mismo!"
    "¿Un collar de oro? Vaya, eso debió ser algo serio..."
    pla "¿Y qué te trae por aquí, Marissa?"
    show alice normal
    show marissa preocupada
    mar "..."
    extend " ¿Puedo cerrar la puerta?"
    pla "¿Eh?"
    mar "Necesito ayuda de ustedes..."
    show alice alegre:
        mright
        brinquitos
    ali "Ah, ¡Un caso al fin!"
    mar "..."
    show alice pensando
    ali "Pe- perdón..."
    mar "Descuida..."
    mar "Entonces... ¿Puedo contar con ustedes?"
    stop music fadeout 5
    mar "Es algo delicado lo que voy a hablar..."
    mar "Y no quisiera que otras personas me escuchen..."
    "Alice y yo intercambiamos miradas, extrañados por la petición de Marissa."
    "Alice asintió con la cabeza, entonces me dirigí a la entrada para cerrar la puerta."
    ali "Pu- puedes sentarte aquí..."
    show marissa sonrojada
    mar "Gracias."
    pla "Entonces... ¿de qué querías hablar?"
    show marissa preocupada
    show alice normal
    mar "..."
    show marissa apenada
    mar "Bueno... es algo confuso... no sé por donde comenzar..."
    show marissa preocupada
    mar "..."
    mar "Ah... bien... lo que pasa,{nw}"
    play sound campana
    extend " es que {amarillo}recibí una carta{/amarillo}..." with flashbulb
    show alice sorprendida
    ali "¿U- una carta?"
    ali "¡Ah! ¿Es alguien que te está chantajeando?" with hpunch
    show marissa sorprendida
    mar "¿Eh?"
    mar "No, no..."
    show alice normal
    show marissa preocupada
    play sound campana
    mar "{amarillo}Es una carta de amor.{/amarillo}" with flashbulb
    ali "..."
    pla "..."
    extend " ¿una carta de amor?"
    play music ambiente2 fadein 10
    "De repente, sentí que toda la tensión en el aire se había desvanecido."
    show marissa preocupada
    mar "Sí. Una carta de amor que recibí {amarillo}el viernes de la semana pasada{/amarillo}."
    pla "¿Todavía hoy en día se siguen escribiendo cartas de amor?"
    mar "Así parece..."
    show alice pensando
    ali "Eh... solo eso..."
    "Alice sonó muy decepcionada."
    show marissa apenada
    mar "Por desgracia, no."
    "Marissa sacó una hoja de papel doblada y me lo entregó."
    mar "Esa es la carta..."
    scene carta_amor with dissolve
    "Alice se acercó a mi lado mientras yo comenzaba a leer la carta."

    #carta bla bla
    "{amarillo}\"Señorita Mar... Le escribo esta carta para expresar el gran amor que siento por usted [...]\"{/amarillo}"
    "{amarillo}\"Desde el primer día que la conocí, me enamoré como un tonto soñador. [...]\"{/amarillo}"
    "{amarillo}\"Me encanta que usted sea tan inteligente y muy responsable con lo que hace.\"{/amarillo}"
    "{amarillo}\"Siendo la persona tan recta y madura que es usted, espero que venga a...\"{/amarillo}"
    "Después de esto se menciona que la destinataria está invitada a ir al café que queda cerca de la escuela a las cinco de la tarde."
    "Y también hay muchas cursilerías que no vale la pena mencionar por ahora."

    scene bg salon club detectives with dissolve
    show marissa preocupada at mleft with dissolve
    show alice normal at mright with dissolve
    pla "..."
    pla "No soy ningún experto en el tema, pero..."
    pla "¿Qué tiene de malo esta carta?"
    "Aparte de que es demasiado cursi."
    mar "Eh... es sobre lo que pone al final..."
    show marissa apenada
    mar "Me citaba para al {i}café{/i} que queda cerca de la escuela."
    mar "Pero al llegar al lugar..."
    mar "No vi a nadie."
    mar "Quedé esperando bastante tiempo, y al final me fui."
    show alice sorprendida
    ali "¿Fu- fuiste plantada?"
    show marissa apenada at decaer
    mar "Eso parece..."
    show marissa at reponerse_rapido
    mar "Alguien que me escribió esa carta tan cursi, tuvo que dejarme plantada..."
    show marissa alegre
    mar "Bueno, tampoco es que me importara tanto, ya que pensaba rechazarlo..."
    ali "¡Wow! ¡Qué directa!" with hpunch
    mar "..."
    show alice normal
    show marissa apenada
    extend " Pero si eso se hubiera quedado hasta ahí, no estaría pidiendo ayuda ahora."
    show marissa preocupada
    mar "..."
    # extend " Quiero que descubran quién me escribió esa carta."
    # show alice sorprendida
    # ali "¿¡Eh!?" with hpunch
    # pla "Pero... ¿no dijiste que no te importaba?"
    # show alice normal
    # mar "Así es... pero..."
    mar "Desde que recibí esa carta..."
    stop music fadeout 5
    mar "Siento que ahora{nw}"
    play sound campana
    extend " {amarillo}alguien me está acosando.{/amarillo}" with flashbulb
    show alice sorprendida
    ali "¿¡Ehhh!? ¿¡Un acosador!?" with hpunch
    show marissa normal
    "Con que era eso..."
    play music tiempo_muerto fadein 5
    mar "Así que..."
    extend " Necesito que me ayuden a descubrir {nw}"
    play sound campana
    extend "{amarillo}quién fue la persona que me envió esa carta.{/amarillo}" with flashbulb
    mar "No he hablado de esto {amarillo}con nadie, ni con los maestros...{/amarillo}"
    mar "No quisiera que esto llegue a más, por eso les pido ayuda a ustedes."
    mar "Sé que este club puede manejar estos asuntos con mucha discresión."
    "Aunque ahora en este club solo estamos un par de novatos, y un pollo con gorra..."
    mar "¿Entonces? ¿Podrían ayudarme?"
    pla "Uh..."
    show alice alegre at brinquitos
    ali "¡Claro que sí! ¡Déjanos el caso a nosotros!"
    show alice normal
    pla "Espera..."
    pla "Marissa, ¿solo quieres saber quién te envió la carta?"
    show marissa alegre hablando
    mar "Sí. Al saber quién fue, podría hablar con un maestro para arreglar este problema debidamente."
    "Como quien dice, ella quiere evidencias sólidas para acusar a alguien."
    show marissa alegre
    mar "Ya sabes, las cosas se resuelven hablando."
    mar "O amenazarlos con alguien de mayor autoridad."
    # pla "..."
    pla "Entiendo..."
    show marissa alegre hablando at brinquitos 
    mar "¡Muchas gracias, sabía que podría contar con ustedes!"
    pla "..."
    hide marissa with slow_dissolve
    show alice normal:
        ease 1.5 center
    ali "... ¿qué pasa, [pla_name]?"
    pla "¿Y qué es lo que vamos a hacer ahora?"
    show alice sorprendida
    pla "Tú deberias tener algo de experiencia en esto..."
    show alice pensando
    ali "Eh... bueno, aunque no lo parezca, no soy popular con los chicos, así que no he recibido alguna carta de amor, o algo parecido..."
    show alice sorprendida
    pla "¡Eso no!" with hpunch
    pla "Me refiero, a lo que debemos hacer después de aceptar un caso."
    show alice alegre
    play sound campana
    ali "¡Ah! Eso, je, je... cierto..." with flashbulb
    ali "..."
    show alice normal
    extend " bien..."
    ali "Antes que todo, en una investigación es primordial tener un registro de las cosas que se descubren."
    show alice sonriendo
    ali "Espérame un momento..."
    hide alice with dissolve
    pause 1
    "Alice se fue de inmediato a buscar algo entre los cajones de una mesa."
    "..."
    show alice sonriendo with dissolve
    ali "Aquí tienes."
    play sound notify
    $renpy.notify("Has recibido un bloc de notas")
    $quick_menu_btn_notepad=True
    pause 1.2
    ali "{amarillo}Aquí puedes apuntar todas las pistas que vayas descubriendo...{/amarillo} o cualquier cosa que se te ocurra."
    if renpy.variant("pc"):
        show text "{font=gui/fonts/fontawesome.ttf}{size=70}{/size}{/font}":
            xpos 0.750 ypos 0.7
            alpha 0
            linear .8 alpha 1
            block:
                ease .5 yoffset -20
                ease .5 yoffset 0
                repeat 4
            linear .8 alpha 0
    "Alice me entregó un bloc de notas y un bolígrafo."
    if renpy.variant("pc"):
        hide text
    pla "Entiendo..."
    hide alice with slow_dissolve
    "Bueno... lo primero sería apuntar lo que sabemos hasta el momento..."
    tuto "Hola, esto es un{nw}"
    play sound campana
    extend " {amarillo}mensaje del tutorial.{/amarillo}" with flashbulb
    $ addNote("Marissa Morstan (perfil)","Marissa Morstan es miembro del club de cocina. Es una persona muy amable y sociable, además es quien nos ha pedido a Alice y a mí identificar a la persona que la está acosando, que también le había entregado una carta de amor.","marissa")
    tuto "Se te notificará cada vez que el bloc de notas {amarillo}se actualice.{/amarillo}"
    tuto "Puedes consultarlo en cualquier momento."
    tuto "Además, este bloc de notas se utilizará a la hora de realizar algún {amarillo}interrogatorio{/amarillo} o incluso en un {amarillo}debate escolar.{/amarillo}"
    # tuto "Incluso será de utilidad consultarlo cuando estés en medio de un {amarillo}debate escolar.{/amarillo}"
    tuto "Ya veremos las {amarillo}mecánicas de juego{/amarillo} más adelante."
    show alice normal with dissolve
    pla "Listo... ¿y qué sigue?"
    ali "Veamos..."
    ali "Ahora toca escuchar el {amarillo}testimonio{/amarillo} de nuestra \"cliente\" sobre como han sucedido los hechos, y realizar preguntas para {amarillo}obtener pistas.{/amarillo}"
    pla "Ya veo..."
    show alice:
        ease .5 mright
    show marissa preocupada at mleft with dissolve
    pla "Marissa, entonces puedes contarnos al detalle tu caso."
    show marissa alegre
    mar "Claro..."
    mar "Supongo que comenzaré a contarles desde el comienzo del día {amarillo}cuando recibí la carta.{/amarillo}"
    show marissa preocupada
    mar "Pero antes de eso..."
    show marissa apenada
    extend " quisiera beber algo de agua."
    show marissa alegre at brinquitos
    stop music fadeout 3
    mar "Siento que hablaré demasiado je, je, je..."
    pla "Claro..."
    # scene bg negro with slow_dissolve
    # stop music fadeout 3
    # pause 2

    jump caso1_testimonio1