label caso1_investigacion1:
    scene bg salon club detectives with dissolve
    "Después de que Marissa se fuera, Alice y yo todavía estábamos en el salón del club."
    "Primero, nos detuvimos a revisar la carta."
    scene carta_amor with dissolve
    ali "Uhm..."
    ali "La letra es muy descuidada..."
    pla "¿Tal vez sean los nervios, no?"
    ali "Puede ser..."
    pla "¿Qué significará ese manchón?"
    ali "Parece como si hubo un exceso de tinta."
    ali "Quizás mantuvo la punta del bolígrafo mucho tiempo en el papel..."
    pla "Uhm, y justamente en el nombre, como si lo estuviera pensando demasiado."
    pla "..."
    pla "Hay algo raro con la letra..."
    ali "¿Eh?"
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    ali "¿A qué te refieres, [pla_name]?"
    show alice sorprendida
    pla "¡Ya sé!"
    pla "Es... es..."
    show alice normal
    ali "¿Lo olvidaste?"
    pla "No... nada de eso..."
    pla "Ah... lo tengo en la punta de la lengua..."
    show alice sorprendida
    pla "Era algo que tenía que ver con la forma de escribir... con la inclinación..."
    ali "¡Necesitas usar la {amarillo}Ruleta de la incógnita{/amarillo}!"
    pla "La- la ruleta de la... ¿qué?"
    show alice alegre
    ali "Es una técnica que usaban mis superiores cuando olvidaban temporalmente una palabra."
    ali "Lo que tienes que hacer, es imaginarte varias letras que giren en círculos..."
    ali "Entonces vas descartando letras una por una hasta formar una palabra."
    pla "No entiendo..."
    show alice enojada
    ali "¡Rápido, [pla_name]!" with hpunch
    ali "¡Cierra los ojos y haz lo que te acabo de decir!"
    pla "E- está bien..."
    pla "No hay nada que perder..."
    stop music fadeout 4
    scene bg negro with fade
    tuto "Es hora de otro minijuego."
    tuto "En la {amarillo}Ruleta de la incógnita{/amarillo} verás una serie de letras que van girando en círculos."
    tuto "El objetivo es seleccionar varias letras para formar una palabra."
    tuto "Si seleccionas una letra incorrecta, se te restará vida..."
    tuto "En este minijuego, las vidas están representadas por un porcentaje."
    tuto "Cada letra incorrecta resta un 10\%"
    tuto "Si seleccionas una letra correcta, esta se irá agregando a un panel en la derecha."
    tuto "Básicamente, es como {amarillo}el juego del ahorcado.{/amarillo}"
    tuto "Buena suerte."

    #-----Inicia minijuego

    $estadoj="Ruleta Incóg."
    $ruleta_porcentaje=100
    $ruleta_id=1

    #palabra a descubir
    $palabra_ruleta="ZURDO"

    #posicion de la letra a averiguar en palabra
    $posicionenpalabra=0

    python:
        #lo que se mostrara en el panel derecho
        lstLetrasActuales=[]
        #agregamos varios guiones bajos
        for x in xrange(0,len(palabra_ruleta)):
            lstLetrasActuales.append("_")

    $letras1=["U","Y","H","Z","R","A","J","R","O"]
    $letras2=["I","B","Z","R","Ñ","D","M","C","H","B"]
    
    $quick_menu_gameplay=True
    $showMinigameTitle("Ruleta de la incógnita")
    $quick_menu_bajo=True
    window hide
    play music deduccion fadein 3
    $change_cursor("target")
    scene bg salon club detectives
    $renpy.show_screen("temporizador",185)#185
    
    call screen ruleta_incognita(letras1,letras2,"A partir de la forma de escribir, se deduce que el autor es...",palabra_ruleta)

label ruleta1_gameover:
    stop music fadeout 3
    $estadoj="Libre"
    # $quick_menu_gameplay=False
    $quick_menu_bajo=False
    window show
    show alice normal with dissolve
    pla "Me rindo."
    ali "Pensé que te esforzarías más."
    show alice pensando at decaer
    ali "Así que ya no tenemos más pistas..."
    jump caso1_gameover

