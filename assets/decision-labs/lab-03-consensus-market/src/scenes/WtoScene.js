import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class WtoScene extends Phaser.Scene {
  constructor() {
    super('WtoScene');
    this.blocSprites = [];
    this.ribbonGraphics = null;
    this.onboarding = null;
  }

  preload() {
    this.load.image('chamber_bg', '../assets/bg/chamber.png');
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('spark', '../assets/fx/spark.png', { frameWidth: 32, frameHeight: 32 });
    this.load.image('stamp_gavel', '../assets/fx/stamp_veto.png');
  }

  create() {
    const W = 820;
    const H = 520;

    // 1. Plenary Bourse Chamber Backdrop
    this.bg = this.add.image(W / 2, H / 2, 'chamber_bg');
    this.bg.setDisplaySize(W, H);

    // Deep Plenary Navy Tint Wash
    this.add.rectangle(W / 2, H / 2, W, H, 0x0c1524, 0.42);

    // 2. Graphic Layer for Animated Trade-Flow Ribbons
    this.ribbonGraphics = this.add.graphics();

    // 3. Central Plenary Dais & Single Undertaking Chain Lock
    this.createPlenaryDais(W, H);

    // 4. Horseshoe of 8 Regional Member Bloc Desks
    this.createBlocDesks(W, H);

    // 5. Signature Moment in First 3 Seconds: Tariff Ticker Scroll + Plenary Gavel Strike
    this.createTariffTicker(W);
    this.playSignatureGavelMoment(W, H);

    // Animation Registry
    this.anims.create({
      key: 'spark_burst',
      frames: this.anims.generateFrameNumbers('spark', { start: 0, end: 3 }),
      frameRate: 12,
      repeat: 0
    });
  }

  createTariffTicker(W) {
    // Illuminated Top Tariff Ticker
    this.add.rectangle(W / 2, 16, W, 32, 0x060b14, 0.96).setStrokeStyle(1.5, 0x1e40af);

    this.tickerText = this.add.text(W + 50, 16, '❖ WTO MINISTERIAL CONFERENCE · GENEVA PLENARY BOURSE · SINGLE UNDERTAKING PRINCIPLE: NOTHING IS AGREED UNTIL EVERYTHING IS AGREED ❖', {
      fontFamily: 'Chakra Petch, sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#38bdf8'
    }).setOrigin(0, 0.5);

    // Continuous ticker scroll animation
    this.tweens.add({
      targets: this.tickerText,
      x: -1200,
      duration: 22000,
      repeat: -1,
      ease: 'Linear'
    });
  }

  createPlenaryDais(W, H) {
    const cx = W / 2;
    const cy = H / 2;

    // Dais Table
    this.daisBox = this.add.rectangle(cx, cy, 260, 140, 0x0a1424, 0.95).setStrokeStyle(2, 0x1e40af);

    // Dais Label
    this.add.text(cx, cy - 50, 'WTO PLENARY ROSTRUM', {
      fontFamily: 'Chakra Petch, sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#fbbf24'
    }).setOrigin(0.5);

    // Single-Undertaking Chain Lock Visual Indicator
    this.chainLockBox = this.add.rectangle(cx, cy - 8, 224, 52, 0x050a12, 0.9).setStrokeStyle(1.5, 0xf43f5e);
    this.chainLockIcon = this.add.text(cx - 85, cy - 8, '🔒', { fontSize: '18px' }).setOrigin(0.5);
    this.chainLockTitle = this.add.text(cx + 10, cy - 16, 'SINGLE UNDERTAKING', {
      fontFamily: 'Chakra Petch, sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#f43f5e'
    }).setOrigin(0.5);
    this.chainLockStatus = this.add.text(cx + 10, cy + 4, 'LOCKED (8/8 VETOES ACTIVE)', {
      fontFamily: 'Share Tech Mono, monospace',
      fontSize: '10px',
      color: '#f43f5e'
    }).setOrigin(0.5);

    // Dais Chair Gavel Sprite
    this.gavel = this.add.image(cx, cy + 46, 'stamp_gavel').setScale(0.85);
  }

  createBlocDesks(W, H) {
    this.blocPositions = [
      // Top Tier (4 Blocs)
      { x: 110, y: 80, id: 'us_eu' },
      { x: 310, y: 80, id: 'g20_ag' },
      { x: 510, y: 80, id: 'china_east' },
      { x: 710, y: 80, id: 'african_ldc' },
      // Bottom Tier (4 Blocs)
      { x: 110, y: 440, id: 'cairns' },
      { x: 310, y: 440, id: 'latam' },
      { x: 510, y: 440, id: 'small_island' },
      { x: 710, y: 440, id: 'nordic' }
    ];

    this.blocSprites = [];

    this.blocPositions.forEach((pos, idx) => {
      const container = this.add.container(pos.x, pos.y);

      const box = this.add.rectangle(0, 0, 175, 78, 0x091322, 0.92).setStrokeStyle(1.5, 0x1e40af);
      const sprite = this.add.sprite(-62, 0, idx % 2 === 0 ? 'envoy' : 'rival', 0).setScale(1.6);
      
      const name = this.add.text(-38, -26, '', {
        fontFamily: 'Chakra Petch, sans-serif',
        fontSize: '10px',
        fontStyle: 'bold',
        color: '#e6f0fb'
      });

      const costBadge = this.add.text(-38, -6, '', {
        fontFamily: 'Share Tech Mono, monospace',
        fontSize: '9px',
        color: '#fbbf24'
      });

      const statusBadge = this.add.text(-38, 14, 'DISSENTING (VETO)', {
        fontFamily: 'Share Tech Mono, monospace',
        fontSize: '8px',
        color: '#f43f5e'
      });

      container.add([box, sprite, name, costBadge, statusBadge]);
      this.blocSprites.push({ container, box, sprite, name, costBadge, statusBadge, id: pos.id, x: pos.x, y: pos.y });
    });
  }

  playSignatureGavelMoment(W, H) {
    audioEngine.init();

    const gavelStrike = this.add.image(W / 2, H / 2, 'stamp_gavel').setScale(0.1).setAlpha(0);
    const gavelBanner = this.add.text(W / 2, H / 2 + 75, 'GENEVA MINISTERIAL CONVENED', {
      fontFamily: 'Chakra Petch, sans-serif',
      fontSize: '13px',
      fontStyle: 'bold',
      color: '#fbbf24',
      backgroundColor: '#0c1524',
      padding: { x: 12, y: 5 }
    }).setOrigin(0.5).setAlpha(0);

    this.tweens.add({
      targets: gavelStrike,
      scale: 1.6,
      alpha: 1,
      duration: 450,
      ease: 'Back.easeOut',
      onComplete: () => {
        audioEngine.playMechanicalClick();
        this.cameras.main.shake(120, 0.006);
        this.spawnSparks(W / 2, H / 2);
      }
    });

    this.tweens.add({
      targets: gavelBanner,
      alpha: 1,
      duration: 350,
      delay: 200
    });

    this.time.delayedCall(2200, () => {
      this.tweens.add({
        targets: [gavelStrike, gavelBanner],
        alpha: 0,
        duration: 350,
        onComplete: () => {
          gavelStrike.destroy();
          gavelBanner.destroy();
        }
      });
    });
  }

  updateState(state) {
    if (!state || !state.blocs) return;

    // Update Blocs
    let dissentingCount = 0;

    this.blocSprites.forEach(item => {
      const b = state.blocs.find(bloc => bloc.id === item.id);
      if (!b) return;

      item.name.setText(b.name.length > 18 ? b.name.substring(0, 16) + '..' : b.name);
      item.costBadge.setText(`COST: ${b.cost} PTS`);

      if (b.satisfied) {
        item.statusBadge.setText('AGREED (NO VETO)').setColor('#10b981');
        item.box.setStrokeStyle(1.5, 0x10b981);
        item.box.setFillStyle(0x0a1e1d, 0.95);
        item.sprite.setTexture(item.sprite.texture.key, 5); // satisfied
      } else {
        dissentingCount++;
        item.statusBadge.setText('DISSENTING (VETO)').setColor('#f43f5e');
        item.box.setStrokeStyle(1.5, 0x1e40af);
        item.box.setFillStyle(0x091322, 0.92);
        item.sprite.setTexture(item.sprite.texture.key, 6); // hostile
      }
    });

    // Update Single Undertaking Chain Lock Status
    if (dissentingCount === 0) {
      this.chainLockBox.setStrokeStyle(2, 0x10b981);
      this.chainLockIcon.setText('🔓');
      this.chainLockTitle.setText('SINGLE UNDERTAKING RATIFIED').setColor('#10b981');
      this.chainLockStatus.setText('UNLOCKED: FULL CONSENSUS').setColor('#10b981');
    } else {
      this.chainLockBox.setStrokeStyle(1.5, 0xf43f5e);
      this.chainLockIcon.setText('🔒');
      this.chainLockTitle.setText('SINGLE UNDERTAKING LOCKED').setColor('#f43f5e');
      this.chainLockStatus.setText(`VETOED BY ${dissentingCount} BLOC(S)`).setColor('#f43f5e');
    }

    // Render Trade-Flow Ribbons between linked packages
    this.drawTradeRibbons(state.packages || []);
  }

  drawTradeRibbons(packages) {
    this.ribbonGraphics.clear();

    packages.forEach(pkg => {
      const [idA, idB] = pkg.blocs;
      const posA = this.blocPositions.find(p => p.id === idA);
      const posB = this.blocPositions.find(p => p.id === idB);

      if (posA && posB) {
        // Draw luminous dual-core ribbon
        this.ribbonGraphics.lineStyle(4, 0x38bdf8, 0.7);
        this.ribbonGraphics.beginPath();
        this.ribbonGraphics.moveTo(posA.x, posA.y);
        
        // Control point curved through center dais
        const midX = (posA.x + posB.x) / 2;
        const midY = (posA.y + posB.y) / 2;
        this.ribbonGraphics.lineTo(midX, midY);
        this.ribbonGraphics.lineTo(posB.x, posB.y);
        this.ribbonGraphics.strokePath();

        this.ribbonGraphics.lineStyle(1.5, 0xfbbf24, 0.9);
        this.ribbonGraphics.strokeCircle(midX, midY, 6);
      }
    });
  }

  playVoteAnimation(voteResult, onComplete) {
    audioEngine.init();

    const W = 820;
    const H = 520;

    // Gavel Strike Shockwave
    this.tweens.add({
      targets: this.gavel,
      angle: -45,
      yoyo: true,
      duration: 150,
      repeat: 1,
      onComplete: () => {
        if (voteResult.passed) {
          audioEngine.playChimeCooperation();
          this.cameras.main.flash(250, 16, 185, 129, false);
          this.spawnSparks(W / 2, H / 2);
          this.showNotification('CONSENSUS ADOPTED! THE SINGLE UNDERTAKING PASSES.', '#10b981');
        } else {
          audioEngine.playBetrayalBoom();
          this.cameras.main.shake(300, 0.018);
          this.cameras.main.flash(250, 244, 63, 94, false);
          this.showNotification(`DEADLOCK: PACKAGE VETOED BY ${voteResult.dissentingBlocs.length} BLOCS!`, '#f43f5e');
        }

        this.time.delayedCall(1400, () => {
          if (onComplete) onComplete();
        });
      }
    });
  }

  showNotification(text, color) {
    const W = 820;
    const notif = this.add.text(W / 2, 210, text, {
      fontFamily: 'Chakra Petch, sans-serif',
      fontSize: '16px',
      fontStyle: 'bold',
      color: color,
      backgroundColor: '#060b14',
      padding: { x: 16, y: 8 },
      stroke: color,
      strokeThickness: 1
    }).setOrigin(0.5);

    this.tweens.add({
      targets: notif,
      y: 180,
      alpha: 0,
      duration: 1600,
      ease: 'Back.easeOut',
      onComplete: () => notif.destroy()
    });
  }

  spawnSparks(x, y) {
    const spark = this.add.sprite(x, y, 'spark', 0).setScale(3);
    spark.play('spark_burst');
    spark.on('animationcomplete', () => spark.destroy());
  }
}
