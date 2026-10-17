/**
 * BootScene — Asset preloading & sprite slicing.
 */
export class BootScene extends Phaser.Scene {
  constructor() {
    super('BootScene');
  }

  preload() {
    // Backgrounds
    this.load.image('chamber_bg', '../assets/bg/chamber.png');

    // Spritesheets
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', {
      frameWidth: 32,
      frameHeight: 48
    });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', {
      frameWidth: 32,
      frameHeight: 48
    });
    this.load.spritesheet('envelope', '../assets/fx/envelope.png', {
      frameWidth: 32,
      frameHeight: 32
    });
    this.load.spritesheet('spark', '../assets/fx/spark.png', {
      frameWidth: 32,
      frameHeight: 32
    });
    this.load.spritesheet('tube', '../assets/ui/tube.png', {
      frameWidth: 16,
      frameHeight: 16
    });
    this.load.spritesheet('pips', '../assets/ui/pips.png', {
      frameWidth: 16,
      frameHeight: 16
    });

    // Static Sprites & UI
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.image('icon_coop', '../assets/ui/icon_coop.png');
    this.load.image('icon_defect', '../assets/ui/icon_defect.png');
    this.load.image('panel_cyan', '../assets/ui/panel_cyan.png');
    this.load.image('panel_gold', '../assets/ui/panel_gold.png');
    this.load.image('logo_labs', '../assets/ui/logo_labs.png');
  }

  create() {
    // Register Animations
    this.anims.create({
      key: 'envoy_idle',
      frames: this.anims.generateFrameNumbers('envoy', { start: 0, end: 3 }),
      frameRate: 3,
      repeat: -1
    });

    this.anims.create({
      key: 'rival_idle',
      frames: this.anims.generateFrameNumbers('rival', { start: 0, end: 3 }),
      frameRate: 3,
      repeat: -1
    });

    this.anims.create({
      key: 'envelope_open',
      frames: this.anims.generateFrameNumbers('envelope', { start: 0, end: 3 }),
      frameRate: 6,
      repeat: 0
    });

    this.anims.create({
      key: 'spark_burst',
      frames: this.anims.generateFrameNumbers('spark', { start: 0, end: 3 }),
      frameRate: 12,
      repeat: 0
    });

    // Launch GameScene and UIScene concurrently
    this.scene.start('GameScene');
    this.scene.launch('UIScene');
  }
}
