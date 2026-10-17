import { CrisisScene } from './src/scenes/CrisisScene.js';

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-container',
  width: 1024,
  height: 600,
  pixelArt: true,
  roundPixels: true,
  transparent: true,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH
  },
  scene: [CrisisScene]
};

window.addEventListener('DOMContentLoaded', () => {
  window.game = new Phaser.Game(config);
});
