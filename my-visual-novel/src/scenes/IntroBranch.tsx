// src/scenes/IntroBranch.tsx
import { Branch, Scene, Say, Choice, Jump } from 'react-visual-novel';

export function IntroBranch() {
  return (
    <Branch>
      <Scene src="/assets/bg/menu_bg.png" />

      {/* Музыка — обычный <audio>, volume от 0 до 1 */}
      <audio autoPlay loop volume={0.4} style={{ display: 'none' }}>
        <source src="/assets/music/backgroundMusic.mp3" type="audio/mpeg" />
      </audio>

      <div className="absolute inset-0 flex items-center justify-center pointer-events-none z-50">
        <img src="/assets/bg/logo.png" alt="Никита Speck" className="w-96 drop-shadow-2xl" />
      </div>

      <Say>
        <div className="text-8xl font-bold text-red-600 text-center drop-shadow-2xl">
          НИКИТА SPECK
        </div>
      </Say>

      <Choice
        options={[
          { label: 'НАЧАТЬ ИГРУ', next: true },
          { label: 'ЗАГРУЗИТЬ', onClick: () => alert('Автосейв работает, ленивая жопа') },
          { label: 'ВЫХОД', onClick: () => confirm('Уверен?') && window.close() },
        ]}
      />

      <Jump branch="prologue" />
    </Branch>
  );
}