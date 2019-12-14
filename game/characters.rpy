## para cambiar color de namebox, agregar: show_custom_namebox="gui/namebox_red.png"

init:
    
    ## la narración y pensamientos de jugador
    define narrator = Character(ctc="ctc_blink", ctc_position="fixed", callback=sound_ctc)
    ## la narración y pensamientos de jugador
    define nvlm = Character(kind=nvl,ctc="ctc_blink_nvl", ctc_position="nestled", callback=sound_ctc)
    define nvl_narrator = Character(kind=nvl,ctc="ctc_blink_nvl", ctc_position="nestled", callback=sound_ctc)
    ## para mostrar mensajes de tutorial
    define tuto = Character("Tutorial", ctc="ctc_blink", ctc_position="fixed", what_color="#48B5E3", callback=sound_ctc,show_custom_namebox="gui/namebox_tuto.png")
    ## El jugador antes de tener nombre
    # define yo = Character("Yo", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_player.png")
    ## Personaje desconocido
    define unk = Character("???", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt)
    ## El jugador
    define pla = Character("[pla_name]", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_player.png")

    define ali = Character("Alice", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_alice.png")
    define she = Character("Sherinford", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_tuto.png")
    define bec = Character("Beck", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_beck.png")
    define nei = Character("Neil", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_neil.png")
    # define cla = Character("Claire", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt)
    define hat = Character("Hatty", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_hatty.png")
    define hel = Character("Hellen", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_hellen.png")
    define hel_hat = Character("Hellen y Hatty", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_hel_hat.png")
    define hen = Character("Henry", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_okamoto.png")
    # define jan = Character("Jane", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt)
    define mar = Character("Marissa", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_marissa.png")
    define mary = Character("Prof. Harrow", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_mary.png")
    define kat = Character("Katherine", ctc="ctc_blink", ctc_position="fixed", callback=sound_txt,show_custom_namebox="gui/namebox_hatty.png")