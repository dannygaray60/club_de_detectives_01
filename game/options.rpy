
## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Club de Detectives - Caso #01")

init -2:
    ## version de desarrollo?
    define config.debug = False
    define config.developer = False

## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para esconder el título.

define gui.show_name = True

## Versión del juego.
define config.version = "1.0"

## alpha, beta, final...
define version_state = "final"


## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""
    {size=-5}{b}Concepto y guion{/b}{/size}{p}
    {size=+5}{a=http:/dannygaray60.blogspot.com}Danny Garay{/a}{/size}

    {size=-5}{b}Arte de personajes (sprites){/b}{/size}{p}
    {size=+5}Tokudaya{/size}

    {size=-5}{b}Ilustraciones adicionales{/b}{/size}{p}
    {size=+5}Danny Garay{/size}

    {size=-5}{b}Escenarios{/b}{/size}{p}
    {size=+5}loo.sakura.ne.jp{/size}{p}
    {size=+5}Pixabay.com{/size}{p}
    {size=+5}LindaHicks{/size}{p}
    {size=+5}Wokandapix{/size}{p}
    {size=+5}Ajalfalro{/size}{p}
    {size=+5}Uncle Mugen{/size}

    {size=-5}{b}Música de fondo{/b}{/size}{p}
    {size=+5}Amacha{/size}{p}
    {size=+5}Kevin Macleod{/size}{p}
    {size=+5}Eric Matyas{/size}{p}
    {size=+5}Vibe Mountain{/size}{p}
    {size=+5}Asher Fulero{/size}{p}
    {size=+5}Dead Seed (Namastaii){/size}{p}
    {size=+5}Silent Partner{/size}

    {size=-5}{b}Efectos de sonido{/b}{/size}{p}
    {size=+5}Freesound.org{/size}{p}
    {size=+5}Taira Komori{/size}

    {size=-5}{b}Programación y diseño gráfico{/b}{/size}{p}
    {size=+5}Danny Garay{/size}

    {size=-5}{b}Jugadores beta (sin ningún orden en particular).{/b}{/size}{p}
    {size=+5}Pablo Canché, Alexis Sánchez, Marcos Lopez, Davar Osorio, Danny Huerta, Iván Medina, Bill García, Williams Chia, Deivid Navarro, Juan Cruz, Matías Barraza, Jeremy Garrido, Sebas BZ, José Veintimilla, Daniel Castro, Juan Vicente, Michel Hernández, Juan Manuel, Ramiro Segovia.{/size}
""")


## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "Club_de_Detectives_Caso_01"

## desactivar autosave y quicksave
define config.has_autosave = False
define config.has_quicksave = False
define config.autosave_frequency = None


## Sonidos y música ############################################################
## agregamos un canal de audio llamado txt
init python:
    renpy.music.register_channel("text",mixer="txt")
define config.default_sfx_volume = 0.8
## Estas tres variables controlan los mezcladores mostrados por defecto al
## jugador. Ajustar alguno a 'False' para esconderlo.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## Para permitir al usuario probar el volumen de los canales de sonido o voz,
## descomenta la línea más abajo y ajústala a un sonido de ejemplo.

define config.sample_sound = "audio/sfx/coin.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Descomenta la línea siguiente para ajustar un archivo de audio que sonará en
## el menú principal. Este archivo seguirá sonando en el juego hasta que sea
## detenido o se reproduzca otro archivo.

define config.main_menu_music = audio.tema_principal


## Transiciones ################################################################
##
## Estas variables ajustan transiciones usadas ante ciertos eventos. Cada
## variable debe indicar una transición o bien 'None', cuando no se desea usar
## ninguna transición.

## Entrar o salir del manú del juego.
define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre pantallas del menú del juego.
define config.intra_transition = dissolve


## Transición tras la carga de una partida.
define config.after_load_transition = fade


## Transición de acceso al menú principal tras finalizar el juego.
define config.end_game_transition = dissolve


## No existe la variable que ajusta la transición cuando el juego comienza. Para
## ello se usa la sentencia 'with' al mostrar la escena inicial.


## Gestión de ventanas #########################################################
##
## Esto controla cuándo se muestra la ventana de diálogo. Si es "show", es
## siempre visible. Si es "hide", solo se muestra cuando hay diálogo presente.
## Si es "auto", la ventana se esconde antes de las sentencias 'scene' y se
## muestra de nuevo cuando hay diálogo que presentar.
##
## Una vez comenzado el juego, esto se puede ajustar con las sentencias "window
## show", "window hide", y "window auto".

define config.window = "show"


## Transiciones usadas para mostrar o esconder la ventana de diálogo
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 60

## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 20


## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "Club_de_Detectives_01"

define config.default_fullscreen = True


## Ícono #######################################################################
##
## El ícono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:

    noInteract(False)

    ## Las funciones siguientes toman patrones de archivos. No son relevantes
    ## las mayúsculas o minúsculas. Son relativos al directorio base, con o sin
    ## una / inicial. Si corresponden más de un patrón, se usa el primero.
    ##
    ## En un patrón:
    ##
    ## / es el separador de directorios.
    ##
    ## * corresponde a todos los carácteres, excepto el separador de
    ##   directorios.
    ##
    ## ** corresponde a todos los carácteres, incluynedo el separador de
    ##    directorios.
    ##
    ## Por ejemplo, "*.txt" corresponde a los archivos .txt en el directorio
    ## de base, "game/**.ogg" corresponde a los archivos .ogg del directorio
    ## 'game' y sus subdirectorios y "**.psd" corresponde a los archivos .psd en
    ## cualquier parte del proyecto.

    ## Clasifica archivos como 'None' para excluirlos de la distribución.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    if not config.debug:
        # Excluimos los scripts no compilados
        build.classify("game/**.rpy", None)
        ## carpetas para desarrollo
        build.classify('DEV/**.*', None)
        build.classify('game/dev_room/**.*', None)

        ## Para archivar, se clasifican como 'archive'.
        build.classify('game/images/**.png', 'archive')
        build.classify('game/images/**.jpg', 'archive')
        build.classify('game/gui/**.png', 'archive')
        build.classify('game/gui/**.jpg', 'archive')
        build.classify('game/**.ogg', 'archive')
        build.classify('game/**.otf', 'archive')
        build.classify('game/**.ttf', 'archive')

    ## Los archivos que corresponden a patrones de documentation se duplican en
    ## la distribución de mac; aparecerán en los archivos app y zip.

    build.documentation('*.html')
    build.documentation('*.txt')

## Ajusta la cadena que contiene tu 'Apple Developer ID Application' para
## permitir el firmado en Mac. Asegúrate de cambiarlo a tu propia ID facilitada
## por Apple.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## Es necesaria una clave de licencia Google Play para descargar archivos de
## expansión y realizar compras en la aplicación. Se puede encontrar en la
## página "Services & APIs" de la consola de desarrollador de Google Play.

# define build.google_play_key = "..."


## Los nombres de usuario y de proyecto asociados con un proyecto itch.io,
## separados por una barra.

# define build.itch_project = "renpytom/test-project"
