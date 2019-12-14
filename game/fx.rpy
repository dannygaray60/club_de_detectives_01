# Efectos visuales personalizados

# para transiciones en escenarios (se usa con el scene bd XXX with nombreefecto)
#--------------------------

#un dissolve más suave que el estandar
define slow_dissolve = Dissolve(1.0)

define fast_dissolve = Dissolve(0.1)

#para hacer resplandor blanco al escenario
define flashbulb = Fade(0.2, 0.0, 0.5, color='#fff')

#barrido en circulo, indicando paso del tiempo
# define circlewipe = ImageDissolve("images/fx/imagedissolve circlewipe.png", 1.0, 8)
