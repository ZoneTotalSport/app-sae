// ============================================
// APP SAE PFEQ — Zone Total Sport
// ============================================

'use strict';

const SAE_SOURCES = [
  { key: 'prescolaire', path: 'data/sae/prescolaire.json', label: 'Prescolaire', cycle: 'Prescolaire' },
  { key: 'primaire', path: 'data/sae/primaire.json', label: 'Primaire', cycle: 'Primaire' },
  { key: 'secondaire', path: 'data/sae/secondaire.json', label: 'Secondaire', cycle: 'Secondaire' },
  { key: 'cooperation', path: 'data/sae/cooperation.json', label: 'Cooperation', cycle: 'Primaire', arrayKey: 'saes' },
  { key: 'collectifs', path: 'data/sae/collectifs.json', label: 'Sports Collectifs', cycle: 'Secondaire', arrayKey: 'saes' },
  { key: 'opposition', path: 'data/sae/opposition.json', label: 'Opposition', cycle: 'Secondaire' },
  { key: 'dodgeball', path: 'data/sae/dodgeball.json', label: 'Ballon Chasseur', cycle: 'Primaire/Secondaire' },
  { key: 'locomotion', path: 'data/sae/locomotion.json', label: 'Locomotion', cycle: 'Primaire' },
  { key: 'mobilite', path: 'data/sae/mobilite.json', label: 'Mobilite', cycle: 'Primaire/Secondaire' },
  { key: 'poursuite', path: 'data/sae/poursuite.json', label: 'Jeux de poursuite', cycle: 'Maternelle → Sec 5' },
  { key: 'duel', path: 'data/sae/duel.json', label: 'Duel / Opposition', cycle: 'Primaire/Secondaire' },
  { key: 'conditionnement', path: 'data/sae/conditionnement.json', label: 'Conditionnement', cycle: 'Primaire/Secondaire' },
  { key: 'expression_corporelle', path: 'data/sae/expression_corporelle.json', label: 'Expression corporelle', cycle: 'Mat → Sec 5' },
  { key: 'sports_collectifs_sae', path: 'data/sae/sports_collectifs_sae.json', label: 'Sports collectifs', cycle: 'Primaire → Sec 5' },
  { key: 'manipulation_new', path: 'data/sae/manipulation_new.json', label: "Manipulation d'objets", cycle: 'Mat → Sec 5' },
  { key: 'locomotion_new', path: 'data/sae/locomotion_new.json', label: 'Locomotion', cycle: 'Mat → Sec 5' },
  { key: 'expression_artistique', path: 'data/sae/expression_artistique.json', label: 'Expression artistique', cycle: 'Mat → Sec 5' },
  { key: 'adresse_individuel', path: 'data/sae/adresse_individuel.json', label: 'Adresse et sports individuels', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_new', path: 'data/sae/cooperation_new.json', label: 'Cooperation (nouveaux)', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_extra', path: 'data/sae/cooperation_extra.json', label: 'Cooperation (extra)', cycle: 'Mat → Sec 5' },
  { key: 'individuelles_part8', path: 'data/sae/individuelles_part8.json', label: 'Individuelles', cycle: 'Mat → Sec 5' },
  { key: 'nonloc_gainage', path: 'data/sae/nonloc_gainage.json', label: 'Gainage et non-locomoteur', cycle: 'Mat → Sec 5' },
  { key: 'variees_extra', path: 'data/sae/variees_extra.json', label: 'Variees (extra)', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_gen', path: 'data/sae/cooperation_gen.json', label: 'Cooperation (generation)', cycle: 'Mat → Sec 5' },
  { key: 'poursuite_gen', path: 'data/sae/poursuite_gen.json', label: 'Poursuite (generation)', cycle: 'Mat → Sec 5' },
  { key: 'prescolaire_primaire_gen', path: 'data/sae/prescolaire_primaire_gen.json', label: 'Prescolaire-Primaire (generation)', cycle: 'Mat → Sec 5' },
];

const MOYENS_ACTION = [
  { key: 'manipulation', label: '🎯 Manipulation', emoji: '🎯', keywords: ['balle', 'ballon', 'raquette', 'baton', 'corde', 'cerceau', 'frisbee', 'cirque', 'foulard', 'manipulation', 'objet', 'jonglerie'] },
  { key: 'locomotion', label: '🏃 Locomotion', emoji: '🏃', keywords: ['courir', 'sauter', 'ramper', 'grimper', 'esquiver', 'locomotion', 'poursuite', 'courir', 'vitesse'] },
  { key: 'stabilisation', label: '⚖️ Stabilisation', emoji: '⚖️', keywords: ['equilibre', 'souplesse', 'gainage', 'coordination', 'mobilite', 'conditionnement', 'yoga', 'stretching', 'force', 'flexibilite'] },
  { key: 'opposition', label: '⚔️ Opposition', emoji: '⚔️', keywords: ['lutte', 'duel', 'territoire', 'opposition', 'dodgeball', 'chasseur', 'combat', 'confrontation'] },
  { key: 'cooperation', label: '🤝 Cooperation', emoji: '🤝', keywords: ['communication', 'strategie', 'construction', 'cooperation', 'collectif', 'equipe', 'entraide', 'basket', 'volleyball', 'handball'] },
  { key: 'expression', label: '💃 Expression', emoji: '💃', keywords: ['danse', 'mime', 'acrosport', 'expression', 'artistique', 'cirque', 'gymnaste', 'gymnastique', 'creation', 'rythme'] },
];

let allSAE = [];
let filtered = [];
let activeMoyen = null;
let favorisFilterActive = false;
let currentPage = 0;
const ITEMS_PER_PAGE = 30;

// Safety timer to hide loading if fetch hangs
const safetyTimer = setTimeout(hideLoading, 8000);

document.addEventListener('DOMContentLoaded', async () => {
  initCanvas();
  renderMoyensAction();
  await loadAllSAE();
  setupFilters();
  renderSAE();
  hideLoading();
  animateCounters();
  updateCoursFab();
  checkDeepLink();
  checkCoursDeepLink();
});

// ===== CHARGEMENT DES DONNEES =====

async function loadAllSAE() {
  const results = await Promise.allSettled(
    SAE_SOURCES.map(source =>
      fetch(source.path)
        .then(r => {
          if (!r.ok) {
            console.warn(`⚠️ Fichier non trouve: ${source.path}`);
            throw new Error(`404: ${source.path}`);
          }
          return r.json();
        })
        .then(data => ({ source, data }))
        .catch(err => {
          console.warn(`Erreur chargement ${source.path}:`, err.message);
          throw err;
        })
    )
  );

  let loaded = 0;
  let skipped = 0;

  results.forEach(result => {
    if (result.status === 'fulfilled') {
      const { source, data } = result.value;
      let saes = extractSAEs(data, source);
      saes = saes.filter(s => s && (s.titre || s.nom));
      saes = saes.map(s => ({ ...s, _source: source.key, _cycle: source.cycle }));
      allSAE.push(...saes);
      loaded++;
    } else {
      skipped++;
    }
  });

  console.log(`✅ ${loaded} fichiers charges, ${skipped} ignores — ${allSAE.length} SAE au total`);
  filtered = [...allSAE];
  clearTimeout(safetyTimer);
}

function extractSAEs(data, source) {
  if (Array.isArray(data)) return data;
  if (source.arrayKey && data[source.arrayKey] && Array.isArray(data[source.arrayKey])) return data[source.arrayKey];
  if (data.saes && Array.isArray(data.saes)) return data.saes;
  if (data.items && Array.isArray(data.items)) return data.items;
  if (data.situations && Array.isArray(data.situations)) return data.situations;
  for (const key of Object.keys(data)) {
    if (Array.isArray(data[key]) && data[key].length > 0 && (data[key][0].titre || data[key][0].nom)) {
      return data[key];
    }
  }
  if (data.titre || data.nom) return [data];
  return [];
}

// ===== MOYENS D'ACTION BROWSER =====

function renderMoyensAction() {
  const grid = document.getElementById('moyens-grid');
  if (!grid) return;
  grid.innerHTML = MOYENS_ACTION.map(m => `
    <button class="moyen-btn" data-key="${m.key}" onclick="filterByMoyen('${m.key}')">
      <span class="moyen-emoji">${m.emoji}</span>
      <span class="moyen-label">${m.label.replace(m.emoji + ' ', '')}</span>
    </button>
  `).join('');
}

function filterByMoyen(key) {
  if (activeMoyen === key) {
    activeMoyen = null;
  } else {
    activeMoyen = key;
  }
  document.querySelectorAll('.moyen-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.key === activeMoyen);
  });
  applyFilters();

  if (activeMoyen) {
    setTimeout(() => {
      document.getElementById('filtres')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  }
}

// ===== FILTRES =====

function setupFilters() {
  ['sae-cycle', 'sae-moyen', 'sae-competence', 'sae-clientele'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', applyFilters);
  });
  const searchEl = document.getElementById('sae-search');
  if (searchEl) {
    searchEl.addEventListener('input', debounce(applyFilters, 250));
  }
}

function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function applyFilters() {
  const search = (document.getElementById('sae-search')?.value || '').toLowerCase().trim();
  const cycle = document.getElementById('sae-cycle')?.value || '';
  const moyen = document.getElementById('sae-moyen')?.value || '';
  const competence = document.getElementById('sae-competence')?.value || '';
  const clientele = document.getElementById('sae-clientele')?.value || '';

  currentPage = 0;
  filtered = allSAE.filter(s => {

    if (favorisFilterActive) {
      if (!isFavori(s)) return false;
    }

    if (search) {
      const text = [
        s.titre, s.nom, s.description, s.contexte_apprentissage,
        s.tache_complexe, s.moyen_action, s._source,
        ...(s.tags || []), ...(s.competences || [])
      ].filter(Boolean).join(' ').toLowerCase();
      if (!text.includes(search)) return false;
    }

    if (cycle) {
      const c = [s.cycle, s.niveau, s._cycle].filter(Boolean).join(' ');
      if (!c.includes(cycle)) return false;
    }

    if (moyen) {
      const moyenStr = [
        s.moyen_action, s.moyens_action, s._source,
        ...(s.tags || []), s.titre, s.nom
      ].filter(Boolean).join(' ').toLowerCase();
      if (!moyenStr.includes(moyen.toLowerCase())) return false;
    }

    if (competence) {
      const comp = [s.competence_pfeq, ...(s.competences || [])].filter(Boolean).join(' ').toLowerCase();
      if (!comp.includes(competence.toLowerCase())) return false;
    }

    if (clientele) {
      const hdaa = JSON.stringify(s.adaptation_hdaa || {}).toLowerCase();
      const tags = (s.tags || []).join(' ').toLowerCase();
      const desc = (s.description || '').toLowerCase();
      if (!hdaa.includes(clientele) && !tags.includes(clientele) && !desc.includes(clientele)) return false;
    }

    if (activeMoyen) {
      const m = MOYENS_ACTION.find(x => x.key === activeMoyen);
      if (m) {
        const text = [
          s.titre, s.nom, s.moyen_action, s.moyens_action, s._source,
          ...(s.tags || []), s.description
        ].filter(Boolean).join(' ').toLowerCase();
        if (!m.keywords.some(kw => text.includes(kw))) return false;
      }
    }

    return true;
  });

  renderSAE();
}

// ===== FAVORIS (localStorage) =====

function getSaeId(s) {
  return s.id || s.titre || s.nom || '';
}

function getFavoris() {
  try {
    return JSON.parse(localStorage.getItem('favoris-sae') || '[]');
  } catch { return []; }
}

function setFavoris(arr) {
  localStorage.setItem('favoris-sae', JSON.stringify(arr));
}

function isFavori(s) {
  return getFavoris().includes(getSaeId(s));
}

function toggleFavori(s) {
  const id = getSaeId(s);
  let favs = getFavoris();
  if (favs.includes(id)) {
    favs = favs.filter(f => f !== id);
  } else {
    favs.push(id);
  }
  setFavoris(favs);
  return favs.includes(id);
}

function toggleFavorisFilter() {
  favorisFilterActive = !favorisFilterActive;
  const btn = document.getElementById('favoris-filter');
  if (btn) {
    btn.classList.toggle('active', favorisFilterActive);
    btn.textContent = favorisFilterActive ? '★ Favoris' : '☆ Favoris';
  }
  applyFilters();
}

// ===== RENDU DES CARTES =====

function getCycleClass(s) {
  const c = [s.cycle, s.niveau, s._cycle].filter(Boolean).join(' ').toLowerCase();
  if (c.includes('prescolaire') || c.includes('maternelle') || c.includes('mat')) {
    return 'cycle-prescolaire';
  }
  if (c.includes('secondaire') || c.includes('sec')) {
    return 'cycle-secondaire';
  }
  return 'cycle-primaire';
}

function renderCard(s) {
  const titre = s.titre || s.nom || 'SAE sans titre';
  const cycle = s.cycle || s.niveau || '';
  const desc = s.description || s.contexte_apprentissage || '';
  const competence = s.competence_pfeq || (s.competences || [])[0] || '';
  const moyen = s.moyen_action || s.moyens_action || '';
  const duree = s.duree_periodes || s.duree || '';
  const hasHDAA = s.adaptation_hdaa && Object.keys(s.adaptation_hdaa).length > 0;

  const div = document.createElement('div');
  div.className = 'sae-card';
  div.setAttribute('role', 'button');
  div.setAttribute('tabindex', '0');
  div.setAttribute('aria-label', `Ouvrir la SAE: ${titre}`);

  const fav = isFavori(s);
  const inCours = isInCours(s);
  div.innerHTML = `
    <button class="fav-star ${fav ? 'active' : ''}" aria-label="Ajouter aux favoris" title="Favori">${fav ? '★' : '☆'}</button>
    <span class="pfeq-badge">PFEQ</span>
    ${cycle ? `<span class="cycle-badge ${getCycleClass(s)}">${escapeHtml(cycle)}</span>` : ''}
    <div class="card-title">${escapeHtml(titre)}</div>
    ${desc ? `<p class="card-desc">${escapeHtml(desc)}</p>` : ''}
    <div class="card-tags">
      ${competence ? `<span class="tag tag-competence">${escapeHtml(competence)}</span>` : ''}
      ${moyen ? `<span class="tag tag-moyen">${escapeHtml(moyen)}</span>` : ''}
      ${hasHDAA ? `<span class="tag tag-hdaa">♿ Adapte HDAA</span>` : ''}
    </div>
    ${duree ? `<div class="duree-badge">⏱ ${escapeHtml(String(duree))} periode${parseInt(duree) > 1 ? 's' : ''}</div>` : ''}
    <button class="sae-card-add-btn ${inCours ? 'added' : ''}" title="${inCours ? 'Retirer de ma SAE' : 'Ajouter a ma SAE'}">${inCours ? '✓' : '+'}</button>
  `;

  // Star click handler
  const starBtn = div.querySelector('.fav-star');
  starBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const nowFav = toggleFavori(s);
    starBtn.textContent = nowFav ? '★' : '☆';
    starBtn.classList.toggle('active', nowFav);
    if (favorisFilterActive) applyFilters();
  });

  // Add to cours button
  const addBtn = div.querySelector('.sae-card-add-btn');
  addBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleCoursItem(s, addBtn);
  });

  div.addEventListener('click', () => openModal(s));
  div.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(s); }
  });

  return div;
}

