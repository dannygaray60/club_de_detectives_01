label inicio:
    stop music fadeout 1
    hide screen quick_menu
    $quick_menu=False        

    "Antes de comenzar, ¿Quieres ponerle un nombre (masculino) a tu personaje?"

    menu:
        "Sí.":
            $inptname=True
        "No.":
            $inptname=False

    if inptname:
    
        window hide
        hide screen quick_menu
        $quick_menu=False

        scene bg salon club detectives with dissolve

        call screen TextBoxPopup("A continuación, escribe tu nombre y luego presiona \"enter\" en tu teclado.")
        
        label name_input:
            python:
                pla_name = renpy.input("Escribe tu nombre...",length=15)
                ## removemos espacios
                pla_name = pla_name.strip()
                ## la primera letra será mayuscula
                pla_name = pla_name.capitalize()
            ## comprobamos si el nombre es valido, codigo en functions.rpy
            $ quick_menu_bajo=False
            if not checkNamePlayer(pla_name):
                tuto "Incorrecto. No se permiten símbolos, números o nombres con menos de tres letras o más de quince."
                jump name_input

    else:
        #si fuera mujer el jugador, habria que cambiar algunas lineas de dialogo... pero que pereza
        #por ahora, john
        $pla_name = "John"

    # scene bg negro with dissolve
    # pause 3
    ## Febrero 11 (del 2019) martes
    $dia="Mar."
    $ hora=9
    $ fecha="Febrero 11"
    scene bg salon maestros dia with dissolve
    show mary normal with dissolve
    pause 0.5
    play music tema_principal fadein 3.0    
    $quick_menu=True
    mary "...and that's the way it is. With the new director in charge, some things will be different starting this year..."
    "I was in the teachers' lounge, on the second day of school."
    "And contrary to what one might think... No, I haven't gotten into trouble."
    "Resulta que {amarillo}no pude asistir al primer día de clases{/amarillo} por haberme enfermado."
    "Por lo tanto, me perdí de la ceremonia de apertura y del aviso sobre los nuevos reglamentos que se implementarán en la escuela."
    "En frente de mí, estaba la {amarillo}profesora Mary Harrow.{/amarillo} Conocida como {i}\"La doncella de los números\"{/i}."
    "Aunque yo más bien la llamaría {i}\"El infierno matemático hecho mujer\"{/i}."
    "Vaya, qué original soy..."
    show mary hablando
    mary "¿Me estás escuchando?"
    pla "¿E- eh? Ah, sí... fuerte y claro..." with hpunch
    show mary normal
    "¿¡De qué estaba hablando!?"
    "Decidí parar con mi monólogo interno, para no enojar a la profesora Harrow."
    "Nadie, absolutamente {amarillo}nadie desea verla enojada...{/amarillo}"
    mary "Apenas ha comenzado el año escolar, y tú llegas tarde..."
    "{i}*Corrección*{/i} Creo que sí estoy metido en un problema..."
    pla "Ah... Bu- bueno... yo... este..."
    "Mientras balbuceaba, buscando una justificación, la profesora continuó hablando."
    show mary hablando
    mary "Espero que esto no vaya a convertirse en un nuevo hábito tuyo."
    show mary normal
    pla "¡N- No! ¡Claro que no!"
    pla "¡Le prometo que no volverá a pasar!"
    mary "Ya estás en tu {amarillo}cuarto año de secundaria{/amarillo}, debes dar el ejemplo a los de años inferiores."
    mary "Es una falta de respeto hacia la institución llegar a la escuela sin una justificación."
    mary "Esto no debe repetirse, ¿entendido?"
    pla "¡Sí, señora!"
    mary "¿Perdón?"
    pla "¡Ah! Digo... entendido, profesora Harrow..."
    "Cuarto año..."
    "Ya solo me falta este año y el próximo para terminar la secundaria."
    "Claro, si logro tener notas que no bajen del promedio..."
    pla "¿Y cuáles son esos nuevos reglamentos de los que me estaba hablando?"
    "Comencé a cambiar de tema, antes de que la profesora también me reprochara las bajas calificaciones que obtuve el año pasado."
    mary "¿Ah?"
    mary "¿Ya lo olvidaste? Te lo acabo de explicar."
    " \"Es que no le presté atención\". Obviamente no diré eso..."
    pla "Sí, lo sé, pero quería asegurarme de que escuché claramente."
    show mary pensando
    mary "..."
    mary "Ah, bien..."
    show mary normal
    mary "A partir de este año, la escuela será más flexible en cuanto al uso del uniforme."
    mary "En otras palabras, {amarillo}no será obligatorio vestir el uniforme.{/amarillo} Aunque solo está permitido para los de primer ingreso."
    pla "Entiendo..."
    mary "Sin embargo, ahora {nw}"
    play sound campana
    extend "{amarillo}será obligatorio que los estudiantes pertenezcan a un club.{/amarillo}" with flashbulb
    pla "¿¡Eh!?" with hpunch
    pla "¿Que ahora será obligación pertencer a un club?"
    pla "¿Por qué?"
    show mary hablando
    mary "El nuevo director, al parecer es alguien que viene con {amarillo}nuevas ideas{/amarillo} para implementar en la educación."
    mary "Es una persona joven que, según sus palabras, busca hacer la educación algo \"más divertida\"."
    mary "Sé que eso no debe ser así... Pero esas son las reglas ahora."
    show mary normal
    pla "Espere..."
    pla "Entonces, ¿la educación no debe ser divertida?"
    show mary hablando
    mary "Así es, la educación es más bien un {amarillo}compromiso{/amarillo} del estudiante consigo mismo para forjarse un buen futuro."
    show mary normal
    mary "Los estudios no deben tomarse como un juego."
    "Se hace evidente que la profesora Harrow tiene un pensamiento algo {amarillo}antiguo{/amarillo} respecto a la educación."
    "No me extraña que sus clases de Matématicas fueran toda una tortura..."
    show mary pensando
    mary "Las actividades extraescolares solo pueden distraer al estudiante de sus verdaderos deberes..."
    "¿Acaso no se habían creado clubes en esta escuela para motivar al estudiante a asistir a clases?"
    "De repente recordé que una vez escuché, que desde la creación de distintos clubes, la asistencia escolar aumentó."
    "Y no he visto que eso sea algún problema para el rendimiento académico."
    "Solo mírenme, tengo notas regulares y no pertenezco a un club..."
    "Espera..."
    pla "Eso será un problema..."
    show mary normal
    mary "¿Uhm?"
    pla "Yo no estoy metido en un club..."
    "Y tampoco tengo el interés de unirme a uno."
    mary "Todas las personas que no estén integradas a un club, tienen un plazo de {amarillo}dos meses{/amarillo} para hacerlo."
    pla "¿Y si no me meto a un club?"
    mary "Eso significa quebrantar el reglamento, y ya debes saber cuales son las consecuencias."
    pla "Ah... entiendo..."
    "No me queda de otra..."
    extend " al final tendré que meterme a un club."
    show mary pensando
    mary "Bien, más o menos eso era lo que necesitabas saber."
    show mary normal
    mary "Tú quedaste en la sección {nw}"
    play sound campana
    extend "{amarillo}\"4-A\"{/amarillo}." with flashbulb
    mary "Ya te puedes ir. Las clases comenzarán dentro de media hora."
    pla "Está bien."
    "Me acomodé la mochila al hombro antes de irme, algo desanimado por esa nueva regla de pertenecer a un club..."
    show mary hablando
    mary "Ah, por cierto, {nw}"
    play sound campana
    extend "{amarillo}yo estaré a cargo de la sección 4-A{/amarillo}." with flashbulb
    pla "¿¡Eeeehhh!?" with hpunch
    "Lo que faltaba..."
    "La maestra más estricta de toda la escuela, la profesora Harrow, será la tutora de mi sección..."
    "Ya lo veo venir..."
    "Los estudios se volverán un verdadero infierno..."
    stop music fadeout 5.0
    hide screen quick_menu
    $quick_menu=False
    window hide
    scene bg negro with slow_dissolve
    pause 2
    $dia="Vie."
    $ hora=14
    $ fecha="Febrero 14"
    $quick_menu=True
    window show
    "{amarillo}- Algunos días después... -{/amarillo}"
    window show
    scene bg escuela corredor with dissolve
    pause 1
    "Al llegar el día viernes, es cuando de verdad empiezo a preocuparme por buscar un club."
    "En este momento son las dos en punto, que es cuando terminan las clases."
    "Por lo tanto, aprovecharé este tiempo libre para ir a visitar algunos clubes, y ver si alguno me llama la atención."
    scene bg negro
    show sepia
    show bg salon clases club dia behind sepia 
    play sound flash
    show claire timida behind sepia with flashbulb
    pause 1
    "Primero fui al club de literatura."
    "En ese lugar noté que sus miembros son muy callados, o más bien... ¿algo tímidos?"
    "{amarillo}La presidenta del club{/amarillo}, Claire Bellamy, me explicó las actividades que realizaban..."
    "Y a decir verdad, se me hicieron algo aburridas..."
    scene bg negro
    show sepia
    show bg salon cocina dia behind sepia 
    play sound flash
    show marissa alegre hablando behind sepia with flashbulb
    pause 1
    "En el club de cocina, las cosas fueron diferentes."
    "Había un ambiente más ameno en ese club."
    "La mayoría de los integrantes en ese club eran mujeres."
    "Una de ellas, {amarillo}Marissa Morstan{/amarillo}, me comentó alegremente de las actividades en el club."
    "Al mismo tiempo que la escuchaba, yo disfutaba comiendo algunos pastelillos que me ofrecieron, como una muestra de sus talentos."
    "Eran realmente deliciosos."
    "Al salir del salón, me fui con una buena impresión de ese club, aunque..."
    "Todavía seguía sin convencerme..."
    scene bg negro
    show sepia
    show bg salon musica dia behind sepia 
    play sound flash
    show jane normal behind sepia with flashbulb
    pause 1
    "En el club de música, las cosas estuvieron algo ruidosas."
    "Sus integrantes eran muy conversadores y algo excéntricos, a exepción de una chica."
    "Se presentó como {amarillo}Jane Stoner{/amarillo}."
    "Y solamente dijo su nombre..."
    "A todas mis preguntas, ella me daba una respuesta de una sola palabra."
    "Y si era posible, me contestaba con algun gesto de cabeza."
    "Además, su mirada y tono de voz me hacía creer que todo le era ajeno a ella."
    "De todas formas, de lo poco que tiene de habilidad en comunicarse, le sobra en habilidad para la guitarra."
    "En fin, era un club alegre y ruidoso, aunque sus gustos musicales no iban acorde a los míos..."
    scene bg negro with dissolve
    "Estuve vagando por el edificio de clubes..."
    "Pero al final, seguía indeciso..."
    "Todos los clubes tienen sus cosas buenas y malas..."
    scene bg escuela corredor clubes tarde with dissolve
    play music ambiente fadein 6
    "Y con eso, ya he visitado todos los clubes que hay en la escuela..."
    "O eso era lo que creía."
    "Luego de haber dado un vistazo general al corredor del edificio donde están los clubes..."
    "Me di cuenta de que hay todavía un salón al que no he ido."
    "Es el último salón del corredor en donde me encuentro, y además la puerta está cerrada."
    pla "Tal vez sea un almacén..." 
    "Ese fue mi razonamiento, ya que en el otro edificio de la escuela, en donde están los salones de clase, también hay un almacén al final del corredor."
    pla "Bueno, parece que no tengo nada más que hacer aquí por hoy..."
    show alice normal with dissolve:
        center
        linear 3 right
    pause 0.5
    hide alice with dissolve
    # "De repente, escuché el sonido de una puerta cerrándose."
    pla "¿Uh?"
    "De reojo vi que una persona había entrado al mismo salón que consideré un almacén."
    pla "..."
    extend " ..."
    extend " ..."
    "Motivado por la curiosidad, caminé con pasos indecisos hacia el mismo salón."
    pla "La puerta está abierta..."
    play sound flash
    stop music fadeout 1
    scene bg salon club detectives with flashbulb:
        # pause 1
        xpan -60
        linear 8 xpan 60
    pause 3
    "Wow..."
    "Poco a poco, me fui adentrando en el salón."
    "Me quedé perplejo al ver la cantidad de cosas que hay aquí."
    "Vi una serie de curiosos objetos encima de una repisa."
    "Había algunas estatuas, también una peluca... y otros artefactos que parecían antiguedades."
    "También noté que en una pared se encontraban colgadas algunas vestimentas."
    "En una pequeña mesa se encuentra... ¿un detector de mentiras? Se miraba idéntico al de las películas."
    "También hay otras baratijas y pila de papeles, además de libros viejos."
    "En fin, había tantas cosas en ese lugar, que de verdad parecía un almacén."
    show alice sorprendida with dissolve
    pause 1.5
    unk "¿¡Eh!?" with hpunch
    pla "H- hola..."
    unk "Eh... este... ¿Ya ha llegado mi hora, verdad?"
    pla "..."
    play music ambiente3 fadein 4
    extend " ¿Disculpa?"
    show alice pensando at decaer
    unk "Uh... por lo menos deje que me despida de este salón..."
    unk "Hay tantos recuerdos aquí..."
    unk "Se me hace doloroso separarme de este lugar..."
    show alice sorprendida at reponerse
    pla "¡Oye! ¿¡De qué rayos estás hablando!?" with hpunch
    pla "No soy la muerte que ha venido por tu alma."
    unk "¿Uh?"
    "La chica me miró sorprendida, como si no entendiera mis palabras."
    unk "¿De qué estás hablando?"
    pla "¿Eh?"
    "Pero qué rayos..."
    show alice normal
    unk "..."
    unk "Espera, ¿acaso no eres del {amarillo}comité estudiantil{/amarillo}?"
    pla "Ehm... no."
    show alice pensando at decaer
    unk "Ah... menos mal..."
    "La chica entonces dejó ir un suspiro de alivio, a la vez que se sentaba en un taburete, como si su vida estaba en peligro hace poco."
    pla "Este... disculpa, me he equivocado del salón, no era mi intención venir a molestar."
    "Decido retirarme. Este lugar es raro."
    show alice sorprendida at reponerse_rapido
    unk "¡E- espera!" with hpunch
    "De repente, la chica se levantó, y al mismo tiempo se posicionó enfrente de la salida."
    "Tengo un mal presentimiento..."
    pla "¿Q- qué quieres?"
    show alice sonriendo
    unk "Si tú no eres del comité estudiantil..."
    show alice alegre
    unk "¿¡Entonces eres un cliente, verdad!?" with hpunch
    pla "¿Qué?"
    show alice at brinquitos
    unk "¡Bienvenido al {amarillo}club de detectives{/amarillo}!"
    show alice sonriendo
    pla "¿Club... de detectives?"
    pla "Entonces, ¿este lugar no era un almacén?"
    show alice enojada
    unk "¡Claro que no!" with hpunch
    pla "Ya... ya veo..."
    pla "Pues, mira... ehm..."
    "Interrumpí mi frase al desconocer su nombre."
    show alice sonriendo
    unk "Ah, qué modales los míos. ¡Soy {amarillo}Alice Baskerville{/amarillo}! ¡Mucho gusto!"
    "¿Baskerville?"
    "¿Será acaso de una familia rica?"
    show alice normal
    pla "Ah, bien. Alice, creo que te estás confundiendo, no soy ningún cliente."
    pla "Solo pasé por casualidad y me llamó la atención este salón..."
    show alice alegre at brinquitos
    ali "¡Ah! ¿¡Así que vienes a unirte al club!?"
    "Sin dejarme terminar de hablar, Alice siguió soltando conclusiones erronéas."
    show alice sonriendo
    ali "Espera un momento, ya traeré un formulario de inscripción."
    show alice sorprendida
    pla "¡Oye! ¡Tampoco vengo a eso!" with hpunch
    pla "Solo vine por pura curiosidad, y..."
    show alice sonriendo
    ali "¡Qué bien! ¡Ser curioso es una cualidad importante para un buen detective!"
    show alice sorprendida
    pla "¡Y dejar hablar a las personas es una cualidad aun más importante!" with vpunch
    pla "¡Deja de interrumpirme!"
    pla "Solo estaba viendo, y parece que ya he visto suficiente. Así que adiós..."
    "A pesar de haber dicho eso, tenía a Alice bloqueándome la salida."
    show alice normal
    ali "Uh..."
    ali "¡Te pierdes de una gran oportunidad! ¿Acaso ya estás en otro club?"
    pla "Pues no, pero..."
    show alice sonriendo
    ali "¡Entonces no hay problema!"
    show alice alegre
    ali "¡El club de detectives te da la bienvenida!"
    pla "Uh... debí haber mentido..."
    show alice pensando
    ali "¿Acaso no estás interesado en unirte?"
    pla "..."
    extend " Bueno, yo..."
    menu:
        "Que me cuente más del club":
            $ eleccion_1=1
            $ updateStat("carisma","+",1)
            $ renpy.notify("Carisma +1")
            #se habla del club,
            #y prota pregunta por los miemnros, se revela verdad, 
            #pataletas
            #prota cede a llenar formulario
            jump inicio_hablando_del_club
        "Decirle que no estoy interesado":
            $ eleccion_1=2
            show alice normal
            pla "La verdad es que no estoy interesado..."
            #pataletas 
            #prota cede a llenar formulario,
            #y prota pregunta por los miemnros, se revela verdad,
            #ya no hay nada que hacer
            jump inicio_berrinche_alice


