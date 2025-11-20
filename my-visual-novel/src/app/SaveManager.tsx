// src/app/SaveManager.tsx
import { useEffect } from 'react';
import { useSceneIndex, useBranchId, useGoto } from 'react-visual-novel';

export function SaveManager({ children }: { children: React.ReactNode }) {
  const sceneIndex = useSceneIndex();
  const branchId = useBranchId();
  const goto = useGoto();

  // Автосейв
  useEffect(() => {
    localStorage.setItem(
      'vn-auto-save',
      JSON.stringify({ branchId, sceneIndex })
    );
  }, [branchId, sceneIndex]);

  // Автозагрузка при монтировании
  useEffect(() => {
    const saved = localStorage.getItem('vn-auto-save');
    if (saved) {
      try {
        const { branchId, sceneIndex } = JSON.parse(saved);
        if (branchId && typeof sceneIndex === 'number') {
          goto({ branch: branchId, scene: sceneIndex });
        }
      } catch {}
    }
  }, [goto]);

  return <>{children}</>;
}