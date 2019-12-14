label caso1_interrogatorio5_final:

    $fase_titulo.append("Interrogatorio de Neil")
    $fase_tipo_vida.append("cantidad")
    $fase_corazones.append(cantidad_corazones)
    $fase_multiplicador.append(10)

    $estadoj="Receso"
    pla "Así que, {amarillo}¿nadie te llamó la atención, eh?{/amarillo}"
    show neil pensativo
    nei "Eh... sí... ¿A- algún pro- problema con eso?"
    hide neil with dissolve
    show alice sorprendida with dissolve
    ali "¡Ha tartamudeado!" with hpunch
    pla "Sí... se hace evidente que a él le atrae Marissa..."
    pla "Tengo una idea."
    ali "¿Eh?"
    pla "Solo sígueme la corriente..."
    ali "E- entendido..."
    show alice normal:
        ease .5 mright
    show neil pensativo at mleft with dissolve
    play music ambiente3 fadein 3
    pla "Hey Neil, esa chica está muy agradecida con tu ayuda..."
    show neil sorprendido
    nei "¿¡Eeeeh!?" with hpunch
    extend " ¿E- en serio?"
    pla "Sí, y demasiado... le ha sorprendido que aún existieran los hombres caballerosos..."
    show neil sonriendo hablando
    nei "Je- je- je, je, je... solo hice lo que un hombre tenía que hacer..."
    show neil normal
    pla "Sabes, yo conozco a esa chica, se llama Marissa."
    show neil sonriendo hablando
    nei "¿Marissa? Je, je, es un lindo nombre."
    pla "Sí, en fin... ella me ha pedido tu número de celular."
    show neil sorprendido
    nei "¿¡Eeeeh!?" with hpunch
    show neil sonriendo hablando at brinquitos
    nei "Je, je, je... ya- ya veo..."
    show neil normal
    nei "Está bien, supongo que debo darle mi número, je, je, je..."
    pla "Puedes apuntarlo aquí."
    "Le ofrecí a Neil mi bolígrafo y el bloc de notas."
    $addNote("Número de Neil","Neil ha escrito de su propia mano su número de celular en mi bloc de notas. Escribió su número inmediatamente después de que yo le dijera que Marissa estaba interesada en llamarlo, esto me hace pensar que Neil está en interesado en esa chica...{p}{p}Uhm... no veo ese temblor que vi en la carta...","numneil",True)
    nei "Bien, aquí lo tienes."
    pla "..."
    nei "El receso no tardará en terminar. Me tengo que ir."
    show neil sonriendo hablando
    nei "Estaré esperando su llamada."
    nei "Je, je, je..."
    hide neil with dissolve
    stop music fadeout 4
    show alice normal:
        ease .5 center
    ali "Se ha ido de muy buen humor..."
    show alice sorprendida
    ali "¡...!" with hpunch
    show alice enojada
    ali "¡[pla_name]!" with hpunch
    ali "¿¡Por qué le dijiste que Marissa quería su número!?"
    pla "Por esto..."
    show alice sorprendida
    "Junto a mi respuesta, le enseñé a Alice mi bloc de notas."
    ali "¿¡Entonces, tú querías el número de Neil!?" with hpunch
    show alice pensando
    ali "[pla_name], no sabía que tuvieras esos gustos..."
    show alice sorprendida
    pla "¡Te equivocas!" with hpunch
    show alice normal
    ali "¿Entonces?"
    pla "Le pedí a Neil que apuntara su número de celular,{nw}"
    play sound campana
    extend " {amarillo}¡y con eso descubrí que Neil es zurdo!{/amarillo}" with flashbulb
    ali "..."
    show alice sorprendida
    ali "¡Ah! {amarillo}¡En el perfil del acosador descubrimos que es zurdo!{/amarillo}"
    pla "Shhhh no lo digas tan alto..."
    $updateNote("Neil London (perfil)",ndesc="\n\nHe descubierto que Neil es zurdo.",add=True)
    show alice alegre at brinquitos
    ali "¡Eres genial, [pla_name]!"
    show alice sonriendo
    # pla "Pero sí, Neil también es zurdo..."
    play music ambiente2 fadein 3
    ali "Uhm... hemos avanzado bastante... ya deberíamos ser capaces de llegar a una solución."
    show alice alegre at brinquitos
    ali "Segun mi experiencia, viene siendo hora de realizar{nw}"
    play sound campana
    extend " {amarillo}un debate escolar.{/amarillo}" with flashbulb
    pla "¿Debate escolar?"
    show alice sonriendo
    ali "Cuando mis superiores tenían un caso donde había mucha información que parecía no encajar..."
    ali "Ellos realizaban un debate con casi todos los involucrados en el caso."
    show alice normal
    ali "Primero, se establecía una interrogante, y luego los integrantes del debate {amarillo}comenzaban a dar ideas uno por uno.{/amarillo}"
    ali "O también expresábamos opiniones..."
    ali "Al final, las contradicciones salían a flote."
    ali "Y así lográbamos tener nuevas pistas importantes con las cuales resolver el caso."
    show alice alegre
    ali "Incluso... ¡Hasta mis superiores atrapaban al culpable en el mismo debate!" with hpunch
    pla "Eh..."
    pla "Eso es una buena idea... necesitamos hacer algo así."
    show alice sonriendo at brinquitos
    ali "Claro, es algo que se le ocurrió al fundador del club."
    ali "Es una persona muy inteligente y astuta."
    pla "..."
    pla "Así que en ese debate, deben estar todos los involucrados..."
    show alice pensando
    ali "Sí... tenemos a Marissa, la profesora Harrow, Beck, Neil y nosotros..."
    show alice normal
    ali "En total somos seis personas."
    pla "¿Es necesario que todos estén en el debate?"
    ali "No es necesario."
    ali "Pero si se establece que su presencia es importante, se tendría que mandar a llamar."
    show alice pensando
    ali "Claro que cuando eramos un club reconocido... teníamos permiso de la dirección {amarillo}para obligar a cualquier alumno unirse al debate.{/amarillo}"
    pla "Eh... me lo imagino..."
    pla "Hay que trabajar con lo que tenemos..."
    pla "Habrá que avisar con tiempo a todos, de que podríamos llamarlos para ir al salón del club..."
    show alice normal
    ali "Si, hay que preparar todo con tiempo."
    ali "Yo me encargaría de limpiar el salón, ya que está algo desordenado..."
    pla "En fin, ya hablaremos de eso con más calma, ahora quiero ir a la cafetería antes de que el receso..."
    stop music
    play sound campana_escuela
    show alice sorprendida
    pause 4
    ali "El receso ya ha terminado."
    show alice alegre
    ali "¡Nos vemos, [pla_name]!"
    hide alice with dissolve
    pla "¿¡Ehhh!?" with hpunch
    pla "Ah... qué hambre tengo..."
    stop music fadeout 3
    scene bg negro with dissolve
    "Le envié un mensaje a Marissa, resumiéndole lo que Alice y yo hemos avanzado, y también le comenté sobre que mañana haríamos un debate."
    "Ella no tardó en contestar, diciendo que por ella estaría bien."

    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=17
    $estadoj="Libre"
    $quick_menu=True
    window show
    scene bg escuela edificio principal corredor with dissolve

    play music ambiente fadein 2
    "Son las cinco de la tarde."
    "Después que las clases terminaron, fui al salón del club, para arreglar con Alice todo lo necesario para realizar un debate."
    "Y ahora, estaba pasando por el edificio principal de la escuela, cuando..."
    show beck sonriendo with dissolve
    pause 1
    pla "¿Beck?"
    "Me encontré con Beck, {amarillo}quien había salido del salón de maestros.{/amarillo}"
    show beck sorprendido
    bec "¿Eh? ¿[pla_name]?"
    show beck sonriendo
    bec "¿Qué pasa? ¿Cómo va la investigación?"
    pla "Eh... pues avanzando... oye, ¿estabas hablando con la profesora Harrow?"
    show beck sorprendido
    bec "¿¡Eh!? ¿¡Cómo lo sabes!?" with hpunch
    pla "Ah... solo dije lo primero que se me vino a la cabeza..."
    hide beck with dissolve
    show mary normal with dissolve
    "Y también vi a la profesora Harrow..."
    mary "¿[pla_name]? Qué milagro verte a estas horas por la escuela..."
    pla "Sí, he estado algo ocupado con las actividades del club."
    show mary pensando
    mary "..."
    mary "Espero que no te estés olvidando que tienes tareas que hacer para mañana."
    pla "¡Cla- claro que no lo he olvidado!" with hpunch
    "A decir verdad, lo había olvidado, por estar pensando demasiado en el caso de Marissa..."
    mary "En fin, me voy."
    show mary normal
    mary "Hasta mañana, [pla_name]."
    hide mary with dissolve
    show beck sorprendido with dissolve
    bec "..."
    extend " ..."
    extend " ..."
    bec "¿¡Son ideas mías, o tuviste una charla casual con la profesora Harrow!?" with hpunch
    pla "Ehm... sí... supongo..."
    show beck pensando
    bec "¿Cómo puedes hablar tan tranquilamente con la profesora Harrow?"
    pla "Pues... este... ella es como una amiga de la familia..."
    # pla "Así que... bueno..."
    pla "La profesora Harrow ha estado pendiente de mis calificaciones desde que entré a esta escuela."
    show beck sorprendido
    bec "¿La profesora Harrow es amiga de tu familia?"
    show beck pensando
    bec "Ah... qué suerte tienes..."
    # pla "..."
    pla "¿Suerte?"
    pla "No creo que me sienta tan afortunado por eso..."
    bec "Cuánto {amarillo}desearía recibir ese tipo de atención por parte de la profesora Harrow...{/amarillo}"
    # pla "Oye Beck... ¿Te gusta la profesora Harrow?"
    pla "¿Qué?"
    show beck sorprendido
    bec "¿¡Eeeeh!? No- no, nada..." with hpunch
    show beck sonrojado
    # bec "Cla- claro que no..."
    bec "..."
    pla "..."
    # bec "..."
    bec "¿Qué? No me mires así..."
    menu:
        "Seguir viendo fijamente a Beck":
            bec "..."
            show beck pensando
            bec "Lo siento [pla_name], pero yo no juego de ese lado, solo me interesan las mujeres."
            $updateStat("carisma","+",2)
            $renpy.notify("Carisma +2")
            pla "¿¡Qué!? No soy gay..." with hpunch
            bec "Si tú lo dices..."
            "Ah, cielos..."
        "Seguir hablando":
            $updateStat("carisma","-",1)
            $renpy.notify("Carisma -1")
    
    show beck preocupado
    bec "Hey... ¿de casualidad no sabes si ella tiene novio?"
    pla "¿Que si la profesora Harrow tiene novio?"
    show beck sorprendido
    bec "No- no es lo que piensas." with hpunch
    show beck pensando
    bec "Solo estaba pensando en voz alta, es que tengo curiosidad."
    bec "Si una persona como ella tiene pareja..."
    bec "..."
    
    # bec "No- no sé de lo que estás hablando... Solo tenía curiosidad..."
    # pla "¿QUde las chicas que están siempre pendientes de ti te gusta?"
    # bec "Pues... no..."
    # bec "Si las trato con amabilidad, es solo por cortesía, {amarillo}pero ninguna chica de esta escuela me gusta.{/amarillo}"
    # pla "Vaya... no me quiero imaginar la depeción que tendrán cuando se enteren..."
    # show beck sorprendido
    # bec "¡Oye! ¡Tampoco se lo digas a nadie!" with hpunch
    # show beck sonrojado
    # bec "Es... vergonzoso..."
    # "... ya desearía tener un poco de su popularidad..."
    show beck sonriendo
    bec "¿Entonces? ¿La profesora Harrow tiene novio?"
    pla "Pues... no que yo sepa."
    show beck sorprendido
    bec "..."
    show beck sonriendo
    bec "¡Genial!"
    show beck pensando
    bec "¡Ejem! Quiero decir, interesante..." with hpunch
    "Beck en serio es pésimo para mentir..."
    show beck guino
    bec "Bueno, me tengo que ir. ¡Nos vemos, [pla_name]!"
    hide beck with dissolve
    "Sin perder tiempo, Beck se escapó..."
    $updateNote("Beck Doran (perfil)",ndesc="\n\nTengo la sospecha de que Beck está enamorado de la profesora Harrow. Vaya... quién lo diría...",add=True)
    "¿Debería decirle que a la profesora Harrow solo le interesan los hombres inteligentes?"
    "Uhmm... nah. Estoy cansado, ya quiero irme a mi casa."
    stop music fadeout 2
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $dia="Mar."
    $hora=14
    $fecha="Febrero 25"
    $quick_menu=True
    window show
    play music ambiente2 fadein 3
    scene bg salon club detectives with dissolve

    jump caso1_predebate

