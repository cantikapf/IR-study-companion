import { LearningSession } from '../../shared/learn/LearningSession.js';

export const UNCLOS_OBJECTIVES = [
  'Map state authority across internal waters, territorial sea, contiguous zone, EEZ, continental shelf, and high seas.',
  'Distinguish full territorial sovereignty from functional sovereign resource rights.',
  'Apply Articles 8, 17, 33, 56, 77, and 110 to operational maritime interception incidents.'
];

export const UNCLOS_INCIDENTS = [
  {
    id: 'inc-01',
    zoneId: 'internal_waters',
    zoneName: 'Internal Waters',
    limit: 'Landward of Baseline (0 NM)',
    vesselType: 'Commercial Bulk Carrier',
    vesselName: 'M/V Pacific Dawn',
    domain: 'surface',
    location: 'Enclosed Inner Bay (Landward of Baseline)',
    depth: 18,
    targetCoords: { x: -65, z: 0 },
    scenario: 'A foreign-flagged commercial freighter enters an enclosed baseline bay and drops anchor without port clearance or customs manifest, refusing radio contact with the harbor master.',
    predictionPrompt: 'Predict coastal state legal authority in internal waters under Article 8:',
    predictionOptions: [
      { key: 'A', text: 'Vessel enjoys innocent passage; coastal authorities cannot seize without proof of environmental crime.' },
      { key: 'B', text: 'Coastal state exercises plenary sovereignty; vessel has no right of innocent passage and may be seized.' },
      { key: 'C', text: 'Only the flag state possesses criminal jurisdiction in ports.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 8):',
    correctAction: 'SEIZE_ARREST',
    objectiveIndex: 0,
    rationale: 'Under UNCLOS Article 8(1), internal waters form part of the sovereign territory of the coastal state. Foreign vessels possess no customary right of innocent passage landward of the baseline.',
    mechanism: 'Plenary coastal territorial sovereignty over internal waters',
    citation: 'UNCLOS (1982), Article 8(1) & Article 25(2)',
    consequence: 'Coast Guard boarding team boards and seizes the vessel under domestic port jurisdiction. The vessel is detained pending judicial investigation.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_eez_sovereignty',
        label: 'Innocent Passage Assumption in Internal Waters',
        remediation: 'Internal waters lie landward of the baseline. Unlike the territorial sea, there is zero customary right of innocent passage in internal waters under Article 8.'
      },
      BOARD_VERIFY: {
        tag: 'misc_eez_sovereignty',
        label: 'Hesitant Enforcement in Sovereign Waters',
        remediation: 'Under Article 25(2), coastal states possess plenary sovereignty in internal waters to arrest unauthorized entries, exceeding mere high-seas verification visits.'
      }
    }
  },
  {
    id: 'inc-02',
    zoneId: 'territorial_sea',
    zoneName: 'Territorial Sea',
    limit: '0 to 12 Nautical Miles',
    vesselType: 'Container Vessel',
    vesselName: 'M/V Atlantic Trader',
    domain: 'water_column',
    location: '7.5 NM Offshore (Territorial Sea)',
    depth: 42,
    targetCoords: { x: -42, z: -5 },
    scenario: 'A foreign container ship navigates along a standard commercial traffic lane 7.5 NM off the coast with AIS transmitting, weapons stowed, and in continuous expeditious passage.',
    predictionPrompt: 'Predict the legal regime governing merchant shipping in the 12 NM territorial sea:',
    predictionOptions: [
      { key: 'A', text: 'Coastal states can block any foreign merchant ship from entering the 12 NM zone.' },
      { key: 'B', text: 'All vessels enjoy the right of innocent passage provided navigation is continuous and peaceful.' },
      { key: 'C', text: 'Merchant ships require prior diplomatic clearance before transiting the territorial sea.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 17):',
    correctAction: 'PERMIT_TRANSIT',
    objectiveIndex: 1,
    rationale: 'Article 17 guarantees innocent passage through the territorial sea to ships of all states, provided transit is continuous, expeditious, and non-prejudicial to peace and good order (Article 19).',
    mechanism: 'The innocent passage regime as a balance of coastal sovereignty and international transit',
    citation: 'UNCLOS (1982), Article 17 & Article 18',
    consequence: 'Patrol cutter monitors the transit via radar telemetry. The container vessel safely traverses the territorial sea without impediment.',
    misconceptions: {
      SEIZE_ARREST: {
        tag: 'misc_eez_sovereignty',
        label: 'Territorial Sea Absolute Closure Fallacy',
        remediation: 'While the territorial sea is sovereign territory, Article 17 limits sovereignty by granting foreign vessels the inviolable right of innocent passage.'
      },
      BOARD_VERIFY: {
        tag: 'misc_universal_boarding',
        label: 'Unwarranted Interdiction of Innocent Passage',
        remediation: 'Coastal states cannot arbitrarily stop or board vessels in innocent passage unless the ship commits an act prejudicial to peace or security under Article 19.'
      }
    }
  },
  {
    id: 'inc-03',
    zoneId: 'territorial_sea',
    zoneName: 'Territorial Sea',
    limit: '0 to 12 Nautical Miles',
    vesselType: 'Armed Private Escort Craft',
    vesselName: 'M/V Sentinel Alpha',
    domain: 'surface',
    location: '4.5 NM Offshore (Territorial Sea)',
    depth: 28,
    targetCoords: { x: -48, z: 8 },
    scenario: 'An armed private maritime security contractor conducts live-fire machine gun calibration drills and launches tactical drones 4.5 NM off the coast without notifying coastal authorities.',
    predictionPrompt: 'Predict the legal effect of military exercises on innocent passage under Article 19:',
    predictionOptions: [
      { key: 'A', text: 'Weapons practice and surveillance render the passage non-innocent under Article 19(2).' },
      { key: 'B', text: 'Private security craft retain full innocent passage rights regardless of weapon firing.' },
      { key: 'C', text: 'Coastal states can only file diplomatic complaints and cannot use force.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Coast Guard Enforcement Action (Article 19 & 25):',
    correctAction: 'SEIZE_ARREST',
    objectiveIndex: 2,
    rationale: 'Under Article 19(2)(b), any exercise or practice with weapons of any kind renders passage non-innocent. Under Article 25(1), the coastal state may take the necessary steps to prevent passage which is not innocent.',
    mechanism: 'Loss of innocent passage status triggering enforcement interception',
    citation: 'UNCLOS (1982), Article 19(2)(b) & Article 25(1)',
    consequence: 'Patrol cutter executes close-quarters interdiction, orders weapons disarmed, and arrests the craft under Article 25 for non-innocent weapons discharge in territorial waters.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_eez_sovereignty',
        label: 'Unconditional Passage Fallacy',
        remediation: 'Innocent passage is strictly conditional. Article 19 lists explicit disqualifying activities, including weapons practice, surveillance, and pollution.'
      },
      BOARD_VERIFY: {
        tag: 'misc_eez_sovereignty',
        label: 'Insufficient Enforcement Against Territorial Violations',
        remediation: 'Armed live-fire in territorial waters is an immediate violation of coastal security; Article 25 authorizes decisive interdiction and arrest.'
      }
    }
  },
  {
    id: 'inc-04',
    zoneId: 'contiguous_zone',
    zoneName: 'Contiguous Zone',
    limit: '12 to 24 Nautical Miles',
    vesselType: 'Refrigerated Cargo Ship',
    vesselName: 'S/S Frost Queen',
    domain: 'surface',
    location: '18 NM Offshore (Contiguous Zone)',
    depth: 75,
    targetCoords: { x: -18, z: -4 },
    scenario: 'A vessel bound for the coastal state port arrives from an acute viral epidemic outbreak zone, having intentionally severed communications and skipped mandatory maritime sanitary declarations.',
    predictionPrompt: 'Predict coastal state enforcement jurisdiction in the 24 NM contiguous zone:',
    predictionOptions: [
      { key: 'A', text: 'Coastal states have zero authority outside 12 NM.' },
      { key: 'B', text: 'Article 33 authorizes coastal states to prevent and punish infringements of customs, fiscal, immigration, or sanitary (FISC) laws.' },
      { key: 'C', text: 'Contiguous zone powers apply only to environmental pollution.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 33):',
    correctAction: 'BOARD_VERIFY',
    objectiveIndex: 0,
    rationale: 'Under Article 33, in a zone contiguous to its territorial sea extending up to 24 NM, the coastal state may exercise the control necessary to prevent and punish infringement of its customs, fiscal, immigration, or sanitary (FISC) laws.',
    mechanism: 'Functional FISC enforcement jurisdiction in the contiguous zone',
    citation: 'UNCLOS (1982), Article 33(1)(a)',
    consequence: 'Specialized biohazard boarding team boards the vessel under Article 33 sanitary powers, enforces quarantine isolation, and verifies health documentation.',
    misconceptions: {
      SEIZE_ARREST: {
        tag: 'misc_eez_sovereignty',
        label: 'Contiguous Zone Sovereignty Confusion',
        remediation: 'The contiguous zone is not sovereign territory. Article 33 confers control powers to prevent or punish FISC violations, requiring verification before seizure.'
      },
      PERMIT_TRANSIT: {
        tag: 'misc_eez_sovereignty',
        label: 'Neglect of FISC Jurisdiction',
        remediation: 'Article 33 expressly grants coastal states powers to intercept vessels entering territorial waters to enforce sanitary and immigration compliance.'
      }
    }
  },
  {
    id: 'inc-05',
    zoneId: 'contiguous_zone',
    zoneName: 'Contiguous Zone',
    limit: '12 to 24 Nautical Miles',
    vesselType: 'Foreign Guided-Missile Destroyer',
    vesselName: 'Warship DDG-88',
    domain: 'water_column',
    location: '21.5 NM Offshore (Contiguous Zone)',
    depth: 110,
    targetCoords: { x: -10, z: 12 },
    scenario: 'A foreign naval destroyer transits at 24 knots through the contiguous zone 21.5 NM offshore. Local port authorities order the cutter to board the warship to inspect its cargo manifest.',
    predictionPrompt: 'Predict warship status in the contiguous zone under UNCLOS Articles 33, 58, and 95:',
    predictionOptions: [
      { key: 'A', text: 'Warships enjoy sovereign immunity and freedom of navigation; coastal FISC powers do not permit boarding foreign warships.' },
      { key: 'B', text: 'Coastal states can subject foreign warships to commercial customs boardings in the contiguous zone.' },
      { key: 'C', text: 'Warships are barred from entering the contiguous zone without prior notification.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Coast Guard Enforcement Action (Articles 33 & 95):',
    correctAction: 'PERMIT_TRANSIT',
    objectiveIndex: 1,
    rationale: 'Under UNCLOS Articles 58 and 95, warships on the high seas and in the EEZ/contiguous zone enjoy complete immunity from the jurisdiction of any state other than the flag state. FISC powers do not apply to sovereign warships.',
    mechanism: 'Sovereign immunity and navigational freedoms of naval vessels',
    citation: 'UNCLOS (1982), Article 33, Article 58 & Article 95',
    consequence: 'Patrol cutter maintains standoff tracking and acknowledges the destroyer transit. Foreign warships preserve complete sovereign immunity under international law.',
    misconceptions: {
      BOARD_VERIFY: {
        tag: 'misc_universal_boarding',
        label: 'Warship Boarding Fallacy',
        remediation: 'Warships possess complete sovereign immunity under Article 95. A coastal state cannot board a foreign warship in the contiguous zone or EEZ.'
      },
      SEIZE_ARREST: {
        tag: 'misc_universal_boarding',
        label: 'Illegal Use of Force Against Sovereign Vessel',
        remediation: 'Attempting to seize a foreign warship is an unlawful act of aggression violating Article 95 sovereign immunity and UN Charter Article 2(4).'
      }
    }
  },
  {
    id: 'inc-06',
    zoneId: 'eez',
    zoneName: 'Exclusive Economic Zone',
    limit: '24 to 200 Nautical Miles',
    vesselType: 'Industrial Purse-Seine Trawler',
    vesselName: 'F/V Mar Del Sol',
    domain: 'water_column',
    location: '85 NM Offshore (EEZ)',
    depth: 280,
    targetCoords: { x: 12, z: -8 },
    scenario: 'An unauthorized foreign distant-water trawler is caught on forward-looking infrared actively deploying purse-seine nets and hauling pelagic yellowfin tuna inside the coastal state 200 NM EEZ.',
    predictionPrompt: 'Predict coastal state sovereign rights over living marine resources in the EEZ:',
    predictionOptions: [
      { key: 'A', text: 'EEZ waters are high seas commons where all nations fish freely.' },
      { key: 'B', text: 'Coastal state has sovereign rights over biological resources and full legal authority to arrest illegal fishers under Article 73.' },
      { key: 'C', text: 'Coastal state can only issue diplomatic complaints without physical arrest.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 56 & 73):',
    correctAction: 'SEIZE_ARREST',
    objectiveIndex: 2,
    rationale: 'Article 56(1)(a) grants coastal states sovereign rights for exploring, exploiting, conserving, and managing living natural resources. Article 73(1) authorizes the coastal state to board, inspect, arrest, and initiate judicial proceedings against illegal fishing vessels.',
    mechanism: 'Exclusive sovereign rights over living resources in the EEZ coupled with enforcement powers',
    citation: 'UNCLOS (1982), Article 56(1)(a) & Article 73(1)',
    consequence: 'Patrol cutter launches its interceptor boat, boards the trawler, impounds the fishing gear and catch, and escorts the vessel to port for prosecution under Article 73.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_eez_sovereignty',
        label: 'EEZ Living Resource Misconception',
        remediation: 'Freedom of navigation in the EEZ does not include fishing. Living marine resources in the EEZ belong exclusively to the coastal state under Article 56.'
      },
      BOARD_VERIFY: {
        tag: 'misc_eez_sovereignty',
        label: 'Under-Enforcement in EEZ Resource Theft',
        remediation: 'Article 73 gives explicit power to seize and arrest vessels caught actively poaching living resources in the EEZ, not merely observe.'
      }
    }
  },
  {
    id: 'inc-07',
    zoneId: 'eez',
    zoneName: 'Exclusive Economic Zone',
    limit: '24 to 200 Nautical Miles',
    vesselType: 'Commercial Freighter',
    vesselName: 'M/V Nordic Pioneer',
    domain: 'water_column',
    location: '145 NM Offshore (EEZ)',
    depth: 1200,
    targetCoords: { x: 22, z: 6 },
    scenario: 'A foreign merchant freighter transits 145 NM offshore carrying consumer electronic containers between two foreign ports. Coastal ministry orders patrol cutter to halt and search its commercial cargo manifest.',
    predictionPrompt: 'Predict coastal state authority over foreign commercial navigation in the EEZ:',
    predictionOptions: [
      { key: 'A', text: 'Coastal states can inspect any commercial ship passing through their 200 NM EEZ.' },
      { key: 'B', text: 'In the EEZ, all foreign vessels enjoy high-seas freedom of navigation under Article 58.' },
      { key: 'C', text: 'Merchant vessels require prior innocent passage clearance in the EEZ.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 58):',
    correctAction: 'PERMIT_TRANSIT',
    objectiveIndex: 1,
    rationale: 'Under Article 58(1), all states enjoy the freedoms of navigation and overflight in the EEZ as referred to in Article 87. Coastal state rights in the EEZ are strictly functional and economic (Article 56), not general police sovereignty.',
    mechanism: 'Preservation of high-seas freedoms of navigation in the EEZ',
    citation: 'UNCLOS (1982), Article 58(1) & Article 87',
    consequence: 'Patrol cutter stands down and permits unhindered transit. Merchant navigation in the EEZ is governed by high-seas navigation freedoms.',
    misconceptions: {
      SEIZE_ARREST: {
        tag: 'misc_eez_sovereignty',
        label: 'EEZ Territorial Sovereignty Fallacy',
        remediation: 'The EEZ is not a 200 NM territorial sea. Coastal rights are limited to natural resources; foreign vessels enjoy freedom of navigation under Article 58.'
      },
      BOARD_VERIFY: {
        tag: 'misc_eez_sovereignty',
        label: 'Unlawful EEZ Navigation Interference',
        remediation: 'A coastal state has no right to board a merchant ship in the EEZ simply to audit cargo unless there is reasonable suspicion under Article 110 or coastal pollution under Article 220.'
      }
    }
  },
  {
    id: 'inc-08',
    zoneId: 'eez',
    zoneName: 'Exclusive Economic Zone',
    limit: '24 to 200 Nautical Miles',
    vesselType: 'Oceanographic Research Vessel',
    vesselName: 'R/V Poseidon Echo',
    domain: 'water_column',
    location: '175 NM Offshore (EEZ)',
    depth: 1850,
    targetCoords: { x: 28, z: -10 },
    scenario: 'A foreign research ship is detected deploying autonomous seismic survey probes and acoustic seafloor scanners 175 NM offshore without obtaining prior consent from the coastal state.',
    predictionPrompt: 'Predict coastal state rights over Marine Scientific Research (MSR) in the EEZ:',
    predictionOptions: [
      { key: 'A', text: 'Marine scientific research in the EEZ requires coastal state consent under Article 246.' },
      { key: 'B', text: 'All scientific research in the EEZ is an unrestricted freedom of the seas.' },
      { key: 'C', text: 'Only military oceanography requires coastal state approval.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Coast Guard Enforcement Action (Article 246 & 253):',
    correctAction: 'BOARD_VERIFY',
    objectiveIndex: 2,
    rationale: 'Under Article 246, coastal states have the right to regulate, authorize, and conduct marine scientific research in their EEZ. Under Article 253, coastal states may require the suspension or cessation of research conducted without consent.',
    mechanism: 'Coastal state jurisdiction over Marine Scientific Research',
    citation: 'UNCLOS (1982), Article 246 & Article 253',
    consequence: 'Boarding detachment boards the research ship, audits scientific authorizations, and orders immediate cessation and retrieval of survey probes under Article 253.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_eez_sovereignty',
        label: 'MSR Anarchy Assumption',
        remediation: 'Marine scientific research is not an unrestricted freedom in the EEZ. Article 246 gives coastal states the right to regulate and consent to MSR.'
      },
      SEIZE_ARREST: {
        tag: 'misc_eez_sovereignty',
        label: 'Disproportionate Response to MSR Breach',
        remediation: 'Article 253 prescribes ordering the suspension or cessation of unauthorized research before punitive seizure of the scientific vessel.'
      }
    }
  },
  {
    id: 'inc-09',
    zoneId: 'continental_shelf',
    zoneName: 'Extended Continental Shelf',
    limit: 'Up to 350 NM / Outer Continental Shelf',
    vesselType: 'Deep-Sea Core Drillship',
    vesselName: 'M/V Subsea Titan',
    domain: 'seabed',
    location: '275 NM Offshore (Outer Continental Shelf)',
    depth: 2600,
    targetCoords: { x: 45, z: 5 },
    scenario: 'A foreign exploration drillship positions dynamic positioning thrusters over the coastal state approved extended continental shelf 275 NM offshore and begins core-drilling into the subsoil for polymetallic nodules.',
    predictionPrompt: 'Predict the legal status of seabed minerals on the extended continental shelf beyond 200 NM:',
    predictionOptions: [
      { key: 'A', text: 'Beyond 200 NM, seabed minerals belong to the high seas commons and can be drilled freely.' },
      { key: 'B', text: 'The coastal state has exclusive sovereign rights over seabed and subsoil mineral resources under Article 77.' },
      { key: 'C', text: 'Continental shelf rights extend to the water column above, closing the area to fishing.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Coast Guard Enforcement Action (Article 77 & 80):',
    correctAction: 'BOARD_VERIFY',
    objectiveIndex: 1,
    rationale: 'Under Article 77, the coastal state exercises sovereign rights over the continental shelf for the purpose of exploring it and exploiting its natural resources. These rights are exclusive: if the coastal state does not exploit them, no one may undertake these activities without express consent.',
    mechanism: 'Exclusive sovereign rights over continental shelf seabed minerals distinct from superjacent water column',
    citation: 'UNCLOS (1982), Article 77 & Article 78',
    consequence: 'Cutter team boards to verify exploitation permits, inspects subsoil drilling logs, and orders drilling operations halted under Article 77 and Article 80.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_seabed_water_column',
        label: 'Seabed vs Water Column Rights Confusion',
        remediation: 'Do not confuse the water column with the seabed. While the superjacent water column beyond 200 NM is High Seas (Article 78), seabed mineral rights belong exclusively to the coastal state under Article 77.'
      },
      SEIZE_ARREST: {
        tag: 'misc_seabed_water_column',
        label: 'Overreach on High Seas Water Surface',
        remediation: 'Because the surface waters 275 NM offshore remain High Seas under Article 78, enforcement begins with inspection and cessation orders regarding seabed drilling, not immediate vessel forfeiture.'
      }
    }
  },
  {
    id: 'inc-10',
    zoneId: 'high_seas',
    zoneName: 'High Seas',
    limit: 'Beyond 200 NM (International Waters)',
    vesselType: 'Unflagged Suspicious Trawler',
    vesselName: 'Nameless Vessel',
    domain: 'surface',
    location: '310 NM Offshore (High Seas)',
    depth: 4200,
    targetCoords: { x: 72, z: 0 },
    scenario: 'A 45-meter vessel on the high seas flies no flag, shows no registration markings, broadcasts no AIS signal, and attempts evasive maneuvers when hailed by radio.',
    predictionPrompt: 'Predict right of visit conditions on the high seas under UNCLOS Article 110:',
    predictionOptions: [
      { key: 'A', text: 'Warships have zero boarding rights on the high seas under any circumstance.' },
      { key: 'B', text: 'Warships have the universal Right of Visit if there is reasonable ground for suspecting statelessness or piracy.' },
      { key: 'C', text: 'Only United Nations chartered vessels can board unflagged ships.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Warship Enforcement Action (Article 110):',
    correctAction: 'BOARD_VERIFY',
    objectiveIndex: 2,
    rationale: 'Article 110(1)(d) authorizes a warship to board a foreign merchant ship on the high seas if there is reasonable ground for suspecting that the ship is without nationality (stateless). This is the universal Right of Visit.',
    mechanism: 'Universal Right of Visit on the high seas for statelessness and piracy',
    citation: 'UNCLOS (1982), Article 110(1)(d)',
    consequence: 'Warship dispatches an armed boarding party under Article 110 to verify ship documentation and determine nationality. If confirmed stateless, the ship lacks flag state protection.',
    misconceptions: {
      PERMIT_TRANSIT: {
        tag: 'misc_universal_boarding',
        label: 'Stateless Immunity Misconception',
        remediation: 'High-seas freedom of navigation requires ship registration under a responsible flag state. Under Article 110, warships have the right to board stateless vessels to verify identity.'
      },
      SEIZE_ARREST: {
        tag: 'misc_universal_boarding',
        label: 'Premature Seizure on High Seas',
        remediation: 'Article 110 requires first boarding for verification of documents. Only if documentation reveals statelessness, piracy, or slave trading does seizure follow.'
      }
    }
  }
];

export const UNCLOS_MASTERY_QUESTIONS = [
  {
    questionId: 'unclos-mc-01',
    prompt: 'Under UNCLOS Article 56, what is the fundamental legal distinction between the Territorial Sea and the Exclusive Economic Zone (EEZ)?',
    options: [
      { key: 'A', text: 'The Territorial Sea grants full territorial sovereignty (subject to innocent passage), whereas the EEZ confers only functional sovereign rights for natural resource exploitation.' },
      { key: 'B', text: 'The EEZ extends full criminal and civil police sovereignty out to 200 NM.' },
      { key: 'C', text: 'The Territorial Sea is an international commons while the EEZ is closed to all foreign navigation.' }
    ],
    correct: 'A',
    objectiveIndex: 1,
    rationale: 'The Territorial Sea (Article 2) is sovereign state territory where the coastal state exercises full legislative and judicial sovereignty. In contrast, the EEZ (Article 56) is a sui generis zone granting functional sovereign rights strictly over resources, preserving high seas freedoms of navigation (Article 58).',
    citation: 'UNCLOS (1982), Article 2 & Article 56',
    misconceptionTag: 'misc_eez_sovereignty'
  },
  {
    questionId: 'unclos-mc-02',
    prompt: 'A foreign vessel catches swimming pelagic tuna 250 NM offshore over an approved Extended Continental Shelf claim. Under Articles 77 and 78, how is this activity regulated?',
    options: [
      { key: 'A', text: 'The coastal state may arrest the vessel because continental shelf rights include all living resources in the water above.' },
      { key: 'B', text: 'The vessel may fish freely because the water column beyond 200 NM is High Seas; continental shelf rights are strictly confined to seabed and sedentary species.' },
      { key: 'C', text: 'The International Seabed Authority must auction fishing permits.' }
    ],
    correct: 'B',
    objectiveIndex: 1,
    rationale: 'Article 78 explicitly provides that coastal rights over the continental shelf do not affect the legal status of the superjacent waters. Beyond 200 NM, the water column is High Seas where freedom of fishing applies (Article 87); continental shelf rights (Article 77) apply only to mineral resources and sedentary species attached to the seabed.',
    citation: 'UNCLOS (1982), Article 77 & Article 78',
    misconceptionTag: 'misc_seabed_water_column'
  },
  {
    questionId: 'unclos-mc-03',
    prompt: 'Under UNCLOS Article 110 (Right of Visit), which of the following provides legitimate legal grounds for a warship to board a foreign merchant ship on the high seas?',
    options: [
      { key: 'A', text: 'The foreign ship is transporting commercial cargo without paying coastal tariffs.' },
      { key: 'B', text: 'The foreign ship is flying the flag of an unfriendly or non-allied nation during peacetime.' },
      { key: 'C', text: 'Reasonable grounds exist to suspect the vessel is engaged in piracy, the slave trade, unauthorized broadcasting, or is without nationality (stateless).' }
    ],
    correct: 'C',
    objectiveIndex: 2,
    rationale: 'Article 110 codifies an exhaustive list of exceptions to the exclusive jurisdiction of the flag state on the high seas: piracy, slave trade, unauthorized broadcasting, statelessness, or flying a false flag.',
    citation: 'UNCLOS (1982), Article 110',
    misconceptionTag: 'misc_universal_boarding'
  }
];

export const UNCLOS_TRANSFER_SCENARIO = {
  scenarioId: 'transfer-south-china-sea',
  title: 'The 2016 South China Sea Arbitral Award (Philippines v. China)',
  prompt: 'In Philippines v. China (2016), the Permanent Court of Arbitration (PCA) evaluated maritime entitlements in the Spratly Islands. A claimant state constructed massive artificial installations and military airfields on submerged low-tide elevations (e.g., Mischief Reef, Subi Reef) and claimed a 200 NM Exclusive Economic Zone radiating from them. Based on UNCLOS Articles 13, 60(8), and 121(3), does an artificial island or modified low-tide elevation generate an EEZ?',
  options: [
    { key: 'A', text: 'Yes: once an artificial island contains permanent structures and military garrisons, it legally qualifies as a natural island with a 200 NM EEZ.' },
    { key: 'B', text: 'No: under Article 60(8), artificial islands have no territorial sea of their own and do not affect delimitation; under Article 121(3), rocks that cannot sustain human habitation or economic life cannot generate an EEZ.' },
    { key: 'C', text: 'Yes, but only if approved unanimously by the International Seabed Authority.' }
  ],
  correct: 'B',
  objectiveIndex: 0,
  rationale: 'The 2016 PCA Arbitral Tribunal held under UNCLOS Article 60(8) that artificial islands and installations do not possess the status of islands, have no territorial sea of their own, and do not generate an EEZ or continental shelf. Furthermore, under Article 121(3), features that in their natural condition cannot sustain human habitation or economic life are rocks that cannot generate an EEZ regardless of artificial engineering.',
  citation: 'PCA (2016), South China Sea Arbitration (Philippines v. China), Award on Merits, paras 508-540; UNCLOS (1982), Arts 60(8), 121(3).'
};

export class UnclosState {
  constructor() {
    this.session = new LearningSession('lab-07', UNCLOS_OBJECTIVES);
    this.reset();
  }

  reset() {
    this.session = new LearningSession('lab-07', UNCLOS_OBJECTIVES);
    this.incidentIndex = 0;
    this.tokens = 3;
    this.score = 0;
    this.streak = 0;
    this.currentPrediction = null;
    this.currentFeedback = null;
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, MASTERY, TRANSFER, DEBRIEF
    this.masteryIndex = 0;
  }

  getCurrentIncident() {
    return UNCLOS_INCIDENTS[this.incidentIndex] || null;
  }

  recordPrediction(predictionKey) {
    const inc = this.getCurrentIncident();
    if (!inc) return;
    this.currentPrediction = predictionKey;
    this.session.recordPrediction(inc.id, predictionKey);
    this.phase = 'DECIDE';
  }

  executeDecision(actionVerb) {
    const inc = this.getCurrentIncident();
    if (!inc) return null;

    const isCorrect = (actionVerb === inc.correctAction);
    const predictedMatch = (this.currentPrediction === inc.expectedPrediction);

    let misconception = null;
    if (!isCorrect && inc.misconceptions && inc.misconceptions[actionVerb]) {
      misconception = inc.misconceptions[actionVerb];
    }

    if (isCorrect) {
      this.streak++;
      const multiplier = this.streak >= 3 ? 1.5 : 1.0;
      this.score += Math.round(15 * multiplier);
    } else {
      this.streak = 0;
      this.tokens = Math.max(0, this.tokens - 1);
    }

    const payload = {
      outcome: isCorrect ? 'success' : 'failure',
      consequence: inc.consequence,
      mechanism: inc.mechanism,
      citation: inc.citation,
      misconception,
      predictionMatch: predictedMatch
    };

    this.session.recordDecision({
      decisionId: inc.id,
      choice: actionVerb,
      correctChoice: inc.correctAction,
      rationale: inc.rationale,
      misconceptionTag: misconception ? misconception.tag : null,
      misconception,
      predicted: this.currentPrediction,
      actual: inc.expectedPrediction,
      outcome: payload.outcome,
      consequence: payload.consequence,
      mechanism: payload.mechanism,
      citation: payload.citation,
      objectiveIndex: inc.objectiveIndex
    });

    this.currentFeedback = payload;
    this.phase = 'CONSEQUENCE';

    return {
      isCorrect,
      payload,
      tokensLeft: this.tokens,
      score: this.score
    };
  }

  advanceIncident() {
    this.incidentIndex++;
    this.currentPrediction = null;
    this.currentFeedback = null;

    if (this.incidentIndex < UNCLOS_INCIDENTS.length) {
      this.phase = 'PREDICT';
      return true;
    }
    this.phase = 'MASTERY';
    return false;
  }

  getCurrentMasteryQuestion() {
    return UNCLOS_MASTERY_QUESTIONS[this.masteryIndex] || null;
  }

  answerMasteryQuestion(chosenKey) {
    const q = this.getCurrentMasteryQuestion();
    if (!q) return null;

    const isCorrect = (chosenKey === q.correct);
    this.session.recordMasteryCheck({
      questionId: q.questionId,
      chosen: chosenKey,
      correct: q.correct,
      misconceptionTag: !isCorrect ? q.misconceptionTag : null,
      objectiveIndex: q.objectiveIndex
    });

    this.masteryIndex++;
    const hasMore = this.masteryIndex < UNCLOS_MASTERY_QUESTIONS.length;
    if (!hasMore) {
      this.phase = 'TRANSFER';
    }

    return {
      isCorrect,
      hasMore,
      rationale: q.rationale,
      citation: q.citation
    };
  }

  answerTransfer(chosenKey) {
    const t = UNCLOS_TRANSFER_SCENARIO;
    const isCorrect = (chosenKey === t.correct);

    this.session.recordTransfer({
      scenarioId: t.scenarioId,
      choice: chosenKey,
      correct: t.correct,
      objectiveIndex: t.objectiveIndex
    });

    this.phase = 'DEBRIEF';
    return {
      isCorrect,
      rationale: t.rationale,
      citation: t.citation
    };
  }

  getReport() {
    return this.session.getReport();
  }

  getStars() {
    return this.session.getStars();
  }
}

