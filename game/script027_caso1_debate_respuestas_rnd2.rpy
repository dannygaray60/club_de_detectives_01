label d1r2_incorrecto_marissa:
    jump d1r0_incorrecto_marissa

label d1r2_incorrecto_beck:
    $change_cursor()
    $clearDebateText()
    $quick_menu_bajo=False
    show beck enojado
    bec "¿Eh?"
    $restCorazones()
    bec "¿Qué rayos pretendes demostrar con eso?" with hpunch
    jump inicio_d1r2

label d1r2_correcto:
    stop music fadeout 1
    $clearDebateText()
    $change_cursor()
    $addCorazones()
    $showplay_excl("esonoescierto")
    $quick_menu_bajo=False
    # $quick_menu_gameplay = False
    hide screen debateArgumento
    $hide_gameplay_layout()
    play music tiempo_muerto fadein 2
    pla "Te equivocas, Beck."
    bec "¿Eh? Explícate..."
    pla "No creo que sea posible que el acosador sea del mismo club que Marissa..."
    pla "Alice, ¿recuerdas lo que nos dijo ella cuando vino a pedirnos ayuda?"
    show beck:
        ease .5 mleft
    show alice pensando at mright with dissolve
    ali "Uhm..."
    show alice sorprendida
    play sound campana
    extend " ¡Ah! {amarillo}Nos contó en qué lugares se sentía acosada.{/amarillo}" with flashbulb
    pla "Exacto, y el único lugar que no mencionó es el {amarillo}club de cocina.{/amarillo}"
    show beck:
        ease .5 left
    show alice:
        ease .5 right
    show marissa normal with dissolve
    mar "Ahora lo recuerdo..."
    mar "Es cierto, tenía esa sensación que solo en el club me sentía segura..."
    show beck sorprendido
    bec "¿Una sensación?"
    show beck pensando
    bec "Lo veo algo flojo como para ser una pista o algo por el estilo..."
    pla "Lo sé, pero es lo que tenemos."
    pla "Pienso que es buena idea {amarillo}partir desde ese punto de vista.{/amarillo}"
    show beck preocupado
    bec "Está bien..."
    bec "Ustedes son los \"detectives\", deben saber lo que están haciendo..."
    bec "..."
    $renpy.choice_for_skipping()
    $renpy.save("checkpoint")
    show beck pensando
    bec "De lo que [pla_name] me ha contado... hay algo que no entiendo..."
    jump caso1_debate_rnd3