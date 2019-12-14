init python:

    #desactivamos self... y access...
    config.keymap['self_voicing']=[]
    config.keymap['accessibility']=[]
    ##auto avance en letra a
    config.keymap['toggle_afm'].append('a')

    ## para versiones de "no desarrollo"
    if not config.debug:
        ##removemos botones que hacen retroceder el script/dialogo
        config.keymap['rollback']=[]
        #creates keymap "history"
        config.underlay.append(renpy.Keymap(history = ShowMenu("history"))) 
        ##Y en cambio, los controles originales del rollback activarán el historial
        config.keymap["history"] = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ]

    ##configurar teclas para gamepad (posiblemente en un futuro...)