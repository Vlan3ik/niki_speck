// src/characters/index.ts
export const characters = {
  nikita: {
    name: "Никита",
    color: "#ff3366",
    sprites: {
      normal: "/assets/characters/nikita/main.png",
      angry: "/assets/characters/nikita/main.png",
    },
  },
  kein: {
    name: "Кейн",
    color: "#00ffff",
    sprites: {
      normal: "/assets/characters/kein/main.png",
      smirk: "/assets/characters/kein/main.png",
    },
  },
} as const;

export type CharacterKey = keyof typeof characters;