function renderSAE() {
  const grid = document.getElementById('sae-grid');
  if (!grid) return;
  grid.innerHTML = '';

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div style="font-size:3rem;margin-bottom:16px">🔍</div>
        <p style="font-size:1.1rem;color:var(--text-muted)">Aucune SAE trouvee</p>
        <p style="font-size:0.85rem;color:var(--text-faint);margin-top:8px">Essayez de modifier les filtres ou la recherche</p>
      </div>`;
    renderPagination();
    updateStats();
    return;
  }

  const start = currentPage * ITEMS_PER_PAGE;
  const end = start + ITEMS_PER_PAGE;
  const pageItems = filtered.slice(start, end);

  const fragment = document.createDocumentFragment();
  pageItems.forEach(s => fragment.appendChild(renderCard(s)));
  grid.appendChild(fragment);

  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('animate-in');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });

  grid.querySelectorAll('.sae-card').forEach(c => observer.observe(c));
  renderPagination();
  updateStats();
}

function renderPagination() {
  const container = document.getElementById('pagination');
  if (!container) return;
  container.innerHTML = '';

  const totalPages = Math.ceil(filtered.length / ITEMS_PER_PAGE);
  if (totalPages <= 1) return;

  const prevBtn = document.createElement('button');
  prevBtn.className = 'page-btn page-prev' + (currentPage === 0 ? ' disabled' : '');
  prevBtn.textContent = '\u2190 Precedent';
  prevBtn.disabled = currentPage === 0;
  prevBtn.addEventListener('click', () => goToPage(currentPage - 1));
  container.appendChild(prevBtn);

  const pagesDiv = document.createElement('div');
  pagesDiv.className = 'page-numbers';

  const maxVisible = 7;
  let pages = [];

  if (totalPages <= maxVisible) {
    for (let i = 0; i < totalPages; i++) pages.push(i);
  } else {
    pages.push(0);
    let start = Math.max(1, currentPage - 2);
    let end = Math.min(totalPages - 2, currentPage + 2);
    if (currentPage <= 3) { start = 1; end = 4; }
    if (currentPage >= totalPages - 4) { start = totalPages - 5; end = totalPages - 2; }
    if (start > 1) pages.push(-1);
    for (let i = start; i <= end; i++) pages.push(i);
    if (end < totalPages - 2) pages.push(-1);
    pages.push(totalPages - 1);
  }

  pages.forEach(p => {
    if (p === -1) {
      const dots = document.createElement('span');
      dots.className = 'page-dots';
      dots.textContent = '\u2026';
      pagesDiv.appendChild(dots);
    } else {
      const btn = document.createElement('button');
      btn.className = 'page-btn page-num' + (p === currentPage ? ' active' : '');
      btn.textContent = p + 1;
      btn.addEventListener('click', () => goToPage(p));
      pagesDiv.appendChild(btn);
    }
  });

  container.appendChild(pagesDiv);

  const nextBtn = document.createElement('button');
  nextBtn.className = 'page-btn page-next' + (currentPage >= totalPages - 1 ? ' disabled' : '');
  nextBtn.textContent = 'Suivant \u2192';
  nextBtn.disabled = currentPage >= totalPages - 1;
  nextBtn.addEventListener('click', () => goToPage(currentPage + 1));
  container.appendChild(nextBtn);

  const info = document.createElement('div');
  info.className = 'page-info';
  const s = currentPage * ITEMS_PER_PAGE + 1;
  const e = Math.min((currentPage + 1) * ITEMS_PER_PAGE, filtered.length);
  info.textContent = `${s}\u2013${e} sur ${filtered.length} SAE`;
  container.appendChild(info);
}

function goToPage(page) {
  const totalPages = Math.ceil(filtered.length / ITEMS_PER_PAGE);
  if (page < 0 || page >= totalPages) return;
  currentPage = page;
  renderSAE();
  const grid = document.getElementById('sae-grid');
  if (grid) {
    grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function updateStats() {
  const countEl = document.getElementById('sae-count');
  if (countEl) countEl.textContent = `${filtered.length} SAE`;

  const totalEl = document.getElementById('hstat-sae');
  if (totalEl) totalEl.innerHTML = `${allSAE.length}<span>SAE</span>`;

  const counterEl = document.getElementById('counter-sae');
  if (counterEl) counterEl.textContent = allSAE.length;
}

// ===== MODAL =====

function openModal(s) {
  const modal = document.getElementById('modal');
  const body = document.getElementById('modal-body');
  if (!modal || !body) return;

  const titre = s.titre || s.nom || 'SAE';

  const sections = [
    s.description && `
      <div class="modal-section">
        <h3>📋 Description</h3>
        <p>${escapeHtml(s.description)}</p>
      </div>`,
    s.contexte_apprentissage && `
      <div class="modal-section">
        <h3>🏫 Contexte d'apprentissage</h3>
        <p>${escapeHtml(s.contexte_apprentissage)}</p>
      </div>`,
    s.tache_complexe && `
      <div class="modal-section">
        <h3>🎯 Tache complexe</h3>
        <p>${escapeHtml(typeof s.tache_complexe === 'string' ? s.tache_complexe : JSON.stringify(s.tache_complexe))}</p>
      </div>`,
    s.objectifs && `
      <div class="modal-section">
        <h3>🎓 Objectifs</h3>
        <ul>${(Array.isArray(s.objectifs) ? s.objectifs : [s.objectifs])
          .map(o => `<li>${escapeHtml(typeof o === 'string' ? o : JSON.stringify(o))}</li>`).join('')}</ul>
      </div>`,
    s.materiel && `
      <div class="modal-section">
        <h3>🎒 Materiel requis</h3>
        <ul>${(Array.isArray(s.materiel) ? s.materiel : [s.materiel])
          .map(m => `<li>${escapeHtml(typeof m === 'string' ? m : JSON.stringify(m))}</li>`).join('')}</ul>
      </div>`,
    s.deroulement && `
      <div class="modal-section">
        <h3>📝 Deroulement</h3>
        ${typeof s.deroulement === 'string'
          ? `<p>${escapeHtml(s.deroulement)}</p>`
          : `<ul>${(Array.isArray(s.deroulement) ? s.deroulement : Object.values(s.deroulement))
              .map(d => `<li>${escapeHtml(typeof d === 'string' ? d : JSON.stringify(d))}</li>`).join('')}</ul>`
        }
      </div>`,
    s.criteres_evaluation && `
      <div class="modal-section">
        <h3>📊 Criteres d'evaluation</h3>
        <ul>${(Array.isArray(s.criteres_evaluation) ? s.criteres_evaluation : [s.criteres_evaluation])
          .map(c => `<li>${escapeHtml(typeof c === 'string' ? c : (c.critere || JSON.stringify(c)))}</li>`).join('')}</ul>
      </div>`,
    s.progression && `
      <div class="modal-section">
        <h3>📈 Progression</h3>
        <p>${escapeHtml(typeof s.progression === 'string' ? s.progression : JSON.stringify(s.progression, null, 2))}</p>
      </div>`,
    s.variantes && `
      <div class="modal-section">
        <h3>🔄 Variantes et differenciation</h3>
        ${typeof s.variantes === 'string'
          ? `<p>${escapeHtml(s.variantes)}</p>`
          : `<ul>${(Array.isArray(s.variantes) ? s.variantes : [s.variantes])
              .map(v => `<li>${escapeHtml(typeof v === 'string' ? v : JSON.stringify(v))}</li>`).join('')}</ul>`
        }
      </div>`,
    s.adaptation_hdaa && Object.keys(s.adaptation_hdaa).length > 0 && `
      <div class="modal-section">
        <h3>♿ Adaptations HDAA</h3>
        ${Object.entries(s.adaptation_hdaa)
          .map(([k, v]) => `<p><strong style="color:#FFD700">${escapeHtml(k)} :</strong> ${escapeHtml(typeof v === 'string' ? v : JSON.stringify(v))}</p>`)
          .join('')}
      </div>`,
    (s.notes || s.remarques) && `
      <div class="modal-section">
        <h3>💡 Notes pedagogiques</h3>
        <p>${escapeHtml(s.notes || s.remarques)}</p>
      </div>`,
  ].filter(Boolean).join('');

  const modalFav = isFavori(s);
  const saeId = getSaeId(s);
  const inCours = isInCours(s);

  body.innerHTML = `
    <div class="modal-header">
      <h2 class="modal-title" id="modal-title">📚 ${escapeHtml(titre)}</h2>
      <button class="modal-close" onclick="closeModal()" aria-label="Fermer">✕</button>
    </div>
    <div class="modal-meta">
      ${s.cycle || s.niveau ? `<span class="modal-badge cycle-badge ${getCycleClass(s)}">${escapeHtml(s.cycle || s.niveau)}</span>` : ''}
      ${s.competence_pfeq ? `<span class="modal-badge">${escapeHtml(s.competence_pfeq)}</span>` : ''}
      ${s.moyen_action ? `<span class="modal-badge">${escapeHtml(s.moyen_action)}</span>` : ''}
      ${s.duree_periodes ? `<span class="modal-badge">⏱ ${escapeHtml(String(s.duree_periodes))} periode${parseInt(s.duree_periodes) > 1 ? 's' : ''}</span>` : ''}
      ${s.espace ? `<span class="modal-badge">📍 ${escapeHtml(s.espace)}</span>` : ''}
      ${s.nb_eleves ? `<span class="modal-badge">👥 ${escapeHtml(String(s.nb_eleves))}</span>` : ''}
    </div>
    <div class="modal-actions">
      <button class="modal-action-btn ${modalFav ? 'fav-active' : ''}" id="modal-fav-btn" onclick="handleModalFavori()">
        ${modalFav ? '★' : '☆'} Favori
      </button>
      <button class="modal-action-btn ${inCours ? 'fav-active' : ''}" id="modal-cours-btn" onclick="handleModalCours()">
        ${inCours ? '✓ Dans ma SAE' : '📋 Ajouter a ma SAE'}
      </button>
      <button class="modal-action-btn" onclick="handlePrint()">🖨️ Imprimer</button>
      <button class="modal-action-btn" onclick="handlePDF()">📄 PDF</button>
      <button class="modal-action-btn" onclick="handleShare('${escapeHtml(saeId).replace(/'/g, "\\'")}')">🔗 Partager</button>
    </div>
    ${sections || '<p style="color:rgba(255,255,255,0.6);text-align:center;padding:24px">Aucun detail supplementaire disponible.</p>'}
    <div class="modal-footer-logo">
      <a href="https://zonetotalsport.ca" target="_blank">
        <img src="img/logo-zonetotalsport.png" alt="ZoneTotalSport.ca" />
      </a>
    </div>
  `;

  window._currentModalSAE = s;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  setTimeout(() => {
    body.querySelector('.modal-close')?.focus();
  }, 50);
}

function closeModal() {
  const modal = document.getElementById('modal');
  if (modal) modal.classList.add('hidden');
  document.body.style.overflow = '';
}

// ===== LOADING =====

function hideLoading() {
  clearTimeout(safetyTimer);
  const loading = document.getElementById('loading');
  const app = document.getElementById('app');
  if (loading) {
    loading.style.opacity = '0';
    setTimeout(() => { loading.style.display = 'none'; }, 400);
  }
  if (app) app.classList.remove('hidden');
}

// ===== COUNTERS ANIMES =====

function animateCounters() {
  const counterEl = document.getElementById('counter-sae');
  if (counterEl) {
    const target = allSAE.length;
    let count = 0;
    const step = Math.max(1, Math.ceil(target / 60));
    const interval = setInterval(() => {
      count = Math.min(count + step, target);
      counterEl.textContent = count;
      if (count >= target) clearInterval(interval);
    }, 16);
  }

  document.querySelectorAll('[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count);
    if (isNaN(target)) return;
    let count = 0;
    const step = Math.max(1, Math.ceil(target / 60));
    const interval = setInterval(() => {
      count = Math.min(count + step, target);
      el.textContent = count;
      if (count >= target) clearInterval(interval);
    }, 16);
  });
}

// ===== CANVAS ANIME =====

function initCanvas() {
  const canvas = document.getElementById('bgCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let particles = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = canvas.height + Math.random() * 40;
      this.size = Math.random() * 2.5 + 0.5;
      this.speedY = -(Math.random() * 0.6 + 0.2);
      this.speedX = (Math.random() - 0.5) * 0.3;
      this.life = 0;
      this.maxLife = Math.random() * 200 + 100;
      this.hue = Math.random() * 30 + 10;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      this.life++;
      if (this.life >= this.maxLife) this.reset();
    }
    draw() {
      const alpha = Math.sin((this.life / this.maxLife) * Math.PI) * 0.4;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = `hsla(${this.hue}, 100%, 65%, ${alpha})`;
      ctx.fill();
    }
  }

  for (let i = 0; i < 60; i++) {
    const p = new Particle();
    p.life = Math.random() * p.maxLife;
    particles.push(p);
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    requestAnimationFrame(animate);
  }

  animate();
  window.addEventListener('resize', resize);
}

// ===== UTILITAIRES =====

function escapeHtml(str) {
  if (typeof str !== 'string') return String(str);
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ===== MODAL ACTIONS =====

function handleModalFavori() {
  const s = window._currentModalSAE;
  if (!s) return;
  const nowFav = toggleFavori(s);
  const btn = document.getElementById('modal-fav-btn');
  if (btn) {
    btn.classList.toggle('fav-active', nowFav);
    btn.innerHTML = `${nowFav ? '★' : '☆'} Favori`;
  }
  renderSAE();
}

function handleModalCours() {
  const s = window._currentModalSAE;
  if (!s) return;
  const btn = document.getElementById('modal-cours-btn');
  if (isInCours(s)) {
    removeFromCours(getSaeId(s));
    if (btn) {
      btn.classList.remove('fav-active');
      btn.textContent = '📋 Ajouter a ma SAE';
    }
    showToast('Retire de ma SAE');
  } else {
    addToCours(s);
    if (btn) {
      btn.classList.add('fav-active');
      btn.textContent = '✓ Dans ma SAE';
    }
    showToast('Ajoute a ma SAE !');
  }
  refreshCardCoursState(s);
}

function handlePrint() {
  window.print();
}

function handlePDF() {
  const s = window._currentModalSAE;
  if (!s) return;
  const titre = s.titre || s.nom || 'SAE';
  const printWin = window.open('', '_blank');
  printWin.document.write(`<!DOCTYPE html>
