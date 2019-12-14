label caso1_investigacion2:
    play music ambiente fadein 5
    scene bg escuela frente dia with dissolve
    "Al día siguiente, me encontré con Marissa afuera de la escuela, poco más de media hora antes de que comenzaran las clases."
    show marissa alegre with dissolve
    mar "¡[pla_name], buenos días!"
    "Frente a mí, estaba una Marissa totalmente diferente a la que yo vi frente a la profesora Harrow."
    pla "Buenos días, Marissa."
    show marissa alegre hablando
    mar "¿Y cómo va la investigación?"
    pla "Eh... bien... vamos avanzando."
    show marissa normal
    mar "¿Con que es así?"
    show marissa alegre at brinquitos
    mar "¡Qué bueno!"
    pla "Y la verdad, es que ayudó bastante enterarme de tu incidente con la profesora de matemáticas..."
    show marissa apenada at decaer
    mar "Ah, eso..."
    pla "Hubiera sido mejor que nos lo hubiera contado antes..."
    show marissa preocupada sudor at reponerse
    mar "Bueno..."
    extend " no pensé que fuera importante..."
    show marissa apenada
    mar "Además, es algo vergonzoso lo que pasó..."
    pla "Aunque sea vergonzoso, ahora necesito que me contestes algunas preguntas."
    show marissa sorprendida
    mar "¿Eh? ¿Aquí?"
    "Marissa vio a sus alrededores..."
    "Tomando en cuenta lo que nos dijo a Alice y a mí, sobre lo de mantener esto con la mayor discreción posible..."
    "Obviamente no podemos seguir hablando acá."
    show marissa normal
    pla "Vamos al salón del club, ahí nos está esperando Alice."
    mar "E- está bien..."
    scene bg negro with slow_dissolve
    pause 1.5
    scene bg salon club detectives with dissolve
    show alice normal with dissolve
    pause 1
    show alice sonriendo
    show sherinford pequeño at center with dissolve:
        ypos .200
        xoffset 10
    ali "Buenos días, [pla_name]."
    she "¡Pío, pío, pío!"
    pla "Buenos días a los dos..."
    show alice normal:
        ease .5 mright
    show sherinford pequeño:
        ypos .200
        ease .5 xpos 0.650
        xoffset 10

    show marissa alegre at mleft with dissolve
    mar "¡Hola, buenos días, Alice!"
    mar "¡Hola, pollito!"
    show alice pensando
    ali "Bu- buenos días..."
    show alice normal
    show marissa normal
    pla "Bien, vayamos directo al grano."
    mar "¿Qué necesitan saber?"
    # pla "Sabemos lo que pasó el viernes, pero ahora..."
    play sound campana
    show marissa preocupada sudor
    pla "Tienes que contarnos todo {amarillo}sobre ese incidente.{/amarillo}" with flashbulb
    pla "Específicamente, desde el tiempo libre que ustedes tuvieron."
    hide sherinford with dissolve
    hide alice with dissolve
    show marissa normal:
        ease .5 center
    mar "Está bien..."
    stop music fadeout 1.5
    jump caso1_testimonio4