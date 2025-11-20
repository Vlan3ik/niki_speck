// src/scenes/PrologueBranch.tsx
import { Branch, Scene, Character, Say, Choice } from 'react-visual-novel';
import { useGameStore } from '@/store/useGameStore';

export function PrologueBranch() {
  const { addAffection, affection } = useGameStore();

  return (
    <Branch>
      <Scene src="/assets/bg/menu_bg.png" />

      <audio autoPlay loop volume={0.3} style={{ display: 'none' }}>
        <source src="/assets/music/backgroundMusic.mp3" type="audio/mpeg" />
      </audio>

      {/* Показываем персонажей */}
      <Character
        id="nikita"
        name="Никита"
        color="#ff3366"
        src="/assets/characters/nikita/main.png"
        position="left"
      />

      <Character
        id="kein"
        name="Кейн"
        color="#00ffff"
        src="/assets/characters/kein/main.png"
        position="right"
      />

      <Say speaker="nikita">
        Блять, опять этот ебаный день в этой помойке под названием школа...
      </Say>

      <Say speaker="nikita">
        Кому вообще нужна эта хуйня? Лучше бы дома сидел, дрочил на нормальное порно.
      </Say>

      <Say speaker="kein">
        О, смотрите-ка, наш любимый долбоёб Никита опять ноет как сука.
      </Say>

      <Say speaker="kein">
        Ты чё, опять всю ночь хуй клал на уроки? Или мамка не высосала?
      </Say>

      <Say speaker="nikita">
        Заткнись нахуй, Кейн! Ты мне уже в печени сидишь, мразь циановолосая!
      </Say>

      <Say speaker="kein">
        А ты всё так же сосёшь у учителей за оценки, да? Пиздец, Никита, ты просто ходячая спермоприёмница.
      </Say>

      <Choice
        options={[
          {
            label: 'Засадить ему по ебалу прямо тут',
            onClick: () => addAffection('kein', -30),
          },
          {
            label: 'Сплюнуть и уйти — не тратить нервы',
            onClick: () => addAffection('kein', -10),
          },
          {
            label: '«Пошли нахуй вместе, Кейн»',
            onClick: () => addAffection('kein', 25),
          },
        ]}
      />

      <Say speaker="nikita">Ладно... хуй с тобой. Пошли в этот ебаный класс.</Say>

      <Say>
        <div className="text-center space-y-4">
          <div className="text-6xl font-bold text-red-600">ПРОДОЛЖЕНИЕ СЛЕДУЕТ...</div>
          <div className="text-4xl text-cyan-400">
            Отношения с Кейном: {affection.kein ?? 0}
          </div>
        </div>
      </Say>
    </Branch>
  );
}