label inicio_hablando_del_club:
    show alice normal
    pla "Está bien."
    pla "Si me cuentas acerca del club, quizás lo considere..."
    show alice alegre at brinquitos
    ali "¡Genial!"
    show alice sonriendo
    ali "Pues bien..."
    ali "Ehm..."
    ali "Aquí investigamos todo tipo de casos y le damos una solución."
    ali "Encontrar a un ladrón o algún objeto que se ha perdido..."
    ali "Investigar a personas..."
    ali "Y resolver misterios en general."
    ali "El club tiene un largo historial de casos resueltos con éxito."
    pla "Uhm... ahora que lo pienso, creo haber escuchado de este club antes..."
    "Pero como tenía nulo interés en los clubes, mi memoria es borrosa."
    pla "Eh... ¿Acaso hay tantos casos por resolver en esta escuela?"
    ali "Las personas esconden muchos secretos y problemas."
    show alice normal
    ali "Eso lo sé por experiencia."
    ali "Ahí, en ese estante tenemos un recopilatorio de los casos resueltos."
    "Vi al lugar que estaba señalando Alice."
    pla "Oh..."
    "Por la cantidad de papeles, puede ser cierto lo que dijo esta chica."
    jump inicio_verdad_del_club


label inicio_verdad_del_club:
    pla "Bien, ¿y en dónde están los demás miembros del club?"
    ali "..."
    stop music fadeout 7
    show alice pensando at decaer
    ali "Ellos ya no están con nosotros..."
    pla "..."
    show alice at reponerse
    extend " ¿Disculpa?"
    ali "Bi- bienvenido... {amarillo}Soy la presidenta del club{/amarillo}. Mu- mucho gusto..."
    pla "¿Qué... qué quieres decir?"
    ali "Lo que pasa, es que... Los demás miembros se graduaron el año pasado..."
    ali "Y al final, solo quedé yo..."
    "Creo que voy entendiendo el porqué de la actitud de Alice al inicio..."
    pla "Así que eso de que había llegado tu hora..."
    pla "Fue porque me confundiste con alguien del comité estudiantil, ¿verdad?"
    show alice normal
    ali "Si, es una deducción correcta, tienes talento para ser un buen detective. Je, je, je..."
    show alice sorprendida
    pla "¡Espera, no me cambies el tema!" with hpunch
    pla "Si no me equivoco, los clubes tienen ciertos requisitos para cumplir..."
    show alice pensando
    ali "Eh... sí..."
    play sound campana
    ali "{amarillo}Un club debe tener como mínimo cinco miembros{/amarillo} para ser considerado uno." with flashbulb
    ali "Y si el club no cumple con ese requisito, {amarillo}está en peligro de ser cerrado...{/amarillo}"
    pla "Ah... qué tonto he sido."
    pla "Debí haberme dado cuenta antes..."
    if eleccion_1==1:
        # pla "Devuélveme esa hoja."
        # ali "¿Eh?"
        # ali "¿Pa- para qué?"
        # pla "Para destruirla, obviamente."
        pla "Si el club está en peligro de ser cerrado..."
        pla "No puedo estar aquí."
        pla "Mejor me voy."
        jump inicio_berrinche_alice
    elif eleccion_1==2:
        ## antes de este label, se llenó formulario
        "He llenado el formulario y se lo entregué a Alice..."
        "Para luego darme cuenta de la verdad sobre el club."
        "Ya era demasiado tarde..."
        pla "Alice, ¿dónde está el formulario que te di?"
        show alice sonriendo
        ali "Ju, ju, ju. Está en un lugar seguro, no te preocupes [pla_name]."
        ali "¡Cuento contigo!"
        "Pero qué hija de..."
        jump inicio_fin_del_dia


