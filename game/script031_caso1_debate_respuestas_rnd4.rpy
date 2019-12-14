label d1r4_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r4_incorrecto_alice:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show alice sonriendo
    ali "[pla_name], me alegra que estés tan involucrado en el debate..."
    $restCorazones()
    show alice enojada
    ali "¡Pero ese argumento no explica muy bien sobre cómo llegó la carta a Marissa!" with hpunch
    jump inicio_d1r4

label d1r4_incorrecto_beck:
    jump d1r3_incorrecto_beck

label d1r4_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("esoescierto")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2

    show alice sorprendida
    
    pla "Tienes razón, Alice."
    ali "¿Eh?"
    pla "La carta no llegó hasta Marissa{nw}"
    play sound campana
    extend " {amarillo}dentro del salón...{/amarillo}" with flashbulb
    pla "Sino afuera, específicamente {amarillo}en la entrada.{/amarillo}"
    show alice normal:
        ease .5 mright
    show marissa preocupada sudor at mleft with dissolve
    mar "¿¡En la entrada!?" with hpunch
    mar "¿Cómo puede ser posible?"
    show alice sorprendida
    play sound campana
    ali "{amarillo}¡El momento cuando Marissa se tropezó{/amarillo} con la profesora Harrow!" with flashbulb
    pla "Correcto."
    show alice normal:
        ease .5 right
    show marissa normal:
        ease .5 center
    show beck sorprendido at left with dissolve
    bec "¿¡Ehhh!? ¡E- espera! ¿¡De qué están hablando!?" with hpunch
    $renpy.choice_for_skipping()
    bec "¿Cómo pueden estar seguros de eso?"
    pla "Posiblemente, alguien..."
    show beck preocupado
    $renpy.save("checkpoint")
    label tropiezo_alguien_pudo:
        show screen corazones
        if cantidad_corazones==0:
            jump d1_gameover
        menu:
            "\"... aprovechó el momento.\"":
                mar "Así que me estás diciendo que..."
                $renpy.save("checkpoint")
                show screen corazones
                show marissa preocupada sudor
                mar "¿Alguien aprovechó la confusión del momento y metió la carta en mi bolso?"
                show marissa normal
                mar "Uhm... eso explicaría mucho..."
                show marissa preocupada
                mar "¿Y quién pudo haberlo hecho?"
            "\"... tomó el bolso de Marissa.\"":
                show marissa preocupada
                mar "Creo que en ningún momento mencioné eso."
                $restCorazones()
                pla "¿En serio?" with hpunch
                pla "Perdón, error mío..."
                jump tropiezo_alguien_pudo

    pla "Es muy fácil, esa persona es..."
    
    label esa_persona_es:
        show screen corazones
        if cantidad_corazones==0:
            jump d1_gameover
        menu:
            "Beck Doran":
                show beck sorprendido
                bec "¿Es una broma, no?"
                show beck enojado
                $restCorazones()
                bec "Yo ni siquiera estuve tan cerca como para hacer eso." with hpunch
                show beck preocupado
                jump esa_persona_es
            "Profesora Harrow":
                show marissa sorprendida
                mar "¿¡EEEEEEEHHHH!?" with hpunch
                mar "¿¡La- la- la- la profesora Harrow me dio esa carta!?"
                show alice enojada
                $restCorazones()
                ali "¡[pla_name]! ¡No es hora de estar bromeando!" with hpunch
                pla "Eh- pe- perdón..."
                show alice normal
                show marissa normal
                jump esa_persona_es
            "Neil London":
                play sound campana
                show marissa sorprendida
                mar "¿Neil London?" with flashbulb
                mar "¿De quién estás hablando?"
            "Fui yo":
                show beck serio
                bec "..."
                show marissa enojada
                mar "..."
                show alice enojada
                ali "..."
                pla "Je- je- je..."
                $restCorazones()
                pla "Qué momento más incómodo..." with hpunch
                show alice normal
                show marissa normal
                jump esa_persona_es

    $addCorazones()
    pause 2
    hide screen corazones
    pla "La persona que ayudó a la profesora Harrow y a ti a recoger las cosas que se cayeron al suelo cuando ustedes tropezaron."
    show marissa preocupada sudor
    mar "¿Eh? ¿Hablas de esa persona? ¿Acaso lo conocías?"
    pla "No, pero estuve hablando con él..."
    bec "Eh..."
    bec "Así que ese es el sospechoso."
    pla "Algo así..."
    ali "[pla_name]... ¿no pensarás llamarlo, o sí?"
    pla "No hay de otra..."
    mar "¿¡Eeehh!?" with hpunch
    show marissa normal
    show beck guino
    bec "No te preocupes Marissa, si ese tipo se te acerca yo te defenderé."
    mar "Beck... gracias..."
    pla "..."
    pla "No tardaré, llamaré a Neil para que venga a este salón."
    stop music fadeout 3
    $hora=15
    scene bg negro with fade
    $quick_menu_gameplay=False
    "Al salir del salón, busqué en mi bloc de notas el número que Neil había escrito, y lo llamé."
    "Le dije que necesitaba hablar con él acerca del tropiezo en el salón del club."
    "Y para sorpresa mía, él aceptó felizmente..."

    scene bg salon club detectives with dissolve

    show neil normal with dissolve
    pause 2
    show neil:
        ease .5 mleft
    show marissa preocupada sudor at mright with dissolve
    nei "..."
    mar "E- eres tú..."
    "Marissa se puso a la defensiva al ver a Neil."
    nei "Eh... hola..."
    nei "¿Por qué me ves de esa manera?"
    show neil:
        ease .5 left
    show marissa normal:
        ease .5 right
    show beck enojado with dissolve
    bec "Oye, no te le acerques."
    show neil sorprendido
    nei "¿Eh? ¿Qué está pasando?"
    nei "Hey, [pla_name], ¿por qué todos me están viendo como si hubiera hecho algo malo?"
    nei "¿Acaso no me llamaste para hablar acerca del tropiezo de la profesora Harrow?"
    pla "Eh... pues algo así..."
    pla "Neil,{nw}"
    play sound campana
    extend " {amarillo}eres sospechoso de acosar a Marissa.{/amarillo}" with flashbulb
    show neil pensativo
    nei "..."
    nei "¿Disculpa?"
    show neil sorprendido
    nei "¿¡Yo!? ¿Que estoy acosando a... Marissa?" with hpunch
    nei "¿Qué pruebas tienes de eso?"
    show neil pensativo
    pla "Mira, solo queremos resolver el problema de Marissa, si tú no eres el acosador, puedes decirnos solamente la verdad."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    nei "..."
    nei "Está bien, jugaré a su juego."
    pla "Oye... esto no es un juego..."
    jump caso1_debate_rnd5