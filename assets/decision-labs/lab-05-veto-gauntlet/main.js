import { VetoScene } from './src/scenes/VetoScene.js';

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-container',
  width: 1024,
  height: 520,
  pixelArt: true,
  roundPixels: true,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH
  },
  scene: [VetoScene]
};

window.addEventListener('DOMContentLoaded', () => {
  window.game = new Phaser.Game(config);
});
