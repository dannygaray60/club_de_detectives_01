label caso1:
    $hora=15#3pm
    $quick_menu=True
    window show
    play music ambiente2 fadein 3
    scene bg escuela edificio principal corredor with dissolve
    "Mientras caminaba hacia el club de detectives, pensé en cómo podría atraer nuevos miembros."
    # "No es como si cometer un crimen y luego resolverlo sea una opción."
    "No creo que Alice se ponga a chantajear a otras personas con su llanto..."
    "..."
    extend " Solo por si acaso, le dejaré en claro que eso no debe volver a hacerlo..."
    "Esa chica sí que llega a ser algo molesta cuando quiere... Espero que no sea así todo el tiempo."
    unk "Disculpa..."
    pla "..."
    extend " ¿Eh?"
    "Escuché la voz de alguien a mis espaldas, y cuando me giré para ver de quién se trataba..."
    show hellen sonriendo with dissolve
    unk "Hola..." 
    unk "Disculpa, necesito ayuda..."
    "Al verla, lo primero que me llamó la atención fue la ropa que llevaba."
    pla "Ese uniforme es..."
    "Sin querer expresé mi curiosidad."
    unk "¡Ah! Este... soy de nuevo ingreso."
    show hellen alegre
    unk "Me llamo {amarillo}Hellen Turner{/amarillo}, mucho gusto..."
    pla "Ah... igualmente. Soy [pla_name]."
    show hellen sonriendo
    hel "..."
    extend " ¿pasa algo?"
    "Ahora que lo recuerdo..."
    "Creo haber escuchado que la profesora Harrow me comentó sobre que los de nuevo ingreso no tienen la obligación de portar el uniforme."
    "Supongo que ese es el uniforme de su escuela anterior..."
    show hellen preocupada
    hel "Este... ¿[pla_name]?"
    pla "¡Ah! Disculpa..." with hpunch
    pla "Así que... ¿en qué te puedo ayudar?"
    hel "... es algo penoso..."
    hel "Resulta que este lugar es más grande que la escuela donde estudiábamos, y bueno... nos hemos perdido..."
    pla "¿Nos?"
    show hellen sonriendo
    "Después de lo que dijo, noté que al lado de la chica había alguien más."
    show hellen:
        easein 0.5 mright
    pause 0.5
    show hatty sonriendo at mleft with dissolve 
    pause 1.5
    show hatty alegre
    unk "Hola, je, je, je."
    pla "H- hola..."
    show hatty sonriendo
    hel "Ella es Hatty, {amarillo}mi hermana gemela.{/amarillo}"
    pla "¿Hermana gemela?"
    # extend " Pero si no se parecen..."
    # hel "Eso nos lo han dicho mucho, pero estás en un error."
    # hel "Somos gemelas, pero no mellizas."
    # hel "Nacimos el mismo día."
    show hatty alegre
    hat "Yo nací cuatro minutos antes je, je, je."
    pla "Oh, entiendo..."
    "Así que... ¿Hatty es la hermana mayor?"
    "¿Por qué tengo la sensación de que me demostrarán lo contrario?"
    show hatty sonriendo
    pla "Entonces, ¿en qué necesitas ayuda?"
    hel "Ah, sí... como he dicho, nos hemos perdido, y no sabemos cómo llegar a la biblioteca."
    if pla_stat["carisma"]==0:
        pla "Entiendo."
        pla "Bueno, la biblioteca está en..."
        "Le di indicaciones al par de hermanas sobre como llegar a la biblioteca."
        show hellen alegre
        hel "Muchas gracias por ayudarnos."
        pla "De nada."
        hide hellen with dissolve
        hide hatty with dissolve
        "..."
        "Mientras miraba a las hermanas irse, reflexioné en que debí aprovechar la oportunidad..."
        "Eran de nuevo ingreso, debí hablarles sobre el club..."
        $renpy.notify("No tener carisma, puede llegar a ser contraproducente...")
        "Ah... qué lento soy.{nw}"
    else:
        hel "Aunque no lo creas, tenemos el sentido de la orientación algo deficiente."
        show hellen alegre
        hel "En especial mi hermana..."
        show hatty asustada
        hat "¡Oye! ¡No tenías que decirlo!"
        show hatty pensando
        pla "Entiendo..."
        pla "Bien, si quieren, puedo guiarlas a la biblioteca."
        pla "Ya que por el camino paso por ahí."
        show hellen sonriendo
        hel "¿En serio?"
        show hellen alegre at brinquitos
        hel "¡Muchísimas gracias!"
        scene bg escuela corredor afuera tarde with slow_dissolve
        pause 1
        show hellen sonriendo at mright with dissolve
        show hatty sonriendo at mleft with dissolve
        "Mientras caminábamos, continué conversando."
        pla "Así que... con que son de nuevo ingreso..."
        show hatty hablando
        hat "Sí, {amarillo}¡somos de la sección 1-A!{/amarillo}"
        show hatty sonriendo
        pla "Eh... con que el primer salón del corredor..."
        pla "¿Y ya están en algún club?"
        hel "¿Eh?"
        hel "¿Por qué lo preguntas?"
        "... Me dejé llevar por mi necesidad de conseguir miembros..."
        pla "Ah, bueno... es que tenía curiosidad, ¿ya han leído el reglamento escolar, no?"
        show hellen alegre
        hel "Claro, ya lo he leído."
        show hatty hablando
        hat "Yo no lo leí."
        pla "..."
        show hatty sonriendo
        show hellen sonriendo
        hel "¡Ah! Cierto, es obligatorio pertenecer a un club."
        show hatty hablando
        hat "Qué regla más rara..."
        hat "..."
        show hatty molesta
        hat "Eh... lo entiendo..."
        pla "..."
        extend " ¿Qué?"
        hat "No creas que somos tontas."
        show hatty alegre
        hat "Estás intentando reclutarnos a tu club je, je, je."
        "Ah... ¿eso fue tan evidente?"
        hel "[pla_name], ¿Y a qué club perteneces?"
        pla "Al club de detectives..."
        show hatty sonriendo
        #un character, que une los nombre de las hermanas
        hel_hat "¿El club de detectives?"
        pla "Sí..."
        show hellen alegre
        hel "Eh... suena interesante."
        hel "Tal vez podría necesitar de tu ayuda cuando se pierda mi hermana."
        show hatty asustada
        hat "¡Ah!"
        pla "Oh, sobre su sentido de la orientación..."
        show hatty pensando
        show hellen sonriendo
        hel "Sí, el año pasado fuimos a una excursión."
        hel "Y por seguir las indicaciones de Hatty, terminamos perdidas."
        hel "A pesar de que ella llevaba el mapa..."
        show hatty asustada:
            mleft
            temblor
        hat "Eh... sobre eso... yo..." with hpunch
        show hellen alegre
        show hatty pensando
        hel "Hatty se puso a llorar y pedirme perdón cuando estaba empezando a oscurecer."
        hel "Pero al final solo habíamos caminado en círculos sin alejarnos del punto de partida."
        hel "Así que no hubo peligro alguno."
        show hellen sonriendo
        show hatty asustada at mleft
        hat "¡Wuuaaah! ¡N- no sigas!" with hpunch
        hel "Je, je, je..."
        show hatty pensando
        "Hellen soltó una pequeña risita al ver a su hermana alterada."
        "Como me lo suponía, la hermana menor es la verdadera \"mayor\"."
        "Hellen resultó ser una persona muy amable y buena conversadora."
        "Y Hatty demostró ser una persona con la personalidad opuesta..."
        pla "Bien, ya llegamos, el pequeño edificio de allá es la biblioteca."
        hel "En serio, muchas gracias por ayudarnos, espero que no haya sido una molestia."
        pla "No, para nada."
        hide hellen with dissolve
        hide hatty with dissolve
        "¡Ah!"
        "Mientras ellas caminaban hacia la biblioteca, caí en la cuenta de que no pude seguir con el tema del club."
        "Aunque Hellen no se miraba tan interesada..."
        "Y Hatty sorrprendenmente fue algo perspicaz sobre mis intenciones..."
        "Espero que ellas se pasen por el club un día de estos..."
    stop music fadeout 4
    scene bg negro with slow_dissolve
    pause 3
    play music ambiente fadein 3
    scene bg salon club detectives with fade
    pause 2
    show alice enojada with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "Ah, [pla_name], ¡llegaste tarde!"
    pla "Oye, tampoco es como si hubieramos establecido un horario."
    she "¡Pío, pío, pío!" with hpunch
    "Genial, hasta el pollo me está regañando."
    pla "Al menos muestra algo de gratitud de que haya venido a pesar de todo lo que ha pasado."
    show alice pensando
    ali "Uh... yo..."
    pla "..."
    extend " como sea."
    show alice normal
    pla "¿Y cuál es el plan ahora?"
    ali "¿Plan?"
    she "¿Pío?"
    pla "He hablado con la profesora Harrow, acerca de que me uní a este club..."
    ali "¿A la profesora {amarillo}de matématicas{/amarillo}?"
    pla "Sí, ella es la tutora de mi salón."
    ali "Oh, entiendo."
    pla "Como iba diciendo, ella mencionó que tenemos hasta dos meses antes de que el comité estudiantil..."
    show alice pensando
    ali "Cierre el club..."
    pla "Exacto."
    pla "Así, que... ¿Cuál es el plan? No podemos quedarnos de brazos cruzados."
    show alice normal
    ali "Un plan..."
    show alice pensando
    extend " uhm..."
    extend " bueno..."
    show alice normal
    ali "No tengo un plan."
    pla "..."
    extend " ¿qué?"
    show alice sorprendida
    pla "¿¡Cómo que no tienes un plan!?" with hpunch
    pla "¿¡Cómo esperabas conseguir que alguien se uniera al club!?"
    show alice pensando at decaer
    show sherinford pequeño at decaer
    ali "Uh..."
    ali "Perdón..."
    ali "No tengo idea..."
    she "Pío..."
    "En serio... esta chica..."
    pla "..."
    pla "No tiene caso."
    hide sherinford with dissolve
    hide alice with dissolve
    pla "..."
    "Tratando de pensar en algo, recorrí el salón del club."
    "Me acerqué al estante que Alice me había señalado el otro día..."
    pla "¿Estos son los casos que han llegado al club?"
    show alice sonriendo with dissolve
    show sherinford pequeño at center with dissolve:
        ypos .450
        xoffset 70
    ali "Sí. Ahí están todos los casos desde que se fundó el club."
    show alice alegre
    ali "El club tiene un {amarillo}95\%{/amarillo} de casos resueltos."
    # "D Alice con tono triunfal."
    pla "Eh... vaya que son muchos... ¿desde hace cuánto se fundó el club?"
    show alice normal
    ali "... uhm... creo que hace unos diez años."
    pla "Sorprendente..."
    show alice alegre
    ali "¿¡Verdad que sí!?"
    pla "Pero en serio que son demasiados... ¿Es que esta escuela no es tan tranquila como pensaba?"
    show alice normal
    ali "Uh, pues desde que me uní sí hubo una considerable cantidad de casos..."
    ali "Habían estudiantes, maestros y personal de la escuela involucrados en algunos..."
    pla "Vaya..."
    extend " ¿eh?"
    pla "Espera, Alice..."
    pla "¿Desde hace cuánto estás en este club?"
    ali "{amarillo}Desde hace cuatro años{/amarillo}, cuando comencé a estudiar en esta escuela."
    pla "¿¡Que!? E- entonces... ¿eres también de cuarto año?" with hpunch
    show alice sonriendo
    ali "Una deducción acertada, soy del {amarillo}4-B.{/amarillo}"
    pla "Pero qué... pensé que eras de segundo año..."
    show alice enojada
    ali "¿¡Uhhm!? ¿¡Qué quieres decir con eso!?" with vpunch
    pla "N- nada, olvídalo..."
    "Marissa mencionó que Alice era como la novata del club..."
    "Pero si ella se unió hace cuatro años..."
    "¿Es que acaso no ha mejorado en todo ese tiempo?"
    # pla "¡Ah!"
    pla "Por cierto..."
    pla "Alice, ¿por qué te uniste a este club?"
    show alice normal
    ali "¿Eh? ¿Qué pasa con esa pregunta?"
    pla "Pienso que sería bueno saber qué te empujó a unirte a este club."
    # pla "Qué es lo que te gusta tanto de este club."
    pla "Y así usar esa información para pensar en algo para atraer a nuevos miembros."
    show alice alegre
    ali "¡Oh! ¡Bien pensado, [pla_name]!"
    show alice pensando
    ali "... uhm..."
    ali "Bueno..."
    ali "No sé si podría contártelo..."
    pla "¿Qué?"
    show alice normal
    ali "Es algo muy personal..."
    ali "..."
    show alice pensando
    extend " fue algo difícil..."
    ali "Aunque si es para salvar el club..."
    ali "Puedo decir que... de forma resumida..."
    show alice normal
    ali "Yo recibí ayuda del club para resolver un caso en el que fui involucrada..."
    ali "No me siento cómoda hablando al respecto..."
    ali "Pero después de que todo se solucionó..."
    show alice pensando
    ali "Vi que los únicos que creyeron en mí, fueron ellos..."
    ali "Los miembros del club de detectives."
    pla "¿Creyeron en ti?"
    show alice sorprendida
    ali "¡Ah! ¡He dicho demasiado!" with hpunch
    show alice normal
    ali "Cómo sea, en resumen, fui conmovida por la forma en resolvieron todo."
    show alice sonriendo
    ali "Fueron tan geniales... casi como si hubieran salido de una película."
    ali "Eso es todo lo que puedo contarte..."
    show alice pensando
    ali "L- lo siento..."
    pla "Descuida..."
    "Al menos es mejor que nada."
    "Aunque tenga curiosidad por ese caso donde Alice estuvo involucrada, lo mejor será no indagar más..."
    show alice normal
    pla "Así que impresionar a alguien cuando se resuelve un caso... es una manera efectiva de atraer alguien a este club..."
    pla "¿Pero de donde se supone que sacaremos un caso?"
    show alice alegre at brinquitos
    show sherinford pequeño at brinquitos
    ali "¿Y si planeamos uno? Y luego fingimos resolverlo..."
    show alice sorprendida
    pla "Denegado."
    show alice pensando
    ali "Uh... aguafiestas... Podría haber hecho {amarillo}un crimen perfecto...{/amarillo}"
    pla "Si fuera un crimen perfecto, eso quiere decir que {amarillo}no se puede resolver...{/amarillo}"
    show alice sorprendida
    ali "Ah, cierto."
    pla "Y para que quede claro, ese chantaje tuyo no te va a servir de nuevo."
    pla "¡Así que ni pienses volver a hacerlo!"
    show alice enojada
    ali "..."
    show alice pensando
    ali "Está bien..."
    "¿Por qué se tardó en contestar?"
    "Tendré que echarle un ojo encima."
    show alice normal
    pla "Bien, de lo que puedo concluir con la situación del club..."
    pla "Es que este club necesita casos por resolver..."
    ali "Y para que lleguen casos importantes se necesita mérito."
    pla "Y ese mérito se gana resolviendo casos..."
    ali "Vaya círculo vicioso, ¿no lo crees Sherinford?"
    she "Pío, pío."
    ali "Uhm, sí... tienes razón."
    "¿¡Está... hablando con el pollo!?" with hpunch
    pla "Como sea, tampoco debemos pensar en esperar casos \"importantes\"."
    pla "Recuerda que yo soy un novato..."
    pla "Así que mi sugerencia es partir de algo básico."
    ali "¿Algo básico?"
    pla "Sí, me refiero a {amarillo}repartir volantes{/amarillo} para hacer saber a la escuela que este club sigue activo."
    pla "Y esperando que la reputación del club en años pasados... nos ayuden a conseguir miembros y casos."
    show alice sorprendida
    ali "Oh..."
    show alice alegre
    extend " ¡Puede funcionar!"
    show alice at brinquitos
    show sherinford pequeño at brinquitos
    ali "¡Bien, manos a la obra!"
    show alice:
        ease .3 xoffset 90
        ease .5 xoffset -900
    show sherinford pequeño estatico at temblor:
        ypos .450
        xoffset 70
        linear 1 yoffset -50
        pause .5
        linear .5 yoffset 600
    $ renpy.pause(2,hard=True)
    hide alice with hpunch
    $ renpy.pause(1.5,hard=True)
    "A la vez que Alice se adentró rápidamente en los rincones del salón, el pollo, digo, Sherinford cayó al suelo de pie."
    "Eso me dio a entender que Alice posiblemente se olvidaba de que Sherinford se posaba en su hombro."
    "Pero Sherinford está ileso."
    "¿Es que ahora el pollo se cree un gato?"
    # "Vaya, el pollo cayó de pie,"
    ali "Creo que aquí tenemos varios paquetes de hojas, marcadores..."
    "Mientras murmuraba para sí misma, Alice irradiaba entusiasmo, lo cual me puso de buen humor."
    "Y verla en ese estado hace que me pregunte..."
    scene bg negro with dissolve
    "¿Por qué ha tenido problemas hasta ahora para conseguir nuevos miembros para el club?"
    stop music fadeout 2
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 3
    $hora=17#5pm
    $quick_menu=True
    window show
    "Esa tarde nos la pasamos haciendo diseños para los volantes."
    "Después de eso, Alice dijo que se haría cargo de hacer las fotocopias."
    "Mañana desde muy temprano, nos reuniríamos en el club para comenzar."
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2



    $quick_menu=True
    window show
    $dia="Mar."
    $ hora=8
    $ fecha="Febrero 18"
    "{amarillo}- Al día siguiente... -{/amarillo}"
    play music ambiente2 fadein 4
    scene bg salon club detectives with dissolve
    show alice alegre with dissolve
    ali "¡[pla_name]! ¡Buenos días!"
    pla "Buenos días, Alice."
    show alice sonriendo
    show sherinford grande behind alice at left with dissolve:
        xoffset -300
        on show:
            linear 1 xoffset 20
    pause 1
    she "¡Pío, pío!"
    pla "Bu- buenos días, Sherinford..."
    ali "[pla_name], ya tengo lista las copias."
    hide sherinford with dissolve
    "Sherinford se paró encima de una pila de papeles, como si me los estuviera señalando."
    # "Alice señaló la pila de papeles que estaba encima de una mesa."
    pla "Eh... sacaste bastantes."
    pla "Bien, ahora toca entregarlos."
    show alice at brinquitos
    ali "¡M- me esforzaré, ya lo verás!"
    "Siento que Alice está algo nerviosa."
    pla "Supongo que esa es la actitud, yo también me esforzaré."
    "Mutuamente nos dimos motivación con nuestras palabras."
    ali "Bueno, [pla_name], nos vemos en la tarde."
    pla "Sí. Está bien, hasta luego."
    "Agarré un paquete como de cincuenta volantes y salí del lugar, directo a mi salón de clases."
    scene bg negro with slow_dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2
    $hora=15 #3pm
    $quick_menu=True
    window show
    "Logré entregar un volante a la mayoría de mis compañeros de clase."
    extend " Y también a algunas personas con las que me encontraba en el camino."
    "Aún así, todavía me quedaron algunas hojas."
    "Pero no me quejo, me fue bien."
    "¿Cómo le habra ido a Alice?"
    scene bg escuela corredor clubes tarde with dissolve
    "Mientras camino hacia el club..."
    show henry tranquilo with slow_dissolve:
        mright
        ease 3 center
    pause 3.5
    unk "..."
    show henry sonriendo with dissolve
    unk "¡Oh!"
    unk "Oye, tú, chico..."
    pla "¿S- sí?"
    "De repente se apareció una persona de singular apariencia."
    unk "Hola, disculpa si te molesto, pero necesito ayuda..."
    "Sentí un {i}dejá-vu...{/i}"
    pla "¿En qué le puedo ayudar?"
    "¿Quién es él?"
    extend " Su ropa y sus rasgos faciales lo hacen parecer alguien oriental..."
    "Sus ojos tranquilos se posaron en mí, a la vez que él comienza a hablarme."
    unk "Necesito saber dónde está el salón de maestros."
    "¿Entonces es un maestro?"
    pla "Bueno, eso queda en el edificio principal, en la parte oeste."
    unk "Oh... así que me equivoqué de edificio..."
    extend " ya veo."
    show henry alegre
    unk "Muchas gracias, chico."
    show henry sonriendo
    unk "..."
    show henry tranquilo
    unk " Oh... ¿un club?"
    "El miró los volantes que yo traía en la mano."
    show henry sonriendo
    unk "¿Puedo?"
    "Sin pensarlo demasiado le entregué uno de los volantes."
    unk "Eh... qué interesante..."
    extend " un club de detectives."
    pla "Ah.. sí... estamos en busca de nuevos miembros o casos por resolver..."
    unk "Ya veo, ya veo... Chico, ¿y cuántos casos has resuelto?"
    pla "¿Yo? Eh... ninguno... soy nuevo en el club..."
    show henry serio
    unk "¿Eh?"
    show henry tranquilo
    unk "Bueno, te deseo suerte, señor Holmes je, je, je."
    pla "Eh, mi apellido no es Holmes..."
    hide henry with dissolve
    "Sin hacerme caso, el hombre se fue con el volante en mano."
    "..."
    extend " Qué hombre tan raro."
    scene bg salon club detectives with fade
    "Cuando entré en el salón, vi que Alice estaba ahí, aunque no se había percatado de mi presencia."
    pla "Alice..."
    show alice sorprendida
    ali "¡Aaah!" with hpunch
    "Alice se giró rápidamente."
    pla "¿Qué estabas haciendo?"
    show alice pensando
    ali "Eh, yo nada..."
    pla "¿Cómo te ha ido?"
    ali "Eh... pues bien, las clases estuvieron tranquilas hoy."
    pla "Me refiero a cómo te fue con la entrega de los volantes..."
    ali "... bien. ¿Y tú?"
    show alice normal
    pla "Me quedaron como quince hojas, pero creo que lo hice bien."
    show alice pensando
    ali "Eh... ya- ya veo..."
    # pla "¿Y a ti cómo te fue?"
    # ali "Ah, bu- bueno, no me- me quejo, je, je, je."
    pla "Uhm..."
    "Incliné un poco la cabeza, algo me está ocultando. Alice comenzó a verme con recelo."
    pla "¿Estás escondiendo algo detrás de ti?"
    show alice sorprendida
    ali "¿Ah? Cla- claro que no..." with hpunch
    pla "¿En serio?"
    pla "Veo que tus manos no se despegan de tu espalda..."
    show alice pensando
    ali "Je, je, je, estás imaginando cosas..."
    pla "¿Ah, sí? Déjame ver..."
    "Me acerqué a Alice a la vez que giro un poco para ver lo que estaba escondiendo."
    play music comico fadein 2
    show alice sorprendida
    ali "¿¡Qu- que te deje ver!?" with vpunch
    show alice asustada
    ali "¡No, no, no!"
    ali "¡No te dejaré ver mi trasero!"
    pla "¿¡Qué!?" with hpunch
    show alice pensando at temblor
    ali "¡Pe- pervertido! ¡Te denunciaré por acoso!"
    pla "¡Deja de decir estupideces y muestrámelo!"
    show alice asustada
    ali "¡Nooo!" with hpunch
    extend " ¡No le pidas eso a una chica decente!"
    show alice:
        parallel:
            temblor
        parallel:
            linear 0.3 right
            ease .5 center
    pla "¡¡¡Aaaahhh!!!"
    show alice:
        parallel:
            temblor
        parallel:
            linear 0.3 left
            ease .5 center
    pla "¡Ven acá!"
    show alice:
        parallel:
            temblor
        parallel:
            linear 0.3 right
            ease .5 center
    show alice:
        parallel:
            temblor
        parallel:
            linear 0.3 left
            ease .5 center
    pause .9
    ali "¡Nooooo!"
    show alice:
        parallel:
            temblor
        parallel:
            linear 0.3 right
            ease .5 center
    pla "¡Alice!"
    #alice de un lado a otro
    "Comenzamos una pequeña persecución."
    "A medida que yo trataba de ver su espalda, ella se giraba rápidamente."
    "Aproveché un descuido cuando giré de improviso, lo que la tomó por sorpresa."
    show alice sorprendida at center
    "Entonces le pude arrebatar la pila de papeles que escondía." with hpunch
    ali "¡Ah!"
    pla "Me lo suponía..."
    show alice pensando
    pla "Creo que aquí están casi todos los volantes con los que comenzaste..."
    show alice sorprendida
    pla "¡No has entregado ninguno!" with hpunch
    show alice normal
    ali "¡Cl- claro que no! Yo... ehm... entregué solo uno..."
    pla "¿Ah, sí? ¿A quién?"
    show alice pensando
    ali "Al profesor tutor de mi salón..."
    pla "Lo cual no es muy útil..."
    "Qué decepción..."
    show alice at decaer
    ali "Lo- lo siento..."
    ali "Nadie quiso recibir un volante..."
    "Al ver su reacción, noté que ella de verdad estaba apenada por el resultado."
    # "Lo que parecía indicar que ella no estaba haciendo el vago por ahí..."
    "Qué debo hacer..."
    stop music fadeout 10
    menu:
        "Ayudarle a repartir volantes":
            show alice normal at reponerse
            pla "Todavía hay tiempo..."
            ali "¿Eh?"
            pla "Vamos, no te quedes parada ahí."
            pla "Te ayudaré a entregar volantes."
            pla "Todavía hay estudiantes rondando por la escuela que no están en un club."
            show alice sonrojada
            ali "[pla_name]..."
            extend " gracias..."
            $ updateStat("carisma","+",1)
            $renpy.notify("Carisma +1")
            pla "Ya, vamos, no perdamos el tiempo..."
            show alice sonriendo
            ali "Sí..."
            pla "¿Sherinford no te acompaña?"
            ali "No, le gusta estar aquí."
            pla "Eh... así que se mantiene en el salón, ya veo..."
        "Eso es todo por hoy":
            pla "¿Y con esa actitud planeas restaurar el club?"
            pla "Pues vaya ayuda..."
            ali "Lo siento..."
            pla "Como sea, lo dejaremos hasta aquí."
            pla "Ya mañana será otro día."
            pla "He entregado suficientes volantes, así que no importa."
            $ updateStat("carisma","-",1)
            $renpy.notify("Carisma -1")
            ali "E- entiendo..."

    scene bg negro with dissolve
    hide screen quick_menu
    $quick_menu=False
    window hide
    pause 2

    jump caso1_inicio
