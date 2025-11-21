define config.gl2 = True

transform center_pos:
    xalign 0.5 yalign 1.0
transform left_pos:
    xalign 0.25 yalign 1.0
transform right_pos:
    xalign 0.75 yalign 1.0

define k  = DynamicCharacter('k_name',  image='kein',   color="#8a2be2")
define n  = DynamicCharacter('n_name',  image='nikita', color="#ffff00")
define b  = DynamicCharacter('b_name',  image='belarus', color="#ff5555")
define ki = DynamicCharacter('ki_name', image='kiselman', color="#55aaee")
define r  = DynamicCharacter('r_name',  image='rolya', color="#ffaa33")

init python:
    k_name  = "Кейн"
    n_name  = "Никита"
    b_name  = "Беларус"
    ki_name = "Кисельман"
    r_name  = "Роля"

image nikita normal = "images/nikita/normal.png"
image nikita love   = "images/nikita/love.png"
image nikita ispug  = "images/nikita/ispug.png"
image nikita grust  = "images/nikita/grust.png"
image nikita smeh   = "images/nikita/smeh.png"
image nikita zloy   = "images/nikita/zloy.png"
image nikita pohot  = "images/nikita/pohot.png"

image kein normal  = "images/kein/normal.png"
image kein love    = "images/kein/love.png"
image kein ispug   = "images/kein/ispug.png"
image kein grus    = "images/kein/grus.png"
image kein smeh    = "images/kein/smeh.png"
image kein zloy    = "images/kein/zloy.png"
image kein pohot   = "images/kein/pohot.png"
image kein erotic  = "images/kein/erotic.png"

image belarus normal  = "images/belarus/normal.png"
image kiselman = "images/kiselman/normal.png"
image rolya normal = "images/rolya/normal.png"

image bg menu:
    "images/menu_bg.png"
    fit "cover"
image bg dorm_room_morning:
    "images/dorm_room_morning.jpg"
    fit "cover"
image bg spek_courtyard_morning:
    "images/spek_courtyard_morning.jpg"
    fit "cover"
image bg spek_stairs:
    "images/spek_stairs.jpg"
    fit "cover"


image bg black = Solid("#000000")
image logo = im.FactorScale("images/logo.png", 0.8)

define audio.bgm = "audio/backgroundMusic.mp3"
define audio.kein_laugh = "audio/kein_smeh.mp3"     
define audio.kein_theme = "audio/strahmusic.mp3"

init python:
    config.main_menu_music = audio.bgm