label ruleta1_fin:

    $fase_titulo.append("Ruleta de la incógnita")
    $fase_tipo_vida.append("porcentaje")
    $fase_corazones.append(ruleta_porcentaje)
    $fase_multiplicador.append(5)

    $showplay_excl("esoes")
    stop music fadeout 3
    $estadoj="Libre"
    $quick_menu_gameplay=False
    $quick_menu_bajo=False
    window show
    show alice sorprendida with dissolve
    play sound campana
    pla "¡El autor es zurdo!" with flashbulb
    ali "¿¡Eh!?"
    ali "¿Por qué dices eso?"
    show alice normal
    pla "Por la inclinación de la letra."
    pla "Esa inclinación se me hacía algo extraña..."
    pla "Y es justamente porque alguien que escribe con la mano izquierda, tendrá la letra inclinada a ese lado..."
    pla "Además, eso también explicaría la mancha en la carta."
    show alice sorprendida
    ali "¿¡Eh!? ¿En serio?"
    pla "Sí. Al dejar el bolígrafo puesto sobre el papel en un punto específico durante algún tiempo..."
    pla "Haría que la tinta se escurriera, y como se escribe de izquierda a derecha..."
    show alice normal
    ali "Alguien zurdo pasaría la mano con la que escribe sobre la tinta..."
    pla "Así es."
    ali "..."
    play music ambiente fadein 3
    show alice alegre at brinquitos
    ali "¡Eso es increíble! ¡[pla_name], eres muy listo!"
    ali "¡Me alegra mucho tenerte en el club!"
    #actualizamos perfil de sospechoso
    #--nota: actualizar de acuerdo al nombre, usar la posicion del array no es confiable, ya que esta posicion puede variar de acuerdo a cuando se obtiene una pista
    $updateNote("Perfil del sospechoso",ndesc="\n\nHay pistas que indican que el autor de la carta es zurdo.",add=True)
    pla "Ah... vamos... tampoco es para tanto..."
    pla "..."
    show alice normal
    pla "El tiempo ha pasado volando, ya van a ser las cinco."
    show alice sorprendida
    ali "Eh, no me había dado cuenta..."
    show alice normal
    ali "Ya va siendo hora de salir..."
    ali "Pero antes, deberíamos revisar el casillero de Marissa..."
    pla "Uhm, claro..."
    ali "Vámonos, Sherinford."
    show sherinford grande behind alice at left with dissolve:
        xoffset -300
        on show:
            linear 1 xoffset 20
    she "¡Pío, pío, pío!"
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    $hora=17
    pause 2
    $quick_menu=True
    window show
    scene bg escuela corredor with slow_dissolve
    show alice normal with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    "Junto a Alice y su pollo, fui al corredor de los salones de clase, en donde están los casilleros."
    "Le había enviado un mensaje a Marissa que nos indicara cuál era su casillero."
    ali "Uhm..."
    "Alice murmuró mientras revisaba el casillero con una enorme lupa."
    ali "Uuuuuhhhmmm..."
    ali " Ya veo..."
    pla "¿Has descubierto algo?"
    show alice sonriendo at brinquitos
    show sherinford pequeño at brinquitos
    ali "Efectivamente..."
    ali "Los rayones en el cerrojo del casillero no son para nada comunes."
    pla "..."
    "Gracias capitana obvia, eso ya lo vi sin necesidad de una lupa..."
    show alice pensando
    ali "No he encontrado más pistas..."
    ali "Creo que eso es todo..."
    show alice sorprendida
    pla "No tan rápido."
    pla "Deberíamos preguntarnos{nw}"
    play sound campana
    extend " {amarillo}por qué este casillero estuvo siendo forcejeado por alguien.{/amarillo}" with flashbulb
    ali "¡Ah! ¡Po- por supuesto! Claro que eso ya lo sabía." with hpunch
    show alice pensando
    ali "So- solo estaba poniéndote a prueba..."
    "Lo dudo mucho..."
    pla "Como sea, teniendo en cuenta lo que nos contó Marissa..."
    show alice normal
    pla "Si esos rayones aparecieron el sábado..."
    pla "Tendríamos que averiguar si alguien vio algo sospechoso en ese lapso de tiempo."
    ali "No creo que eso sea fácil..."
    ali "{amarillo}Los fines de semana, solo vienen estudiantes por actividades del club...{/amarillo}"
    ali "Y este edificio {amarillo}permanece generalmente vacío...{/amarillo}"
    ali "Incluso los salones de aquí se mantienen cerrados."
    $addNote("Salones de clase en fin de semana","Los salones de clase permanecen cerrados los fines de semana, a exepción del edificio de clubes.\nPor lo tanto, el edificio en donde están los casilleros se mantiene vacío.")
    pla "Oh, eso no lo sabía..."
    pla "Entonces, regresando al motivo del forcejeo..."
    pla "Considerando que se trata de un acosador, ¿esta persona quería algo de Marissa?"
    pla "Ya sabes, algo así como un tesoro... O un premio..."
    show alice pensando
    ali "Uh... siento escalofríos de tan solo pensar en eso..."
    show alice normal
    play sound campana
    ali "{amarillo}¿Pero qué cosa quería sacar el acosador del casillero de Marissa?{/amarillo}" with flashbulb
    $addNote("¿Hay algo de valor en el casillero?","¿Qué buscaba el responsable del forcejeo en el casillero de Marissa? ¿Hay algo de valor que Marissa guarda en su casillero?")
    pla "Habrá que preguntarle a Marissa si guardaba algo de valor..."
    ali "Buena idea..."
    show alice sorprendida
    play sound campana
    ali "¡Ah!" with flashbulb
    pla "¿Alice?"
    ali "¡Ya sé! ¿¡Y qué tal si el responsable buscaba meter algo en el casillero!?"
    # ali "Entonces al ver que no podía abrirlo..."
    hide sherinford with dissolve
    hide alice with dissolve
    "Claramente emocionada, Alice sacó de su mochila una hoja de cuaderno."
    pla "¿Qué tienes ahora en mente?"
    ali "[pla_name], he estado pensándolo..."
    ali "¿Cómo llegó esa carta al bolso de Marissa?"
    ali "Creo que el acosador quiso meter la carta en el casillero, por eso forzó la cerradura."
    ali "Y al ver que era muy difícil hacerlo, entonces..."
    "Alice comenzó a tratar de meter la hoja a través de las hendiduras de la puerta."
    "Incluso trató de meterlo por los orificios que están al frente."
    "Sin embargo..."
    show alice pensando with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "No- no entra..."
    she "Pío..."
    "La hipótesis de Alice no tardó en desmoronarse."
    pla "No creo que haya sido eso..."
    pla "De lo contrario, {amarillo}Marissa nos habría dicho que encontró la carta en el casillero, y no en su bolso.{/amarillo}"
    ali "Uh... eso parece... pensé que estaba en lo correcto..."
    $addNote("Papel y casillero","Alice demostró que no se puede meter una hoja de papel en un casillero sin tener que abrirlo antes.")
    "Alice sonó decepcionada, pero no estaría de más apuntar lo descubierto."
    show alice normal
    # ali "..."
    # pla "¿Qué pasa ahora, Alice?"
    # "Vi que ella de repente se quedó viendo a la nada, sumida en sus pensamientos."
    # ali "¿Cómo estamos seguros de que el acosador realmente no pudo abrir el casillero?"
    # $addNote("¿Cerradura fue forzada?","Alice sugirió que quizás el acosador sí pudo abrir el casillero...")
    # pla "..."
    pla "Bien, creo que tenemos suficiente información por hoy."
    pla "Ya es tarde."
    ali "Ah, sí... no hay nada más que investigar aquí."
    pla "Bueno, me voy."
    show alice pensando
    ali "..."
    if pla_stat["carisma"]>=2:
        show alice pensando
        ali " [pla_name]..."
        pla "¿Qué pasa?"
        ali "Este... bu- bueno..."
        show alice sonrojada
        ali "{size=25}Deberíamos intercambiar números...{/size}"
        pla "¿Perdón?"
        show alice asustada
        ali "..."
        ali "No- no me hagas repetirlo..." with hpunch
        "No lo haría, si ella hablara con una voz más audible."
        show alice sonrojada
        ali "Me preguntaba..."
        extend " si podríamos intercambiar números..."
        show alice asustada
        ali "¡N- no pienses nada extraño!" with hpunch
        show alice sonrojada
        ali "Es que yo..."
        pla "No estoy pensando en nada extraño... está bien."
        show alice sorprendida
        ali "¿¡Eh!?" with hpunch
        pla "¿Por qué actúas así?"
        show alice pensando
        ali "Eh... no... nada..."
        stop music fadeout 3
        scene bg negro with dissolve
        pause 1.5
        "Antes de despedirnos, intercambié números con Alice."
        $numero_alice_obtenido=True
    else:
        $numero_alice_obtenido=False
        extend " adiós [pla_name]."
        stop music fadeout 3
        scene bg negro with dissolve
        pause 1.5
    
    if numero_alice_obtenido:
        hide screen quick_menu
        window hide
        $quick_menu=False
        $hora=20 #8 pm
        pause 2
        window show
        $quick_menu=True
        "..."
        #ring
        "En la noche, recibí un mensaje de Alice."
        ali "{amarillo}\"Hola, ¿cómo estás?\"{/amarillo}"
        ali "{amarillo}\"Espero que logremos resolver este caso...\"{/amarillo}"
        ali "{amarillo}\"Cuento contigo, [pla_name] :3\"{/amarillo}"

    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide

    $hora=20 #8 pm
    pause 2
    
    $hora=10
    $dia="Vie."
    $fecha="Febrero 21"
    $estadoj="Receso"

    window show
    $quick_menu=True

    scene bg escuela corredor with dissolve
    "{amarillo}- Al día siguiente, en la hora de receso... -{/amarillo}"
    play music ambiente2 fadein 5
    "Al salir de mi salón de clases, me encontré con una cara conocida."
    show alice alegre with dissolve
    ali "¡[pla_name]! ¡Buenos días!" with hpunch
    pla "Alice... Buenos días..."
    "Vi que ella estaba de muy buen humor."
    show alice enojada
    ali "¡Vamos! ¡La investigación debe continuar!" with hpunch
    pla "Eh..."
    pla "Preferiría tener un descanso... las clases son más exigentes en este año..."
    ali "¿¡Cómo puedes decir eso!?" with hpunch
    ali "No puedes dejar que una investigación se enfríe demasiado, sino se echará a perder."
    show alice normal
    pla "Ahh... ahora ya me dio hambre..."
    "Ignorando mis quejas, Alice continuó hablando."
    ali "He estado pensando mucho en el caso anoche..."
    ali "Con lo que nos ha contado Marissa..."
    ali "Sería bueno establecer como punto de partida... {nw}"
    play sound campana
    extend "{amarillo}que el acosador es un conocido de ella.{/amarillo}" with flashbulb
    pla "Tiene sentido..."
    "Comencé a caminar rumbo a la cafetería, y Alice me estaba siguiendo a la vez que exponía sus ideas."
    ali "Así que... hay que aprovechar este receso para saber más {amarillo}acerca de los compañeros de Marissa.{/amarillo}"
    pla "Uh, vamos... dame un respiro..."
    show alice enojada
    ali "¡[pla_name]!" with hpunch
    extend " No hay tiempo que perder."
    show alice pensando
    ali "Sino el club..."
    ali "Podría cerrar..."
    pla "Ni se te ocurra hacer un escándalo de esos."
    ali "Jum..."
    pla "..."
    "Dejé de caminar, y comencé a rascarme la cabeza."
    pla "Ah... está bien..."
    show alice alegre at brinquitos
    ali "¡Yaaay!"
    extend " ¡Así se habla!"
    hide alice with dissolve
    "Veamos... el salón de Marissa sería el..."
    pla "..."
    "Vi que Alice no me estaba siguiendo..."
    pla "Alice... ¿no pretenderás que vaya yo solo, verdad?"
    show alice pensando with dissolve
    ali "..."
    ali "Eh- bu- bueno..."
    "La chica comenzó a balbucear hasta dar con una respuesta."
    show alice sorprendida
    ali "¡Ah, sí!" with hpunch
    show alice normal
    ali "¿Recuerdas que Marissa nos dijo que fueramos discretos?"
    ali "Pueees... sería sospechoso que lleguemos los dos."
    pla "..."
    extend " touché."
    show alice sonriendo
    ali "Así que... da lo mejor de ti para encontrar sospechosos."
    ali "Yo estaré investigando en otro lado."
    pla "¿Y si mejor cambiamos de lugar?"
    show alice alegre at brinquitos
    ali "¡Hasta luego!"
    show alice:
        ease .3 xoffset 90
        ease .5 xoffset -900
    pause 1.5
    hide alice
    # hide alice with dissolve
    "Sin terminar de escucharme, Alice se fue corriendo..."
    "Ah... me las pagarás..."
    scene bg negro with dissolve
    pause 1.4
    # "Le envié un mensaje a Marissa, avisándole que iría a su salón para buscar sospechosos."
    # "Ella me contestó de inmediato, y me dijo que no había problema."
    # "Acordamos que yo iría porque supuestamente estoy interesado en el club de cocina."
    # "Y aprovechando el don de Marissa para ser muy sociable... ella me presentaría a sus compañeros de clase."
    scene bg salon clases with dissolve
    pla "Disculpen... ¿está Marissa aquí?"
    unk "¿Eh?"
    unk "Marissa, alguien te está buscando."
    mar "Ya voy..."
    show marissa alegre hablando with dissolve
    mar "¡Hola! ¿Eh? ¿[pla_name]?"
    # "Marissa fingió no conocerme, de acuerdo al plan que establecimos en el chat."
    show marissa normal
    pla "Hola, vengo por lo del club de cocina, estoy interesado."
    "A la vez que digo esto, le guiño un ojo disimuladamente."
    show marissa alegre hablando at brinquitos
    mar "Ah, ¿quieres unirte al club de cocina?"
    "Y menos mal que Marissa captó mi señal."
    pla "No estoy seguro, pero quisiera saber algunas cosas acerca del club."
    show marissa alegre
    mar "¡Claro, no hay problema!"
    unk "¿Quién es, Marissa? ¿Lo conoces?"
    "Una de las chicas cerca de ella preguntó con mucha curiosidad."
    show marissa alegre hablando
    mar "Por supuesto, él es... [pla_name]. Hace algunos días fue al club ya que estaba en busca de uno adonde unirse."
    "Como se esperaba de alguien tan popular, Marissa manejó la situación con total naturalidad."
    unk "Eh... con que es así... ya veo..."
    scene bg negro with dissolve
    "Y sin ser para nada sospechosa, Marissa estuvo presentándome con todos sus amigos, y también me habló acerca del resto de sus compañeros."
    "Es lo único que se me ocurrió en poco tiempo..."
    "Sin embargo, descubrí algunas cosas interesantes."
    scene bg salon clases with dissolve
    show marissa alegre hablando with dissolve
    unk "Hey, Marissa... ¿Quién es ese chico?"
    unk "¿Acaso es tu novio? Ja, ja, ja."
    show marissa alegre
    mar "Je, je, no estés bromeando."
    show marissa:
        ease .5 mright
    show beck sonriendo at mleft with dissolve
    pause 1
    "¡Wooaa... ese tipo es muy alto!" with vpunch
    show marissa alegre
    mar "[pla_name], te presento a {amarillo}Beck Doran.{/amarillo} Beck, te presento a [pla_name]."
    bec "¿Qué onda?"
    pla "Mucho gusto..."
    "Beck... recuerdo que Marissa se encontró con él en la cafetería..."
    mar "[pla_name] vino a buscarme por que está interesado en el club de cocina."
    show beck sorprendido
    bec "Oh... ¿en serio?"
    "El chico parecía que estaba analizándome con la mirada, espero que no se dé cuenta de nuestra mentira..."
    stop music fadeout 4
    show beck serio
    bec "Ya veo..."
    show marissa sorprendida
    mar "..."
    show beck enojado
    bec "Sé cual es la verdad."
    pla "..."
    mar "¿Eh?"
    show beck serio
    bec "Te llamas... [pla_name], ¿no?"
    bec "Eres un chico listo... pero ya sé tus verdaderas intenciones."
    pla "..."
    pla "No- No sé de lo que estás hablando..."
    # "¿Acaso es verdad lo que está diciendo?"
    mar "Beck... ¿a qué te refieres?"
    show beck enojado
    bec "Marissa... ese chico..."
    play music ambiente2 fadein 2
    show beck sonriendo at brinquitos
    bec "¡Quiere unirse al club para estar rodeado de lindas chicas!"
    show beck guino
    bec "Eres todo un rufián, [pla_name], ja, ja, ja."
    pla "..."
    extend " ¡Ah! Ja, ja, ja..." with hpunch
    "Solo pude reír, aliviado, esperando que cambiara de tema."
    show marissa normal
    show beck sonriendo
    bec "Hey [pla_name], no nos hagamos los tontos, si el club de cocina no es lo tuyo..."
    play sound campana
    bec "Date una vuelta por {amarillo}el club de fútbol.{/amarillo} Te aseguro que tendrás a más chicas siguiendote je, je, je." with flashbulb
    bec "Bien, nos vemos ja, ja, ja."
    hide beck with dissolve
    show marissa:
        ease .5 center
    "Y con eso Beck se marchó del salón mientras emitía algunas carcajadas."
    "Además, mientras salía, algunas chicas fueron a seguirlo..."
    pla "... eso estuvo cerca..."
    show marissa alegre at decaer
    mar "Eso parece, je, je..."
    show marissa alegre hablando at reponerse
    mar "Como pudiste ver, él es Beck Doran, es miembro del club de fútbol."
    mar "Es toda una celebridad en nuestro salón."
    pla "..."
    show marissa normal
    mar "¿[pla_name]?"
    pla "Ah, hay algo de lo que me dijo que me llamó la atención..."
    pla "¿Qué quiso decir con eso de que {amarillo}\"tendría más chicas siguiendome\"{/amarillo}?"
    mar "Eh... ¿estás interesado en eso?"
    pla "No, no..."
    "Bueno, sí..."
    pla "Ese chico, ¿en serio es tan popular?"
    show marissa alegre
    mar "Claro, casi todas las chicas del salón lo tienen como un ídolo.{nw}"
    play sound campana
    extend " {amarillo}Incluso ha tenido acosadoras.{/amarillo}" with flashbulb
    show marissa normal
    pla "¿¡Eh!?" with hpunch
    "Con que ese chico ha tenido acosadoras..."
    $addNote("Beck Doran (perfil)","Miembro del club de fútbol. Es una persona muy popular en su salón, en especial entre las mujeres. Según Marissa, él ha tenido algunas acosadoras molestándolo.","beck")
    "Debería hablar con él más adelante."
    pla "Ah... por cierto..."
    $renpy.choice_for_skipping()
    pla "Marissa, tengo que preguntarte algo..."
    tuto "Ahora, deberás seleccionar un elemento del bloc de notas."
    tuto "Solo debes hacer click en \"Presentar\" debajo del elemento a elegir."

    $initCorazones()
    show screen corazones
    $quick_menu_gameplay=True
    mar "¿Sí? ¿Qué quieres preguntar?"

    ##ahora se debe seleccionar un item del bloc de notas, usaremos como id, el titulo del elemento
    $idevidencia_correcta="¿Hay algo de valor en el casillero?"

    label mostrar_evidencia1:

        show marissa normal

        if cantidad_corazones==0:
            jump evidencia_mostrada1_gameover

        call screen notepad("evidenc",jumpto="evidencia_mostrada1") with dissolve

    label evidencia_mostrada1:
        if idevidencia_mostrar==idevidencia_correcta:
            $evidencia1_fallida1erintento=False
            jump evidencia_mostrada1_correcto
        else:
            $evidencia1_fallida1erintento=True
            $randomnum = renpy.random.randint(1, 5)
            if randomnum==1:
                mar "No entiendo tu pregunta..."
            elif randomnum==2:
                show marissa alegre hablando
                mar "Sabes... A veces dices cosas extrañas..."
            elif randomnum==3:
                show marissa enojada
                mar "¿Podrías ir directo al grano? El tiempo de receso es muy corto."
            elif randomnum==4:
                mar "¿Te gusta perder el tiempo, eh?"
            elif randomnum==5:
                show marissa apenada
                mar "[pla_name]... Date prisa, quiero ir a comprarme algo en la cafetería..."         
            $restCorazones()
            pla "Ah, lo siento... eso no era..." with hpunch
            jump mostrar_evidencia1

    label evidencia_mostrada1_gameover:
        $evidencia_mostrada1_resuelta=False
        hide screen corazones
        stop music fadeout 1
        show marissa preocupada
        mar "¿Qué estás intentando hacer, [pla_name]?"
        $updateStat("intel","-",1)
        $renpy.notify("Inteligencia -1")
        pla "La verdad, es que ni yo lo sé..."
        jump evidencia_mostrada1_final

    label evidencia_mostrada1_correcto:
        $evidencia_mostrada1_resuelta=True
        hide screen corazones
        $showplay_excl("esoes")
        if not evidencia1_fallida1erintento:
            $updateStat("intel","+",1)
            $renpy.notify("Inteligencia +1")
        pla "Marissa... ¿Guardas algo de valor en tu casillero?"
        show marissa sorprendida
        mar "¿Eh?"
        mar "¿Por qué lo preguntas?"
        pla "Bueno... eso explicaría que hayan forcejeado la cerradura de tu casillero..."
        "Me aseguré de hablar en voz baja para que otros no escucharan."
        show marissa normal
        mar "Uhm..."
        mar "Pues no guardo nada de valor en mi casillero."
        mar "Solo tengo libros y cuadernos ahí."        
        pla "Oh, entiendo... gracias, eso era lo que quería saber."
        $removeNote("¿Hay algo de valor en el casillero?")
        "Pregunta resuelta..."
        jump evidencia_mostrada1_final