label inicio_berrinche_alice:
    show alice at decaer
    ali "Oh..."
    ali "Uhhh..."
    show alice at reponerse_rapido
    pause 0.8
    show alice llorando at temblor
    play music comico fadein 1.5
    ali "¡Wuaaah!" with hpunch
    ali "¡Por favor, únete al club!" with hpunch
    ali "¡No seas malo!" with hpunch
    ali "¡Haré lo que sea si te unes!" with hpunch
    pla "¿¡Lo que sea!?" with vpunch
    pla "¡Espera, no digas esas cosas tan a la ligera!" with hpunch
    pla "¡Y deja de agitarme!" with vpunch
    ali "¡¡¡¡Por faaaaa!!!!" with hpunch
    ali "¡Ya verás que será la decisión correcta!" with hpunch
    pla "¡Dudo mucho que una decisión correcta venga por una de tus pataletas!" with vpunch
    ali "¡Wuaaaaaaahhhhhh!" with hpunch
    pla "¡Ya cá- cállate!"
    ali "¡WUUUUUUAAAAAAAAAAAAHHHHHH!" with hpunch
    pla "¿¡Acaso eres una niña mimada!?"
    pla "¡Deja de hacer tanto escándalo!" with hpunch
    show alice llorando at center
    ali "Eres malo." with hpunch
    ali "Si no estás en otro club, ¡no te haría ningún daño unirte a este!" with hpunch
    ali "¡WUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
    ali "¡Mi vida depende de esto!" with hpunch
    pla "¿¡No planeas suicidarte, verdad!?" with hpunch
    ali "¡WUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
    "Alice parecía una niña que llora en el supermercado cuando sus padres no le compran lo que ella quiere."
    ali "¡Qué malo eres!"
    "La chica no dejaba de llorar y repetir que yo era una muy mala persona."
    "Con este escándalo, si alguien viene... podría malinterpretar las cosas."
    ali "¡WUUUUUUUUUUUUUAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH!" with hpunch
    pla "¡B- bien! ¡Ya cállate!"
    pla "Creo que podría unirme al club, ¡pero deja de hacer tanto escándalo!"
    jump inicio_llenando_formulario

