// ============================================
// APP SAÉ PFEQ — Zone Total Sport
// ============================================

const SAE_SOURCES = [
  { key: 'prescolaire', path: 'data/sae/prescolaire.json', label: 'Préscolaire', cycle: 'Préscolaire' },
  { key: 'primaire', path: 'data/sae/primaire.json', label: 'Primaire', cycle: 'Primaire' },
  { key: 'secondaire', path: 'data/sae/secondaire.json', label: 'Secondaire', cycle: 'Secondaire' },
  { key: 'cooperation', path: 'data/sae/cooperation.json', label: 'Coopération', cycle: 'Primaire', arrayKey: 'saes' },
  { key: 'collectifs', path: 'data/sae/collectifs.json', label: 'Sports Collectifs', cycle: 'Secondaire', arrayKey: 'saes' },
  { key: 'opposition', path: 'data/sae/opposition.json', label: 'Opposition', cycle: 'Secondaire' },
  { key: 'dodgeball', path: 'data/sae/dodgeball.json', label: 'Ballon Chasseur', cycle: 'Primaire/Secondaire' },
  { key: 'locomotion', path: 'data/sae/locomotion.json', label: 'Locomotion', cycle: 'Primaire' },
  { key: 'mobilite', path: 'data/sae/mobilite.json', label: 'Mobilité', cycle: 'Primaire/Secondaire' },
  { key: 'poursuite', path: 'data/sae/poursuite.json', label: 'Jeux de poursuite', cycle: 'Maternelle → Sec 5' },
  { key: 'duel', path: 'data/sae/duel.json', label: 'Duel / Opposition', cycle: 'Primaire/Secondaire' },
  { key: 'conditionnement', path: 'data/sae/conditionnement.json', label: 'Conditionnement', cycle: 'Primaire/Secondaire' },
  { key: 'expression_corporelle', path: 'data/sae/expression_corporelle.json', label: 'Expression corporelle', cycle: 'Mat → Sec 5' },
  { key: 'sports_collectifs_sae', path: 'data/sae/sports_collectifs_sae.json', label: 'Sports collectifs', cycle: 'Primaire → Sec 5' },
  { key: 'manipulation_new', path: 'data/sae/manipulation_new.json', label: "Manipulation d'objets", cycle: 'Mat → Sec 5' },
  { key: 'locomotion_new', path: 'data/sae/locomotion_new.json', label: 'Locomotion', cycle: 'Mat → Sec 5' },
  { key: 'expression_artistique', path: 'data/sae/expression_artistique.json', label: 'Expression artistique', cycle: 'Mat → Sec 5' },
  { key: 'adresse_individuel', path: 'data/sae/adresse_individuel.json', label: 'Adresse et sports individuels', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_new', path: 'data/sae/cooperation_new.json', label: 'Coopération (nouveaux)', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_extra', path: 'data/sae/cooperation_extra.json', label: 'Coopération (extra)', cycle: 'Mat → Sec 5' },
  { key: 'individuelles_part8', path: 'data/sae/individuelles_part8.json', label: 'Individuelles', cycle: 'Mat → Sec 5' },
  { key: 'nonloc_gainage', path: 'data/sae/nonloc_gainage.json', label: 'Gainage et non-locomoteur', cycle: 'Mat → Sec 5' },
  { key: 'variees_extra', path: 'data/sae/variees_extra.json', label: 'Variées (extra)', cycle: 'Mat → Sec 5' },
  { key: 'cooperation_gen', path: 'data/sae/cooperation_gen.json', label: 'Coopération (génération)', cycle: 'Mat → Sec 5' },
  { key: 'poursuite_gen', path: 'data/sae/poursuite_gen.json', label: 'Poursuite (génération)', cycle: 'Mat → Sec 5' },
  { key: 'prescolaire_primaire_gen', path: 'data/sae/prescolaire_primaire_gen.json', label: 'Préscolaire-Primaire (génération)', cycle: 'Mat → Sec 5' },
];

const MOYENS_ACTION = [
  { key: 'manipulation', label: '🎯 Manipulation', emoji: '🎯', keywords: ['balle', 'ballon', 'raquette', 'baton', 'corde', 'cerceau', 'frisbee', 'cirque', 'foulard', 'manipulation', 'objet', 'jonglerie'] },
  { key: 'locomotion', label: '🏃 Locomotion', emoji: '🏃', keywords: ['courir', 'sauter', 'ramper', 'grimper', 'esquiver', 'locomotion', 'poursuite', 'courir', 'vitesse'] },
  { key: 'stabilisation', label: '⚖️ Stabilisation', emoji: '⚖️', keywords: ['equilibre', 'souplesse', 'gainage', 'coordination', 'mobilite', 'conditionnement', 'yoga', 'stretching', 'force', 'flexibilite'] },
  { key: 'opposition', label: '⚔️ Opposition', emoji: '⚔️', keywords: ['lutte', 'duel', 'territoire', 'opposition', 'dodgeball', 'chasseur', 'combat', 'confrontation'] },
  { key: 'cooperation', label: '🤝 Coopération', emoji: '🤝', keywords: ['communication', 'strategie', 'construction', 'cooperation', 'collectif', 'equipe', 'entraide', 'basket', 'volleyball', 'handball'] },
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
  checkDeepLink();
});

