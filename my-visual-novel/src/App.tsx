// src/App.tsx
import { Game, prepareBranches } from 'react-visual-novel';
import 'react-visual-novel/dist/index.css';

import { IntroBranch } from './scenes/IntroBranch';
import { PrologueBranch } from './scenes/PrologueBranch';
import { SaveManager } from './app/SaveManager';

const branches = prepareBranches({
  intro: IntroBranch,
  prologue: PrologueBranch,
});

type MyBranches = typeof branches;
declare module 'react-visual-novel' {
  interface RegisteredBranches extends MyBranches {}
}

export default function App() {
  return (
    <div className="w-screen h-screen bg-black">
      <SaveManager>
        <Game
          assets={{}}
          branches={branches}
          initialBranchId="intro"  // <-- строка, всё ок
        />
      </SaveManager>
    </div>
  );
}