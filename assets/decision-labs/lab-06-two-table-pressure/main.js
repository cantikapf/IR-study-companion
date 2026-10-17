import { PutnamScene } from './src/scenes/PutnamScene.js';

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-container',
  width: 820,
  height: 520,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH
  },
  scene: [PutnamScene]
};

window.addEventListener('DOMContentLoaded', () => {
  window.game = new Phaser.Game(config);
});