// ===== CHARGEMENT DES DONNÉES =====

async function loadAllSAE() {
  const results = await Promise.allSettled(
    SAE_SOURCES.map(source =>
      fetch(source.path)
        .then(r => {
          if (!r.ok) {
            console.warn(`⚠️ Fichier non trouvé: ${source.path}`);
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

  console.log(`✅ ${loaded} fichiers chargés, ${skipped} ignorés — ${allSAE.length} SAÉ au total`);
  filtered = [...allSAE];
  clearTimeout(safetyTimer);
}

function extractSAEs(data, source) {
  if (Array.isArray(data)) return data;
  if (source.arrayKey && data[source.arrayKey] && Array.isArray(data[source.arrayKey])) return data[source.arrayKey];
  if (data.saes && Array.isArray(data.saes)) return data.saes;
  if (data.items && Array.isArray(data.items)) return data.items;
  if (data.situations && Array.isArray(data.situations)) return data.situations;
  // Chercher la première propriété qui est un tableau de SAÉ
  for (const key of Object.keys(data)) {
    if (Array.isArray(data[key]) && data[key].length > 0 && (data[key][0].titre || data[key][0].nom)) {
      return data[key];
    }
  }
  // Objet SAÉ direct
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

  // Scroll vers les résultats
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

    // Filtre favoris
    if (favorisFilterActive) {
      if (!isFavori(s)) return false;
    }

    // Filtre recherche textuelle
    if (search) {
      const text = [
        s.titre, s.nom, s.description, s.contexte_apprentissage,
        s.tache_complexe, s.moyen_action, s._source,
        ...(s.tags || []), ...(s.competences || [])
      ].filter(Boolean).join(' ').toLowerCase();
      if (!text.includes(search)) return false;
    }

    // Filtre cycle
    if (cycle) {
      const c = [s.cycle, s.niveau, s._cycle].filter(Boolean).join(' ');
      if (!c.includes(cycle)) return false;
    }

    // Filtre moyen d'action (select)
    if (moyen) {
      const moyenStr = [
        s.moyen_action, s.moyens_action, s._source,
        ...(s.tags || []), s.titre, s.nom
      ].filter(Boolean).join(' ').toLowerCase();
      if (!moyenStr.includes(moyen.toLowerCase())) return false;
    }

    // Filtre compétence PFEQ
    if (competence) {
      const comp = [s.competence_pfeq, ...(s.competences || [])].filter(Boolean).join(' ').toLowerCase();
      if (!comp.includes(competence.toLowerCase())) return false;
    }

    // Filtre clientèle HDAA
    if (clientele) {
      const hdaa = JSON.stringify(s.adaptation_hdaa || {}).toLowerCase();
      const tags = (s.tags || []).join(' ').toLowerCase();
      const desc = (s.description || '').toLowerCase();
      if (!hdaa.includes(clientele) && !tags.includes(clientele) && !desc.includes(clientele)) return false;
    }

    // Filtre moyen d'action (boutons browser)
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
  if (c.includes('préscolaire') || c.includes('prescolaire') || c.includes('maternelle') || c.includes('mat')) {
    return 'cycle-prescolaire';
  }
  if (c.includes('secondaire') || c.includes('sec')) {
    return 'cycle-secondaire';
  }
  return 'cycle-primaire';
}

function renderCard(s) {
  const titre = s.titre || s.nom || 'SAÉ sans titre';
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
  div.setAttribute('aria-label', `Ouvrir la SAÉ: ${titre}`);

  const fav = isFavori(s);
  div.innerHTML = `
    <button class="fav-star ${fav ? 'active' : ''}" aria-label="Ajouter aux favoris" title="Favori">${fav ? '★' : '☆'}</button>
    <span class="pfeq-badge">PFEQ</span>
    ${cycle ? `<span class="cycle-badge ${getCycleClass(s)}">${escapeHtml(cycle)}</span>` : ''}
    <div class="card-title">${escapeHtml(titre)}</div>
    ${desc ? `<p class="card-desc">${escapeHtml(desc)}</p>` : ''}
    <div class="card-tags">
      ${competence ? `<span class="tag tag-competence">${escapeHtml(competence)}</span>` : ''}
      ${moyen ? `<span class="tag tag-moyen">${escapeHtml(moyen)}</span>` : ''}
      ${hasHDAA ? `<span class="tag tag-hdaa">♿ Adapté HDAA</span>` : ''}
    </div>
    ${duree ? `<div class="duree-badge">⏱ ${escapeHtml(String(duree))} période${parseInt(duree) > 1 ? 's' : ''}</div>` : ''}
  `;

  // Star click handler (stop propagation so card doesn't open)
  const starBtn = div.querySelector('.fav-star');
  starBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const nowFav = toggleFavori(s);
    starBtn.textContent = nowFav ? '★' : '☆';
    starBtn.classList.toggle('active', nowFav);
    // If favoris filter is active, re-render to remove unfavorited cards
    if (favorisFilterActive) applyFilters();
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
        <p style="font-size:1.1rem;color:var(--text-muted)">Aucune SAÉ trouvée</p>
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

  // Animation IntersectionObserver
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

  // Previous button
  const prevBtn = document.createElement('button');
  prevBtn.className = 'page-btn page-prev' + (currentPage === 0 ? ' disabled' : '');
  prevBtn.textContent = '\u2190 Précédent';
  prevBtn.disabled = currentPage === 0;
  prevBtn.addEventListener('click', () => goToPage(currentPage - 1));
  container.appendChild(prevBtn);

  // Page numbers
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
    if (start > 1) pages.push(-1); // ellipsis
    for (let i = start; i <= end; i++) pages.push(i);
    if (end < totalPages - 2) pages.push(-1); // ellipsis
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

  // Next button
  const nextBtn = document.createElement('button');
  nextBtn.className = 'page-btn page-next' + (currentPage >= totalPages - 1 ? ' disabled' : '');
  nextBtn.textContent = 'Suivant \u2192';
  nextBtn.disabled = currentPage >= totalPages - 1;
  nextBtn.addEventListener('click', () => goToPage(currentPage + 1));
  container.appendChild(nextBtn);

  // Info text
  const info = document.createElement('div');
  info.className = 'page-info';
  const start = currentPage * ITEMS_PER_PAGE + 1;
  const end = Math.min((currentPage + 1) * ITEMS_PER_PAGE, filtered.length);
  info.textContent = `${start}\u2013${end} sur ${filtered.length} SAÉ`;
  container.appendChild(info);
}

function goToPage(page) {
  const totalPages = Math.ceil(filtered.length / ITEMS_PER_PAGE);
  if (page < 0 || page >= totalPages) return;
  currentPage = page;
  renderSAE();
  // Scroll to grid section
  const grid = document.getElementById('sae-grid');
  if (grid) {
    grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

function updateStats() {
  const countEl = document.getElementById('sae-count');
  if (countEl) countEl.textContent = `${filtered.length} SAÉ`;

  const totalEl = document.getElementById('hstat-sae');
  if (totalEl) totalEl.innerHTML = `${allSAE.length}<span>SAÉ</span>`;

  const counterEl = document.getElementById('counter-sae');
  if (counterEl) counterEl.textContent = allSAE.length;
}

// ===== MODAL =====

function openModal(s) {
  const modal = document.getElementById('modal');
  const body = document.getElementById('modal-body');
  if (!modal || !body) return;

  const titre = s.titre || s.nom || 'SAÉ';

  // Construction des sections
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
        <h3>🎯 Tâche complexe</h3>
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
        <h3>🎒 Matériel requis</h3>
        <ul>${(Array.isArray(s.materiel) ? s.materiel : [s.materiel])
          .map(m => `<li>${escapeHtml(typeof m === 'string' ? m : JSON.stringify(m))}</li>`).join('')}</ul>
      </div>`,
    s.deroulement && `
      <div class="modal-section">
        <h3>📝 Déroulement</h3>
        ${typeof s.deroulement === 'string'
          ? `<p>${escapeHtml(s.deroulement)}</p>`
          : `<ul>${(Array.isArray(s.deroulement) ? s.deroulement : Object.values(s.deroulement))
              .map(d => `<li>${escapeHtml(typeof d === 'string' ? d : JSON.stringify(d))}</li>`).join('')}</ul>`
        }
      </div>`,
    s.criteres_evaluation && `
      <div class="modal-section">
        <h3>📊 Critères d'évaluation</h3>
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
        <h3>🔄 Variantes et différenciation</h3>
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
          .map(([k, v]) => `<p><strong style="color:var(--accent)">${escapeHtml(k)} :</strong> ${escapeHtml(typeof v === 'string' ? v : JSON.stringify(v))}</p>`)
          .join('')}
      </div>`,
    (s.notes || s.remarques) && `
      <div class="modal-section">
        <h3>💡 Notes pédagogiques</h3>
        <p>${escapeHtml(s.notes || s.remarques)}</p>
      </div>`,
  ].filter(Boolean).join('');

  const modalFav = isFavori(s);
  const saeId = getSaeId(s);

  body.innerHTML = `
    <div class="modal-header">
      <h2 class="modal-title" id="modal-title">📚 ${escapeHtml(titre)}</h2>
      <button class="modal-close" onclick="closeModal()" aria-label="Fermer">✕</button>
    </div>
    <div class="modal-meta">
      ${s.cycle || s.niveau ? `<span class="modal-badge cycle-badge ${getCycleClass(s)}">${escapeHtml(s.cycle || s.niveau)}</span>` : ''}
      ${s.competence_pfeq ? `<span class="modal-badge">${escapeHtml(s.competence_pfeq)}</span>` : ''}
      ${s.moyen_action ? `<span class="modal-badge" style="background:var(--secondary-dim);color:#38bdf8;border-color:rgba(8,145,178,0.3)">${escapeHtml(s.moyen_action)}</span>` : ''}
      ${s.duree_periodes ? `<span class="modal-badge">⏱ ${escapeHtml(String(s.duree_periodes))} période${parseInt(s.duree_periodes) > 1 ? 's' : ''}</span>` : ''}
      ${s.espace ? `<span class="modal-badge">📍 ${escapeHtml(s.espace)}</span>` : ''}
      ${s.nb_eleves ? `<span class="modal-badge">👥 ${escapeHtml(String(s.nb_eleves))}</span>` : ''}
    </div>
    <div class="modal-actions">
      <button class="modal-action-btn ${modalFav ? 'fav-active' : ''}" id="modal-fav-btn" onclick="handleModalFavori()">
        ${modalFav ? '★' : '☆'} Favori
      </button>
      <button class="modal-action-btn" onclick="handlePrint()">🖨️ Imprimer</button>
      <button class="modal-action-btn" onclick="handleShare('${escapeHtml(saeId).replace(/'/g, "\\'")}')">🔗 Partager</button>
    </div>
    ${sections || '<p style="color:var(--text-muted);text-align:center;padding:24px">Aucun détail supplémentaire disponible.</p>'}
  `;

  // Store reference to current SAÉ for modal actions
  window._currentModalSAE = s;

  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';

  // Focus trap
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

// ===== COUNTERS ANIMÉS =====

function animateCounters() {
  // Mettre à jour le counter hero avec le nombre réel
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

  // Animer les data-count génériques
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

// ===== CANVAS ANIMÉ =====

function initCanvas() {
  const canvas = document.getElementById('bgCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();

  let t = 0;

  function draw() {
    const w = canvas.width;
    const h = canvas.height;

    ctx.clearRect(0, 0, w, h);

    // Gradient principal animé
    const grad = ctx.createLinearGradient(0, 0, w, h);
    const greenVal = 60 + Math.sin(t) * 12;
    const blueVal = 20 + Math.sin(t * 0.5) * 8;
    grad.addColorStop(0, `rgba(0, ${greenVal}, ${blueVal}, 0.25)`);
    grad.addColorStop(0.5, `rgba(0, 25, 35, 0.15)`);
    grad.addColorStop(1, `rgba(0, ${40 + Math.cos(t * 0.7) * 10}, ${30 + Math.sin(t * 0.3) * 6}, 0.2)`);

    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Orbes flottants subtils
    drawOrb(ctx, w * 0.15, h * 0.25, 180, `rgba(0,229,160,${0.025 + Math.sin(t * 0.8) * 0.01})`);
    drawOrb(ctx, w * 0.85, h * 0.6, 220, `rgba(8,145,178,${0.02 + Math.sin(t * 0.6 + 1) * 0.008})`);
    drawOrb(ctx, w * 0.5, h * 0.85, 160, `rgba(0,229,160,${0.015 + Math.cos(t * 0.4) * 0.008})`);

    t += 0.004;
    requestAnimationFrame(draw);
  }

  draw();
  window.addEventListener('resize', resize);
}

function drawOrb(ctx, x, y, r, color) {
  const grad = ctx.createRadialGradient(x, y, 0, x, y, r);
  grad.addColorStop(0, color);
  grad.addColorStop(1, 'transparent');
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fill();
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
  // Update the corresponding card star if visible
  renderSAE();
}

function handlePrint() {
  window.print();
}

function handleShare(saeId) {
  const url = `https://sae.zonetotalsport.ca/?id=${encodeURIComponent(saeId)}`;
  navigator.clipboard.writeText(url).then(() => {
    showToast('Lien copié !');
  }).catch(() => {
    // Fallback for older browsers
    const ta = document.createElement('textarea');
    ta.value = url;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Lien copié !');
  });
}

function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.classList.remove('hidden');
  // Force reflow
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

// ===== ÉVÉNEMENTS GLOBAUX =====

document.addEventListener('click', e => {
  if (e.target.id === 'modal-backdrop') closeModal();
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeModal();
});
