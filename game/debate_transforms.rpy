## similar a dissolve
transform aparecer:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0

transform centro_pantalla:
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5

transform zoom_alterno:
    parallel:
        linear 2.0 zoom 1.5
        linear 2.0 zoom 1.0
    repeat

transform girar:
    xanchor 0.5 yanchor 0.5
    rotate 0
    linear 4.0 rotate 360
    repeat

transform rebotar_en_pantalla:
    parallel:
        linear 2.0 xalign 0.1
        linear 2.0 xalign 0.980
        repeat
    parallel:
        linear 2.3 yalign 0.970
        linear 2.3 yalign 0.020
        repeat

#################################
# debate1 ronda0 ################
#################################

transform d1r0f0:
    ypos 0.3 xpos 0.2
    parallel:
        aparecer
    parallel:
        easein 2 ypos 0.350 xpos 0.150

transform d1r0f1:
    ypos 0.4 xpos 0.7
    parallel:
        aparecer
    parallel:
        easein 2 ypos 0.450 xpos 0.5

transform d1r0f2:
    xalign 0.5
    ypos 0.6
    parallel:
        aparecer
    parallel:
        easein 2 ypos 0.650
    parallel:
        linear 4 zoom 1.2

transform d1r0f3:
    xalign 0.5
    ypos 0.3
    parallel:
        aparecer
    parallel:
        easein 1 xpos 0.750

transform d1r0f4:
    xalign 0.5
    ypos 0.5
    parallel:
        aparecer
    parallel:
        easein 3 xpos 0.6

transform d1r0f5:
    parallel:
        aparecer
    parallel:
        easein 3 centro_pantalla
    parallel:
        zoom_alterno
    on hide:
        linear 0.5 ypos 1.0

transform d1r0f6:
    parallel:
        centro_pantalla
    parallel:
        aparecer
    parallel:
        easein 5 ypos 0.8
        

transform d1r0f7:
    parallel:
        d1r0f3
    parallel:
        pause 7
        linear .4 alpha 0.2

transform d1r0f8:
    zoom 3
    xpos .3 ypos .430
    parallel:
        aparecer
    parallel:
        easein 1 zoom 1
        pause 4
        linear .4 alpha 0.2

transform d1r0f9:
    zoom 3
    xpos .1 ypos .550
    parallel:
        aparecer
    parallel:
        easein 1 zoom 1
        pause 2
        linear .4 alpha 0.2

transform d1r0f10:
    zoom 5
    xpos .5 ypos .5
    rotate -40
    parallel:
        aparecer
    parallel:
        easein 1 zoom 1.2
    parallel:
        easein 1 xoffset -300 yoffset -400 
    zoom_alterno

#################################
# debate1 ronda1 ################
#################################

transform d1r1f0:
    xpos 0.1
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 70

transform d1r1f1:
    xpos 0.2
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r1f2:
    xoffset -50
    ypos 0.2
    parallel:
        aparecer
    parallel:
        ease .8 xoffset 200  


transform d1r1f3:
    xpos 1.0
    xoffset 200
    ypos 0.350
    parallel:
        aparecer
    parallel:
        ease 0.7 xoffset -500   


transform d1r1f4:
    xpos 0.7
    ypos 0.4
    zoom 5
    parallel:
        aparecer
    parallel:
        easein 1 zoom 1.2
    parallel:
        xoffset -500


transform d1r1f5:
    parallel:
        aparecer
    parallel:
        pass  

transform d1r1f6:
    parallel:
        aparecer
    parallel:
        pass  


transform d1r1f7:
    yoffset -300
    xalign 0.5
    parallel:
        aparecer
    parallel:
        ease 1 ypos 0.680
    parallel:
        ease 1 yoffset 0


transform d1r1f8:
    xpos .150
    ypos .2
    aparecer


transform d1r1f9:
    xpos .6
    ypos .3
    aparecer 


transform d1r1f10:
    xpos .150
    ypos .4
    aparecer 


transform d1r1f11:
    xpos .6
    ypos .6
    aparecer        


transform d1r1f12:
    zoom 5
    parallel:
        aparecer
    parallel:
        linear .9 zoom 1.2
    parallel:
        ease .5 xalign .5 yalign .5
    parallel:
        ease 0.250 yoffset 3
        ease 0.250 yoffset 0
        repeat
    parallel:
        easein .050 xoffset 2
        ease .150 xoffset -2
        easeout .050 xoffset 0
        repeat

#################################
# debate1 ronda2 ################
#################################

transform d1r2f0:
    xpos 0.1
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 200

transform d1r2f1:
    xpos 0.010
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r2f2:
    xalign  0.5
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 2 yoffset 450

transform d1r2f3:
    pass

transform d1r2f4:
    xpos 0.4
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r2f5:
    pass

transform d1r2f7:
    xpos 0.010
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 350

transform d1r2f11:
    xpos 0.7
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 350

#################################
# debate1 ronda3 ################
#################################

transform d1r3f3:
    xpos 0.3
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 350

transform d1r3f9:
    zoom 5
    parallel:
        aparecer
    parallel:
        linear .9 zoom 1.2
    parallel:
        linear .9 xpos 0.1
    parallel:
        pause 1
        linear 10 xoffset 400

#################################
# debate1 ronda4 ################
#################################

transform d1r4f1:
    xpos 0.050
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 400

transform d1r4f2:
    xpos 0.010
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 350

transform d1r4f3:
    xalign 0.5
    ypos 0.1
    parallel:
        aparecer
    parallel:
        easein 2 ypos 0.650
    parallel:
        linear 4 zoom 1.2

transform d1r4f4:
    zoom 5
    parallel:
        aparecer
    parallel:
        linear .9 zoom 1
    parallel:
        ease .5 xalign .5 yalign .5

transform d1r4f5:
    xpos 0.1
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r4f6:
    xpos 0.010
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 500

#################################
# debate1 ronda5 ################
#################################

transform d1r5f2:
    xalign 0.5
    ypos 0.3
    parallel:
        aparecer
    parallel:
        easein 1 xpos 0.650
    parallel:
        pause 7
        linear .4 alpha 0.2

transform d1r5f6:
    xpos 0.5
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 400

transform d1r5f10:
    xpos 0.5
    yoffset 400
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 280

transform d1r5f11:
    xanchor 1.0
    xoffset -5
    ypos 0.6
    parallel:
        aparecer
    parallel:
        linear 5 xoffset 10 xanchor 0.0 xpos 1.0

#################################
# debate1 ronda6 ################
#################################

transform d1r6f1:
    xalign 0.5
    ypos 0.3
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 90

transform d1r6f2:
    xalign 0.5
    ypos 0.3
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 200


transform d1r6f4:
    xpos 0.5
    yoffset -50
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r6f5:
    xalign 0.5
    ypos 0.3
    parallel:
        aparecer
    parallel:
        ease 1 yoffset 300

transform d1r6f6:
    xanchor 1.0
    xoffset -40
    ypos 0.3
    parallel:
        aparecer
    parallel:
        ease 1 xoffset 0 xpos .4

transform d1r6f7:
    xpos 1.0
    xoffset 40
    ypos 0.5
    parallel:
        aparecer
    parallel:
        ease 1 xoffset 0 xpos .2

transform d1r6f10:
    zoom 5
    parallel:
        aparecer
    parallel:
        linear .9 zoom 1.2
    parallel:
        ease .5 xalign .5 yalign .5

transform d1r6f13:
    xpos .3
    ypos .6
    aparecer 