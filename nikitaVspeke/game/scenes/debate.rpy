# game/scenes/debate.rpy

init python:
    debate_score = 0  # –100 → Кейн уничтожил, +100 → Никита король Спека

label scene_great_debate:

    scene bg kabinet with fade
    play music audio.strahmusic fadein 2.0 volume 0.65

    "Аудитория 404 забита под завязку. Свет приглушён, только лампы над трибунами горят холодным белым."
    "В центре — Кисельман с микрофоном и в чёрных очках."

    show kiselman at center_pos with dissolve
    ki "Тема дебатов: кто станет единоличным правителем СмолАРО в этом учебном году."
    ki "Кейн Журавлёв — действующий бог."
    play sound audio.crowd_cheer volume 0.9
    show kein normal at right_pos with moveinright

    ki "И претендент — Никита."
    play sound audio.crowd_boo volume 0.7
    show nikita normal at left_pos with moveinleft

    ki "Судья от народа — товарищ Роля Кябинин."
    show rolya normal at center_pos with moveinbottom
    r "Власть — советам, а не чёрным худи!"

    hide kiselman with moveouttop

    k pohot "Я уже правлю этим местом. Вы просто ещё не все это приняли."
    k erotic "Vue 3 Composition API, Pinia, TypeScript — это новый порядок. React умер в 2019-м."
    play sound audio.crowd_cheer volume 0.8
    $ debate_score -= 15

    menu round1:
        "Твой ход Никиты:"

        "«Ты не бог, ты просто токсик с правами админа в студсовете»":
            n zloy "Ты запугал половину курса, подкупил вторую и заставил третью носить чёрные худи. Это не власть — это секта."
            play sound audio.crowd_laugh volume 0.8
            $ debate_score += 25

        "«Твоя власть держится только на страхе и оценках Юлии Михайловны»":
            n normal "Все знают: не поставишь Vue — получишь пару и ночную смену на складе Озона."
            play sound audio.crowd_ooooh volume 0.85
            $ debate_score += 20

        "Промолчать":
            n grust "…"
            k smeh "Молчание — знак согласия."
            play sound audio.crowd_cheer volume 0.7
            $ debate_score -= 20

    k zloy "Назови хоть одну причину, почему Спек должен пойти за тобой."

    menu round2:
        "Ответ:"

        "«Я за свободу выбора стека и чтобы никто не боялся ходить по вечерам»":
            n normal "Я не буду заставлять никого писать на React. Пиши хоть на jQuery 1.8 — твоё дело. Главное — чтобы Сергей Парчевский перестал шантажировать девчонок."
            play sound audio.crowd_cheer volume 1.0
            $ debate_score += 35

        "«При мне будет бесплатное пиво по пятницам и шансон 24/7»":
            n smeh "Балтика-9, «Мурка» на репите и никаких ночных стендапов по Pinia."
            play sound audio.crowd_laugh volume 0.9
            $ debate_score += 20

        "«Эээ… React же… быстрее Virtual DOM…»":
            n grust "Ну… Virtual DOM… он как бы… оптимизирует…"
            k erotic "Слабак."
            play sound audio.crowd_boo volume 0.9
            $ debate_score -= 30

    show rolya normal at center_pos with hpunch
    r "НИ ОДИН ИЗ КАПИТАЛИСТОВ НЕ ДОСТОИН! ЭКСПРОПРОПРИАЦИЯ СТОЛОВКИ СЕГОДНЯ В 18:00!"
    play sound audio.crowd_laugh
    n zloy "Роля, сядь нахуй."
    k zloy "Заткнись, Ленин с AliExpress."

    "Кисельман возвращается и даёт финальный вопрос."

    k normal "Последний вопрос тебе, Никита. Если победишь — что будет с теми, кто останется со мной и с Vue?"

    menu final_blow:
        "Финальный ответ:"

        "«Ничего. Пусть пишут на чём хотят. Это и есть свобода»":
            n normal "Я не ты, Кейн. Я не заставляю. Выбирай любой стек — и живи спокойно."
            "Зал на секунду замирает… а потом взрывается."
            play sound audio.crowd_cheer volume 1.0
            $ debate_score += 45

        "«Всех на React и публичное покаяние в Telegram-канале»":
            n zloy "Переписываете курсовые за неделю. Кто не успеет — на склад к Змагару."
            play sound audio.crowd_boo volume 1.0
            $ debate_score -= 40

        "«Устроим большой костёр из чёрных худи на заднем дворе»":
            n pohot "И зажарим маршмеллоу на цепочками от Vue."
            play sound audio.crowd_laugh
            $ debate_score += 10

    # ─────── ИТОГИ ───────
    if debate_score >= 50:
        # Никита побеждает
        stop music fadeout 1.0
        play sound audio.crowd_cheer volume 1.0
        k ispug "Это… невозможно…"
        n normal "Ты больше не бог, Кейн."
        "Толпа скандирует: «Ни-ки-та! Ни-ки-та!»"
        scene bg black with dissolve
        centered "{size=+30}{color=#ffff00}НИКИТА СВЕРГ БОГА\nСпек свободен{/color}{/size}"
        $ persistent.nikita_won_debate = True

    elif debate_score <= -40:
        # Кейн раздавил
        stop music fadeout 1.5
        play sound audio.crowd_cheer volume 0.9
        k erotic "Видишь? Даже они выбрали меня."
        n grust "..."
        scene bg black with dissolve
        centered "{size=+30}{color=#8a2be2}КЕЙН — НАВСЕГДА\nТы проиграл, жёлтый{/color}{/size}"
        $ persistent.kein_won_debate = True

    else:
        # Ничья → начинается мясо
        stop music fadeout 0.8
        play music "audio/pyyala-aigel.mp3" volume 0.9  # твоя «пиала ангел» как саундтрек к драке
        "Толпа взрывается. Кто-то кидает стулом. Роля орёт про революцию."
        show kein zloy at right_pos
        show nikita zloy at left_pos
        "Кейн и Никита одновременно прыгают друг на друга через трибуну."
        scene bg black with hpunch
        centered "{size=+35}{color=#ff5555}ДРАКА ЗА СПЕК НАЧАЛАСЬ\nПиала ангела гремит на всю общагу{/color}{/size}"
        $ persistent.debate_draw_chaos = True

    return