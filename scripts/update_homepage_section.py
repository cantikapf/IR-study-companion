import os

index_md_path = r"D:\PERSONAL PROJECT\IR-study-companion\_pages\index.md"
with open(index_md_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '  <section class="labs-section" id="simulations">'
end_marker = '  <!-- Master Video Companion Channel Showcase -->'

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

print(f"idx_start: {idx_start}, idx_end: {idx_end}")
assert idx_start != -1 and idx_end != -1, "Markers not found!"

new_homepage_section = """  <!-- Interactive Diplomatic Decision Labs (Total Replacement with Live Game Arena) -->
  <section class="labs-section" id="simulations">
    <div class="home-section-header">
      <div>
        <h2 class="home-section-title">Interactive Diplomatic Decision Labs</h2>
        <div class="home-section-subtitle">Playable game sandboxes testing strategic paradigms against realistic crisis constraints</div>
      </div>
      <div>
        <a href="{{ site.baseurl }}/assets/decision-labs/index.html" target="_blank" class="sync-btn sync-btn-primary" style="font-family: ui-monospace, 'JetBrains Mono', monospace; font-size: 0.8rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem;">
          <i class="fa fa-th-large"></i> Mission Control Hub &rarr;
        </a>
      </div>
    </div>

    <!-- Live Game Arena + Direct Switcher Grid -->
    <div style="display: grid; grid-template-columns: 1.35fr 0.85fr; gap: 1.75rem; margin-bottom: 2rem;">
      
      <!-- Live Game Frame -->
      <div style="background: var(--lms-surface); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-lg); overflow: hidden; display: flex; flex-direction: column; box-shadow: var(--lms-shadow-md); height: 680px; box-sizing: border-box;">
        <div style="background: var(--lms-subtle); border-bottom: 1px solid var(--lms-hairline); padding: 0.85rem 1.25rem; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; box-sizing: border-box;">
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span style="font-family: ui-monospace, 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #059669; background: rgba(5, 150, 105, 0.12); border: 1px solid rgba(5, 150, 105, 0.25); padding: 0.2rem 0.5rem; border-radius: 4px;" id="homeLiveBadge">
              &bull; LIVE ARENA &bull; LAB 02
            </span>
            <span style="font-size: 0.95rem; font-weight: 750; color: var(--lms-ink-primary);" id="homeLiveTitle">
              Diplomacy Duel: The Prisoner's Dilemma
            </span>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <a href="{{ site.baseurl }}/assets/decision-labs/lab-02-diplomacy-duel/index.html" target="_blank" id="homeLiveTabBtn" class="sync-btn" style="padding: 0.35rem 0.75rem; font-size: 0.75rem; font-family: ui-monospace, monospace; text-decoration: none; border: 1px solid var(--lms-hairline); color: var(--lms-ink-secondary);" title="Open in Dedicated Tab">
              <i class="fa fa-external-link"></i> Fullscreen
            </a>
          </div>
        </div>

        <iframe 
          id="homeLabFrame"
          src="{{ site.baseurl }}/assets/decision-labs/lab-02-diplomacy-duel/index.html" 
          style="width: 100%; flex: 1 1 0; min-height: 0; border: none; background: #040711; display: block;"
          allow="autoplay; fullscreen"
          title="Interactive Diplomatic Game Arena">
        </iframe>

        <div style="background: var(--lms-subtle); border-top: 1px solid var(--lms-hairline); padding: 0.6rem 1.25rem; display: flex; justify-content: space-between; font-size: 0.72rem; font-family: ui-monospace, monospace; color: var(--lms-ink-tertiary); flex-shrink: 0; box-sizing: border-box;">
          <span id="homeLiveEngine">&bull; Engine: Phaser 3 (2D Vector + Procedural WebAudio)</span>
          <span>&bull; 7-Phase Pedagogical Cycle Active</span>
        </div>
      </div>

      <!-- Live Interactive Selector Pane -->
      <div style="background: var(--lms-surface); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-lg); padding: 1.25rem 1.25rem 1rem; display: flex; flex-direction: column; box-shadow: var(--lms-shadow-md); height: 680px; box-sizing: border-box; overflow: hidden; position: relative;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--lms-hairline); padding-bottom: 0.75rem; margin-bottom: 0.85rem; flex-shrink: 0; box-sizing: border-box;">
          <div style="font-size: 0.95rem; font-weight: 750; color: var(--lms-ink-primary); display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa fa-gamepad" style="color: #2563eb;"></i> Select Simulation (10 Labs)
          </div>
          <span style="font-family: ui-monospace, monospace; font-size: 0.7rem; color: var(--lms-ink-tertiary);">CLICK TO SWITCH LIVE</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 0.6rem; flex: 1 1 0; min-height: 0; overflow-y: auto; padding-right: 0.35rem; margin-bottom: 0.5rem; mask-image: linear-gradient(to bottom, black calc(100% - 32px), transparent 100%); -webkit-mask-image: linear-gradient(to bottom, black calc(100% - 32px), transparent 100%);" id="homeCatalogList">
          
          <div class="home-lab-card" data-id="lab-01" data-url="{{ site.baseurl }}/assets/decision-labs/lab-01-crisis-command/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Crisis Command: Allison FPA Models" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #dc2626; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #dc2626;">LAB 01 &bull; FPA MODEL</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Crisis Command: Thirteen Days</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Allison Models I, II, III in 1962 naval missile crisis with DEFCON clocks.</div>
          </div>

          <div class="home-lab-card is-active-home-lab" data-id="lab-02" data-url="{{ site.baseurl }}/assets/decision-labs/lab-02-diplomacy-duel/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Diplomacy Duel: Prisoner's Dilemma" style="background: var(--lms-subtle); border: 1.5px solid #059669; border-left: 4px solid #059669; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease; box-shadow: 0 0 10px rgba(5, 150, 105, 0.15);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #059669;">LAB 02 &bull; GAME THEORY &bull; ACTIVE</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: #059669; font-weight: 700;">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Diplomacy Duel: Iterated PD</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Axelrod Tit-for-Tat and Nowak Pavlov Win-Stay/Lose-Shift duel.</div>
          </div>

          <div class="home-lab-card" data-id="lab-03" data-url="{{ site.baseurl }}/assets/decision-labs/lab-03-consensus-market/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Consensus Market: WTO Rounds" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #7c3aed; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #7c3aed;">LAB 03 &bull; TRADE DIPLOMACY</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Consensus Market: WTO Rounds</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Single Undertaking cross-sector issue logrolling across 8 trade blocs.</div>
          </div>

          <div class="home-lab-card" data-id="lab-04" data-url="{{ site.baseurl }}/assets/decision-labs/lab-04-spiral-watch/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Spiral Watch: Security Dilemma" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #dc2626; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #dc2626;">LAB 04 &bull; SECURITY DILEMMA</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Spiral Watch: Security Dilemma</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Jervis spiral model on Arctic PPI radar with offensive/defensive postures.</div>
          </div>

          <div class="home-lab-card" data-id="lab-05" data-url="{{ site.baseurl }}/assets/decision-labs/lab-05-veto-gauntlet/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Veto Gauntlet: UNSC Chapter VII" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #7c3aed; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #7c3aed;">LAB 05 &bull; GLOBAL GOVERNANCE</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Veto Gauntlet: UNSC Chapter VII</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Article 27(3) P5 veto constraints and E10 coalition bargaining.</div>
          </div>

          <div class="home-lab-card" data-id="lab-06" data-url="{{ site.baseurl }}/assets/decision-labs/lab-06-two-table-pressure/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Two-Table Pressure: Putnam Win-Sets" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #2563eb; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #2563eb;">LAB 06 &bull; DIPLOMACY</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Two-Table Pressure: Putnam Win-Sets</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Putnam two-level games synchronizing international and domestic tables.</div>
          </div>

          <div class="home-lab-card" data-id="lab-07" data-url="{{ site.baseurl }}/assets/decision-labs/lab-07-zone-runner/index.html" data-engine="Three.js 3D Engine" data-title="Zone Runner: UNCLOS 1982 (3D)" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #0284c7; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #0284c7;">LAB 07 &bull; LAW OF THE SEA</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: #0284c7; font-weight: 700;">Three.js 3D</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Zone Runner: UNCLOS 1982 (3D)</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Lawful maritime interdictions across 3D bathymetric coastal zones.</div>
          </div>

          <div class="home-lab-card" data-id="lab-08" data-url="{{ site.baseurl }}/assets/decision-labs/lab-08-equilibrium-keeper/index.html" data-engine="Three.js 3D Engine" data-title="Equilibrium Keeper: Balance of Power (3D)" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #dc2626; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #dc2626;">LAB 08 &bull; REALISM & BOP</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: #0284c7; font-weight: 700;">Three.js 3D</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Equilibrium Keeper: 1914 (3D)</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Great Power polarity shocks and chain-ganging on 3D tactical map.</div>
          </div>

          <div class="home-lab-card" data-id="lab-09" data-url="{{ site.baseurl }}/assets/decision-labs/lab-09-chairs-gambit/index.html" data-engine="Phaser 3 (2D Vector)" data-title="Chair's Gambit: ASEAN Consensus" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #2563eb; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #2563eb;">LAB 09 &bull; REGIONALISM</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: var(--lms-ink-tertiary);">Phaser 3</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Chair's Gambit: ASEAN Way</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">South China Sea consensus communiqué drafting without walkouts.</div>
          </div>

          <div class="home-lab-card" data-id="lab-10" data-url="{{ site.baseurl }}/assets/decision-labs/lab-10-second-strike-ledger/index.html" data-engine="Three.js 3D Engine" data-title="Second-Strike Ledger: Nuclear Triad (3D)" style="background: var(--lms-subtle); border: 1px solid var(--lms-hairline); border-left: 3px solid #dc2626; border-radius: var(--lms-radius-md); padding: 0.85rem 1rem; cursor: pointer; transition: all 0.15s ease;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
              <span style="font-family: ui-monospace, monospace; font-size: 0.68rem; font-weight: 700; color: #dc2626;">LAB 10 &bull; NUCLEAR DETERRENCE</span>
              <span style="font-family: ui-monospace, monospace; font-size: 0.65rem; color: #0284c7; font-weight: 700;">Three.js 3D</span>
            </div>
            <div style="font-size: 0.88rem; font-weight: 750; color: var(--lms-ink-primary);">Second-Strike Ledger (3D)</div>
            <div style="font-size: 0.75rem; color: var(--lms-ink-secondary); margin-top: 0.2rem; line-height: 1.4;">Schelling MAD triad budget balance and ABM dome stability on 3D globe.</div>
          </div>

        </div>
      </div>

    </div>

    <!-- Live Switcher Script -->
    <script>
      (function() {
        var frame = document.getElementById('homeLabFrame');
        var badge = document.getElementById('homeLiveBadge');
        var title = document.getElementById('homeLiveTitle');
        var engine = document.getElementById('homeLiveEngine');
        var tabBtn = document.getElementById('homeLiveTabBtn');
        var cards = document.querySelectorAll('.home-lab-card');

        cards.forEach(function(card) {
          card.addEventListener('click', function() {
            cards.forEach(function(c) {
              c.classList.remove('is-active-home-lab');
              c.style.border = '1px solid var(--lms-hairline)';
              c.style.boxShadow = 'none';
            });

            card.classList.add('is-active-home-lab');
            card.style.border = '1.5px solid #059669';
            card.style.boxShadow = '0 0 10px rgba(5, 150, 105, 0.15)';

            var url = card.getAttribute('data-url');
            var id = card.getAttribute('data-id');
            var t = card.getAttribute('data-title');
            var eng = card.getAttribute('data-engine');

            frame.src = url;
            badge.innerHTML = '&bull; LIVE ARENA &bull; ' + id.toUpperCase();
            title.textContent = t;
            engine.innerHTML = '&bull; Engine: ' + eng;
            tabBtn.href = url;
          });
        });
      })();
    </script>
  </section>

"""

new_content = content[:idx_start] + new_homepage_section + content[idx_end:]

with open(index_md_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Updated {index_md_path} successfully!")
