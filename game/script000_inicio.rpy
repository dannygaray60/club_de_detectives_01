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
   "It turns out that {amarillo} I couldn't attend the first day of school{/amarillo} because I got sick."
     "Therefore, I missed the opening ceremony and the announcement about the new regulations that will be implemented at the school."
     "In front of me was {amarillo}Professor Mary Harrow.{/amarillo} Known as {i}\"The Maiden of Numbers\"{/i}."
     "Although I would rather call her {i}\"Mathematical hell turned into a woman\"{/i}."
     "How original I am..."
     show mary hablando
     mary "Are you listening to me?"
     pla "hu- huh? Ah, yes...loud and clear..." with hpunch
     show mary normal
     "What was she talking about!?"
     "I decided to stop with my internal monologue, so as not to anger Professor Harrow."
     "Nobody, absolutely {amarillo}nobody wants to see her angry...{/amarillo}"
     mary "The school year has barely started, and you're late..."
     "{i}*Corrección*{/i} I think I am in trouble..."
     pla "Ah... We-well... I... um..."
     "While I stammered, looking for a justification, the teacher continued speaking."
     show mary hablando
     mary "I hope this isn't going to become a new habit of yours."
     show mary normal	
     pla "N-No! Of course not!"
     pla "I promise it won't happen again!"
     mary "You are already in your {amarillo}fourth year of high school{/amarillo}, you must set an example for the lower years."
     mary "It is disrespectful towards the institution to come school without justification."
     mary "This is not to be repeated, understand?"
     pla "Yes, ma'am!"
     mary "Excuse me?"
     pla "Ah! I mean...understood, Professor Harrow..."
     "Fourth year..."
     "I only have this year and the next to finish high school."
     "Sure, if I manage to get grades that don't drop below average..."
     pla "And what are those new regulations you were talking about?"
     "I started to change the subject, before the teacher also scolded me for the low grades I got last year."
     mary "Huh?"
     mary "Have you already forgotten? I just explained it to you."
     " \"I just didn't pay attention to it\". Obviously I won't say that..."
     pla "Yes, I know, but I wanted to make sure I heard clearly."
     show mary pensando
     mary "..."
     mary "Oh, well..."
     show mary normal
     mary "Starting this year, the school will be more flexible regarding the use of the uniform."
     mary "In other words, {amarillo}it will not be mandatory to wear the uniform.{/amarillo} Although it is only allowed for first-timers."
     pla "I understand..."
     mary "However, now {nw}"
     play sound campana
     extend "{amarillo}it will be obligatory for students to belong to a club.{/amarillo}" with flashbulb
     pla "Huh!?" with hpunch
     pla "That now it will be an obligation to belong to a club?"
     pla "why?"
     show mary hablando
     mary "The new principal, apparently is someone who comes up with {amarillo}new ideas{/amarillo} to implement in education."
     mary "He is a young person who, according to his words, seeks to make education something \"more fun\"."
     mary "I know it's not supposed to be like that... But those are the rules now."
     show mary normal
     pla "Wait..."
     pla "So education shouldn't be fun?"
     show mary hablando
     mary "That's right, education is rather a {amarillo}commitment{/amarillo} of the student to himself to build a good future for himself."
     show mary normal
     mary "Studies should not be taken as a game."
     "It becomes apparent that Professor Harrow has a slightly {amarillo}old {/amarillo} thinking about education."
     "No wonder her math class was torture..."
     show mary pensando
     mary "Extracurricular activities can only distract students from their true duties..."
     "Haven't clubs been created in this school to motivate the student to attend classes?"
     "Suddenly I remembered that I once heard that since the creation of different clubs, the school attendance increased."
     "And I haven't seen that that's a problem for academic performance."
     "Just look at me, I have fair grades and I don't belong to a club..."
     "Wait..."
     pla "That will be a problem..."
     show mary normal
     mary "Uhm?"
     pla "I'm not involved in a club..."
     "And I don't have the interest to join one either."
     mary "All people who are not members of a club have {amarillo}two months{/amarillo} to do so."
     pla "And if I don't join a club?"
     mary "That means breaking the rules, and you should already know what the consequences are."
     pla "Ah... I understand..."
     "I have no choice..."
     extend "In the end, I'll have to join a club."
     show mary pensando
     mary "Well, that's more or less what you needed to know."
     show mary normal
     mary "You stayed in section {nw}"
     play sound campana
     extend "{amarillo}\"4-A\"{/amarillo}." with flashbulb
     mary "You can go now. Classes will start in half an hour."
     pla "Okay."
     "I settled my backpack on my shoulder before leaving, somewhat discouraged by this new rule of belonging to a club..."
     show mary hablando
     mary "Oh, by the way, {nw}"
     play sound campana
     extend "{amarillo}I'll be in charge of section 4-A{/amarillo}." with flashbulb
     pla "Eeeehhh!?" with hpunch
     "What was missing..."
     "The firmest teacher in the entire school, Professor Harrow, will be the tutor of my section..."
     "I see it coming..."
     "Studies will become a real hell..."
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
     "{amarillo}- A few days later... -{/amarillo}"
     window show
     scene bg escuela corredor with dissolve
     pause 1
     "When Friday arrives, that's when I really start to worry about looking for a club."
     "Right now it's two o'clock, which is when classes end."
     "Therefore, I'll take advantage of this free time to go visit some clubs, and see if any catch my eye."
     scene bg negro
    show sepia
    show bg salon clases club dia behind sepia 
    play sound flash
    show claire timida behind sepia with flashbulb
     pause 1
     "First I went to the literature club."
     "In that place I noticed that its members are very quiet, or rather... a bit shy?"
     "{amarillo}The president of the club{/amarillo}, Claire Bellamy, explained to me the activities they were doing..."
     "And to tell the truth, I found them somewhat boring..."
    scene bg negro
    show sepia
    show bg salon cocina dia behind sepia 
    play sound flash
    show marissa alegre hablando behind sepia with flashbulb
     pause 1
     "At the cooking club, things were different."
     "There was a more pleasant atmosphere in that club."
     "Most of the members in that club were women."
     "One of them, {amarillo}Marissa Morstan{/amarillo }, happily told me about the activities at the club."
     "At the same time that I listened to her, I enjoyed eating some cakes that they offered me as an example of their talents."
     "They were really delicious."
     "When I left the room, I left with a good impression of that club, although..."
     "I was still not convinced..."
    scene bg negro
    show sepia
    show bg salon musica dia behind sepia 
    play sound flash
    show jane normal behind sepia with flashbulb   pause 1
     "In the music club, things were a bit noisy."
     "Its members were very talkative and somewhat eccentric, with the exception of one girl."
     "She introduced herself as {amarillo} Jane Stoner {/amarillo}."
     "And she only said her name..."
     "To all my questions, she gave me a one-word answer."
     "And if it was possible, she would answer me with a head nod."
     "Besides, her look and her tone of voice made me believe that everything was alien to her."
     "Anyway, for what little communication skills she has, she has guitar skills to spare."
     "In short, it was a lively and noisy club, although their musical tastes were not according to mine..."
     scene bg negro with dissolve
     "I was wandering around the club building..."
     “But in the end, I was still unsure…”
     "All clubs have their good and bad things..."
     scene bg escuela corredor clubes tarde with dissolve
     play music ambiente fadein 6
     "And with that, I've already visited all the clubs in the school..."
     "Or so I thought."
     "After taking a general look at the corridor of the building where the clubs are..."
     "I realized there's still a salon I haven't been to."
     "It is the last room in the corridor where I am, and also the door is closed."
     pla "Maybe it's a warehouse..."
     "That was my reasoning, since in the other building of the school, where the classrooms are, there is also a store at the end of the corridor."
     pla "Well, it looks like I don't have anything else to do here today..."
     show alice normal with dissolve:
         center
         linear 3 right
     pause 0.5
     hide alice with dissolve
     # "Suddenly, I heard the sound of a door closing."
     Pla "Huh?"
     "Out of the corner of my eye I saw that a person had entered the same room that I considered a warehouse."
     pla "..."
     extend "..."
     extend "..."
     "Motivated by curiosity, I walked with hesitant steps towards the same room."
     pla "The door is open..."
     play sound flash
     stop music fadeout 1
     scene bg salon club detectives with flashbulb:
         # pause 1
         xpan -60
         linear 8 xpan 60
     pause 3
     "Wow..."
     "Little by little, I went deeper into the room."
     "I was shocked to see how many things are here."
     "I saw a series of curious objects on top of a ledge."
     "There were some statues, also a wig... and other artifacts that looked like antiques."
     "I also noticed that some clothes were hanging on a wall."
     "On a small table is...a lie detector? It looked just like the one in the movies."
     "There are also other trinkets and a pile of papers, as well as old books."
     "Anyway, there were so many things in that place; it really looked like a warehouse."
     show alice sorprendida with dissolve
     pause 1.5
     unk "Huh?" with hpunch
     pla "H-hello..."
     unk "Uh... er... my time is up, right?"
     pla "..."
     play music ambiente3 fadein 4
     extend " Excuse me?"
     show alice pensando at decaer
     unk "Uh... at least let me say goodbye to this room..."
     unk "There are so many memories here..."
     unk "It's painful for me to be separated from this place..."
     show alice sorprendida at reponerse
     pla "Hey! What the hell are you talking about!?" with hpunch
     pla "I am not the death that has come for your soul."
     unk "Huh?"
     "The girl looked at me in surprise, as if she didn't understand my words."
     unk "What are you talking about?"
     pla "Huh?"
     "What the hell..."
     show alice normal
     unk "..."
     unk "Wait, aren't you from the {amarillo}student committee{/amarillo}?"
     pla "Um... no."
     show alice pensando at decaer
     unk "Ah... thank goodness..."
     "The girl then let out a sigh of relief, as she sat on a stool, as if her life was in danger recently."
     pla "Er... excuse me, I made the wrong room, I didn't mean to come here to bother you."
     "I decide to retire. This place is weird."
     show alice sorprendida at reponerse_rapido
     unk "W-wait!" with hpunch
     "Suddenly, the girl stood up, and at the same time she positioned herself in front of the exit."
     "I have a bad feeling..."
     pla "W-what do you want?"
     show alice sonriendo
     unk "If you're not from the student council..."
     show alice alegre
     unk "Then you're a customer right!?" with hpunch
     pla "What?"
     show alice at brinquitos
     unk "Welcome to the {amarillo}detective club{/amarillo}!"
     show alice sonriendo
     pla "Detective... club?"
     pla "So this place wasn't a warehouse?"
     show alice enojada	
     unk "Of course not!" with hpunch
     pla "I... I see..."
     pla "Well, look... erm..."
     "I interrupted my sentence by not knowing her name."
     show alice sonriendo
     unk "Ah, my manners. I'm {amarillo}Alice Baskerville{/amarillo}! Nice to meet you!"
     "Baskerville?"
     "Could he be from a rich family?"
     show alice normal
     pla "Ah, good. Alice, I think you're getting it wrong, I'm not a customer."
     pla "I just passed by chance and this room caught my attention..."
     show alice alegre at brinquitos
     ali "Ah! So you're here to join the club!?"
     "Without letting me finish speaking, Alice continued to jump to the wrong conclusions."
     show alice sonriendo
     ali "Wait a minute, I'll bring a registration form."
     show alice sorprendida
     pla "Hey! I'm not here for that either!" with hpunch
     pla "I just came out of pure curiosity, and..."
     show alice sonriendo
     ali "Great! Being curious is an important quality for a good detective!"
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
