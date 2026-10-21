import os

embed_map = {
    '_includes/sim_crisis.html': {
        'id': 'lab-01-crisis-command',
        'title': 'Interactive Decision Lab 01: Crisis Command',
        'sub': 'Allison FPA Models (I, II, III) \u2022 1962 ExComm Cuban Missile Crisis'
    },
    '_includes/sim_game_theory.html': {
        'id': 'lab-02-diplomacy-duel',
        'title': 'Interactive Decision Lab 02: Diplomacy Duel',
        'sub': 'Axelrod Iterated PD \u2022 Nowak Pavlov WS/LS'
    },
    '_includes/sim_wto.html': {
        'id': 'lab-03-consensus-market',
        'title': 'Interactive Decision Lab 03: Consensus Market',
        'sub': 'WTO Ministerial Plenary \u2022 Single Undertaking Logrolling'
    },
    '_includes/sim_security_dilemma.html': {
        'id': 'lab-04-spiral-watch',
        'title': 'Interactive Decision Lab 04: Spiral Watch',
        'sub': 'Jervis Spiral Model \u2022 Arctic Early Warning Radar'
    },
    '_includes/sim_unsc_veto.html': {
        'id': 'lab-05-veto-gauntlet',
        'title': 'Interactive Decision Lab 05: Veto Gauntlet',
        'sub': 'UNSC Chapter VII Enforcement \u2022 Article 27(3) P5 Veto'
    },
    '_includes/sim_treaty_negotiation.html': {
        'id': 'lab-06-two-table-pressure',
        'title': 'Interactive Decision Lab 06: Two-Table Pressure',
        'sub': 'Putnam Two-Level Games \u2022 Win-Set Ratification'
    },
    '_includes/sim_unclos_zones.html': {
        'id': 'lab-07-zone-runner',
        'title': 'Interactive Decision Lab 07: Zone Runner (3D)',
        'sub': 'UNCLOS 1982 Maritime Regimes \u2022 3D Coastal Bathymetry'
    },
    '_includes/sim_balance_of_power.html': {
        'id': 'lab-08-equilibrium-keeper',
        'title': 'Interactive Decision Lab 08: Equilibrium Keeper (3D)',
        'sub': 'Balance of Power Polarity \u2022 1914 European Alliance Arcs'
    },
    '_includes/sim_scs_dispute.html': {
        'id': 'lab-09-chairs-gambit',
        'title': 'Interactive Decision Lab 09: Chair\'s Gambit',
        'sub': 'ASEAN Way Consensus \u2022 South China Sea Communiqu\u00e9'
    },
    '_includes/sim_nuclear_deterrence.html': {
        'id': 'lab-10-second-strike-ledger',
        'title': 'Interactive Decision Lab 10: Second-Strike Ledger (3D)',
        'sub': 'Schelling Deterrence Triad \u2022 3D Strategic Defense Globe'
    }
}

template = """<!-- ================================================================= -->
<!-- {title} -->
<!-- ================================================================= -->
<section class="lab-embed-wrapper" id="sim-{id}-container" aria-label="{title}">
  <div class="lab-embed-header">
    <div class="lab-embed-meta">
      <div class="lab-icon-tag">&#9874;</div>
      <div>
        <div class="lab-embed-title-text">{title}</div>
        <div class="lab-embed-sub-text">{sub}</div>
      </div>
    </div>
    <div class="lab-embed-actions">
      <a href="{{{{ site.baseurl }}}}/assets/decision-labs/{id}/index.html" target="_blank" class="embed-action-btn" title="Open Lab in Dedicated Window">
        <span>&#x2922; EXPAND / FULLSCREEN</span>
      </a>
    </div>
  </div>

  <iframe 
    id="{id}-frame"
    src="{{{{ site.baseurl }}}}/assets/decision-labs/{id}/index.html" 
    class="lab-embed-frame" 
    loading="lazy" 
    allow="autoplay; fullscreen"
    title="{title}">
  </iframe>

  <div class="lab-embed-footer">
    <span>STATUS: 7-PHASE PEDAGOGICAL CYCLE ACTIVE</span>
    <span>ONBOARDING: ACTIVE &bull; PRESS [?] IN LAB FOR MANUAL</span>
  </div>
</section>
"""

base_dir = r"D:\PERSONAL PROJECT\IR-study-companion"

for rel_path, info in embed_map.items():
    full_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
    rendered = template.format(id=info['id'], title=info['title'], sub=info['sub'])
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Wrote {rel_path}")

print("ALL 10 SIM_*.HTML REPLACED!")
