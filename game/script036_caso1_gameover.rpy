label caso1_gameover:
    $persistent.gameover_counter[id_partida]+=1
    $hide_gameplay_layout()
    stop music fadeout 1.0
    $quick_menu_gameplay = True
    $quick_menu_timescr=False
    scene bg negro with slow_dissolve
    "Al final, no pudimos ayudar a Marissa a resolver su problema."
    "Después de esto, no llegó otro caso al club."
    "El tiempo pasó... y entonces... El comité estudiantil cerró el club de detectives."
    hide screen quick_menu
    $quick_menu=False
    window hide

    call screen game_over
    play sound game_over3
    scene bg negro with dissolve
    pause 2
    return