<html><head><title>${escapeHtml(titre)} — Zone Total Sport</title>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  body { font-family: 'Nunito', sans-serif; margin: 40px; color: #222; }
  h1 { font-family: 'Fredoka', sans-serif; font-size: 2rem; color: #0077CC; margin-bottom: 8px; }
  .badges span { display: inline-block; padding: 4px 14px; border-radius: 20px; font-family: 'Fredoka', sans-serif; font-size: 0.9rem; font-weight: 700; margin-right: 8px; }
  .badge-blue { background: #E3F2FD; color: #0D47A1; border: 2px solid #42A5F5; }
  .badge-orange { background: #FFF3E0; color: #E65100; border: 2px solid #FF9800; }
  h2 { font-family: 'Fredoka', sans-serif; font-size: 1.2rem; color: #E91E63; margin-top: 24px; margin-bottom: 8px; border-bottom: 2px solid #E91E63; padding-bottom: 4px; }
  p { font-size: 1rem; line-height: 1.8; }
  ul { padding-left: 20px; }
  li { margin-bottom: 6px; }
  .footer { margin-top: 40px; text-align: center; color: #999; font-size: 0.9rem; font-family: 'Fredoka', sans-serif; }
</style></head><body>
<h1>📚 ${escapeHtml(titre)}</h1>
<div class="badges">
  ${s.cycle || s.niveau ? `<span class="badge-blue">${escapeHtml(s.cycle || s.niveau)}</span>` : ''}
  ${s.competence_pfeq ? `<span class="badge-orange">${escapeHtml(s.competence_pfeq)}</span>` : ''}
  ${s.duree_periodes ? `<span class="badge-blue">⏱ ${s.duree_periodes} periode(s)</span>` : ''}
</div>
${s.description ? '<h2>📋 Description</h2><p>' + escapeHtml(s.description) + '</p>' : ''}
${s.contexte_apprentissage ? '<h2>🏫 Contexte</h2><p>' + escapeHtml(s.contexte_apprentissage) + '</p>' : ''}
${s.objectifs ? '<h2>🎓 Objectifs</h2><ul>' + (Array.isArray(s.objectifs) ? s.objectifs : [s.objectifs]).map(o => '<li>' + escapeHtml(typeof o === 'string' ? o : JSON.stringify(o)) + '</li>').join('') + '</ul>' : ''}
${s.materiel ? '<h2>🎒 Materiel</h2><ul>' + (Array.isArray(s.materiel) ? s.materiel : [s.materiel]).map(m => '<li>' + escapeHtml(typeof m === 'string' ? m : JSON.stringify(m)) + '</li>').join('') + '</ul>' : ''}
${s.variantes ? '<h2>🔄 Variantes</h2><p>' + escapeHtml(typeof s.variantes === 'string' ? s.variantes : JSON.stringify(s.variantes)) + '</p>' : ''}
${s.adaptation_hdaa && Object.keys(s.adaptation_hdaa).length > 0 ? '<h2>♿ Adaptations HDAA</h2>' + Object.entries(s.adaptation_hdaa).map(([k,v]) => '<p><strong>' + escapeHtml(k) + ' :</strong> ' + escapeHtml(typeof v === 'string' ? v : JSON.stringify(v)) + '</p>').join('') : ''}
<div class="footer"><a href="https://zonetotalsport.ca" target="_blank" style="display:inline-block; background:#fff; border-radius:12px; padding:10px 20px;"><img src="${window.location.origin + '/img/logo-zonetotalsport.png'}" alt="ZoneTotalSport.ca" style="max-width:260px; height:auto; display:block;" /></a><br><a href="https://zonetotalsport.ca" target="_blank">zonetotalsport.ca</a> — SAE PFEQ</div>
</body></html>`);
  printWin.document.close();
  setTimeout(() => { printWin.print(); }, 500);
}

function handleShare(saeId) {
  const url = `https://sae.zonetotalsport.ca/?id=${encodeURIComponent(saeId)}`;
  navigator.clipboard.writeText(url).then(() => {
    showToast('Lien copie !');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = url;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Lien copie !');
  });
}

function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.classList.remove('hidden');
  void toast.offsetWidth;
  toast.classList.add('visible');
  setTimeout(() => {
    toast.classList.remove('visible');
    setTimeout(() => toast.classList.add('hidden'), 300);
  }, 2000);
}

// ===== DEEP LINK (partage) =====

function checkDeepLink() {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');
  if (!id) return;
  const sae = allSAE.find(s => getSaeId(s) === id);
  if (sae) {
    setTimeout(() => openModal(sae), 300);
  }
}

// ===== EVENEMENTS GLOBAUX =====

document.addEventListener('click', e => {
  if (e.target.id === 'modal-backdrop') closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});

// =============================================
// CONCEPTION DE MA SAE
// =============================================

function getMonCours() {
  try {
    return JSON.parse(localStorage.getItem('mon-cours-sae') || '[]');
  } catch { return []; }
}

function setMonCours(arr) {
  localStorage.setItem('mon-cours-sae', JSON.stringify(arr));
  updateCoursFab();
}

function getCoursConfig() {
  try {
    return JSON.parse(localStorage.getItem('mon-cours-sae-config') || '{}');
  } catch { return {}; }
}

function setCoursConfig(config) {
  localStorage.setItem('mon-cours-sae-config', JSON.stringify(config));
}

function isInCours(s) {
  const id = getSaeId(s);
  return getMonCours().some(e => (e.id || e.titre || e.nom) === id);
}

function addToCours(s) {
  const cours = getMonCours();
  const id = getSaeId(s);
  if (cours.some(e => (e.id || e.titre || e.nom) === id)) return false;
  cours.push({
    titre: s.titre || s.nom || '',
    description: s.description || s.contexte_apprentissage || '',
    cycle: s.cycle || s.niveau || '',
    competence_pfeq: s.competence_pfeq || '',
    moyen_action: s.moyen_action || s.moyens_action || '',
    duree_periodes: s.duree_periodes || s.duree || '',
    _source: s._source || '',
    _note: ''
  });
  setMonCours(cours);
  return true;
}

function removeFromCours(id) {
  const cours = getMonCours().filter(e => (e.titre || e.nom) !== id);
  setMonCours(cours);
}

function updateCoursFab() {
  const count = getMonCours().length;
  const badge = document.getElementById('cours-fab-count');
  if (badge) {
    badge.textContent = count;
    badge.classList.toggle('hidden', count === 0);
  }
}

function toggleCoursItem(s, btn) {
  if (isInCours(s)) {
    removeFromCours(getSaeId(s));
    if (btn) {
      btn.classList.remove('added');
      btn.textContent = '+';
      btn.title = 'Ajouter a ma SAE';
    }
    showToast('Retire de ma SAE');
  } else {
    addToCours(s);
    if (btn) {
      btn.classList.add('added');
      btn.textContent = '✓';
      btn.title = 'Retirer de ma SAE';
    }
    showToast('Ajoute a ma SAE !');
  }
}

function refreshCardCoursState(s) {
  const id = getSaeId(s);
  document.querySelectorAll('.sae-card').forEach(card => {
    const titleEl = card.querySelector('.card-title');
    if (titleEl && titleEl.textContent === (s.titre || s.nom)) {
      const addBtn = card.querySelector('.sae-card-add-btn');
      if (addBtn) {
        const inC = isInCours(s);
        addBtn.classList.toggle('added', inC);
        addBtn.textContent = inC ? '✓' : '+';
        addBtn.title = inC ? 'Retirer de ma SAE' : 'Ajouter a ma SAE';
      }
    }
  });
}

function openCours() {
  // Hide main content
  const app = document.getElementById('app');
  const fab = document.getElementById('cours-fab');
  if (app) app.classList.add('hidden');
  if (fab) fab.classList.add('hidden');

  // Show cours section
  const section = document.getElementById('cours-section');
  if (!section) return;
  section.classList.remove('hidden');

  // Load config
  const config = getCoursConfig();
  const titreInput = document.getElementById('cours-titre');
  const niveauSelect = document.getElementById('cours-niveau');
  const dureeInput = document.getElementById('cours-duree');
  const notesArea = document.getElementById('cours-notes');
  if (titreInput) titreInput.value = config.titre || '';
  if (niveauSelect) niveauSelect.value = config.niveau || '';
  if (dureeInput) dureeInput.value = config.duree || '';
  if (notesArea) notesArea.value = config.notes || '';

  // Auto-save config on change
  [titreInput, niveauSelect, dureeInput, notesArea].forEach(el => {
    if (el) {
      el.removeEventListener('input', saveCoursConfigFromUI);
      el.addEventListener('input', saveCoursConfigFromUI);
    }
  });

  populateCoursCatSelect();
  renderCoursList();
  updateCoursBrowser();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function saveCoursConfigFromUI() {
  setCoursConfig({
    titre: document.getElementById('cours-titre')?.value || '',
    niveau: document.getElementById('cours-niveau')?.value || '',
    duree: document.getElementById('cours-duree')?.value || '',
    notes: document.getElementById('cours-notes')?.value || ''
  });
}

function closeCours() {
  saveCoursConfigFromUI();
  const section = document.getElementById('cours-section');
  const app = document.getElementById('app');
  const fab = document.getElementById('cours-fab');
  if (section) section.classList.add('hidden');
  if (app) app.classList.remove('hidden');
  if (fab) fab.classList.remove('hidden');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderCoursList() {
  const list = document.getElementById('cours-list');
  const cours = getMonCours();
  const countEl = document.getElementById('cours-count');
  const actionsEl = document.getElementById('cours-actions');
  const totalMinEl = document.getElementById('cours-total-min');

  if (countEl) countEl.textContent = cours.length;

  if (cours.length === 0) {
    list.innerHTML = `
      <div class="cours-empty">
        <div class="cours-empty-icon">📭</div>
        <p>Aucune SAE ajoutee. Retourne a la banque et clique sur le <strong>+</strong> des cartes pour ajouter des SAE a ta planification.</p>
      </div>
    `;
    if (actionsEl) actionsEl.classList.add('hidden');
    return;
  }

  if (actionsEl) actionsEl.classList.remove('hidden');

  let totalPeriodes = 0;
  list.innerHTML = '';

  cours.forEach((sae, index) => {
    totalPeriodes += parseInt(sae.duree_periodes) || 0;

    const item = document.createElement('div');
    item.className = 'cours-item';
    item.innerHTML = `
      <div class="cours-item-num">${index + 1}</div>
      <div class="cours-item-body">
        <div class="cours-item-title">${escapeHtml(sae.titre)}</div>
        <div class="cours-item-meta">
          <span>${escapeHtml(sae.cycle || '')}</span>
          <span>${escapeHtml(sae.competence_pfeq || '')}</span>
          ${sae.duree_periodes ? `<span>⏱ ${sae.duree_periodes} per.</span>` : ''}
          ${sae.moyen_action ? `<span>${escapeHtml(sae.moyen_action)}</span>` : ''}
        </div>
        <div class="cours-item-note">
          <input type="text" placeholder="Ajouter une note pour cette SAE..." value="${escapeHtml(sae._note || '')}" data-index="${index}" />
        </div>
      </div>
      <div class="cours-item-actions">
        <button title="Monter" class="cours-up-btn" ${index === 0 ? 'disabled' : ''}>▲</button>
        <button title="Descendre" class="cours-down-btn" ${index === cours.length - 1 ? 'disabled' : ''}>▼</button>
        <button title="Retirer" class="cours-remove-btn">✕</button>
      </div>
    `;

    // Click title to view SAE details
    const titleEl = item.querySelector('.cours-item-title');
    titleEl.addEventListener('click', () => {
      const found = allSAE.find(s => (s.titre || s.nom) === sae.titre);
      if (found) openModal(found);
    });

    // Note input
    const noteInput = item.querySelector('.cours-item-note input');
    noteInput.addEventListener('input', () => {
      const c = getMonCours();
      if (c[index]) {
        c[index]._note = noteInput.value;
        setMonCours(c);
      }
    });

    // Move up
    item.querySelector('.cours-up-btn').addEventListener('click', () => {
      if (index > 0) {
        const c = getMonCours();
        [c[index - 1], c[index]] = [c[index], c[index - 1]];
        setMonCours(c);
        renderCoursList();
      }
    });

    // Move down
    item.querySelector('.cours-down-btn').addEventListener('click', () => {
      if (index < cours.length - 1) {
        const c = getMonCours();
        [c[index], c[index + 1]] = [c[index + 1], c[index]];
        setMonCours(c);
        renderCoursList();
      }
    });

    // Remove
    item.querySelector('.cours-remove-btn').addEventListener('click', () => {
      removeFromCours(sae.titre);
      renderCoursList();
      updateCoursBrowser();
      showToast('SAE retiree');
    });

    list.appendChild(item);
  });

  if (totalMinEl) totalMinEl.textContent = totalPeriodes;
}

function clearCours() {
  if (getMonCours().length === 0) return;
  setMonCours([]);
  renderCoursList();
  updateCoursBrowser();
  showToast('SAE videe');
}

function populateCoursCatSelect() {
  const select = document.getElementById('cours-cat-select');
  if (!select) return;
  select.innerHTML = '<option value="">— Choisir un moyen d\'action —</option>';
  MOYENS_ACTION.forEach(m => {
    const opt = document.createElement('option');
    opt.value = m.key;
    opt.textContent = `${m.emoji} ${m.label.replace(m.emoji + ' ', '')}`;
    select.appendChild(opt);
  });
}

function updateCoursBrowser() {
  const container = document.getElementById('cours-browser-results');
  if (!container) return;

  const catKey = document.getElementById('cours-cat-select')?.value;
  const search = (document.getElementById('cours-browser-search')?.value || '').toLowerCase().trim();

  if (!catKey) {
    container.innerHTML = '<p class="cours-browser-hint">Selectionne un moyen d\'action pour voir les SAE disponibles.</p>';
    return;
  }

  const m = MOYENS_ACTION.find(x => x.key === catKey);
  if (!m) return;

  // Filter allSAE by moyen keywords
  let results = allSAE.filter(s => {
    const text = [
      s.titre, s.nom, s.moyen_action, s.moyens_action, s._source,
      ...(s.tags || []), s.description
    ].filter(Boolean).join(' ').toLowerCase();
    return m.keywords.some(kw => text.includes(kw));
  });

  // Apply search filter
  if (search) {
    results = results.filter(s => {
      const text = [s.titre, s.nom, s.description, s.contexte_apprentissage].filter(Boolean).join(' ').toLowerCase();
      return text.includes(search);
    });
  }

  container.innerHTML = '';

  const countDiv = document.createElement('div');
  countDiv.className = 'cours-browser-count';
  countDiv.innerHTML = `<strong>${results.length}</strong> SAE disponible${results.length > 1 ? 's' : ''}`;
  container.appendChild(countDiv);

  if (results.length === 0) {
    const hint = document.createElement('p');
    hint.className = 'cours-browser-hint';
    hint.textContent = 'Aucune SAE trouvee avec ces criteres.';
    container.appendChild(hint);
    return;
  }

  // Show max 50 results in browser
  results.slice(0, 50).forEach(s => {
    const inCours = isInCours(s);
    const item = document.createElement('div');
    item.className = 'cours-browse-item';
    item.innerHTML = `
      <div class="cours-browse-item-info">
        <div class="cours-browse-item-title">${escapeHtml(s.titre || s.nom || '')}</div>
        <div class="cours-browse-item-meta">
          <span>${escapeHtml(s.cycle || s.niveau || '')}</span>
          <span>${escapeHtml(s.competence_pfeq || '')}</span>
          ${s.duree_periodes ? `<span>⏱ ${s.duree_periodes} per.</span>` : ''}
        </div>
      </div>
      <button class="cours-browse-add-btn ${inCours ? 'already-added' : ''}">${inCours ? '✓ Ajoutee' : '+ Ajouter'}</button>
    `;

    // Click on info to open modal
    const info = item.querySelector('.cours-browse-item-info');
    info.style.cursor = 'pointer';
    info.addEventListener('click', () => openModal(s));

    const btn = item.querySelector('.cours-browse-add-btn');
    btn.addEventListener('click', () => {
      if (isInCours(s)) return;
      addToCours(s);
      btn.textContent = '✓ Ajoutee';
      btn.classList.add('already-added');
      renderCoursList();
      showToast('Ajoutee a ma SAE !');
    });

    container.appendChild(item);
  });
}

// ===== EXPORT COURS =====

function buildCoursHTML() {
  const cours = getMonCours();
  const config = getCoursConfig();

  let totalPeriodes = 0;
  cours.forEach(e => totalPeriodes += parseInt(e.duree_periodes) || 0);

  let saesHTML = '';
  cours.forEach((sae, i) => {
    saesHTML += `
      <div style="border:1px solid #ddd; border-radius:12px; padding:16px; margin-bottom:12px; page-break-inside:avoid; background:#fafafa;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
          <div style="width:36px; height:36px; border-radius:50%; background:#0077CC; color:#fff; display:flex; align-items:center; justify-content:center; font-family:'Fredoka',sans-serif; font-weight:700; font-size:1.1rem; flex-shrink:0;">${i + 1}</div>
          <div>
            <div style="font-family:'Fredoka',sans-serif; font-size:1.2rem; font-weight:700; color:#222;">${escapeHtml(sae.titre)}</div>
            <div style="font-size:0.85rem; color:#666; font-family:'Nunito',sans-serif;">
              ${escapeHtml(sae.cycle || '')} · ${escapeHtml(sae.competence_pfeq || '')} ${sae.duree_periodes ? '· ⏱ ' + sae.duree_periodes + ' per.' : ''}
            </div>
          </div>
        </div>
        ${sae.description ? '<p style="font-size:0.95rem; line-height:1.6; color:#333; font-family:\'Nunito\',sans-serif; margin:8px 0;">' + escapeHtml(sae.description) + '</p>' : ''}
        ${sae._note ? '<div style="font-size:0.85rem; color:#0077CC; margin-top:6px; font-style:italic;">📝 Note : ' + escapeHtml(sae._note) + '</div>' : ''}
      </div>
    `;
  });

  return `<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<title>${escapeHtml(config.titre || 'Ma SAE')} — Zone Total Sport</title>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  @page { margin: 20mm 15mm 25mm 15mm; }
  body { font-family: 'Nunito', sans-serif; margin: 0; padding: 30px; color: #222; }
  .header { text-align: center; margin-bottom: 24px; border-bottom: 3px solid #0077CC; padding-bottom: 16px; }
  .header h1 { font-family: 'Fredoka', sans-serif; font-size: 2.2rem; color: #0077CC; margin: 0 0 6px; }
  .header .info { font-size: 0.95rem; color: #555; }
  .header .info strong { color: #333; }
  .notes { background: #f0f7ff; border: 1px solid #b3d4fc; border-radius: 10px; padding: 14px 18px; margin-bottom: 20px; font-size: 0.95rem; line-height: 1.6; }
  .notes-label { font-family: 'Fredoka', sans-serif; font-weight: 700; color: #0077CC; margin-bottom: 4px; }
  .footer { position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-family: 'Fredoka', sans-serif; font-size: 0.8rem; color: #999; padding: 10px; border-top: 1px solid #ddd; background: #fff; }
  .footer a { color: #0077CC; text-decoration: none; }
  @media print { .footer { position: fixed; bottom: 0; } }
</style></head><body>
<div class="header">
  <h1>📋 ${escapeHtml(config.titre || 'Conception de ma SAE')}</h1>
  <div class="info">
    ${config.niveau ? '<strong>Niveau :</strong> ' + escapeHtml(config.niveau) + ' · ' : ''}
    ${config.duree ? '<strong>Duree :</strong> ' + escapeHtml(config.duree) + ' · ' : ''}
    <strong>${cours.length}</strong> SAE · Duree estimee : <strong>${totalPeriodes} periodes</strong>
  </div>
</div>
${config.notes ? '<div class="notes"><div class="notes-label">📝 Notes</div>' + escapeHtml(config.notes) + '</div>' : ''}
${saesHTML}
<div class="footer">
  <a href="https://zonetotalsport.ca" target="_blank" style="display:inline-block; background:#fff; border-radius:12px; padding:10px 20px;"><img src="${window.location.origin + '/img/logo-zonetotalsport.png'}" alt="ZoneTotalSport.ca" style="max-width:280px; height:auto; display:block;" /></a><br>
  Cree avec <a href="https://zonetotalsport.ca" target="_blank">zonetotalsport.ca</a> — SAE PFEQ
</div>
</body></html>`;
}

function printCours() {
  saveCoursConfigFromUI();
  const html = buildCoursHTML();
  const w = window.open('', '_blank');
  w.document.write(html);
  w.document.close();
  setTimeout(() => w.print(), 500);
}

function exportCoursPDF() {
  saveCoursConfigFromUI();
  const html = buildCoursHTML();
  const w = window.open('', '_blank');
  w.document.write(html);
  w.document.close();
  setTimeout(() => w.print(), 500);
}

function shareCours() {
  saveCoursConfigFromUI();
  const cours = getMonCours();
  const config = getCoursConfig();

  const shareData = {
    t: config.titre || '',
    n: config.niveau || '',
    d: config.duree || '',
    no: config.notes || '',
    e: cours.map(e => ({
      t: e.titre,
      nt: e._note || ''
    }))
  };

  const encoded = btoa(unescape(encodeURIComponent(JSON.stringify(shareData))));
  const url = `https://sae.zonetotalsport.ca/?cours=${encoded}`;

  navigator.clipboard.writeText(url).then(() => {
    showToast('Lien de la SAE copie !');
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = url;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Lien de la SAE copie !');
  });
}

function checkCoursDeepLink() {
  const params = new URLSearchParams(window.location.search);
  const coursParam = params.get('cours');
  if (!coursParam) return;

  try {
    const data = JSON.parse(decodeURIComponent(escape(atob(coursParam))));
    setCoursConfig({
      titre: data.t || '',
      niveau: data.n || '',
      duree: data.d || '',
      notes: data.no || ''
    });

    const titres = (data.e || []).map(e => ({ titre: e.t, note: e.nt || '' }));
    const cours = [];
    for (const item of titres) {
      const found = allSAE.find(s => (s.titre || s.nom) === item.titre);
      if (found) {
        cours.push({
          titre: found.titre || found.nom || '',
          description: found.description || found.contexte_apprentissage || '',
          cycle: found.cycle || found.niveau || '',
          competence_pfeq: found.competence_pfeq || '',
          moyen_action: found.moyen_action || found.moyens_action || '',
          duree_periodes: found.duree_periodes || found.duree || '',
          _source: found._source || '',
          _note: item.note
        });
      }
    }
    setMonCours(cours);
    openCours();
  } catch (err) {
    console.warn('Cours deep link invalide', err);
  }
}