label inicio_llenando_formulario:
    show alice pensando
    ali "¿E- en serio? {i}*snif*{/i} ¿Te unirás?"
    pla "Sí, sí, ¡pero ya deja de llorar!"
    show alice alegre at brinquitos
    play music ambiente2 fadein 1
    ali "¡Sí!"
    ali "Ya te traeré el formulario de inscripción."
    show alice:
        ease .3 xoffset 90
        ease .5 xoffset -900
    pause .8
    hide alice
    "..."
    "¿Qué?"
    "He cumplido el capricho de una niña..."
    pla "En qué rayos me he metido..."
    show alice sonriendo at center:
        xoffset -900
        easein .8 xoffset 60
        easein .3 xoffset -40
        easein .2 xoffset 0
    pause 1.5
    ali "Listo, aquí está."
    pla "Qué rápida..."
    "Sin ningún rastro de llanto en su rostro, Alice me entregó una hoja de papel."
    "Mientras leía las preguntas del formulario, pensaba en que si no era demasiado tarde para escaparme."
    "Pero Alice seguía bloqueándome la salida."
    "Tampoco quería usar la violencia para apartarla, podría terminar empeorando las cosas..."
    show alice normal
    ali "¿Pasa algo?"
    "A la vez que pregunta, Alice me ofreció un bolígrafo."
    pla "¡Ah! Este... no... nada..." with hpunch
    show alice sonriendo
    "Mi voz sonó algo temblorosa..."
    "De alguna manera, esto parece como si le estuviera vendiendo mi alma al diablo..."
    "A un diablo infantil y llorón..."
    "Ya qué, veamos..."
    "Las preguntas del formulario eran las típicas: mi nombre, código de carné, en qué año estoy, y otras cosas..."
    "Con clara inseguridad, rellené los campos."
    pla "Bien, aquí lo tienes."
    show alice normal
    ali "¿Eh?"
    ali "Todavía no lo has llenado."
    pla "¿Qué?"
    ali "Mira, detrás de la hoja hay más preguntas."
    pla "Ah, cierto..."
    pla "..."
    extend " ..."
    extend " ..."
    pla "Pero qué rayos pasa con esto..."
    ali "En el formulario, los clubes también pueden agregar sus propias preguntas."
    pla "¿Son realmente necesarias estas extras?"
    "Las preguntas extras eran nada más que algunas adivinanzas básicas..."
    "De esas adivinanzas que te encuentras en videos del tipo {amarillo}\"Solo el 1\% de las personas logran resolver este test\"{/amarillo}..."
    ali "Sí. Es para evaluar tu capacidad de razonamiento."
    pla "Qué loco..."
    # "Las preguntas extras del formulario fueron las siguientes..."
    jump inicio_formulario_preguntas