label evidencia_mostrada1_final:
    $quick_menu_gameplay=False
    pla "Bueno, creo que ya debo irme."
    pla "Nos vemos, Marissa..."
    stop music fadeout 1
    show marissa sorprendida:
        ease .5 mright
    show mary normal at mleft with dissolve
    play sound campana
    pla "¡...!" with flashbulb
    show mary hablando
    mary "Marissa Morstan..."
    mar "¡Aaah!" with hpunch
    mar "¡Pro- pro- profesora Harrow!"
    show mary normal
    mary "..."
    mary "¿[pla_name]? No esperaba verte por aquí..."
    pla "Hola, profesora Harrow..."
    "La profesora Harrow estaba en la entrada del salón. Como siempre, con un aura intimidante..."
    "Y vi que Marissa de repente se volvió nerviosa, como un ciervo frente a los faros de un automovil."
    "¿Qué está pasando aquí?"
    show mary hablando
    mary "Marissa... ven conmigo."
    mar "¡Aaaahhh!" with hpunch
    mary "Marissa."
    show marissa at brinquitos
    mar "¡Iiiihh!" with hpunch
    show mary normal
    "Marissa soltó un extraño gemido, como el de un pequeño animal, a medida que la profesora se adentraba en el salón."
    "La chica, que hasta hace poco tenía una actitud amable, ahora está mostrando una faceta nerviosa."
    "Es lo que causa, la ira de la profesora Harrow..."
    show marissa apenada at decaer
    "Como si hubiera aceptado un terrible destino, Marissa tomó su bolso, y cabizbaja se dirigió hacia la salida."
    pla "Espere... profesora Harrow..."
    show marissa normal at reponerse
    pla "¿Por qué se está llevando a Marissa?"
    show mary hablando
    mary "No tengo porque dar detalles. No es de tu incumbencia."
    play music ambiente3 fadein 4
    show mary normal
    show marissa apenada
    mar "¡[pla_name]! ¡Salvameeeee!" with hpunch
    pla "..."
    pla "Profesora Harrow..."
    pla "Agradecería que me dijera que está pasando..."
    show mary hablando
    mary "Solo tengo que hablar con Marissa acerca de su rendimiento académico del año pasado, eso es todo."
    show mary normal
    show marissa sorprendida
    mar "¡Me- me- mentira! ¡Usted solo me está llevando por que sigue enojada por {amarillo}aquel tropiezo{/amarillo}!" with hpunch
    play sound campana
    pla "¿Tropiezo?" with flashbulb
    extend " Es no me lo has contado Marissa."
    # "Eso es algo que no me ha contado Marissa..."
    show marissa preocupada
    mar "¿En serio? Eh, lo olvidé..."
    "Debería indagar más..."
    show marissa normal
    pla "Profesora Harrow, me gustaría hacerle algunas preguntas."
    show mary sorprendida
    mary "¿Eh? ¿A qué viene eso?"
    pla "Es... por actividades de mi club..."
    show mary normal
    "Me aseguré de mantener mi voz baja al decirlo."
    "Aunque de todas formas, seguramente ya parezco sospechoso por tratar de averiguar lo que ha pasado entre ellas..."
    mary "..."
    show mary pensando
    extend " entiendo."
    mary "Podemos hablar en el salón de maestros."
    pla "Muchas gracias..."
    stop music fadeout 2.5
    scene bg negro with dissolve
    pause 2
    scene bg salon maestros dia with fade
    show mary normal with dissolve
    # show marissa preocupada at mright with dissolve
    pla "¿Entonces, podría contarme lo que pasó el día de ese \"tropiezo\"?"
    # hide marissa with dissolve
    # show mary:
    #     ease .5 center
    mary "Está bien..."
    #reiniciamos corazones, si antes se acabaron corazones, al tratar de preguntar a marissa si tenia algo de valor, esto evitara que el interrogatorio se termine (por que corazones=0)
    $initCorazones()
    jump caso1_testimonio2