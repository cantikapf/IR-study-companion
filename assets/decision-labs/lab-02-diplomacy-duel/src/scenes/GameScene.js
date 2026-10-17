import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class GameScene extends Phaser.Scene {
  constructor() {
    super('GameScene');
    this.onboarding = null;
  }

  preload() {
    this.load.image('chamber_bg', '../assets/bg/chamber.png');
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('envelope', '../assets/fx/envelope.png', { frameWidth: 32, frameHeight: 32 });
    this.load.spritesheet('spark', '../assets/fx/spark.png', { frameWidth: 32, frameHeight: 32 });
    this.load.image('stamp_seal', '../assets/fx/stamp_veto.png');
  }

  create() {
    const W = 820;
    const H = 520;

    // 1. Chamber Background
    this.bg = this.add.image(W / 2, H / 2, 'chamber_bg');
    this.bg.setDisplaySize(W, H);

    // Warm ambient tint wash (Oxblood / Tungsten salon)
    this.add.rectangle(W / 2, H / 2, W, H, 0x180a0a, 0.35);

    // 2. Seated Diplomats
    this.envoy = this.add.sprite(220, 270, 'envoy', 0);
    this.envoy.setScale(3.6);

    this.rival = this.add.sprite(600, 270, 'rival', 0);
    this.rival.setScale(3.6);

    // Diplomat Nametags
    this.add.rectangle(220, 365, 170, 24, 0x0a0505, 0.85).setStrokeStyle(1, 0x78350f);
    this.envoyTag = this.add.text(220, 365, 'YOUR EXCELLENCY', {
      fontFamily: 'Cinzel, serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#fdf3e7'
    }).setOrigin(0.5);

    this.add.rectangle(600, 365, 170, 24, 0x0a0505, 0.85).setStrokeStyle(1, 0x78350f);
    this.rivalTag = this.add.text(600, 365, 'RIVAL PLENIPOTENTIARY', {
      fontFamily: 'Cinzel, serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#d97706'
    }).setOrigin(0.5);

    // 3. Wide Conference Table
    this.table = this.add.image(W / 2, 420, 'table_wide');
    this.table.setScale(3.2);

    // 4. Diplomatic Sealed Envelopes (On table)
    this.envoyEnvelope = this.add.sprite(280, 400, 'envelope', 0).setScale(2.5).setVisible(false);
    this.rivalEnvelope = this.add.sprite(540, 400, 'envelope', 0).setScale(2.5).setVisible(false);

    // 5. Payoff Matrix HUD (Center top, responsive highlight)
    this.createPayoffMatrix();

    // 6. Trust Filament (Luminous capacitor glowing across table center)
    this.createTrustFilament();

    // 7. Animations
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

    this.envoy.play('envoy_idle');
    this.rival.play('rival_idle');

    // 8. Signature Moment in First 3 Seconds: Wax Seal Stamp lands on table
    this.playSignatureSealMoment();
  }

  createPayoffMatrix() {
    const startX = 410;
    const startY = 48;
    const cellW = 88;
    const cellH = 34;

    this.matrixCells = {};

    // Matrix Container
    this.add.rectangle(startX, startY + 18, 196, 88, 0x120707, 0.92).setStrokeStyle(1.5, 0x78350f);
    this.add.text(startX, startY - 16, 'PAYOFF MATRIX [YOU / RIVAL]', {
      fontFamily: 'Cinzel, serif',
      fontSize: '10px',
      fontStyle: 'bold',
      color: '#d97706'
    }).setOrigin(0.5);

    const cellsData = [
      { key: 'CC', x: startX - cellW / 2 - 2, y: startY + 6, label: 'CC: +5 / +5', sub: 'COOPERATE' },
      { key: 'CD', x: startX + cellW / 2 + 2, y: startY + 6, label: 'CD: -10 / +10', sub: 'SUCKER' },
      { key: 'DC', x: startX - cellW / 2 - 2, y: startY + cellH + 8, label: 'DC: +10 / -10', sub: 'TEMPT' },
      { key: 'DD', x: startX + cellW / 2 + 2, y: startY + cellH + 8, label: 'DD: -2 / -2', sub: 'CONFLICT' }
    ];

    cellsData.forEach(c => {
      const box = this.add.rectangle(c.x, c.y, cellW, cellH, 0x240e0e, 0.9).setStrokeStyle(1, 0x522307);
      const text = this.add.text(c.x, c.y, c.label, {
        fontFamily: 'Share Tech Mono, monospace',
        fontSize: '10px',
        color: '#fdf3e7'
      }).setOrigin(0.5);
      this.matrixCells[c.key] = { box, text, baseColor: 0x240e0e, baseStroke: 0x522307 };
    });
  }

  createTrustFilament() {
    const W = 820;
    // Central glowing capacitor tube on the conference table
    this.add.rectangle(W / 2, 485, 340, 14, 0x180a0a, 0.9).setStrokeStyle(1.5, 0x78350f);
    this.filamentGlow = this.add.rectangle(W / 2 - 168, 485, 0, 10, 0xd97706).setOrigin(0, 0.5);
    this.filamentText = this.add.text(W / 2, 465, 'TRUST FILAMENT: INERT (1.0x)', {
      fontFamily: 'Share Tech Mono, monospace',
      fontSize: '11px',
      color: '#d97706'
    }).setOrigin(0.5);
  }

  playSignatureSealMoment() {
    const W = 820;
    const seal = this.add.image(W / 2, 140, 'stamp_seal').setScale(0.1).setAlpha(0);
    const label = this.add.text(W / 2, 215, 'GENEVA BILATERAL DISPATCH SEALED', {
      fontFamily: 'Cinzel, serif',
      fontSize: '13px',
      fontStyle: 'bold',
      color: '#d97706',
      backgroundColor: '#180a0a',
      padding: { x: 10, y: 4 }
    }).setOrigin(0.5).setAlpha(0);

    audioEngine.init();

    this.tweens.add({
      targets: seal,
      scale: 1.4,
      alpha: 0.9,
      duration: 500,
      ease: 'Back.easeOut',
      onComplete: () => {
        audioEngine.playMechanicalClick();
        this.cameras.main.shake(120, 0.005);
      }
    });

    this.tweens.add({
      targets: label,
      alpha: 1,
      duration: 400,
      delay: 200
    });

    this.time.delayedCall(2400, () => {
      this.tweens.add({
        targets: [seal, label],
        alpha: 0,
        duration: 400,
        onComplete: () => {
          seal.destroy();
          label.destroy();
        }
      });
    });
  }

  updateRivalTag(name) {
    if (this.rivalTag) {
      this.rivalTag.setText(name.toUpperCase());
    }
  }

  setDiplomatExpression(diplomat, expr) {
    diplomat.anims.stop();
    const frameMap = {
      neutral: 0,
      thinking: 4,
      satisfied: 5,
      hostile: 6,
      alarmed: 7
    };
    const frameIdx = frameMap[expr] ?? 0;
    diplomat.setTexture(diplomat.texture.key, frameIdx);
  }

  resetDiplomats() {
    this.envoy.play('envoy_idle');
    this.rival.play('rival_idle');
  }

  highlightMatrixCell(activeKey) {
    Object.keys(this.matrixCells).forEach(key => {
      const cell = this.matrixCells[key];
      if (key === activeKey) {
        cell.box.setFillStyle(0xd97706, 0.95);
        cell.box.setStrokeStyle(2, 0xfdf3e7);
        cell.text.setColor('#180a0a').setFontStyle('bold');

        this.tweens.add({
          targets: cell.box,
          scaleX: 1.08,
          scaleY: 1.08,
          yoyo: true,
          duration: 250,
          repeat: 1
        });
      } else {
        cell.box.setFillStyle(cell.baseColor, 0.9);
        cell.box.setStrokeStyle(1, cell.baseStroke);
        cell.text.setColor('#fdf3e7').setFontStyle('normal');
      }
    });
  }

  updateTrustFilament(streak, multiplier) {
    const W = 820;
    const maxStreak = 4;
    const clamped = Math.min(streak, maxStreak);
    const targetW = (clamped / maxStreak) * 336;

    this.tweens.add({
      targets: this.filamentGlow,
      width: targetW,
      duration: 300,
      ease: 'Sine.easeOut'
    });

    if (streak > 0) {
      this.filamentGlow.setFillStyle(0x10b981);
      this.filamentText.setText(`TRUST FILAMENT: STREAK ${streak} (${multiplier.toFixed(1)}x MULTIPLIER)`).setColor('#10b981');
    } else {
      this.filamentGlow.setFillStyle(0xd97706);
      this.filamentText.setText('TRUST FILAMENT: COLLAPSED (1.0x)').setColor('#d97706');
    }
  }

  playTurnAnimation(pMove, rMove, feedback, onComplete) {
    audioEngine.init();
    audioEngine.playMechanicalClick();

    this.setDiplomatExpression(this.rival, 'thinking');

    // Slide envelopes onto table
    this.envoyEnvelope.setVisible(true).setAlpha(0).setY(370);
    this.rivalEnvelope.setVisible(true).setAlpha(0).setY(370);

    this.tweens.add({
      targets: [this.envoyEnvelope, this.rivalEnvelope],
      y: 400,
      alpha: 1,
      duration: 260,
      ease: 'Back.easeOut'
    });

    this.time.delayedCall(500, () => {
      // Reveal cards
      this.envoyEnvelope.play('envelope_open');
      this.rivalEnvelope.play('envelope_open');

      const W = 820;
      const envoyCard = this.add.text(280, 350, pMove === 'C' ? 'COOPERATE' : 'DEFECT', {
        fontFamily: 'Cinzel, serif',
        fontSize: '15px',
        fontStyle: 'bold',
        color: pMove === 'C' ? '#10b981' : '#f43f5e',
        backgroundColor: '#180a0a',
        padding: { x: 8, y: 4 }
      }).setOrigin(0.5);

      const rivalCard = this.add.text(540, 350, rMove === 'C' ? 'COOPERATE' : 'DEFECT', {
        fontFamily: 'Cinzel, serif',
        fontSize: '15px',
        fontStyle: 'bold',
        color: rMove === 'C' ? '#10b981' : '#f43f5e',
        backgroundColor: '#180a0a',
        padding: { x: 8, y: 4 }
      }).setOrigin(0.5);

      this.highlightMatrixCell(feedback.key);

      // Reaction & Micro-expressions
      if (feedback.key === 'CC') {
        audioEngine.playChimeCooperation();
        this.setDiplomatExpression(this.envoy, 'satisfied');
        this.setDiplomatExpression(this.rival, 'satisfied');
        this.cameras.main.flash(200, 16, 185, 129, false);
        this.spawnSparks(W / 2, 380);
      } else if (feedback.key === 'DC') {
        audioEngine.playMechanicalClick();
        this.setDiplomatExpression(this.envoy, 'satisfied');
        this.setDiplomatExpression(this.rival, 'hostile');
        this.cameras.main.shake(150, 0.008);
        this.playSealShatter();
      } else if (feedback.key === 'CD') {
        audioEngine.playBetrayalBoom();
        this.setDiplomatExpression(this.envoy, 'alarmed');
        this.setDiplomatExpression(this.rival, 'satisfied');
        this.cameras.main.shake(250, 0.015);
        this.cameras.main.flash(250, 244, 63, 94, false);
        this.playSealShatter();
      } else {
        // DD
        audioEngine.playMechanicalClick();
        this.setDiplomatExpression(this.envoy, 'hostile');
        this.setDiplomatExpression(this.rival, 'hostile');
        this.cameras.main.shake(120, 0.005);
        this.playSealShatter();
      }

      this.time.delayedCall(1200, () => {
        envoyCard.destroy();
        rivalCard.destroy();
        this.envoyEnvelope.setVisible(false);
        this.rivalEnvelope.setVisible(false);
        this.resetDiplomats();
        if (onComplete) onComplete();
      });
    });
  }

  playSealShatter() {
    const W = 820;
    const shatter = this.add.image(W / 2, 390, 'stamp_seal').setScale(1.1).setAlpha(0.85);

    this.tweens.add({
      targets: shatter,
      scaleX: 1.5,
      scaleY: 1.5,
      alpha: 0,
      duration: 350,
      ease: 'Power2',
      onComplete: () => shatter.destroy()
    });

    this.spawnSparks(W / 2, 390);
  }

  spawnSparks(x, y) {
    const spark = this.add.sprite(x, y, 'spark', 0).setScale(2.5);
    spark.play('spark_burst');
    spark.on('animationcomplete', () => spark.destroy());
  }
}