label inicio_formulario_preguntas:
    #unos cuantos acertijos faciles
    #preguntas correctas aumentan inteligencia
    #incorrectas restan inteligencia
    ## que pereza, ya no puedo más u,u
    # "{amarillo}- Formulario completo -{/amarillo}"
    "Una vez que llené todos los campos del formulario, se lo entregué a Alice, quien de inmediato le echó una ojeada."
    show alice sonriendo
    ali "Sí, todo está en orden."
    ali "¡Una vez más, déjame darte oficialmente la bienvenida al club, [pla_name]!"
    pla "Ah..."
    pla "Qué molestia..."
    if eleccion_1==1:
        ali "¡Cuento contigo para restaurar el prestigio de este club y conseguir nuevos miembros!"
        jump inicio_fin_del_dia
    elif eleccion_1==2:
        jump inicio_verdad_del_club

##revisar orden de los eventos anteriores

label inicio_fin_del_dia:

    pla "Así que ahora solo somos dos miembros en este club, qué cliché."
    show alice normal
    ali "Uhm, eso no es del todo así."
    pla "¿Qué? ¿Acaso hay alguien más?"
    show alice sonriendo
    ali "Sí. Todavía no te he presentado a {amarillo}Sherinford.{/amarillo}"
    pla "¿Sherinford? Qué nombre tan raro... ¿Y en donde está? Me gustaría conocerlo..."
    show alice alegre
    ali "¡Claro!"
    ali "¡Sherinford! ¡Ven aquí pequeñín!"
    show sherinford grande behind alice at left with dissolve:
        xoffset -300
        on show:
            linear 1 xoffset 20

    pause 1.5
    "... ¿eh?"
    "De una caja salió saltando un pequeño pollo..."
    show alice sonriendo
    ali "Mira Sherinford, te presento a [pla_name]."
    ali "[pla_name], te presento a Sherinford."
    pla "Hola, mucho gus-{w=1}{nw}"
    pla "¿¡Sherinford es un pollo!?" with hpunch
    show alice normal
    ali "¿Y qué mas va a hacer?"
    pla "No... es que yo pensé que era una persona... ah, olvídalo..."
    "Seguimos siendo solo dos personas en este club..."
    show alice sonriendo
    ali "¿A que no es lindo? Nació el año pasado."
    pla "Eh, ya veo..."
    "El pollo hasta trae una gorra en miniatura..."
    hide sherinford with dissolve
    pause .6
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    she "Pío, pío, pío."
    show alice alegre
    ali "Je, je, je, buen chico."
    "El pollo, o mejor dicho, {amarillo}Sherinford{/amarillo}, con gran agilidad se subió hasta los hombros de Alice..."
    show alice sonriendo
    ali "Sherinford es también miembro del club."
    ali "Uno de los últimos casos que resolvieron mis superiores el año pasado, involucró al club de {amarillo}Cuidado de animales.{/amarillo}"
    ali "Ellos tenían conejos, tortugas y también gallinas."
    show alice normal
    ali "Misteriosamente los huevos que ponían las gallinas desaparecían."
    ali "Pero un huevo en especial apareció en un lugar inusual, cerca del club de cocina."
    ali "Entonces llevamos el huevo que encontramos a este salón mientras discutíamos lo que en realidad había sucedido."
    show alice sonriendo
    ali "Y de repente, el huevo se quebró, ¡y Sherinford había nacido!"
    ali "Todos en el club nos encariñamos con él, así que nos lo quedamos."
    ali "Además, el hecho de que Sherinford naciera, indicaba que había un gallo oculto en la escuela..."
    pla "Eh... qué caso tan curioso..."
    ali "Sí, ¿te sigo contando?"
    show alice normal
    pla "¡Ah! No, está bien." with hpunch
    "No hay que ser un gran detective para saber por qué ese huevo apareció cerca del club de cocina..."
    ali "Bueno..."
    "..."
    "Con que este es el club de detectives, o al menos, lo que queda de él..."
    "Qué aventuras me esperan aquí..."
    hide screen quick_menu
    $quick_menu=False
    window hide
    stop music fadeout 4
    scene bg negro with slow_dissolve
    #febrero 17 (lunes)
    $dia="Lun."
    $hora=8
    $fecha="Febrero 17"
    pause 5
    play music ambiente fadein 4
    scene bg escuela frente dia with slow_dissolve
    pause 3
    $quick_menu=True
    "Hoy es lunes."
    "Esta será mi primera semana como miembro del club de detectives."
    "Aunque no es precisamente un club por ahora..."
    "¿Será que podremos solo Alice y yo conseguir miembros para el club?"
    "La verdad es que no tengo ni idea de cómo hacerlo."
    "Hoy llegué temprano."
    "Son poco mas de las ocho, y estoy afuera de la escuela sentado en una banca, pensando en lo que debía hacer a continuación..."
    "A pesar de que me metí a ese club debido al escándalo que estaba haciendo Alice aquella vez..."
    # if eleccion_1==2:
    #     "Y además fui engañado..."
    "Senti algo de enojo, "
    extend "pero también pena por ella..."
    "Desconozco qué tan importante sea este club para Alice o desde hace cuánto es miembro, pero si esa chica está tan aferrada a ese lugar..."
    "Sería triste que cerraran el club..."
    "O eso supongo."
    # "Eso significa que está desesperada."
    pla "Ah... qué debo hacer..."
    unk "¡Hey!"
    pla "¿Eh?"
    window show
    show marissa alegre hablando with slow_dissolve
    pause 2
    pla "Ah..."
    "Una chica de radiante presencia se me acercó."
    show marissa preocupada
    unk "¿Estás bien?"
    pla "Eh... s- sí..."
    "Debido a la sorpresa, di una respuesta tambaleante."
    pla "... "
    extend "¿T- te conozco?"
    "Sin darme cuenta, le hice una pregunta."
    show marissa normal
    unk "Uh... ¿ya no te acuerdas de mi?"
    pla "Este..."
    "Espera..."
    "Ahora que la veo con más calma..."
    "Sí... podría ser... ella es..."

    menu:
        "La chica del club de música":
            pla "Eres del club de música, ¿cierto?"
            jump charla_1_marissa_mala_respuesta
        "La chica del club de cocina":
            pla "¡Ah! Lo recuerdo." with hpunch
            pla "Te vi en el club de cocina."
            pla "Eres... Marissa, ¿no?"
            $ updateStat("carisma","+",1)
            $renpy.notify("Carisma +1")
            show marissa alegre at brinquitos
            mar "¡Sí! "
            extend "Marissa Morstan."
            mar "¡Me alegra que me hayas recordado!"
            $ updateStat("intel","+",1)
            $renpy.notify("Inteligencia +1")
            mar "Y para que veas que yo también me acuerdo, tú eres [pla_name]."
            pla "Sí, así es."
            show marissa at brinquitos
            mar "Je, je, je. ¡Yaaay!"
            mar "..."
            jump charla_1_marissa
        "La presidenta del club de literatura":
            pla "¡Ah! ¡Ya sé!"
            pla "La presidenta del club de literatura."
            jump charla_1_marissa_mala_respuesta

