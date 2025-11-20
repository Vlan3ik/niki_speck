// src/store/useGameStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

type CharacterAffection = Record<string, number>;

interface GameState {
  // Переменные новеллы
  variables: Record<string, any>;
  affection: CharacterAffection;
  flags: Set<string>;

  // Действия
  setVariable: (key: string, value: any) => void;
  addAffection: (character: string, value: number) => void;
  setFlag: (flag: string) => void;
  hasFlag: (flag: string) => boolean;
  reset: () => void;
}

export const useGameStore = create<GameState>()(
  persist(
    (set, get) => ({
      variables: {},
      affection: {},
      flags: new Set(),

      setVariable: (key, value) =>
        set({ variables: { ...get().variables, [key]: value } }),

      addAffection: (character, value) =>
        set({
          affection: {
            ...get().affection,
            [character]: (get().affection[character] ?? 0) + value,
          },
        }),

      setFlag: (flag) =>
        set({ flags: new Set(get().flags).add(flag) }),

      hasFlag: (flag) => get().flags.has(flag),

      reset: () => set({ variables: {}, affection: {}, flags: new Set() }),
    }),
    {
      name: 'vn-save', // localStorage key
    }
  )
);