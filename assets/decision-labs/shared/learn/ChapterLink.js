/**
 * ChapterLink — Canonical chapter bindings for Decision Labs.
 * Maps lab IDs to canonical curriculum chapters on ir-guide.netlify.app.
 */

export const CHAPTER_BASE = 'https://ir-guide.netlify.app';

export const LAB_CHAPTERS = {
  'lab-01': [
    { slug: 'models-fpdm', title: 'Understanding Models Of Decision Making In FPA' },
    { slug: 'realism-security', title: 'Realism In Security Studies' }
  ],
  'lab-02': [
    { slug: 'game-theory-ir', title: 'Game Theory' },
    { slug: 'rational-choice-theory', title: 'Rational Choice Theory' }
  ],
  'lab-03': [
    { slug: 'wto-decision-making', title: 'How the WTO Makes Decisions' },
    { slug: 'world-trading-system', title: 'World Trading System In The 20th Century And Beyond' }
  ],
  'lab-04': [
    { slug: 'realism-security', title: 'Realism In Security Studies' },
    { slug: 'institution-security', title: 'Institution In International Security' }
  ],
  'lab-05': [
    { slug: 'un-security', title: 'The United Nations: Maintaining International Peace And Security' },
    { slug: 'the-use-of-force-in-international-law', title: 'The Use Of Force In International Law' }
  ],
  'lab-06': [
    { slug: 'level-of-analysis-fpdm', title: 'Level Of Analysis In Foreign Policy Decision Making' },
    { slug: 'factors-fpdm', title: 'Factor Affecting Foreign Policy Decision' }
  ],
  'lab-07': [
    { slug: 'law-of-the-sea', title: 'The Law Of The Sea' },
    { slug: 'the-use-of-force-in-international-law', title: 'The Use Of Force In International Law' }
  ],
  'lab-08': [
    { slug: 'neorealism-ir', title: 'Neorealism' },
    { slug: 'classical-realism', title: 'Classical Realism' }
  ],
  'lab-09': [
    { slug: 'asean-chapter', title: 'Understanding the ASEAN Charter' },
    { slug: 'asean-community', title: 'Understanding ASEAN Community' }
  ],
  'lab-10': [
    { slug: 'realism-security', title: 'Realism In Security Studies' },
    { slug: 'neorealism-ir', title: 'Neorealism' }
  ]
};

/**
 * Builds canonical URL for a chapter slug.
 * @param {string} slug
 * @returns {string}
 */
export function chapterUrl(slug) {
  if (!slug) return CHAPTER_BASE;
  return `${CHAPTER_BASE}/${slug}.html`;
}

/**
 * Retrieves curriculum chapters bound to a lab ID.
 * @param {string} labId
 * @returns {Array<{ slug: string, title: string }>}
 */
export function chaptersFor(labId) {
  return LAB_CHAPTERS[labId] || [];
}