label charla_1_marissa_mala_respuesta:
    $ updateStat("carisma","-",1)
    $renpy.notify("Carisma -1")
    unk "Eh... no..."
    show marissa preocupada at decaer
    unk "Bueno... es normal... apenas nos hemos visto una vez..."
    show marissa at reponerse
    unk "Como sea, soy Marissa Morstan."
    mar "Ayer fuiste al club de cocina. Y yo te estuve mostrando el club."
    pla "¡Ah, ya recuerdo!" with hpunch
    "Aunque demasiado tarde..."
    mar "Y tú eres... [pla_name], ¿no?"
    pla "Si, así es."
    show marissa alegre
    mar "Para que veas que yo sí me acuerdo je, je, je."
    mar "..."
    jump charla_1_marissa

label charla_1_marissa:
    show marissa normal
    extend " ¿Y qué pasa?"
    mar "Te veo algo preocupado..."
    pla "Ah, no es nada."
    pla "Solo estaba pensando acerca de los clubes..."
    mar "Cierto, tú estabas buscando un club al que unirte..."
    mar "Por eso del nuevo reglamento."
    pla "Exacto."
    mar "Entiendo..."
    mar "Aunque si lo estás pensando demasiado..."
    extend " ¿Es que no te has decidido todavía?"
    pla "A decir verdad..."
    pla "Ya... ya estoy en un club..."
    show marissa sorprendida
    mar "¡Oh!"
    show marissa alegre
    mar "Qué lástima... Así que no has elegido mi club je, je, je..."
    show marissa normal
    mar "¿Y a cuál te uniste?"
    pla "Al club de detectives..."
    mar "..."
    mar " ¿Eh?"
    show marissa alegre at brinquitos
    mar "¡Así que siguen {nw}"
    play sound campana
    extend "activos!" with flashbulb
    mar "¡Qué bueno saberlo!"
    pla "¿Eh?"
    pla "¿Ya conocías el club?"
    mar "¡Sip!"
    show marissa normal
    mar "Ellos ayudaron a mi hermana mayor con un problema hace tiempo..."
    mar "A ella le habían robado algo importante."
    mar "¡Pero todo se solucionó tan rápido!"
    show marissa sorprendida
    mar "... ¿eh?"
    "De repente Marissa puso cara de sorpresa, como si recién se hubiera dado cuenta de algo."
    mar "Pero... ¿No que sus miembros ya se habían graduado?"
    pla "Así es, ahora solo queda una sola persona en el club a exepción de mí."
    pla "Ah, y un pollo..."
    show marissa normal
    mar "¿Un pollo?"
    mar "Uhm... la única persona que quedó debió ser la chica más joven..."
    pla "¿Te... te refieres a Alice?"
    mar "Alice... "
    show marissa alegre
    extend " ¡Sí! ¡Esa misma!"
    mar "Era como la novata del grupo."
    pla "¿Así que la conoces?"
    show marissa normal
    mar "Uhm... un poco nada más. Solo la he visto un par de veces."
    mar "La conocí cuando mi hermana me llevó con ella al club, para que nos dijeran ahí la solución del caso."
    mar "Recuerdo que hicieron algo así como... {amarillo}un debate escolar.{/amarillo}."
    show marissa alegre
    mar "¡Eso fue genial!"
    mar "Deberías haberlo visto."
    show marissa normal with dissolve
    mar "..."
    extend " Así que si solo ha quedado ella en el club..."
    mar "Supongo que no le ha sido fácil conseguir nuevos miembros."
    show marissa alegre
    mar "Pero al menos ya consiguió una persona je, je, je."
    show marissa normal
    mar "¿Y porqué te uniste a ese club? Si es que se puede saber..."
    pla "Eh... Yo... este..." with hpunch

    menu:
        "Mentirle":
            pla "Pues..."
            pla "Pasaba por el lugar, me llamó la atención el salón."
            pla "Conocí a Alice, y luego me contó acerca de la situación del club."
            pla "Sentí pena por ella, entonces pensé que sería bueno ayudarla a reconstruir el club."
            mar "Eh... Qué buena persona eres..."
            mar "Interesante."
        "Decirle la verdad":
            pla "..."
            pla "Fui arrastrado de alguna manera..."
            mar "¿Mmm? ¿A qué te refieres?"
            pla "Es una historia larga..."
            "Bueno, tampoco tan larga, pero no se me apetecía contarlo todo..."
            pla "De forma resumida, ella comenzó a llorar, a hacer un alboroto."
            pla "Yo no sabía como calmarla."
            pla "Y ella no dejaba de repetir que me uniera al club."
            pla "Así que al final terminé aceptando..."
            show marissa sorprendida
            mar "..."
            extend " Mpppff..."
            show marissa alegre
            mar "¡Mppff Ja, ja, ja!" with vpunch
            mar "Así que fuiste chantajeado ja, ja, ja."
            pla "Hey... tampoco lo digas en voz alta..."
            mar "Ja, ja, ja. ¡Es que es tan gracioso!"
            mar "Nunca escuché una razón tan absurda para unirse a un club."
            pla "Lo sé... pero dejemos ese tema aparte..."
            show marissa alegre hablando
            mar "Sí... ja, ja... ya basta de risas... ja, ja, ja."
            "Veo que Marissa hasta ha llorado de la tremenda carcajada que se ha pegado..."
            $ updateStat("carisma","+",1)
            $renpy.notify("Carisma +1")
            "Al menos la hice reír, ¿eso es bueno, no?"

    # mar "Bueno..."
    mar "¿Y estás bien con la decisión tomada?"
    pla "¿Eh?"
    show marissa normal
    mar "Digo, ese club está en peligro de cerrar..."
    mar "Y tú justamente te decidiste a integrarte a un club para cumplir con el nuevo reglamento..."
    pla "Entiendo a lo que te refieres..."
    pla "La verdad es que no sé como sentirme al respecto..."
    pla "Se que es una decisión arriesgada..."
    "Aunque no fue tomada dentro de mis cabales..."
    pla "Pero a la vez... Siento que podría ser algo interesante..."
    pla "Solo piénsalo, un club de detectives no es justamente algo común en una escuela."
    show marissa alegre hablando
    mar "Eh... así que te gusta experimentar cosas nuevas."
    mar "Te entiendo."
    unk "Buenos días, Marissa."
    mar "Ah, buenos días."
    "Marissa regresó el saludo a una chica que se acercó a ella, quizás era una compañera de clases."
    mar "Bien, [pla_name], tengo que irme."
    mar "Fue un gusto haber hablado contigo."
    #si carisma es mayor o igual a 2
    if pla_stat["carisma"]>=2:
        show marissa at brinquitos
        mar "¡En serio me has caído bien!"
        mar "Antes de irme, ¿te parece si intercambiamos números?"
        pla "¿Eh? Se- seguro..."
        "¿¡Le he caído tan bien a una chica que incluso me pide que intercambiemos números!?"
        "¡Esto no se ve todos los días!"
        show marissa alegre
        mar "Y... ... ¡listo!"
        $ numero_marissa_obtenido=True
        mar "¡Bien, nos vemos, [pla_name]!"
        mar "Estamos en contacto, je, je, je."
        pla "Sí... hasta luego."
        "Después de intercambiar números conmigo, la chica de radiante personalidad se adentró en la escuela en compañía de su amiga."
    else:
        $ numero_marissa_obtenido=False
        pla "Lo mismo digo... Adiós."
    hide marissa with dissolve
    pause 2
    "Pasaron algunos minutos para que yo también me fuera a mi salón de clases."


    hide screen quick_menu
    $quick_menu=False
    window hide
    stop music fadeout 4
    scene bg negro with slow_dissolve
    #febrero 17 (lunes)
    $hora=14
    pause 5
    play music ambiente2 fadein 4
    scene bg salon maestros dia with slow_dissolve
    pause 3
    window show
    $quick_menu=True
    show mary normal with dissolve
    pause 1.5
    mary "Así que... ¿ya estás en un club?"
    pla "Así es."
    mary "Y ese es el club de detectives..."
    pla "Así es..."
    show mary hablando
    mary "El mismo club que no tiene los miembros suficientes para considerarse como un \"club\"."
    pla "A- así... es..."
    show mary pensando
    mary "Ah..."
    show mary normal
    mary "¿Estás consciente de que ese club en cualquier momento lo pueden cerrar, y tú regresarías al punto de partida?"
    pla "Lo- lo sé..."
    pla "Pero, solo tenemos que reclutar a más miembros, ¿no?"
    pla "Si conseguimos al menos tres personas más..."
    show mary hablando
    mary "¿Y crees que podrás conseguirlo? No suenas muy confiado."
    pla "Eh, bueno... ya... ya algo se me ocurrirá..."
    mary "No es bueno hacer las cosas de improviso."
    show mary normal
    mary "Un paso en falso y todo se echa a perder."
    show mary pensando
    mary "Esto me recuerda al extinto club de matemáticas..."
    mary "Lamentablemente tuvo que cerrar medio año después de que fuera creado."
    mary "Los miembros no estaban tan entusiasmados con el club como al inicio. "
    extend"Y a pesar de las sugerencias que di..."
    mary "Como resolver pruebas sorpresa, lecturas del libro de álgebra, crear métodos que resuelvan problemas de forma más rápida."
    mary "Nada de eso fue suficiente..."
    pla "Eh, profesora Harrow... parece que usted estaba muy involucrada en el club..."
    show mary normal
    mary "Por supuesto."
    play sound campana
    mary "{amarillo}Yo era la tutora del club de matemáticas.{/amarillo}" with flashbulb
    pla "Oh... eso no lo sabía..."
    mary "En fin, los miembros se fueron retirando uno por uno..."
    mary "Entonces llegó el comité estudiantil..."
    mary "Y lo cerró."
    show mary pensando
    mary "Por desgracia, a los estudiantes no les interesa mucho un club que sea de estudio..."
    mary "No entiendo por qué."
    pla "Sí... Yo tampoco lo entiendo..."
    "¿Quién en su sano juicio se metería a un club que se trata de hacer lo mismo que en clases?" with hpunch
    mary "..."
    show mary normal
    mary "De todas formas, respetaré tu decisión."
    mary "Haz lo que creas correcto."
    mary "Recuerda que tienes {amarillo}dos meses antes de que el comité estudiantil ponga manos en el asunto sobre el club.{/amarillo}"
    pla "Lo- lo entiendo..."
    mary "Bien, ya te puedes retirar."
    scene bg negro with dissolve
    stop music fadeout 3
    "..."
    "Dos meses, ¿eh?"
    "¿Se podrá reclutar a las personas suficientes en ese tiempo?"
    "Espero que sí..."
    "Si no estaré metido en un gran problema..."
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 0.4
    ## fin del prologo o introduccion
    show text "{size=70}Fin del prólogo.{/size}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    # show text "Continuará.":
    #     xalign 1.0
    #     yalign 1.0
    #     xpos 0.980
    # with dissolve
    # pause 3
    # hide text
    # with dissolve

    jump caso1
