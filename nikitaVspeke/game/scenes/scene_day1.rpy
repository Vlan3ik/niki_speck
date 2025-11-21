label scene_day1:
    scene bg black with fade
    play music audio.bgm fadein 2.0

    scene bg dorm_room_morning with dissolve

    "Утро. 7:42. Будильник орёт «Мурку» на всю общагу."

    show nikita normal at center_pos with dissolve
    n grust "Бл… опять проспал…"
    n grust "Демоэкзамен в 9:00, а я ещё в кровати…"

    "Пытаюсь встать — нога цепляется за провод. Лечу мордой в тапок Роли."

    show nikita ispug at center_pos with vpunch
    n ispug "ФУУУУУУУУУУУУУУУУУУУУ!!!"

    show nikita zloy at center_pos
    show rolya normal at left_pos with moveinleft

    r "Доброе утро, товарищ! Чё орёшь, как империалист на митинге?"

    n zloy "Роля, сука… Ты опять в 7 утра картошку с говном жрёшь?!"

    menu rolya_potato:
        "Спокойно спросить, что внутри":
            n normal "Роль… это что за картошечка такая красивая?"
            r "Экспроприировал вчера в столовке. С мясом, говорят."
            n ispug "…Роля."
            r "Чё?"
            n zloy "ТАМ НЕ МЯСО, ТАМ ГАВНО, ИДИОТ!!!"
            r "Ну… белок же. Органика."

        "Взорваться сразу":
            n zloy "ТЫ ЕБУЧИЙ ПИДОРАС, РОЛЯ!!! ТЫ ОПЯТЬ ГОВНО ЖРЁШЬ!!!"
            r normal "Никита, гомофобия — пережиток капитализма."
            n zloy "А ГОВНО В ТВОЁМ РТУ — ЭТО ПЕРЕЖИТОК КОММУНИЗМА!!!"
            r "Маркс тоже ел всё подряд."
            n zloy "МАРКС НЕ ЖРАЛ КАКАШКИ ИЗ УНИТАЗА, ЛЫСЫЙ ДЕБИЛ!!!"

        "Молча уйти":
            n grust "…"
            r "Чё молчишь?"
            n grust "Считаю, сколько мне ещё терпеть тебя в одной комнате…"

    hide rolya with moveoutleft
    n normal "Ладно, побежал. Демоэкзамен сам себя не сдаст."

    scene bg spek_courtyard_morning with dissolve

    "Ноябрь. Холод, сырость, вороны, бабки с семками. Классика Спека."

    show nikita normal at center_pos
    n "Иду я, Никита, сын React и шансона, по асфальту, где когда-то ступали легенды… а теперь Кейн в своём чёрном худи мнит себя богом."

    show belarus normal at right_pos with moveinright
    b "Жжжыве… ик… Беларусь!"

    show nikita ispug
    n "Змагар, ты с утра уже в говно…"
    b "Я… ик… новый рецепт… картошка + йод + любовь к родине…"
    n grust "Понял. Иди спать, герой."

    b "Не… я тебя… ик… провожу… там Кейн… ик… сказал, что Vue.js… ик… в жопу тебе засунет…"
    n zloy "Спасибо за спойлер, брат."

    hide belarus with moveoutright

    scene bg spek_stairs with dissolve

    "Поднимаюсь на 4-й этаж. Лестница воняет сигаретами и безысходностью. На стенах: «Кейн = бог», «React для лохов»."

    n normal "Аудитория 404… как символично, сука."

    # ─────── ПОЯВЛЕНИЕ КЕЙНА — МАКСИМУМ ДРАМЫ ───────
    stop music fadeout 1.5
    play sound audio.kein_laugh volume 0.9           # страшный смех
    pause 1.0
    play music audio.kein_theme fadein 1.5        # включаем strahmusic.mp3

    "Сверху раздаётся этот мерзкий, леденящий душу голос:"

    k "О-о-о… кого я вижу. Жёлтая футболка с миньоном… собственной персоной."

    scene bg black with hpunch
    pause 0.6

    show kein pohot at center_pos with dissolve:
        zoom 1.5 yoffset 300
        linear 0.8 zoom 1.3 yoffset 200

    k pohot "Никита…"
    k erotic "Как же долго… я ждал этой встречи."
    k smeh "Сегодня ты наконец узнаешь…"
    k erotic "…что такое настоящий framework."

    show nikita zloy at center_pos with moveinright
    n zloy "…"

    k normal "Демоэкзамен начинается через семь минут."
    k smeh "И ты его… не сдашь."

    scene bg black with dissolve
    centered "{size=+20}{color=#8a2be2}Продолжение следует...{/color}{/size}"

    return