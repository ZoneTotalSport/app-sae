#!/usr/bin/env python3
"""Generate 140 SAÉ for Expression category."""
import json

sae_list = []

# Helper to make IDs
def mid(n):
    return f"EXPB-{n:03d}"

# ============================================================
# MATERNELLE (4-5 ans) — 23 SAÉ (EXPB-001 to EXPB-023)
# ============================================================

sae_list.append({
    "id": mid(1), "titre": "Les papillons dansants",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent les mouvements légers et fluides en s'imaginant être des papillons. Ils découvrent les niveaux (haut, moyen, bas) et les qualités de mouvement à travers l'imagerie de la métamorphose.",
    "contexte_apprentissage": "L'enseignant raconte l'histoire d'une chenille qui devient papillon. Les enfants vivent chaque étape avec leur corps.",
    "tache_complexe": "L'élève crée une séquence de 3 mouvements illustrant la métamorphose du papillon et la présente à un camarade.",
    "criteres_evaluation": ["Variété des mouvements explorés", "Utilisation des niveaux haut-moyen-bas", "Respect de l'espace des autres"],
    "savoirs_essentiels": ["Niveaux dans l'espace", "Mouvements légers et fluides", "Parties du corps mobilisées"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marche libre dans le gymnase en imitant différents insectes au signal du tambourin", "role_enseignant": "Donner les consignes sonores, nommer les actions observées"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Exploration guidée : ramper comme une chenille, s'enrouler dans un cocon, déployer ses ailes de papillon", "role_enseignant": "Démontrer chaque étape, encourager la créativité, circuler parmi les élèves"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Chaque enfant crée sa propre danse du papillon en enchaînant 3 mouvements choisis", "role_enseignant": "Observer, offrir des rétroactions positives, aider les élèves en difficulté"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Les papillons se posent doucement sur une fleur et ferment leurs ailes lentement", "role_enseignant": "Guider la relaxation, parler doucement, féliciter les efforts"}
    ],
    "materiel": ["Tambourin", "Musique douce", "Foulards de couleur"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "maternelle", "métamorphose"]
})

sae_list.append({
    "id": mid(2), "titre": "Le zoo en mouvement",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Mime",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants imitent différents animaux du zoo en utilisant tout leur corps. Ils découvrent les contrastes de mouvement : lourd/léger, rapide/lent, grand/petit.",
    "contexte_apprentissage": "L'enseignant présente des images d'animaux et invite les enfants à devenir ces animaux avec leur corps, en exagérant les caractéristiques.",
    "tache_complexe": "L'élève choisit deux animaux contrastants et crée une petite séquence de mime passant de l'un à l'autre.",
    "criteres_evaluation": ["Capacité à imiter les caractéristiques de l'animal", "Utilisation de contrastes de mouvement", "Engagement dans l'activité"],
    "savoirs_essentiels": ["Contrastes de mouvement", "Imitation corporelle", "Expression sans paroles"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu du miroir : imiter les mouvements de l'enseignant qui fait différents animaux", "role_enseignant": "Démontrer des mouvements variés, encourager l'imitation"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "L'enseignant montre des images d'animaux un à un ; les enfants explorent comment bouger comme chaque animal", "role_enseignant": "Présenter les images, donner des indices corporels, valoriser les essais"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "En duo, un enfant mime un animal et l'autre devine. Alterner les rôles.", "role_enseignant": "Circuler, encourager la variété, aider les duos en difficulté"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Devenir un chat qui s'endort : étirements doux et respiration profonde", "role_enseignant": "Guider les étirements, baisser le ton de voix progressivement"}
    ],
    "materiel": ["Images d'animaux plastifiées", "Musique d'ambiance nature"],
    "espace": "Gymnase",
    "tags": ["expression", "mime", "animaux", "maternelle"]
})

sae_list.append({
    "id": mid(3), "titre": "La tempête et le calme",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Expression corporelle",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent les contrastes d'énergie en dansant la tempête (mouvements forts, rapides, saccadés) puis le calme (mouvements doux, lents, fluides). Ils développent leur conscience corporelle.",
    "contexte_apprentissage": "À travers une histoire de météo changeante, les enfants passent d'un état d'énergie à l'autre en contrôlant leur corps.",
    "tache_complexe": "L'élève enchaîne trois moments : vent léger, grosse tempête, retour au soleil, en variant l'énergie de ses mouvements.",
    "criteres_evaluation": ["Capacité à varier l'énergie du mouvement", "Contrôle corporel lors des transitions", "Écoute des consignes sonores"],
    "savoirs_essentiels": ["Qualités d'énergie : fort/doux", "Vitesse du mouvement", "Contrôle corporel"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marche libre en variant la vitesse selon le rythme du tambourin", "role_enseignant": "Varier le tempo, observer les réponses motrices"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Explorer les mouvements de tempête (secouer, tourner vite, sauter) puis de calme (balancer, flotter, fondre)", "role_enseignant": "Narrer l'histoire météo, démontrer les contrastes, encourager l'expression"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Avec musique, les enfants créent leur propre danse de la météo en passant de la tempête au calme", "role_enseignant": "Contrôler la musique, observer la variété, offrir des rétroactions"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Le soleil se couche : les enfants fondent lentement au sol et respirent profondément", "role_enseignant": "Guider la respiration, créer une ambiance apaisante"}
    ],
    "materiel": ["Tambourin", "Musique contrastée (rapide et lente)", "Foulards"],
    "espace": "Gymnase",
    "tags": ["expression", "expression corporelle", "contrastes", "maternelle"]
})

sae_list.append({
    "id": mid(4), "titre": "Le ruban magique",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Gymnastique rythmique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent le ruban de gymnastique rythmique en explorant les formes dans l'espace : cercles, vagues, spirales. Ils développent la coordination œil-main et la fluidité.",
    "contexte_apprentissage": "L'enseignant présente le ruban comme un outil magique qui dessine dans l'air. Les enfants explorent librement puis apprennent des formes de base.",
    "tache_complexe": "L'élève réalise une séquence de 3 formes différentes avec le ruban en se déplaçant dans l'espace.",
    "criteres_evaluation": ["Fluidité du mouvement avec le ruban", "Variété des formes réalisées", "Déplacement dans l'espace général"],
    "savoirs_essentiels": ["Formes dans l'espace : cercle, vague, spirale", "Coordination œil-main", "Déplacement et manipulation simultanés"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Agiter les bras librement comme des rubans humains, en variant les niveaux et les directions", "role_enseignant": "Démontrer les mouvements, encourager l'amplitude"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Distribution des rubans, exploration libre puis apprentissage des 3 formes de base", "role_enseignant": "Distribuer le matériel, démontrer chaque forme, circuler pour aider"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Les enfants se déplacent dans le gymnase en créant des dessins avec leur ruban au son de la musique", "role_enseignant": "Mettre la musique, encourager le déplacement, valoriser la créativité"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Le ruban fait des vagues de plus en plus petites et lentes, puis se pose au sol", "role_enseignant": "Guider le retour au calme, ramasser le matériel, faire un retour verbal"}
    ],
    "materiel": ["Rubans de gymnastique rythmique (1 par élève)", "Musique douce et fluide"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique rythmique", "ruban", "maternelle"]
})

sae_list.append({
    "id": mid(5), "titre": "Petit clown, grand clown",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Cirque",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent l'univers du clown en exagérant leurs expressions faciales et leurs mouvements. Ils découvrent la marche comique, les chutes contrôlées et les émotions théâtrales.",
    "contexte_apprentissage": "L'enseignant présente le personnage du clown et ses caractéristiques : exagération, surprise, maladresse amusante.",
    "tache_complexe": "L'élève crée un petit numéro de clown avec une entrée, une action comique et une sortie.",
    "criteres_evaluation": ["Exagération des expressions faciales", "Contrôle du corps dans les mouvements comiques", "Participation enthousiaste"],
    "savoirs_essentiels": ["Expressions faciales exagérées", "Marche comique", "Chute contrôlée sécuritaire"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu des émotions : marcher en étant très content, très surpris, très triste, très fâché", "role_enseignant": "Nommer les émotions, démontrer l'exagération, encourager l'expression"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre la marche du clown, la surprise exagérée et la chute au ralenti", "role_enseignant": "Démontrer chaque élément, assurer la sécurité des chutes, circuler"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "En petits groupes, chaque enfant présente son petit numéro de clown aux autres", "role_enseignant": "Organiser les présentations, applaudir, encourager le public à réagir"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Le clown fatigué s'étire et bâille de plus en plus lentement", "role_enseignant": "Guider les étirements ludiques, faire un retour sur l'activité"}
    ],
    "materiel": ["Nez de clown (optionnel)", "Musique de cirque"],
    "espace": "Gymnase",
    "tags": ["expression", "cirque", "clown", "maternelle"]
})

sae_list.append({
    "id": mid(6), "titre": "La forêt enchantée",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Relaxation créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "À travers une histoire guidée, les enfants deviennent des arbres, des animaux et des éléments de la forêt. Ils explorent les mouvements lents, la respiration consciente et l'équilibre statique.",
    "contexte_apprentissage": "L'enseignant guide une aventure imaginaire en forêt où les enfants incarnent différents éléments naturels avec leur corps.",
    "tache_complexe": "L'élève maintient une posture d'arbre en équilibre pendant 10 secondes et enchaîne avec un mouvement d'animal.",
    "criteres_evaluation": ["Capacité à maintenir l'équilibre", "Écoute active de l'histoire guidée", "Fluidité des transitions entre les personnages"],
    "savoirs_essentiels": ["Équilibre statique", "Respiration consciente", "Mouvements lents et contrôlés"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marche silencieuse dans la forêt : se déplacer sans faire de bruit comme un renard", "role_enseignant": "Créer l'ambiance avec la voix, jouer une musique de nature"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Devenir un arbre : racines dans le sol, tronc solide, branches qui bougent au vent", "role_enseignant": "Narrer l'histoire, démontrer les postures, aider à l'équilibre"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Parcours dans la forêt enchantée : alterner entre posture d'arbre, déplacement d'animal et mouvement du vent", "role_enseignant": "Guider le parcours, varier les consignes, observer les réponses"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "La nuit tombe sur la forêt : les enfants se couchent au sol et écoutent les sons de la nature", "role_enseignant": "Baisser les lumières si possible, jouer des sons de nature, guider la respiration"}
    ],
    "materiel": ["Musique de nature/forêt", "Tapis de sol (optionnel)"],
    "espace": "Gymnase",
    "tags": ["expression", "relaxation créative", "nature", "maternelle"]
})

sae_list.append({
    "id": mid(7), "titre": "Les roulades rigolotes",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Gymnastique au sol",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent la roulade avant en toute sécurité sur un plan incliné. Ils apprennent à se placer en boule, à rentrer le menton et à rouler de manière fluide.",
    "contexte_apprentissage": "L'enseignant utilise l'image du hérisson qui se met en boule. Les enfants progressent du balancement à la roulade complète.",
    "tache_complexe": "L'élève réalise une roulade avant sur le plan incliné en gardant le menton rentré et en se relevant debout.",
    "criteres_evaluation": ["Menton rentré sur la poitrine", "Corps en boule compact", "Roulade fluide sans arrêt"],
    "savoirs_essentiels": ["Position groupée", "Roulade avant adaptée", "Sécurité : menton rentré"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Se balancer comme un œuf : assis, genoux repliés, se balancer d'avant en arrière", "role_enseignant": "Démontrer la position groupée, vérifier les mentons rentrés"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Sur les tapis, pratiquer le balancement en boule, puis la roulade sur plan incliné avec aide", "role_enseignant": "Installer le matériel, assurer la parade, corriger les positions"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Ateliers : roulade sur plan incliné, roulade sur tapis plat pour les plus avancés, balancement pour les débutants", "role_enseignant": "Superviser les ateliers, offrir la parade, encourager les progrès"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements doux en boule puis en étoile, respiration profonde", "role_enseignant": "Guider les étirements, féliciter les efforts, ramasser le matériel"}
    ],
    "materiel": ["Tapis de gymnastique", "Plan incliné", "Tapis de réception"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique au sol", "roulade", "maternelle"]
})

sae_list.append({
    "id": mid(8), "titre": "Danse des foulards arc-en-ciel",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants utilisent des foulards colorés pour explorer les trajectoires dans l'espace : cercles, vagues et spirales tout en se déplaçant librement au son de la musique.",
    "contexte_apprentissage": "Chaque enfant reçoit un foulard de couleur et explore les possibilités de mouvement. L'enseignant introduit les trajectoires une à une.",
    "tache_complexe": "L'élève enchaîne trois trajectoires différentes avec son foulard en se déplaçant dans le gymnase.",
    "criteres_evaluation": ["Variété des trajectoires", "Déplacement fluide dans l'espace", "Écoute musicale"],
    "savoirs_essentiels": ["Trajectoires : cercle, vague, spirale", "Déplacement avec objet", "Espace personnel et général"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Lancer et rattraper le foulard, le faire voler en soufflant dessus", "role_enseignant": "Distribuer les foulards, encourager l'exploration libre"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre 3 trajectoires : cercle au-dessus de la tête, vague devant soi, spirale en tournant", "role_enseignant": "Démontrer chaque trajectoire, circuler pour corriger, valoriser les essais"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Danse libre avec foulard au son de différentes musiques", "role_enseignant": "Changer les musiques, observer la créativité, encourager les déplacements"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Le foulard descend lentement du ciel comme une feuille d'automne et se pose au sol", "role_enseignant": "Guider le retour au calme, ramasser les foulards, faire un court bilan"}
    ],
    "materiel": ["Foulards de couleur (1 par élève)", "Musiques variées"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "foulards", "maternelle"]
})

sae_list.append({
    "id": mid(9), "titre": "Le robot et la marionnette",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Mime",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent deux qualités de mouvement opposées : le robot (saccadé, rigide) et la marionnette (souple, tirée par des fils imaginaires).",
    "contexte_apprentissage": "L'enseignant présente deux personnages et les enfants explorent les différences de mouvement entre les deux.",
    "tache_complexe": "L'élève alterne entre le mouvement robot et le mouvement marionnette au signal de l'enseignant.",
    "criteres_evaluation": ["Différenciation claire entre les deux qualités", "Contrôle corporel", "Réactivité aux signaux"],
    "savoirs_essentiels": ["Qualités de mouvement : saccadé vs fluide", "Tension et relâchement musculaire", "Écoute des signaux"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu statue/danse : danser librement et se figer au signal", "role_enseignant": "Contrôler la musique, varier les durées, observer les postures"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Explorer séparément le mouvement robot puis la marionnette", "role_enseignant": "Démontrer chaque personnage, utiliser des images, corriger doucement"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Jeu de transformation : au signal, passer de robot à marionnette et vice-versa", "role_enseignant": "Donner les signaux, varier le rythme, encourager la clarté"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "La marionnette dont on coupe les fils : le corps s'affaisse doucement partie par partie", "role_enseignant": "Guider la relaxation progressive, voix douce et calme"}
    ],
    "materiel": ["Tambourin", "Musique mécanique et musique douce"],
    "espace": "Gymnase",
    "tags": ["expression", "mime", "contrastes", "maternelle"]
})

sae_list.append({
    "id": mid(10), "titre": "Équilibristes en herbe",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Cirque",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent l'équilibre de cirque : marcher sur une ligne, se tenir sur un pied, porter un objet en équilibre sur la tête. Ils développent la proprioception.",
    "contexte_apprentissage": "L'enseignant crée un univers de cirque avec des lignes au sol représentant le fil de fer et des défis d'équilibre progressifs.",
    "tache_complexe": "L'élève traverse une ligne au sol en portant un sac de sable sur la tête sans le faire tomber.",
    "criteres_evaluation": ["Maintien de l'équilibre sur la ligne", "Posture droite et regard devant", "Concentration et persévérance"],
    "savoirs_essentiels": ["Équilibre dynamique", "Centre de gravité", "Concentration et focus"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marcher sur les lignes du gymnase de différentes façons", "role_enseignant": "Démontrer les déplacements, encourager la variété"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Ateliers d'équilibre : poutre basse, un pied 5 secondes, sac sur la tête", "role_enseignant": "Installer les ateliers, assurer la sécurité"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Parcours d'équilibriste : enchaîner les défis en musique de cirque", "role_enseignant": "Superviser le parcours, ajuster les défis au niveau de chacun"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "L'arbre qui pousse : posture d'équilibre statique, bras qui montent comme des branches", "role_enseignant": "Guider la posture, respiration calme, féliciter les progrès"}
    ],
    "materiel": ["Poutre basse", "Sacs de sable", "Ruban adhésif au sol", "Musique de cirque"],
    "espace": "Gymnase",
    "tags": ["expression", "cirque", "équilibre", "maternelle"]
})

sae_list.append({
    "id": mid(11), "titre": "Les saisons qui dansent",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Expression corporelle",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent les quatre saisons par le mouvement : la neige qui tombe, les bourgeons qui poussent, le soleil brûlant et les feuilles qui volent.",
    "contexte_apprentissage": "L'enseignant utilise des images et de la musique pour évoquer chaque saison. Les enfants traduisent les sensations en mouvements.",
    "tache_complexe": "L'élève choisit sa saison préférée et crée 3 mouvements qui la représentent.",
    "criteres_evaluation": ["Association mouvement-saison pertinente", "Variété des mouvements", "Expression du ressenti corporel"],
    "savoirs_essentiels": ["Qualités de mouvement associées aux saisons", "Vocabulaire corporel", "Créativité motrice"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marcher en variant la démarche selon la météo annoncée", "role_enseignant": "Annoncer les météos, observer les adaptations motrices"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Explorer chaque saison : flocons (hiver), fleurs (printemps), nager (été), feuilles (automne)", "role_enseignant": "Guider l'exploration avec images et musique, démontrer des exemples"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Chaque enfant crée une petite danse de sa saison préférée à présenter aux autres", "role_enseignant": "Aider les indécis, encourager la créativité, organiser les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "L'hiver arrive : les flocons se posent doucement au sol et tout devient silencieux", "role_enseignant": "Guider la descente au sol, respiration lente, bilan de l'activité"}
    ],
    "materiel": ["Images des saisons", "4 musiques différentes", "Foulards blancs"],
    "espace": "Gymnase",
    "tags": ["expression", "expression corporelle", "saisons", "maternelle"]
})

sae_list.append({
    "id": mid(12), "titre": "Rondes et comptines dansées",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse folklorique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent les rondes traditionnelles québécoises et françaises. Ils apprennent à danser en cercle, à suivre le rythme d'une comptine et à coordonner leurs pas avec le groupe.",
    "contexte_apprentissage": "L'enseignant enseigne des rondes simples en version dansée avec chant collectif.",
    "tache_complexe": "L'élève participe à une ronde complète en chantant et en exécutant les gestes au bon moment.",
    "criteres_evaluation": ["Coordination avec le groupe", "Exécution des gestes au bon moment", "Participation active au chant"],
    "savoirs_essentiels": ["Formation en cercle", "Pas chassé simple", "Coordination mouvement-musique"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Former un grand cercle, se donner la main et marcher ensemble dans un sens puis dans l'autre", "role_enseignant": "Aider à former le cercle, donner le rythme avec la voix"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre la comptine avec les gestes associés, d'abord sans musique puis avec", "role_enseignant": "Enseigner les paroles, démontrer les gestes, répéter patiemment"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Danser la ronde complète avec la musique", "role_enseignant": "Participer à la ronde, maintenir le rythme, encourager le chant"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Ronde très lente en chuchotant la comptine, puis s'asseoir en cercle pour un bilan", "role_enseignant": "Ralentir progressivement, féliciter le groupe"}
    ],
    "materiel": ["Musique de comptines", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "danse folklorique", "rondes", "maternelle"]
})

sae_list.append({
    "id": mid(13), "titre": "Le yoga des animaux",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Relaxation créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent des postures de yoga portant des noms d'animaux : le chat, le chien, le cobra, le papillon. Ils développent souplesse, équilibre et conscience respiratoire.",
    "contexte_apprentissage": "À travers une histoire d'aventure au safari, les enfants rencontrent différents animaux et adoptent leur posture de yoga.",
    "tache_complexe": "L'élève enchaîne 4 postures animales en maintenant chacune pendant 5 respirations.",
    "criteres_evaluation": ["Maintien des postures", "Respiration consciente", "Transition douce entre les postures"],
    "savoirs_essentiels": ["Postures de base en yoga", "Respiration abdominale", "Souplesse et équilibre"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Respiration du ballon : inspirer en gonflant le ventre, expirer en le dégonflant", "role_enseignant": "Démontrer la respiration abdominale, vérifier la compréhension"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre 4 postures : le chat, le chien, le cobra, le papillon", "role_enseignant": "Démontrer chaque posture, corriger les alignements, narrer l'histoire"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Safari yoga : enchaîner les postures au fil de l'histoire", "role_enseignant": "Raconter l'histoire, maintenir le calme, valoriser les postures inventées"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Posture de l'étoile de mer : couché sur le dos, bras et jambes écartés, respiration lente", "role_enseignant": "Guider la relaxation finale, voix très douce, musique zen"}
    ],
    "materiel": ["Tapis de sol", "Images de postures animales", "Musique zen"],
    "espace": "Gymnase",
    "tags": ["expression", "relaxation créative", "yoga", "maternelle"]
})

sae_list.append({
    "id": mid(14), "titre": "Les jongleurs débutants",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Cirque",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants s'initient à la jonglerie avec des foulards légers. Ils apprennent à lancer et rattraper un foulard, puis explorent les lancers alternés.",
    "contexte_apprentissage": "L'enseignant présente la jonglerie comme un art de cirque accessible. Les foulards tombent lentement, facilitant l'apprentissage.",
    "tache_complexe": "L'élève lance un foulard d'une main et le rattrape de l'autre, 5 fois de suite.",
    "criteres_evaluation": ["Lancer contrôlé vers le haut", "Rattraper avec la main opposée", "Persévérance dans la pratique"],
    "savoirs_essentiels": ["Lancer vertical", "Coordination bilatérale", "Suivi visuel de l'objet"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Manipulation libre du foulard : lancer, souffler, faire tourner, rattraper", "role_enseignant": "Distribuer un foulard par enfant, encourager l'exploration"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Lancer et rattraper de la même main, puis lancer d'une main et rattraper de l'autre", "role_enseignant": "Démontrer chaque étape, circuler pour aider"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Défi progressif : 3 rattrapés, puis 5, puis essayer avec 2 foulards", "role_enseignant": "Proposer des défis adaptés, encourager, célébrer les réussites"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Lancer le foulard le plus haut possible et s'asseoir avant qu'il touche le sol", "role_enseignant": "Animer le jeu calme, ramasser les foulards, bilan"}
    ],
    "materiel": ["Foulards légers (1-2 par élève)", "Musique de cirque douce"],
    "espace": "Gymnase",
    "tags": ["expression", "cirque", "jonglerie", "maternelle"]
})

sae_list.append({
    "id": mid(15), "titre": "La danse des prénoms",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Création chorégraphique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Chaque enfant crée un mouvement pour chaque syllabe de son prénom. Le groupe apprend et reproduit les mouvements de chacun, créant une chorégraphie collective.",
    "contexte_apprentissage": "L'enseignant démontre avec son propre prénom comment associer un mouvement à chaque syllabe.",
    "tache_complexe": "L'élève crée et exécute sa danse-prénom devant le groupe, puis apprend celle de deux camarades.",
    "criteres_evaluation": ["Créativité des mouvements", "Mémorisation des mouvements des autres", "Présentation devant le groupe"],
    "savoirs_essentiels": ["Association mouvement-rythme", "Mémorisation de séquences courtes", "Expression personnelle"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Taper le rythme de son prénom dans les mains, puis avec les pieds, puis tout le corps", "role_enseignant": "Démontrer avec son prénom, vérifier que chacun trouve son rythme"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Chaque enfant invente un mouvement par syllabe de son prénom", "role_enseignant": "Circuler, donner des idées, valoriser l'originalité"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Tour de cercle : chacun présente sa danse-prénom, le groupe la reproduit", "role_enseignant": "Animer le cercle, encourager, guider la reproduction en groupe"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Chuchoter son prénom en faisant les mouvements de plus en plus petits et lents", "role_enseignant": "Guider le ralentissement, bilan positif"}
    ],
    "materiel": ["Aucun matériel requis"],
    "espace": "Gymnase",
    "tags": ["expression", "création chorégraphique", "identité", "maternelle"]
})

sae_list.append({
    "id": mid(16), "titre": "Le cerceau dansant",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Gymnastique rythmique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent le cerceau comme engin de gymnastique rythmique : le faire rouler, tourner autour du bras, sauter dedans et créer des formes au sol.",
    "contexte_apprentissage": "Le cerceau est présenté comme un portail magique. Les enfants explorent toutes les façons de jouer avec.",
    "tache_complexe": "L'élève réalise 3 actions différentes avec son cerceau en enchaînement.",
    "criteres_evaluation": ["Variété des manipulations", "Contrôle du cerceau", "Enchaînement fluide"],
    "savoirs_essentiels": ["Manipulation d'engin", "Coordination main-œil", "Créativité avec un objet"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Placer le cerceau au sol et sauter dedans/dehors de différentes façons", "role_enseignant": "Distribuer les cerceaux, proposer des variantes de sauts"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre 4 actions : rouler, tourner au sol, tourner autour du bras, lancer et rattraper", "role_enseignant": "Démontrer chaque action, circuler, assurer la sécurité"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Avec musique, enchaîner librement les actions en se déplaçant", "role_enseignant": "Mettre la musique, encourager la créativité"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "S'asseoir dans son cerceau, respirer calmement", "role_enseignant": "Guider le retour au calme, ranger le matériel"}
    ],
    "materiel": ["Cerceaux (1 par élève)", "Musique rythmée"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique rythmique", "cerceau", "maternelle"]
})

sae_list.append({
    "id": mid(17), "titre": "Les marionnettes humaines",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Expression corporelle",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "En duo, un enfant est la marionnette et l'autre le marionnettiste. Le marionnettiste guide les mouvements par des gestes au-dessus des parties du corps, sans toucher.",
    "contexte_apprentissage": "L'enseignant présente le concept de marionnette à fils et les enfants apprennent à guider et être guidé avec respect.",
    "tache_complexe": "L'élève guide son partenaire-marionnette pour réaliser une marche et un geste, puis inverse les rôles.",
    "criteres_evaluation": ["Douceur et respect du partenaire", "Réactivité de la marionnette", "Communication non verbale"],
    "savoirs_essentiels": ["Communication non verbale", "Confiance et respect mutuel", "Conscience des parties du corps"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu du miroir : face à face, un enfant bouge lentement et l'autre l'imite", "role_enseignant": "Former les duos, démontrer le jeu du miroir"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre le rôle de marionnettiste : lever la main au-dessus de la tête pour le faire grandir, etc.", "role_enseignant": "Démontrer avec un élève, expliquer les règles (pas de toucher)"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "En duo, pratiquer en alternant les rôles avec musique", "role_enseignant": "Observer les interactions, rappeler les règles de respect"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Le marionnettiste coupe tous les fils et la marionnette s'endort doucement", "role_enseignant": "Guider le retour au calme, bilan sur la confiance"}
    ],
    "materiel": ["Musique douce et lente"],
    "espace": "Gymnase",
    "tags": ["expression", "expression corporelle", "duo", "maternelle"]
})

sae_list.append({
    "id": mid(18), "titre": "Mon corps fait de la musique",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent les percussions corporelles : taper des mains, des pieds, des cuisses. Ils créent des rythmes simples puis les transforment en mouvements dansés.",
    "contexte_apprentissage": "L'enseignant montre que le corps peut être un instrument de musique. Les enfants explorent les sons corporels.",
    "tache_complexe": "L'élève crée une séquence rythmique de 4 temps avec des percussions corporelles et la danse.",
    "criteres_evaluation": ["Variété des sons corporels", "Régularité du rythme", "Transformation du rythme en mouvement"],
    "savoirs_essentiels": ["Percussions corporelles", "Rythme et tempo", "Lien son-mouvement"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Suivre le rythme de l'enseignant : taper mains, cuisses, pieds en écho", "role_enseignant": "Créer des rythmes simples, inviter à répéter en écho"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Explorer tous les sons possibles avec le corps. Créer un rythme de 4 temps.", "role_enseignant": "Démontrer les possibilités, aider chaque enfant"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Transformer le rythme en danse : chaque percussion devient un mouvement dans l'espace", "role_enseignant": "Encourager le mouvement, mettre une musique de fond"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Rythme de plus en plus lent et doux, finir par un battement de cœur calme", "role_enseignant": "Ralentir progressivement le tempo, guider la respiration finale"}
    ],
    "materiel": ["Aucun matériel requis"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "percussions corporelles", "maternelle"]
})

sae_list.append({
    "id": mid(19), "titre": "L'histoire sans paroles",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Mime",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants apprennent à raconter de courtes histoires uniquement avec leur corps : se réveiller le matin, manger un repas, jouer au parc.",
    "contexte_apprentissage": "L'enseignant mime des actions de la vie quotidienne et les enfants devinent. Puis chaque enfant choisit une scène à mimer.",
    "tache_complexe": "L'élève mime une scène de la vie quotidienne en 3 actions et ses camarades devinent.",
    "criteres_evaluation": ["Clarté du mime", "Expressivité des gestes", "Enchaînement logique des actions"],
    "savoirs_essentiels": ["Expression non verbale", "Séquence d'actions", "Gestes descriptifs"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu de devinettes corporelles : l'enseignant mime une action, les enfants devinent", "role_enseignant": "Mimer clairement, féliciter les bonnes réponses"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Tous ensemble, mimer des scènes guidées : se brosser les dents, manger, jouer au ballon", "role_enseignant": "Guider les mimes, insister sur l'exagération des gestes"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Chaque enfant choisit une scène et la présente en petits groupes avec devinettes", "role_enseignant": "Aider à choisir les scènes, organiser les groupes"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Mimer en ralenti l'action de se coucher et s'endormir", "role_enseignant": "Guider le ralentissement, voix douce"}
    ],
    "materiel": ["Images d'actions quotidiennes (optionnel)"],
    "espace": "Gymnase",
    "tags": ["expression", "mime", "quotidien", "maternelle"]
})

sae_list.append({
    "id": mid(20), "titre": "Statues vivantes",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse contemporaine",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants explorent le concept de la statue : se figer dans différentes poses expressives sur un thème donné (joie, peur, force, douceur).",
    "contexte_apprentissage": "L'enseignant enrichit le jeu statue/danse en demandant des poses sur des thèmes variés.",
    "tache_complexe": "L'élève se fige en statue expressive sur 4 thèmes différents annoncés par l'enseignant.",
    "criteres_evaluation": ["Immobilité complète en position", "Expression claire de l'émotion", "Variété des poses"],
    "savoirs_essentiels": ["Contrôle de l'immobilité", "Expression des émotions par le corps", "Postures variées"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Danser librement et se figer quand la musique s'arrête", "role_enseignant": "Contrôler la musique, varier les pauses"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Statues à thème : se figer en montrant la joie, la surprise, la force, la peur", "role_enseignant": "Annoncer les thèmes, démontrer, valoriser les interprétations"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Galerie de statues : la moitié fait des statues, l'autre se promène dans la galerie. Alterner.", "role_enseignant": "Organiser les groupes, guider la visite de la galerie"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Statue de la détente : la pose la plus relaxante possible en respirant", "role_enseignant": "Guider la relaxation, musique douce, bilan"}
    ],
    "materiel": ["Musique dansante", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "danse contemporaine", "statues", "maternelle"]
})

sae_list.append({
    "id": mid(21), "titre": "Les acrobates à deux",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Acrosport",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent l'acrosport en créant des figures simples à deux : dos à dos, côte à côte, un assis et un debout. Confiance, sécurité et coopération.",
    "contexte_apprentissage": "L'enseignant présente les règles de sécurité et les rôles. Les figures sont simples et au sol.",
    "tache_complexe": "L'élève réalise 3 figures simples à deux avec un partenaire en respectant les consignes de sécurité.",
    "criteres_evaluation": ["Respect des consignes de sécurité", "Coopération avec le partenaire", "Stabilité des figures"],
    "savoirs_essentiels": ["Figures acrobatiques simples à deux", "Règles de sécurité", "Confiance et coopération"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeux de confiance : se donner la main et tirer doucement, dos à dos se relever ensemble", "role_enseignant": "Former les duos, démontrer, insister sur la sécurité"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre 3 figures : la balançoire, le pont dos à dos, la tour", "role_enseignant": "Démontrer chaque figure, vérifier la sécurité, corriger"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Les duos pratiquent les 3 figures et choisissent leur préférée pour la présenter", "role_enseignant": "Superviser la sécurité, encourager la communication"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Assis dos à dos, respirer ensemble en sentant le dos du partenaire bouger", "role_enseignant": "Guider la respiration synchronisée, bilan"}
    ],
    "materiel": ["Tapis de gymnastique", "Images de figures simples"],
    "espace": "Gymnase",
    "tags": ["expression", "acrosport", "duo", "maternelle"]
})

sae_list.append({
    "id": mid(22), "titre": "La danse des couleurs",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Chaque couleur est associée à une qualité de mouvement : rouge = fort et rapide, bleu = doux et lent, jaune = léger et sautillant, vert = fluide et ondulant.",
    "contexte_apprentissage": "L'enseignant montre des cartons de couleur et les enfants associent chaque couleur à une façon de bouger.",
    "tache_complexe": "L'élève réagit correctement à 4 couleurs différentes en changeant sa qualité de mouvement.",
    "criteres_evaluation": ["Association couleur-mouvement", "Changement rapide entre les qualités", "Engagement corporel"],
    "savoirs_essentiels": ["Qualités de mouvement variées", "Réactivité aux signaux visuels", "Vocabulaire du mouvement"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Courir, marcher, sauter, ramper au signal", "role_enseignant": "Varier les consignes, observer l'énergie"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Présenter chaque couleur et sa qualité de mouvement. Pratiquer une à la fois.", "role_enseignant": "Montrer les cartons, démontrer, vérifier la compréhension"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Jeu des couleurs dansées : l'enseignant montre une couleur, les enfants dansent la qualité associée", "role_enseignant": "Varier les couleurs, augmenter le rythme des changements"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Terminer avec le bleu (doux et lent) et finir couché au sol", "role_enseignant": "Montrer le carton bleu, baisser la voix, relaxation"}
    ],
    "materiel": ["Cartons de couleur (rouge, bleu, jaune, vert)", "Musiques variées"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "couleurs", "maternelle"]
})

sae_list.append({
    "id": mid(23), "titre": "Le petit gymnaste",
    "cycle": "Maternelle", "niveau": "4-5 ans",
    "duree_periodes": 1, "duree_par_periode": "30 min",
    "moyen_action": "Gymnastique au sol",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les enfants découvrent les positions de base en gymnastique : chandelle, pont, planche, équilibre sur un pied. Gainage, souplesse et conscience posturale.",
    "contexte_apprentissage": "L'enseignant présente la gymnastique au sol comme un art du corps. Les enfants apprennent les positions de base.",
    "tache_complexe": "L'élève enchaîne 3 positions de gymnastique tenues chacune 5 secondes.",
    "criteres_evaluation": ["Alignement corporel", "Maintien de la position 5 secondes", "Effort de gainage"],
    "savoirs_essentiels": ["Positions de base en gymnastique", "Gainage et tonicité", "Alignement du corps"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Déplacements gymniques : pas chassés, galop, crabe, ours", "role_enseignant": "Démontrer les déplacements, encourager la variété"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Apprendre 4 positions : chandelle, pont, planche, flamant", "role_enseignant": "Démontrer chaque position, corriger les alignements"},
        {"phase": "Mise en action", "duree": "10 min", "activite": "Mini-enchaînement : choisir 3 positions et les enchaîner avec un déplacement entre chaque", "role_enseignant": "Encourager les enchaînements, observer les progrès"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements doux dans les positions apprises, respiration", "role_enseignant": "Guider les étirements, respiration calme, bilan"}
    ],
    "materiel": ["Tapis de gymnastique"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique au sol", "positions", "maternelle"]
})

# ============================================================
# 1er CYCLE PRIMAIRE (6-7 ans) — 23 SAÉ (EXPB-024 to EXPB-046)
# ============================================================

sae_list.append({
    "id": mid(24), "titre": "Ma première chorégraphie",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Création chorégraphique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves créent en équipe une courte chorégraphie de 16 temps sur une musique populaire. Ils apprennent les bases de la composition : début, milieu, fin.",
    "contexte_apprentissage": "L'enseignant enseigne 4 mouvements de base et les élèves les organisent dans l'ordre de leur choix.",
    "tache_complexe": "L'équipe crée et présente une chorégraphie de 16 temps utilisant au moins 4 mouvements différents.",
    "criteres_evaluation": ["Structure de la chorégraphie", "Synchronisation avec la musique", "Travail d'équipe"],
    "savoirs_essentiels": ["Structure chorégraphique simple", "Comptage musical (8 temps)", "Unisson et canon"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Réveil corporel en musique : bouger chaque partie du corps au rythme", "role_enseignant": "Guider le réveil articulaire, mettre une musique entraînante"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 mouvements de base : pas chassé, tour, saut étoile, vague de bras", "role_enseignant": "Démontrer et faire répéter, insister sur le comptage"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "En équipes de 4, organiser les mouvements, ajouter une pose de début et de fin", "role_enseignant": "Circuler entre les équipes, aider à l'organisation"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements en cercle, retour sur le travail d'équipe", "role_enseignant": "Guider les étirements, animer la discussion"}
    ],
    "materiel": ["Lecteur de musique", "Musique populaire adaptée"],
    "espace": "Gymnase",
    "tags": ["expression", "création chorégraphique", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(25), "titre": "Le mime des métiers",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Mime",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves miment différents métiers (pompier, boulanger, médecin) en utilisant des gestes précis et exagérés. Communication non verbale et précision du geste.",
    "contexte_apprentissage": "L'enseignant présente le mime comme un art de communication sans paroles. Les élèves explorent les gestes caractéristiques.",
    "tache_complexe": "L'élève mime un métier en 5 actions enchaînées et le groupe devine.",
    "criteres_evaluation": ["Précision et clarté des gestes", "Enchaînement logique", "Utilisation de l'espace imaginaire"],
    "savoirs_essentiels": ["Gestes descriptifs précis", "Manipulation d'objets imaginaires", "Communication non verbale"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu du miroir en duo : un mène, l'autre suit exactement", "role_enseignant": "Former les duos, démontrer la lenteur nécessaire"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "L'enseignant mime 3 métiers. Exercice guidé : tous miment le pompier ensemble", "role_enseignant": "Démontrer les techniques de mime, insister sur l'exagération"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Chaque élève tire un métier au hasard et prépare 5 actions. Présentations et devinettes.", "role_enseignant": "Distribuer les cartes-métiers, aider, animer les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Mimer au ralenti le métier de dormir", "role_enseignant": "Guider le mime lent, bilan"}
    ],
    "materiel": ["Cartes-métiers plastifiées"],
    "espace": "Gymnase",
    "tags": ["expression", "mime", "métiers", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(26), "titre": "Danse country pour débutants",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse folklorique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves apprennent les pas de base de la danse country en ligne : pas chassé, touche du talon, quart de tour. Coordination et plaisir de danser en groupe.",
    "contexte_apprentissage": "L'enseignant présente la danse country comme une tradition nord-américaine festive. Les pas sont enseignés un à un.",
    "tache_complexe": "L'élève exécute une chorégraphie country de 32 temps avec les 4 pas de base appris.",
    "criteres_evaluation": ["Exécution des pas de base", "Synchronisation avec la musique", "Orientation dans les quarts de tour"],
    "savoirs_essentiels": ["Pas chassé latéral", "Touche du talon et de la pointe", "Quart de tour", "Comptage musical"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marcher en rythme sur musique country, taper des mains sur le temps fort", "role_enseignant": "Mettre la musique, marquer le rythme, créer l'ambiance"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre les 4 pas un par un sans musique, puis avec musique lente", "role_enseignant": "Démontrer face au groupe, compter à voix haute, répéter"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Enchaîner les 4 pas en séquence sur la musique, augmenter la vitesse", "role_enseignant": "Danser avec le groupe, encourager, aider ceux qui sont perdus"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements doux en musique country lente", "role_enseignant": "Guider les étirements, féliciter"}
    ],
    "materiel": ["Musique country adaptée", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "danse folklorique", "country", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(27), "titre": "Les acrobates du cirque",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Acrosport",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves apprennent des figures d'acrosport à 2 et à 3 : la chaise, l'avion, la pyramide basse. Force, équilibre et coopération.",
    "contexte_apprentissage": "L'enseignant enseigne les règles de sécurité et les rôles (porteur, voltigeur, pareur) avant d'aborder les figures.",
    "tache_complexe": "L'équipe de 3 réalise un enchaînement de 3 figures tenues 3 secondes avec des transitions.",
    "criteres_evaluation": ["Respect des règles de sécurité", "Stabilité des figures (3 secondes)", "Fluidité des transitions"],
    "savoirs_essentiels": ["Rôles en acrosport", "Règles de sécurité", "Figures de base à 2 et 3"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Renforcement ludique : brouette, crabe, planche 10 secondes", "role_enseignant": "Démontrer les exercices, surveiller les positions"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Rappel sécurité. Apprendre 3 figures : la chaise, l'avion, la pyramide à 3", "role_enseignant": "Démontrer avec des élèves, assurer la parade, corriger"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "En trios, pratiquer les figures et créer un enchaînement avec entrée et sortie", "role_enseignant": "Circuler, vérifier la sécurité, aider à la composition"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements en trio, bilan coopération et confiance", "role_enseignant": "Guider les étirements, bilan"}
    ],
    "materiel": ["Tapis de gymnastique", "Fiches de figures plastifiées"],
    "espace": "Gymnase",
    "tags": ["expression", "acrosport", "figures", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(28), "titre": "Le ballon de gymnastique rythmique",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Gymnastique rythmique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves découvrent le ballon de GR : le faire rouler sur les bras, le lancer et le rattraper, le faire rebondir au rythme. Coordination et douceur du geste.",
    "contexte_apprentissage": "L'enseignant présente le ballon comme un engin qui demande douceur et précision. Exploration puis apprentissage des manipulations.",
    "tache_complexe": "L'élève réalise une séquence de 4 manipulations différentes avec le ballon en musique.",
    "criteres_evaluation": ["Douceur et contrôle", "Variété des manipulations", "Coordination avec la musique"],
    "savoirs_essentiels": ["Rouler le ballon sur le corps", "Lancer et rattraper", "Rebond contrôlé"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Exploration libre du ballon : rouler, lancer, rattraper, tourner", "role_enseignant": "Distribuer les ballons, encourager l'exploration"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 manipulations : rouler sur les bras, lancer-rattraper, rebond au sol, équilibre sur une main", "role_enseignant": "Démontrer, circuler pour corriger, insister sur la douceur"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Créer une séquence de 4 manipulations en musique. Pratiquer et présenter.", "role_enseignant": "Aider à l'enchaînement, mettre la musique, organiser les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Rouler le ballon lentement sur chaque partie du corps en respirant", "role_enseignant": "Guider la relaxation, ranger, bilan"}
    ],
    "materiel": ["Ballons de GR (1 par élève)", "Musique classique douce"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique rythmique", "ballon", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(29), "titre": "La danse des émotions",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse contemporaine",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves explorent comment le corps exprime les émotions : joie (mouvements légers et hauts), tristesse (lourds et bas), colère (saccadés), peur (rapides et petits).",
    "contexte_apprentissage": "L'enseignant utilise des musiques évocatrices pour déclencher des émotions traduites en mouvement dansé.",
    "tache_complexe": "L'élève danse 3 émotions différentes avec des qualités de mouvement clairement contrastées.",
    "criteres_evaluation": ["Différenciation claire des émotions", "Utilisation des qualités de mouvement", "Engagement expressif"],
    "savoirs_essentiels": ["Qualités de mouvement et émotions", "Niveaux d'espace liés aux émotions", "Intensité et énergie"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marcher en exprimant l'émotion annoncée avec le visage et le corps", "role_enseignant": "Annoncer les émotions, observer, encourager l'exagération"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Explorer chaque émotion en mouvement avec la musique appropriée", "role_enseignant": "Guider avec la musique, démontrer les qualités, questionner"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "En petits groupes, créer une histoire en 3 émotions et la danser", "role_enseignant": "Aider à structurer, fournir les musiques, observer"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Émotion du calme : mouvements très lents, respiration, yeux fermés", "role_enseignant": "Guider la relaxation, bilan sur les émotions vécues"}
    ],
    "materiel": ["Musiques évocatrices (4 ambiances)", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "danse contemporaine", "émotions", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(30), "titre": "La roulade et l'enchaînement",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Gymnastique au sol",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves perfectionnent la roulade avant et arrière puis les intègrent dans un mini-enchaînement gymnique avec équilibre et souplesse.",
    "contexte_apprentissage": "Ateliers progressifs pour chaque élève avance à son rythme dans la maîtrise des roulades et de l'enchaînement.",
    "tache_complexe": "L'élève réalise un enchaînement de 4 éléments incluant au moins une roulade, un équilibre et une position de souplesse.",
    "criteres_evaluation": ["Technique de la roulade", "Fluidité de l'enchaînement", "Variété des éléments"],
    "savoirs_essentiels": ["Roulade avant et arrière", "Équilibre statique", "Enchaînement gymnique"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Déplacements gymniques : pas chassés, galop, demi-pointes, crabe", "role_enseignant": "Varier les déplacements, préparer les articulations"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Ateliers tournants : roulade avant sur plan incliné, sur plat, roulade arrière guidée, équilibre", "role_enseignant": "Assurer la parade, corriger les techniques, adapter"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Composer un mini-enchaînement : 4 éléments avec une pose de début et de fin", "role_enseignant": "Aider à la composition, encourager la fluidité"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements spécifiques : dos, cou, jambes, poignets", "role_enseignant": "Guider les étirements, rétroactions positives"}
    ],
    "materiel": ["Tapis de gymnastique", "Plan incliné"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique au sol", "roulades", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(31), "titre": "Hip-hop des petits",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Danse hip-hop / moderne",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves apprennent les mouvements de base du hip-hop adaptés : bounce, step touch, bras de robot, freeze. Ils créent une courte routine en équipe.",
    "contexte_apprentissage": "L'enseignant présente le hip-hop comme une danse urbaine. Les mouvements sont simplifiés pour les jeunes.",
    "tache_complexe": "L'équipe présente une routine hip-hop de 24 temps utilisant au moins 4 mouvements appris.",
    "criteres_evaluation": ["Exécution des mouvements de base", "Rythme et énergie", "Synchronisation en équipe"],
    "savoirs_essentiels": ["Bounce", "Step touch", "Isolation tête et bras", "Freeze"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Bouncer en rythme sur la musique hip-hop, bras libres", "role_enseignant": "Mettre la musique, démontrer le bounce, créer l'ambiance"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 mouvements : bounce, step touch, bras robot, freeze en position cool", "role_enseignant": "Démontrer face au groupe, répéter lentement puis en rythme"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "En équipes de 4-5, créer une routine de 24 temps avec un freeze final", "role_enseignant": "Circuler, aider à compter, encourager la créativité"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements en musique R&B douce, discussion", "role_enseignant": "Guider les étirements, recueillir les impressions"}
    ],
    "materiel": ["Musique hip-hop adaptée à l'âge", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "hip-hop", "danse urbaine", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(32), "titre": "Le théâtre des ombres",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Expression corporelle",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves créent des formes et des histoires avec leurs ombres projetées sur un drap blanc. Ils explorent les effets de taille et les formes corporelles surprenantes.",
    "contexte_apprentissage": "L'enseignant installe un projecteur et un drap. Les élèves découvrent que leur corps peut créer des images en ombres chinoises.",
    "tache_complexe": "L'équipe de 3 crée une courte scène en ombres chinoises avec un début, un événement et une fin.",
    "criteres_evaluation": ["Créativité des formes", "Utilisation de la distance au projecteur", "Histoire claire"],
    "savoirs_essentiels": ["Projection d'ombre et distance", "Formes corporelles expressives", "Narration sans paroles"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Explorer les formes que peut faire son corps : grand, petit, large, mince", "role_enseignant": "Proposer les consignes de formes, observer la variété"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Passer derrière le drap et découvrir son ombre. Explorer les effets de distance.", "role_enseignant": "Gérer le passage, montrer les effets, encourager l'exploration"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "En trios, créer une histoire en ombres. Répéter et présenter.", "role_enseignant": "Aider à la création, gérer le temps, animer les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Deviner les formes d'ombres faites par l'enseignant, étirements", "role_enseignant": "Créer des ombres, bilan amusant, ranger"}
    ],
    "materiel": ["Drap blanc", "Projecteur ou lampe puissante"],
    "espace": "Gymnase",
    "tags": ["expression", "expression corporelle", "ombres", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(33), "titre": "La danse africaine",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse folklorique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves découvrent les rythmes et mouvements de la danse africaine traditionnelle : pieds ancrés au sol, ondulations du torse, bras puissants. Ouverture culturelle par le mouvement.",
    "contexte_apprentissage": "L'enseignant situe la danse africaine dans son contexte culturel et enseigne des pas de base inspirés d'Afrique de l'Ouest.",
    "tache_complexe": "L'élève exécute une séquence de 8 temps de danse africaine en rythme avec les percussions.",
    "criteres_evaluation": ["Ancrage au sol", "Mouvement du torse et des bras", "Synchronisation avec les percussions"],
    "savoirs_essentiels": ["Rythmes africains de base", "Ancrage au sol", "Mouvements du torse", "Contexte culturel"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marcher en rythme sur percussions africaines, ajouter des frappes de pieds", "role_enseignant": "Mettre la musique, démontrer l'ancrage, créer l'énergie"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 mouvements : pas ancré, ondulation du torse, bras en rythme, tour avec frappe", "role_enseignant": "Démontrer lentement, expliquer le contexte culturel, répéter"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Danser ensemble en cercle la séquence complète. Accélérer progressivement.", "role_enseignant": "Danser au centre, maintenir l'énergie, encourager l'expression"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Ralentir les percussions, cercle assis pour un partage culturel", "role_enseignant": "Guider le ralentissement, animer la discussion, bilan"}
    ],
    "materiel": ["Musique de percussions africaines", "Djembé (optionnel)"],
    "espace": "Gymnase",
    "tags": ["expression", "danse folklorique", "africaine", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(34), "titre": "Jonglerie à 2 foulards",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Cirque",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves progressent en jonglerie avec 2 foulards simultanément. Ils apprennent le lancer alterné (cascade) et développent la coordination bilatérale.",
    "contexte_apprentissage": "Progression par étapes pour arriver à jongler avec 2 foulards en cascade.",
    "tache_complexe": "L'élève jongle en cascade avec 2 foulards pendant 10 lancers consécutifs.",
    "criteres_evaluation": ["Lancer alterné droite/gauche", "Hauteur régulière", "Nombre de lancers consécutifs"],
    "savoirs_essentiels": ["Cascade à 2 objets", "Coordination bilatérale", "Rythme de lancer"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Révision : lancer-rattraper 1 foulard d'une main à l'autre, 10 fois chaque côté", "role_enseignant": "Distribuer les foulards, vérifier la technique de base"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Un foulard dans chaque main, lancer le droit, quand il est au sommet, lancer le gauche", "role_enseignant": "Démontrer au ralenti, décomposer les étapes, circuler"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Pratiquer la cascade continue. Défi : 4, 6, 8, puis 10 lancers", "role_enseignant": "Encourager, célébrer les records, proposer des défis adaptés"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Lancer les 2 foulards très haut et les regarder descendre. Étirements poignets.", "role_enseignant": "Guider les étirements, bilan sur les progrès, ranger"}
    ],
    "materiel": ["Foulards légers (2 par élève)", "Musique de cirque en fond"],
    "espace": "Gymnase",
    "tags": ["expression", "cirque", "jonglerie", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(35), "titre": "Yoga aventure",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Relaxation créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Une aventure imaginaire en enchaînant des postures de yoga : traverser la rivière (guerrier), escalader la montagne (triangle), voler comme un aigle. Souplesse, force et calme intérieur.",
    "contexte_apprentissage": "L'enseignant raconte une histoire d'aventure et chaque étape correspond à une posture de yoga.",
    "tache_complexe": "L'élève enchaîne 6 postures de yoga en suivant l'histoire, maintenant chacune 5 respirations.",
    "criteres_evaluation": ["Alignement dans les postures", "Respiration contrôlée", "Transitions fluides"],
    "savoirs_essentiels": ["Postures de yoga intermédiaires", "Respiration yogique", "Concentration et calme"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Salutation au soleil simplifiée : 3 répétitions lentes", "role_enseignant": "Démontrer, compter les respirations, vérifier les alignements"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 6 postures : guerrier I, triangle, aigle, arbre, cobra, enfant", "role_enseignant": "Enseigner une posture à la fois, corriger, utiliser des images"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "L'aventure yoga : suivre l'histoire en enchaînant les postures apprises", "role_enseignant": "Raconter de manière engageante, maintenir le rythme, observer"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Posture de l'enfant puis shavasana avec visualisation guidée", "role_enseignant": "Guider la relaxation finale, voix très calme, musique zen"}
    ],
    "materiel": ["Tapis de sol", "Musique zen", "Images de postures"],
    "espace": "Gymnase",
    "tags": ["expression", "relaxation créative", "yoga", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(36), "titre": "Les rubans en mouvement",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Gymnastique rythmique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves approfondissent les manipulations du ruban : spirales, serpentins, grands cercles, lancers. Ils créent un enchaînement individuel de 4 figures avec déplacement.",
    "contexte_apprentissage": "L'enseignant enseigne les figures de base puis les élèves composent leur propre enchaînement en musique.",
    "tache_complexe": "L'élève présente un enchaînement de 4 figures de ruban avec déplacement en musique.",
    "criteres_evaluation": ["Amplitude et fluidité des figures", "Déplacement dans l'espace", "Enchaînement sans interruption"],
    "savoirs_essentiels": ["Spirale verticale et horizontale", "Serpentin", "Grand cercle", "Lancer court"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Mouvements amples des bras sans ruban : grands cercles, vagues, huit", "role_enseignant": "Préparer les épaules et poignets, démontrer l'amplitude"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 figures avec le ruban : spirale, serpentin, grand cercle, lancer court", "role_enseignant": "Démontrer chaque figure, circuler pour corriger la technique"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Créer un enchaînement de 4 figures en se déplaçant. Pratiquer et présenter.", "role_enseignant": "Aider à la composition, varier les musiques, organiser les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Faire danser le ruban lentement en respirant, puis l'enrouler doucement", "role_enseignant": "Guider la relaxation, ranger les rubans, bilan"}
    ],
    "materiel": ["Rubans de GR (1 par élève)", "Musiques variées"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique rythmique", "ruban", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(37), "titre": "Danse créative — les éléments",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves explorent les 4 éléments naturels (eau, feu, terre, air) par le mouvement. Chaque élément propose des qualités de mouvement distinctes.",
    "contexte_apprentissage": "L'enseignant associe chaque élément à des qualités de mouvement et utilise des musiques évocatrices.",
    "tache_complexe": "L'élève crée une danse de 16 temps utilisant 2 éléments contrastants avec des transitions claires.",
    "criteres_evaluation": ["Différenciation des qualités entre les éléments", "Créativité", "Engagement"],
    "savoirs_essentiels": ["Qualités de mouvement par élément", "Contrastes et transitions", "Créativité motrice"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Se déplacer en changeant de qualité au signal : fluide, explosif, lourd, léger", "role_enseignant": "Donner les signaux, observer, encourager la variété"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Explorer chaque élément : eau (vagues), feu (explosions), terre (lenteur), air (légèreté)", "role_enseignant": "Guider l'exploration, démontrer, questionner"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Choisir 2 éléments et créer une danse qui passe de l'un à l'autre", "role_enseignant": "Aider à la création, fournir les musiques, organiser les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Devenir l'eau calme d'un lac : mouvements très lents, respiration comme des vagues", "role_enseignant": "Guider la relaxation, musique de vagues, bilan"}
    ],
    "materiel": ["Musiques évocatrices des 4 éléments", "Foulards (optionnel)"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "éléments", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(38), "titre": "Le conte en mouvement",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Mime",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves mettent en scène un conte connu uniquement par le mouvement et le mime, sans paroles. Travail d'équipe pour raconter l'histoire avec leur corps.",
    "contexte_apprentissage": "L'enseignant rappelle un conte connu et guide les élèves à identifier les moments clés.",
    "tache_complexe": "L'équipe présente le conte en 5 scènes mimées, avec des personnages clairement identifiables.",
    "criteres_evaluation": ["Clarté des personnages", "Enchaînement logique de l'histoire", "Expression corporelle riche"],
    "savoirs_essentiels": ["Caractérisation de personnages", "Narration non verbale", "Travail d'équipe scénique"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Jeu de transformation : passer d'un personnage à l'autre au signal", "role_enseignant": "Annoncer les personnages, observer, encourager l'expression"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Choisir le conte, identifier les 5 scènes clés, distribuer les rôles", "role_enseignant": "Guider le choix, aider à identifier les scènes, proposer des mouvements"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Répéter les 5 scènes avec musique. Travailler les transitions.", "role_enseignant": "Diriger les répétitions, donner des rétroactions, gérer la musique"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Les personnages s'endorment un à un, relaxation guidée", "role_enseignant": "Guider la relaxation, bilan et préparation des présentations"}
    ],
    "materiel": ["Musiques d'ambiance variées", "Accessoires simples (foulard, chapeau)"],
    "espace": "Gymnase",
    "tags": ["expression", "mime", "conte", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(39), "titre": "Les équilibristes sur poutre",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Gymnastique au sol",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves explorent la poutre basse avec des déplacements variés, des positions d'équilibre et un demi-tour. Équilibre dynamique et confiance.",
    "contexte_apprentissage": "Ateliers progressifs de la ligne au sol à la poutre basse, chacun progresse à son rythme.",
    "tache_complexe": "L'élève traverse la poutre avec 3 actions différentes : un déplacement, un équilibre et un demi-tour.",
    "criteres_evaluation": ["Fluidité de la traversée", "Maintien de l'équilibre", "Variété des actions"],
    "savoirs_essentiels": ["Équilibre dynamique sur surface étroite", "Regard fixe devant soi", "Déplacements variés en hauteur"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marche sur les lignes du gymnase : en avant, en arrière, sur les pointes", "role_enseignant": "Varier les déplacements, observer l'équilibre, préparer les chevilles"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Ateliers : marche sur ligne, marche sur poutre basse, équilibre sur un pied, demi-tour", "role_enseignant": "Installer les ateliers, assurer la parade, encourager le regard droit"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Composer une traversée de poutre avec 3 actions. Pratiquer et présenter.", "role_enseignant": "Aider à la composition, parade, valoriser les progrès"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Équilibre les yeux fermés sur le sol, étirements", "role_enseignant": "Guider l'exercice, étirements, bilan"}
    ],
    "materiel": ["Poutre basse", "Tapis de réception"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique au sol", "poutre", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(40), "titre": "Danse contemporaine — les niveaux",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse contemporaine",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves explorent les 3 niveaux de l'espace : bas (au sol), moyen (debout), haut (sauts). Ils créent des phrases de mouvement intégrant les changements de niveau.",
    "contexte_apprentissage": "L'enseignant présente les niveaux comme des zones d'exploration et guide les élèves à travers chaque niveau.",
    "tache_complexe": "L'élève crée une phrase de mouvement de 16 temps intégrant les 3 niveaux avec des transitions fluides.",
    "criteres_evaluation": ["Utilisation claire des 3 niveaux", "Fluidité des transitions", "Originalité"],
    "savoirs_essentiels": ["Niveaux d'espace : bas, moyen, haut", "Transitions entre les niveaux", "Phrase de mouvement"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Suivre les consignes : haut (sur pointe), moyen (debout), bas (accroupi)", "role_enseignant": "Annoncer les niveaux, varier le rythme"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Explorer chaque niveau : au sol (rouler, ramper), moyen (marcher, tourner), haut (sauter, s'étirer)", "role_enseignant": "Guider l'exploration, donner des exemples, encourager"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Créer une phrase de 16 temps passant par les 3 niveaux. Pratiquer et présenter.", "role_enseignant": "Aider à structurer, fournir musique contemporaine, organiser les présentations"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Du niveau haut, descendre lentement au niveau bas comme la neige qui fond", "role_enseignant": "Guider la descente progressive, musique douce, bilan"}
    ],
    "materiel": ["Musique de danse contemporaine"],
    "espace": "Gymnase",
    "tags": ["expression", "danse contemporaine", "niveaux", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(41), "titre": "Les acrobaties du cirque",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Cirque",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves explorent les acrobaties de base du cirque : roulades, chandelle, pont, roue simplifiée. Ils les combinent dans un numéro avec entrée et sortie.",
    "contexte_apprentissage": "L'enseignant crée une ambiance de cirque et propose des ateliers de pratique des acrobaties adaptées.",
    "tache_complexe": "L'élève présente un numéro de 30 secondes incluant une entrée, 3 acrobaties et un salut final.",
    "criteres_evaluation": ["Exécution technique", "Présentation artistique", "Enchaînement fluide"],
    "savoirs_essentiels": ["Acrobaties de base", "Présentation scénique", "Enchaînement acrobatique"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Échauffement de cirque : galops, sauts de chat, roulades libres", "role_enseignant": "Créer l'ambiance cirque, superviser les roulades"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Ateliers : roulade avant, chandelle, pont, roue contre le mur", "role_enseignant": "Assurer la parade, corriger, adapter les exercices"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Composer un numéro : 3 acrobaties, entrée de scène et salut final en musique", "role_enseignant": "Aider à la composition, mettre la musique, encourager"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements de gymnastes, bilan du cours", "role_enseignant": "Guider les étirements, féliciter les efforts"}
    ],
    "materiel": ["Tapis de gymnastique", "Musique de cirque"],
    "espace": "Gymnase",
    "tags": ["expression", "cirque", "acrobaties", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(42), "titre": "La danse du Québec",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse folklorique",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves découvrent les danses traditionnelles québécoises : set carré simplifié, gigue de base. Fierté culturelle et coordination en groupe.",
    "contexte_apprentissage": "L'enseignant présente le patrimoine folklorique québécois. Les pas sont simplifiés pour le niveau.",
    "tache_complexe": "L'élève participe à un set carré simplifié de 32 temps en exécutant les 4 figures de base.",
    "criteres_evaluation": ["Exécution des pas de base", "Coordination avec le groupe", "Plaisir et engagement"],
    "savoirs_essentiels": ["Pas de gigue simplifié", "Figures de set carré", "Tradition dansée québécoise"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Taper des pieds en rythme sur de la musique trad québécoise", "role_enseignant": "Mettre la musique, démontrer le tap, créer l'ambiance festive"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 figures : promenade, moulin, balancez, chaîne", "role_enseignant": "Démontrer, appeler les figures, répéter avec patience"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Former des groupes de 8 et danser les figures enchaînées en musique trad", "role_enseignant": "Appeler les figures, encourager, aider les groupes, danser avec eux"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Ronde chantée douce, étirements, discussion sur les traditions", "role_enseignant": "Enseigner la chanson, guider les étirements, valoriser le patrimoine"}
    ],
    "materiel": ["Musique trad québécoise", "Lecteur de musique"],
    "espace": "Gymnase",
    "tags": ["expression", "danse folklorique", "québécoise", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(43), "titre": "Relaxation par le mouvement",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Relaxation créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Techniques de relaxation active : mouvements en tai-chi simplifié, respiration avec mouvement des bras, visualisation guidée. Gestion du stress et conscience corporelle.",
    "contexte_apprentissage": "L'enseignant guide les élèves à travers des mouvements lents et conscients, combinant respiration et déplacement.",
    "tache_complexe": "L'élève exécute une séquence de 4 mouvements de relaxation en contrôlant sa respiration.",
    "criteres_evaluation": ["Lenteur et contrôle du mouvement", "Coordination mouvement-respiration", "Calme et concentration"],
    "savoirs_essentiels": ["Respiration consciente", "Mouvements lents contrôlés", "Visualisation guidée"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Marche très lente, sentir chaque pied se poser au sol", "role_enseignant": "Créer une ambiance calme, parler doucement"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Apprendre 4 mouvements inspirés du tai-chi : pousser l'eau, caresser la crinière, l'arbre dans le vent, la grue", "role_enseignant": "Démontrer lentement, guider la respiration"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Enchaîner les 4 mouvements en boucle avec visualisation", "role_enseignant": "Guider la visualisation, maintenir le rythme lent"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Couché au sol, scan corporel guidé de la tête aux pieds", "role_enseignant": "Guider le scan corporel, voix très douce, bilan calme"}
    ],
    "materiel": ["Musique zen/nature", "Tapis de sol (optionnel)"],
    "espace": "Gymnase",
    "tags": ["expression", "relaxation créative", "tai-chi", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(44), "titre": "Danse à la corde",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Danse créative",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Les élèves combinent le saut à la corde avec des éléments de danse : sauts variés, tours, croisements, le tout en rythme sur de la musique.",
    "contexte_apprentissage": "L'enseignant montre que la corde peut devenir un outil d'expression artistique avec rythme et créativité.",
    "tache_complexe": "L'élève exécute une séquence de 4 sauts différents à la corde en rythme avec la musique.",
    "criteres_evaluation": ["Variété des sauts", "Rythme avec la musique", "Fluidité de l'enchaînement"],
    "savoirs_essentiels": ["Sauts variés à la corde", "Coordination rythme-mouvement", "Enchaînement fluide"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Sauts sans corde au rythme de la musique : pieds joints, un pied, alterné", "role_enseignant": "Mettre la musique, démontrer les sauts, préparer les chevilles"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Avec la corde : saut de base, sur un pied, croisement des bras, demi-tour", "role_enseignant": "Distribuer les cordes, démontrer chaque saut, circuler"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Créer une routine de 4 sauts enchaînés en musique", "role_enseignant": "Aider à la composition, mettre des musiques entraînantes"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Sauts très lents puis étirements des mollets et chevilles", "role_enseignant": "Guider les étirements, ranger, bilan"}
    ],
    "materiel": ["Cordes à sauter (1 par élève)", "Musiques rythmées"],
    "espace": "Gymnase",
    "tags": ["expression", "danse créative", "corde à sauter", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(45), "titre": "L'appui renversé contre le mur",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 2, "duree_par_periode": "45 min",
    "moyen_action": "Gymnastique au sol",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Progression vers l'appui tendu renversé (ATR) contre le mur. Gainage, force des bras et confiance à être la tête en bas.",
    "contexte_apprentissage": "Ateliers progressifs : appuis faciaux, montées de pieds au mur, brouette et trépied.",
    "tache_complexe": "L'élève réalise un ATR contre le mur tenu 5 secondes avec le corps aligné.",
    "criteres_evaluation": ["Placement des mains", "Alignement du corps", "Gainage et contrôle"],
    "savoirs_essentiels": ["ATR progressif", "Gainage ventral et dorsal", "Sécurité en inversion"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Renforcement : pompes sur les genoux, planche 15 sec, cercles de poignets", "role_enseignant": "Démontrer, insister sur l'échauffement des poignets"},
        {"phase": "Apprentissage", "duree": "15 min", "activite": "Ateliers : brouette, trépied, monter les pieds au mur en reculant les mains", "role_enseignant": "Installer les ateliers, assurer la parade, adapter"},
        {"phase": "Mise en action", "duree": "20 min", "activite": "Pratiquer l'ATR avec parade. Tenir 3 puis 5 secondes.", "role_enseignant": "Assurer la parade, corriger l'alignement, encourager"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements poignets, épaules, dos. Position de l'enfant pour relâcher.", "role_enseignant": "Guider les étirements, bilan, conseils"}
    ],
    "materiel": ["Tapis de gymnastique contre le mur"],
    "espace": "Gymnase",
    "tags": ["expression", "gymnastique au sol", "appui renversé", "1er cycle primaire"]
})

sae_list.append({
    "id": mid(46), "titre": "Le parcours d'expression",
    "cycle": "1er cycle primaire", "niveau": "6-7 ans",
    "duree_periodes": 1, "duree_par_periode": "45 min",
    "moyen_action": "Expression corporelle",
    "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
    "description": "Parcours avec 5 stations d'expression différente : mime d'un animal, danse libre, posture yoga, figure acrobatique, jonglerie. Un tour complet des arts expressifs.",
    "contexte_apprentissage": "L'enseignant installe 5 stations dans le gymnase. Les élèves passent de l'une à l'autre en développant différentes compétences.",
    "tache_complexe": "L'élève complète les 5 stations en démontrant une compétence dans chaque domaine.",
    "criteres_evaluation": ["Engagement dans chaque station", "Variété des réponses motrices", "Autonomie"],
    "savoirs_essentiels": ["Diversité des moyens d'expression", "Autonomie dans les tâches", "Adaptation aux consignes"],
    "progression": [
        {"phase": "Échauffement", "duree": "5 min", "activite": "Échauffement complet : articulaire, cardio léger, étirements dynamiques", "role_enseignant": "Guider l'échauffement, préparer le corps"},
        {"phase": "Apprentissage", "duree": "10 min", "activite": "Présenter les 5 stations et démontrer ce qui est attendu", "role_enseignant": "Expliquer chaque station, répondre aux questions, former les groupes"},
        {"phase": "Mise en action", "duree": "25 min", "activite": "Rotation aux 5 stations (5 min chacune) : mime, danse, yoga, acrosport, jonglerie", "role_enseignant": "Circuler entre les stations, gérer le temps, encourager, sécurité"},
        {"phase": "Retour au calme", "duree": "5 min", "activite": "Cercle de partage : chaque élève dit sa station préférée. Étirements.", "role_enseignant": "Animer le cercle, valoriser, ranger le matériel"}
    ],
    "materiel": ["Cartes-consignes par station", "Foulards", "Tapis", "Musique variée"],
    "espace": "Gymnase",
    "tags": ["expression", "expression corporelle", "parcours", "1er cycle primaire"]
})

# ============================================================
# 2e CYCLE PRIMAIRE (8-9 ans) — 23 SAÉ (EXPB-047 to EXPB-069)
# ============================================================

cycle2_data = [
    (47, "Chorégraphie en canon", "Création chorégraphique", 2, "45 min",
     "Les élèves apprennent le procédé du canon en danse : un groupe commence un mouvement, l'autre le reprend en décalé. Ils créent une chorégraphie intégrant canon et unisson.",
     "L'équipe crée une chorégraphie de 32 temps utilisant au moins un passage en canon et un passage en unisson.",
     ["Compréhension du canon et de l'unisson", "Synchronisation musicale", "Coopération et écoute"],
     ["Canon dansé", "Unisson", "Structure chorégraphique", "Comptage des temps"]),
    (48, "Mime narratif — les aventures", "Mime", 1, "45 min",
     "Les élèves créent en équipe un court récit mimé de 2 minutes avec personnages, péripétie et dénouement. Expression théâtrale approfondie.",
     "L'équipe présente un récit mimé de 2 minutes avec 3 personnages distincts et un rebondissement.",
     ["Clarté de la narration", "Caractérisation des personnages", "Expression faciale et corporelle"],
     ["Caractérisation physique de personnages", "Narration non verbale structurée", "Espace scénique"]),
    (49, "Danses du monde — l'Inde", "Danse folklorique", 1, "45 min",
     "Les élèves découvrent la danse bollywood simplifiée : mudras (gestes des mains), mouvements de tête et de hanches, énergie festive. Ouverture culturelle internationale.",
     "L'élève exécute une séquence de 16 temps de danse bollywood avec les mudras et les déplacements appris.",
     ["Exécution des mudras", "Coordination tête-mains-hanches", "Énergie et expressivité"],
     ["Mudras de base", "Mouvements de la danse indienne", "Contexte culturel indien"]),
    (50, "Pyramides d'acrosport", "Acrosport", 2, "45 min",
     "Les élèves construisent des pyramides à 4-5 personnes en appliquant les principes de sécurité : porteurs stables, voltigeurs légers, pareurs présents. Coopération avancée.",
     "L'équipe de 5 réalise 2 pyramides différentes tenues 5 secondes avec transitions sécuritaires.",
     ["Stabilité de la pyramide 5 secondes", "Respect des règles de sécurité", "Communication dans l'équipe"],
     ["Pyramides à 4-5", "Principes biomécaniques de base", "Communication verbale de sécurité"]),
    (51, "Le ruban en chorégraphie", "Gymnastique rythmique", 1, "45 min",
     "Les élèves créent un enchaînement de GR au ruban incluant des figures variées, des changements de main et des déplacements en musique. Travail individuel vers une présentation artistique.",
     "L'élève présente un enchaînement de 30 secondes au ruban avec au moins 5 figures et un changement de main.",
     ["Variété des figures", "Fluidité et amplitude", "Changement de main réussi"],
     ["Figures avancées au ruban", "Changement de main", "Composition individuelle"]),
    (52, "La roue et la rondade", "Gymnastique au sol", 2, "45 min",
     "Les élèves apprennent la roue latérale puis s'initient à la rondade. Ateliers progressifs avec parade et surfaces adaptées.",
     "L'élève réalise une roue latérale avec les bras tendus et les jambes passant par la verticale.",
     ["Passage par la verticale", "Bras tendus pendant la roue", "Réception stable"],
     ["Roue latérale", "Rondade (initiation)", "Appui sur les mains en mouvement"]),
    (53, "Freestyle dansé", "Danse hip-hop / moderne", 2, "45 min",
     "Les élèves apprennent des mouvements de breakdance adaptés (top rock, indian step) et le concept de freestyle : improviser sur la musique dans un cercle de danse.",
     "L'élève improvise 16 temps de freestyle hip-hop dans le cercle de danse en utilisant au moins 3 mouvements appris.",
     ["Variété des mouvements", "Rythme et musicalité", "Confiance dans l'improvisation"],
     ["Top rock", "Indian step", "Freestyle et improvisation", "Cercle de danse"]),
    (54, "Le cirque jonglé — balles", "Cirque", 1, "45 min",
     "Les élèves passent aux balles de jonglerie (2 balles). Ils apprennent l'échange, la colonne et le début de la cascade. Progression méthodique.",
     "L'élève réalise 10 échanges consécutifs avec 2 balles de jonglerie.",
     ["Lancer régulier en hauteur", "Échange alterné droite-gauche", "Rythme constant"],
     ["Jonglerie à 2 balles", "Cascade débutant", "Colonne à 2 balles"]),
    (55, "Danse contemporaine — le contact", "Danse contemporaine", 1, "45 min",
     "Les élèves explorent le contact improvisation : donner et recevoir le poids, points de contact (dos, épaule, main), se déplacer en maintenant un contact corporel avec un partenaire.",
     "L'élève improvise 30 secondes de contact danse avec un partenaire en maintenant au moins 2 points de contact différents.",
     ["Écoute du partenaire", "Fluidité dans le contact", "Variété des points de contact"],
     ["Points de contact corporels", "Don et réception du poids", "Improvisation en duo"]),
    (56, "Création d'un spectacle de cirque", "Cirque", 2, "45 min",
     "Les élèves combinent jonglerie, acrobatie et équilibre dans un numéro de cirque de groupe. Ils apprennent à structurer un spectacle avec entrée, numéros et finale.",
     "Le groupe présente un spectacle de cirque de 3 minutes avec au moins 3 disciplines différentes.",
     ["Variété des disciplines", "Structure du spectacle", "Transitions entre les numéros"],
     ["Organisation d'un spectacle", "Combinaison de disciplines", "Présentation scénique"]),
    (57, "Expression corporelle — les machines", "Expression corporelle", 1, "45 min",
     "Les élèves créent en groupe une machine humaine : chaque élève est un rouage qui fait un mouvement répétitif et un son. La machine se met en marche progressivement.",
     "Le groupe de 6 crée une machine humaine fonctionnelle avec 6 rouages interconnectés, sons et mouvements synchronisés.",
     ["Connexion entre les rouages", "Régularité du mouvement répétitif", "Coordination sonore"],
     ["Mouvement répétitif synchronisé", "Travail de groupe", "Rythme et sons"]),
    (58, "Danse créative — la musique nous guide", "Danse créative", 1, "45 min",
     "Les élèves apprennent à écouter différents styles musicaux et à adapter leur danse : rythme, énergie, ambiance. Ils développent la musicalité corporelle.",
     "L'élève improvise librement sur 3 styles musicaux différents en adaptant clairement ses mouvements à chaque style.",
     ["Adaptation au style musical", "Variété des réponses motrices", "Écoute musicale active"],
     ["Musicalité corporelle", "Styles musicaux", "Improvisation dirigée"]),
    (59, "Yoga en duo", "Relaxation créative", 1, "45 min",
     "Les élèves pratiquent des postures de yoga à deux : l'arbre en duo, le bateau face à face, la chaise dos à dos. Confiance, communication et équilibre partagé.",
     "L'élève réalise 4 postures de yoga en duo avec maintien de 5 respirations chacune.",
     ["Stabilité en duo", "Communication avec le partenaire", "Respiration synchronisée"],
     ["Postures de yoga en duo", "Équilibre partagé", "Respiration synchronisée"]),
    (60, "Enchaînement gymnique complet", "Gymnastique au sol", 2, "45 min",
     "Les élèves composent un enchaînement gymnique personnel de 45 secondes incluant roulade, roue ou ATR, équilibre et souplesse. Évaluation formative intégrée.",
     "L'élève présente un enchaînement de 45 secondes incluant au moins 5 éléments techniques variés.",
     ["Variété des éléments techniques", "Fluidité et élégance", "Début et fin marqués"],
     ["Composition gymnique", "Éléments techniques variés", "Présentation artistique"]),
    (61, "Le cerceau en mouvement", "Gymnastique rythmique", 1, "45 min",
     "Manipulation avancée du cerceau : rotations autour du corps, lancer et rattraper, rouler au sol et récupérer, passage à travers le cerceau.",
     "L'élève réalise un enchaînement de 5 manipulations de cerceau avec déplacement.",
     ["Contrôle et précision", "Variété des manipulations", "Déplacement fluide"],
     ["Rotations du cerceau", "Lancer-rattraper", "Passage à travers"]),
    (62, "Danse hip-hop — les battles", "Danse hip-hop / moderne", 1, "45 min",
     "Les élèves apprennent le concept du battle de danse : un danseur entre dans le cercle, montre ses meilleurs mouvements, puis cède la place. Respect, créativité et confiance en soi.",
     "L'élève réalise un passage de 8 temps dans le cercle de battle avec au moins 2 mouvements originaux.",
     ["Originalité des mouvements", "Confiance et présence scénique", "Respect des autres danseurs"],
     ["Culture du battle", "Présence scénique", "Respect et fair-play"]),
    (63, "Mime à thème — les sports", "Mime", 1, "45 min",
     "Les élèves miment différents sports en exagérant les actions caractéristiques : le hockey, le soccer, la natation, le basketball. Développement de la précision gestuelle.",
     "L'élève mime 3 sports différents avec des actions précises et reconnaissables.",
     ["Précision des gestes sportifs", "Exagération théâtrale", "Utilisation de l'espace"],
     ["Mime de mouvements sportifs", "Exagération contrôlée", "Communication visuelle"]),
    (64, "Danses du monde — le Brésil", "Danse folklorique", 1, "45 min",
     "Les élèves découvrent la samba brésilienne simplifiée : pas de base avec les hanches, mouvement des bras, rythme festif des percussions.",
     "L'élève exécute le pas de base de la samba pendant 32 temps en maintenant le mouvement des hanches et des bras.",
     ["Rythme des hanches", "Coordination pieds-bras", "Énergie festive"],
     ["Pas de base samba", "Mouvement des hanches", "Culture brésilienne"]),
    (65, "Création d'un mini-spectacle dansé", "Création chorégraphique", 2, "45 min",
     "Les élèves créent en équipe un mini-spectacle de danse de 2 minutes intégrant au moins 2 styles de danse appris. Formation, transitions et costumes improvisés.",
     "L'équipe présente un mini-spectacle de 2 minutes avec 2 styles de danse, des formations variées et des transitions.",
     ["Intégration de 2 styles", "Formations dans l'espace", "Qualité des transitions"],
     ["Mise en scène", "Formations chorégraphiques", "Transitions entre styles"]),
    (66, "L'assiette chinoise et le bâton du diable", "Cirque", 1, "45 min",
     "Les élèves s'initient à deux objets de cirque : l'assiette chinoise sur baguette et le bâton du diable. Patience, coordination et persévérance.",
     "L'élève maintient l'assiette chinoise en rotation 10 secondes OU réalise 5 rattrapés consécutifs au bâton du diable.",
     ["Contrôle de l'objet", "Persévérance dans l'apprentissage", "Sécurité avec le matériel"],
     ["Assiette chinoise", "Bâton du diable", "Patience et persévérance"]),
    (67, "Expression corporelle — l'orchestre humain", "Expression corporelle", 1, "45 min",
     "Les élèves créent un orchestre avec leurs corps : chaque section (cordes, vents, percussions) a des mouvements et des sons spécifiques. Le chef d'orchestre dirige.",
     "Le groupe forme un orchestre humain de 3 sections avec un chef d'orchestre qui dirige les entrées et les volumes.",
     ["Différenciation des sections", "Réactivité au chef d'orchestre", "Sons corporels variés"],
     ["Percussions corporelles avancées", "Direction musicale", "Travail de section"]),
    (68, "Danse contemporaine — la spirale", "Danse contemporaine", 1, "45 min",
     "Les élèves explorent la spirale comme moteur de mouvement en danse contemporaine : spirale ascendante du sol vers debout, spirale descendante, torsions du torse.",
     "L'élève crée une phrase de mouvement de 24 temps utilisant la spirale comme élément principal avec au moins 2 niveaux.",
     ["Qualité de la spirale", "Connexion torse-membres", "Utilisation des niveaux"],
     ["Spirale corporelle", "Torsion du torse", "Continuité du mouvement"]),
    (69, "Relaxation guidée et visualisation", "Relaxation créative", 1, "45 min",
     "Les élèves apprennent des techniques de visualisation pour la relaxation et la préparation mentale. Ils pratiquent la relaxation progressive de Jacobson adaptée.",
     "L'élève pratique la relaxation de Jacobson complète (contracter-relâcher) sur 8 groupes musculaires en 10 minutes.",
     ["Capacité à contracter puis relâcher", "Calme et concentration", "Conscience de la différence tension/détente"],
     ["Relaxation de Jacobson", "Visualisation positive", "Conscience musculaire"])
]

for cid, titre, moyen, dur, dur_p, desc, tache, crit, sav in cycle2_data:
    sae_list.append({
        "id": mid(cid), "titre": titre,
        "cycle": "2e cycle primaire", "niveau": "8-9 ans",
        "duree_periodes": dur, "duree_par_periode": dur_p,
        "moyen_action": moyen,
        "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
        "description": desc,
        "contexte_apprentissage": f"L'enseignant guide les élèves dans l'exploration de {moyen.lower()} adapté au 2e cycle du primaire.",
        "tache_complexe": tache,
        "criteres_evaluation": crit,
        "savoirs_essentiels": sav,
        "progression": [
            {"phase": "Échauffement", "duree": "5 min", "activite": f"Activation corporelle en lien avec {moyen.lower()}", "role_enseignant": "Guider l'échauffement, préparer le corps et l'esprit"},
            {"phase": "Apprentissage", "duree": "15 min", "activite": f"Apprentissage des éléments techniques de {moyen.lower()} adaptés au niveau", "role_enseignant": "Démontrer, expliquer, circuler pour corriger et encourager"},
            {"phase": "Mise en action", "duree": "15 min", "activite": f"Mise en pratique autonome et création en lien avec {moyen.lower()}", "role_enseignant": "Observer, rétroagir, adapter les défis au niveau de chacun"},
            {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements et retour réflexif sur les apprentissages", "role_enseignant": "Guider les étirements, animer le bilan, féliciter les progrès"}
        ],
        "materiel": ["Matériel adapté à l'activité", "Lecteur de musique", "Tapis de sol au besoin"],
        "espace": "Gymnase",
        "tags": ["expression", moyen.lower(), "2e cycle primaire"]
    })

# ============================================================
# 3e CYCLE PRIMAIRE (10-11 ans) — 23 SAÉ (EXPB-070 to EXPB-092)
# ============================================================

cycle3_data = [
    (70, "Chorégraphie de groupe — le spectacle", "Création chorégraphique", 2, "60 min",
     "Les élèves créent une chorégraphie de groupe de 2 minutes intégrant formations, niveaux, canon et unisson. Ils apprennent les principes de mise en scène.",
     "L'équipe présente une chorégraphie de 2 minutes avec au moins 3 formations, 2 niveaux et un passage en canon.",
     ["Variété des formations", "Qualité de l'exécution", "Cohérence artistique"],
     ["Formations scéniques", "Principes de mise en scène", "Direction artistique de groupe"]),
    (71, "Théâtre physique", "Mime", 2, "60 min",
     "Les élèves découvrent le théâtre physique : raconter une histoire complexe uniquement par le mouvement, en intégrant mime, danse et acrobatie.",
     "L'équipe crée et présente une pièce de théâtre physique de 3 minutes avec une narration claire.",
     ["Clarté narrative", "Intégration de différentes disciplines", "Expression dramatique"],
     ["Théâtre physique", "Dramaturgie du mouvement", "Intégration multidisciplinaire"]),
    (72, "Danses du monde — l'Irlande", "Danse folklorique", 1, "60 min",
     "Les élèves apprennent les pas de base de la danse irlandaise : le reel, les pointes et talons, le corps droit avec les bras le long du corps. Énergie des pieds et précision.",
     "L'élève exécute une séquence de reel irlandais de 32 temps avec les bras le long du corps.",
     ["Précision des pieds", "Posture droite", "Rythme et énergie"],
     ["Reel irlandais", "Technique des pieds", "Posture traditionnelle"]),
    (73, "Acrosport — enchaînements complexes", "Acrosport", 2, "60 min",
     "Les élèves créent des enchaînements acrobatiques de groupe avec des figures à 4-6 personnes, des transitions dynamiques et une chorégraphie entre les figures.",
     "Le groupe présente un enchaînement de 90 secondes avec 4 figures, des transitions chorégraphiées et une musique choisie.",
     ["Complexité des figures", "Qualité des transitions", "Sécurité respectée"],
     ["Figures complexes", "Transitions dynamiques", "Chorégraphie acrobatique"]),
    (74, "GR aux massues", "Gymnastique rythmique", 1, "60 min",
     "Les élèves découvrent les massues de GR : petits cercles, moulinets, lancers courts. Coordination fine et symétrie des mouvements.",
     "L'élève réalise un enchaînement de 30 secondes aux massues avec au moins 4 manipulations différentes.",
     ["Symétrie des mouvements", "Contrôle des massues", "Enchaînement fluide"],
     ["Manipulation des massues", "Moulinets", "Symétrie et coordination"]),
    (75, "Gymnastique — l'enchaînement au sol compétitif", "Gymnastique au sol", 2, "60 min",
     "Les élèves composent un enchaînement au sol de 60 secondes de niveau compétitif avec éléments acrobatiques, gymniques et chorégraphiques.",
     "L'élève présente un enchaînement de 60 secondes sur musique avec au moins 6 éléments techniques variés.",
     ["Variété et difficulté des éléments", "Élégance et présentation", "Utilisation de tout l'espace"],
     ["Composition compétitive", "Éléments acrobatiques avancés", "Présentation artistique"]),
    (76, "Breakdance — power moves simplifiés", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves apprennent des power moves adaptés : le baby freeze, le turtle freeze, le swipe débutant. Ils créent un passage de breakdance avec top rock et freezes.",
     "L'élève exécute un passage de 16 temps incluant top rock, 2 mouvements au sol et un freeze final tenu 3 secondes.",
     ["Exécution des freezes", "Fluidité top rock-sol", "Originalité du passage"],
     ["Baby freeze", "Turtle freeze", "Transitions top rock-sol"]),
    (77, "Spectacle de cirque multidisciplinaire", "Cirque", 2, "60 min",
     "Les élèves créent un spectacle de cirque de 5 minutes en groupe, intégrant jonglerie, acrobatie, équilibre, clown et expression. Travail de troupe complet.",
     "Le groupe présente un spectacle de cirque de 5 minutes avec au moins 4 disciplines et des transitions scéniques.",
     ["Variété des disciplines", "Qualité de la présentation", "Cohésion de la troupe"],
     ["Spectacle multidisciplinaire", "Direction de troupe", "Scénographie"]),
    (78, "Danse contemporaine — improvisation structurée", "Danse contemporaine", 1, "60 min",
     "Les élèves apprennent l'improvisation structurée en danse contemporaine : tâches d'improvisation avec contraintes (espace limité, tempo imposé, contact obligatoire).",
     "L'élève improvise pendant 1 minute en respectant 3 contraintes données par l'enseignant.",
     ["Respect des contraintes", "Créativité dans le cadre imposé", "Fluidité du mouvement"],
     ["Improvisation avec contraintes", "Tâches d'improvisation", "Écoute du corps"]),
    (79, "Création d'une danse à message", "Création chorégraphique", 2, "60 min",
     "Les élèves créent une chorégraphie qui transmet un message social (environnement, inclusion, respect). Intégration de la danse comme outil de communication.",
     "L'équipe crée une danse de 2 minutes qui communique clairement un message social choisi.",
     ["Clarté du message", "Originalité de l'interprétation", "Impact émotionnel"],
     ["Danse engagée", "Communication par le mouvement", "Création collective significative"]),
    (80, "Expression corporelle — le tableau vivant", "Expression corporelle", 1, "60 min",
     "Les élèves reproduisent des tableaux célèbres avec leurs corps puis les animent. Ils passent de l'immobilité de la peinture au mouvement de la danse.",
     "L'équipe reproduit 2 tableaux célèbres en tableau vivant puis crée une transition dansée entre les deux.",
     ["Fidélité au tableau original", "Immobilité contrôlée", "Qualité de la transition dansée"],
     ["Tableau vivant", "Immobilité expressive", "Transition image-mouvement"]),
    (81, "Mime — le clown tragique et comique", "Mime", 1, "60 min",
     "Les élèves explorent les deux facettes du clown : le clown blanc (élégant, autoritaire) et l'auguste (maladroit, touchant). Ils créent un duo clownesque.",
     "Le duo présente un numéro de 2 minutes mettant en scène les interactions entre le clown blanc et l'auguste.",
     ["Différenciation des deux personnages", "Timing comique", "Interactions crédibles"],
     ["Clown blanc et auguste", "Timing et rythme comique", "Duo clownesque"]),
    (82, "Danse folklorique — le set carré québécois", "Danse folklorique", 2, "60 min",
     "Les élèves apprennent le set carré québécois complet avec calleur. Ils maîtrisent les 8 figures de base et dansent un set complet en musique traditionnelle.",
     "L'équipe de 8 exécute un set carré complet de 4 minutes avec les 8 figures de base au son du calleur.",
     ["Exécution des 8 figures", "Réactivité au calleur", "Énergie et plaisir"],
     ["Set carré complet", "Rôle du calleur", "Figures avancées"]),
    (83, "GR — enchaînement multi-engins", "Gymnastique rythmique", 2, "60 min",
     "Les élèves créent un enchaînement de GR utilisant 2 engins différents (ruban + cerceau ou ballon + massues). Changement d'engin intégré à la chorégraphie.",
     "L'élève présente un enchaînement de 45 secondes utilisant 2 engins avec un changement d'engin fluide.",
     ["Maîtrise de 2 engins", "Changement d'engin fluide", "Composition musicale"],
     ["Multi-engins", "Changement d'engin", "Composition avancée"]),
    (84, "Relaxation et pleine conscience", "Relaxation créative", 1, "60 min",
     "Les élèves découvrent la pleine conscience : méditation guidée, mouvements conscients, scan corporel, respiration 4-7-8. Gestion du stress et bien-être.",
     "L'élève pratique 15 minutes de pleine conscience en autonomie : respiration 4-7-8, scan corporel et mouvements conscients.",
     ["Capacité à se centrer", "Respiration maîtrisée", "Conscience corporelle"],
     ["Pleine conscience", "Respiration 4-7-8", "Méditation guidée"]),
    (85, "Danse créative — créer avec des objets", "Danse créative", 1, "60 min",
     "Les élèves créent des danses en utilisant des objets du quotidien comme inspiration et accessoire : chaises, parapluies, livres. L'objet devient partenaire de danse.",
     "L'élève crée une danse de 45 secondes avec un objet du quotidien en intégrant au moins 4 façons différentes de l'utiliser.",
     ["Créativité dans l'utilisation de l'objet", "Intégration objet-mouvement", "Originalité"],
     ["Danse avec objets", "Détournement créatif", "Composition avec accessoire"]),
    (86, "Acrosport — la fluidité des transitions", "Acrosport", 1, "60 min",
     "Les élèves se concentrent sur la qualité des transitions entre les figures d'acrosport : portés dynamiques, roulades de liaison, déplacements chorégraphiés.",
     "L'équipe présente 3 figures reliées par des transitions fluides et chorégraphiées, le tout en musique.",
     ["Fluidité des transitions", "Créativité des liaisons", "Cohérence de l'ensemble"],
     ["Transitions dynamiques", "Portés de liaison", "Chorégraphie entre les figures"]),
    (87, "Jonglerie à 3 balles — la cascade", "Cirque", 2, "60 min",
     "Les élèves apprennent la cascade à 3 balles : progression méthodique avec exercices préparatoires. Persévérance et coordination fine.",
     "L'élève réalise au moins 6 lancers consécutifs en cascade à 3 balles.",
     ["Régularité des lancers", "Hauteur constante", "Persévérance dans l'apprentissage"],
     ["Cascade à 3 balles", "Exercices préparatoires", "Rythme de jonglage"]),
    (88, "Danse contemporaine — le sol comme partenaire", "Danse contemporaine", 1, "60 min",
     "Les élèves explorent le travail au sol en danse contemporaine : rouler, glisser, tomber et se relever. Le sol devient un partenaire de danse.",
     "L'élève crée une phrase de mouvement de 32 temps intégrant au moins 3 types de relation avec le sol.",
     ["Variété des contacts au sol", "Fluidité des transitions sol-debout", "Qualité du mouvement"],
     ["Floor work", "Chutes contrôlées", "Relation au sol"]),
    (89, "Expression corporelle — les statues qui s'animent", "Expression corporelle", 1, "60 min",
     "Les élèves créent un musée de statues qui prennent vie progressivement. Exploration de l'immobilité totale, du micro-mouvement et de l'animation complète.",
     "L'élève passe de la statue immobile à la danse complète en 60 secondes avec une progression claire et maîtrisée.",
     ["Qualité de l'immobilité", "Progression graduelle", "Expression lors de l'animation"],
     ["Immobilité active", "Micro-mouvement", "Progression du mouvement"]),
    (90, "Gymnastique au sol — flip avant et arrière (initiation)", "Gymnastique au sol", 2, "60 min",
     "Les élèves s'initient au saut de mains avant (flip avant) sur trampoline puis sur tapis surélevés. Progression ultra-sécuritaire avec parade.",
     "L'élève réalise un saut de mains avant depuis le mini-trampoline vers le matelas de réception avec parade.",
     ["Impulsion correcte", "Position du corps en vol", "Réception stable"],
     ["Saut de mains (initiation)", "Impulsion et envol", "Sécurité en acrobatie aérienne"]),
    (91, "Danse hip-hop — la chorégraphie de clip", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves apprennent une chorégraphie de style clip vidéo : mouvements synchronisés, formations, attitude et énergie. Ils travaillent sur le style et la présence scénique.",
     "L'équipe présente une chorégraphie de style clip de 90 secondes avec formations, synchronisation et attitude.",
     ["Synchronisation du groupe", "Formations dynamiques", "Style et attitude"],
     ["Chorégraphie de style clip", "Synchronisation avancée", "Présence scénique"]),
    (92, "Danse folklorique — danses latines", "Danse folklorique", 1, "60 min",
     "Les élèves découvrent la salsa et le merengue : pas de base, déplacements en couple, tours simples. Rythme, coordination et plaisir de danser à deux.",
     "L'élève exécute les pas de base de la salsa et du merengue en couple pendant 32 temps chacun.",
     ["Rythme latin maintenu", "Coordination en couple", "Transitions entre les danses"],
     ["Pas de base salsa", "Pas de base merengue", "Danse en couple"])
]

for cid, titre, moyen, dur, dur_p, desc, tache, crit, sav in cycle3_data:
    sae_list.append({
        "id": mid(cid), "titre": titre,
        "cycle": "3e cycle primaire", "niveau": "10-11 ans",
        "duree_periodes": dur, "duree_par_periode": dur_p,
        "moyen_action": moyen,
        "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
        "description": desc,
        "contexte_apprentissage": f"L'enseignant guide les élèves du 3e cycle dans l'approfondissement de {moyen.lower()} avec des défis adaptés à leur maturité.",
        "tache_complexe": tache,
        "criteres_evaluation": crit,
        "savoirs_essentiels": sav,
        "progression": [
            {"phase": "Échauffement", "duree": "8 min", "activite": f"Échauffement ciblé pour {moyen.lower()} avec activation cardio et articulaire", "role_enseignant": "Diriger l'échauffement, vérifier la préparation physique"},
            {"phase": "Apprentissage", "duree": "15 min", "activite": f"Enseignement des éléments techniques avancés de {moyen.lower()}", "role_enseignant": "Démontrer, expliquer les critères de réussite, différencier l'enseignement"},
            {"phase": "Mise en action", "duree": "20 min", "activite": f"Création, pratique autonome et présentation en lien avec {moyen.lower()}", "role_enseignant": "Accompagner la création, offrir des rétroactions ciblées, évaluer"},
            {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements et bilan réflexif sur les apprentissages et les défis", "role_enseignant": "Guider les étirements, animer la réflexion, fixer les prochains objectifs"}
        ],
        "materiel": ["Matériel spécifique à l'activité", "Lecteur de musique", "Tapis de sol au besoin"],
        "espace": "Gymnase",
        "tags": ["expression", moyen.lower(), "3e cycle primaire"]
    })

# ============================================================
# 1er CYCLE SECONDAIRE (12-13 ans) — 24 SAÉ (EXPB-093 to EXPB-116)
# ============================================================

sec1_data = [
    (93, "Chorégraphie à thème — identité", "Création chorégraphique", 2, "60 min",
     "Les élèves créent une chorégraphie sur le thème de l'identité personnelle : qui suis-je? D'où je viens? Où je vais? Utilisation de la danse comme médium d'expression personnelle.",
     "L'équipe présente une chorégraphie de 3 minutes sur le thème de l'identité intégrant au moins 3 styles de danse."),
    (94, "Théâtre physique avancé — la commedia dell'arte", "Mime", 2, "60 min",
     "Les élèves découvrent la commedia dell'arte et ses archétypes (Arlequin, Colombine, Pantalone). Ils créent des scènes avec masques et mouvements codifiés.",
     "L'équipe présente une scène de commedia de 3 minutes avec 3 archétypes identifiables et des lazzi."),
    (95, "Danses du monde — le flamenco", "Danse folklorique", 2, "60 min",
     "Les élèves découvrent le flamenco : les palmas (frappes de mains), le zapateado (frappes de pieds), les bras serpentins. Passion et énergie de la danse espagnole.",
     "L'élève exécute une séquence de flamenco de 32 temps avec palmas, zapateado et port de bras."),
    (96, "Acrosport — chorégraphie acrobatique complète", "Acrosport", 2, "60 min",
     "Les élèves créent une routine d'acrosport chorégraphiée de 3 minutes avec figures complexes, transitions dansées et musique. Préparation de type compétition.",
     "L'équipe de 5-6 présente une routine de 3 minutes avec 5 figures, des transitions dansées et une musique."),
    (97, "GR — enchaînement de compétition", "Gymnastique rythmique", 2, "60 min",
     "Les élèves composent un enchaînement de GR individuel de compétition de 75 secondes avec un engin au choix (ruban, cerceau, ballon ou massues).",
     "L'élève présente un enchaînement de 75 secondes avec l'engin choisi, incluant au moins 8 manipulations différentes."),
    (98, "Gymnastique au sol — enchaînement libre", "Gymnastique au sol", 2, "60 min",
     "Les élèves composent et présentent un enchaînement au sol libre de 75 secondes sur musique. Éléments acrobatiques, gymniques et chorégraphiques selon le niveau.",
     "L'élève présente un enchaînement de 75 secondes au sol sur musique avec au moins 8 éléments variés."),
    (99, "Street dance et chorégraphie urbaine", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves approfondissent le vocabulaire de la street dance : locking, popping, waving. Ils créent une chorégraphie urbaine de groupe intégrant ces styles.",
     "L'équipe présente une chorégraphie urbaine de 2 minutes intégrant locking, popping et au moins une section freestyle."),
    (100, "Arts du cirque — numéro individuel", "Cirque", 2, "60 min",
     "Chaque élève développe un numéro de cirque individuel dans la discipline de son choix (jonglerie, équilibre, acrobatie, clown). Préparation de type spectacle.",
     "L'élève présente un numéro de cirque individuel de 2 minutes dans sa spécialité avec entrée, numéro et salut."),
    (101, "Danse contemporaine — composition et interprétation", "Danse contemporaine", 2, "60 min",
     "Les élèves créent un solo ou duo de danse contemporaine de 90 secondes sur un thème émotionnel choisi. Focus sur l'interprétation et la qualité du mouvement.",
     "L'élève présente un solo de 90 secondes de danse contemporaine avec une interprétation émotionnelle claire."),
    (102, "Expression corporelle — performance artistique", "Expression corporelle", 2, "60 min",
     "Les élèves créent une performance artistique interdisciplinaire mêlant danse, mime, acrobatie et manipulation d'objets. Art de la performance comme moyen d'expression.",
     "L'équipe présente une performance de 3 minutes intégrant au moins 3 disciplines et un concept artistique original."),
    (103, "Danse créative — musique et vidéoclip", "Danse créative", 2, "60 min",
     "Les élèves créent une chorégraphie de style vidéoclip sur une musique populaire actuelle. Formations, synchronisation, style et attitude sont au centre du projet.",
     "L'équipe présente une chorégraphie de style vidéoclip de 2 minutes avec formations variées et synchronisation."),
    (104, "Relaxation et gestion du stress par le mouvement", "Relaxation créative", 1, "60 min",
     "Les élèves apprennent des techniques de gestion du stress combinant mouvement et respiration : qi gong simplifié, yoga flow, relaxation musculaire progressive.",
     "L'élève exécute une routine de 10 minutes de qi gong/yoga flow pour la gestion du stress de façon autonome."),
    (105, "Danses du monde — danse polynésienne", "Danse folklorique", 1, "60 min",
     "Les élèves découvrent les danses polynésiennes : mouvements fluides des hanches et des mains racontant une histoire. Grâce et narration par le mouvement.",
     "L'élève exécute une séquence de danse polynésienne de 32 temps avec les gestes narratifs des mains et le mouvement des hanches."),
    (106, "Acrosport — trios et quatuors dynamiques", "Acrosport", 2, "60 min",
     "Les élèves créent des figures dynamiques d'acrosport intégrant des éléments de mouvement : portés lancés, réceptions contrôlées, rotations. Niveau intermédiaire.",
     "L'équipe de 4 réalise 3 figures dynamiques avec des portés incluant du mouvement, le tout enchaîné avec des transitions."),
    (107, "Mime — le monologue corporel", "Mime", 1, "60 min",
     "Chaque élève crée un monologue corporel de 2 minutes sur un thème personnel : un souvenir, un rêve, une peur. Expression intime par le corps seul.",
     "L'élève présente un monologue corporel de 2 minutes avec une progression narrative claire et une émotion authentique."),
    (108, "GR en groupe — l'ensemble", "Gymnastique rythmique", 2, "60 min",
     "Les élèves créent un enchaînement de GR de groupe (5 gymnastes) avec échanges d'engins, formations et synchronisation. Travail collectif avancé.",
     "Le groupe de 5 présente un enchaînement de 90 secondes avec échanges d'engins synchronisés et formations variées."),
    (109, "Danse contemporaine — le duo dramatique", "Danse contemporaine", 2, "60 min",
     "Les élèves créent un duo de danse contemporaine explorant une relation : amitié, conflit, complicité. Contact, portés simples et narration par le mouvement.",
     "Le duo présente une danse de 2 minutes explorant une relation avec portés, contact et progression narrative."),
    (110, "Hip-hop choreo — styles fusionnés", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves fusionnent le hip-hop avec d'autres styles (jazz, contemporain, africain) dans une chorégraphie de fusion. Exploration de l'hybridation des styles de danse.",
     "L'équipe présente une chorégraphie fusion de 2 minutes intégrant le hip-hop et au moins un autre style de danse."),
    (111, "Cirque — le numéro de duo", "Cirque", 2, "60 min",
     "Les élèves créent un numéro de cirque en duo combinant leurs spécialités respectives. Synchronisation, complémentarité et mise en scène à deux.",
     "Le duo présente un numéro de cirque de 3 minutes combinant 2 disciplines avec synchronisation et mise en scène."),
    (112, "Gymnastique au sol — éléments combinés", "Gymnastique au sol", 2, "60 min",
     "Les élèves apprennent à combiner des éléments gymniques en séries : rondade-saut, roue-roulade, ATR-roulade. Fluidité et continuité du mouvement.",
     "L'élève réalise au moins 2 combinaisons gymniques fluides (ex. rondade-saut, roue-roulade)."),
    (113, "Expression corporelle — installation vivante", "Expression corporelle", 2, "60 min",
     "Les élèves créent une installation artistique vivante dans le gymnase : corps immobiles et mobiles créant un environnement. Le public circule à travers l'installation.",
     "Le groupe crée une installation vivante de 5 minutes avec zones immobiles et mobiles à travers lesquelles le public circule."),
    (114, "Danse créative — improvisation en groupe", "Danse créative", 1, "60 min",
     "Les élèves pratiquent l'improvisation collective en danse : écoute du groupe, réponses spontanées, flocking (suivre le leader invisible), essaim.",
     "L'élève participe à 3 exercices d'improvisation collective en démontrant écoute, réactivité et créativité."),
    (115, "Création chorégraphique — la pièce de danse", "Création chorégraphique", 2, "60 min",
     "Les élèves créent collectivement une pièce de danse de 5 minutes en plusieurs tableaux. Ils apprennent la dramaturgie de la danse et la direction artistique.",
     "La classe présente une pièce de danse de 5 minutes en plusieurs tableaux avec une dramaturgie cohérente."),
    (116, "Danse folklorique — gigue québécoise avancée", "Danse folklorique", 2, "60 min",
     "Les élèves approfondissent la gigue québécoise : pas de base, syncopes, improvisations de pieds. Ils apprennent à giguer en solo et en groupe avec calleur.",
     "L'élève exécute une gigue de 32 temps avec des syncopes et des improvisations de pieds au son du violon traditionnel.")
]

for cid, titre, moyen, dur, dur_p, desc, tache in sec1_data:
    sae_list.append({
        "id": mid(cid), "titre": titre,
        "cycle": "1er cycle secondaire", "niveau": "12-13 ans",
        "duree_periodes": dur, "duree_par_periode": dur_p,
        "moyen_action": moyen,
        "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
        "description": desc,
        "contexte_apprentissage": f"L'enseignant accompagne les élèves du 1er cycle secondaire dans la maîtrise de {moyen.lower()} avec des exigences techniques et artistiques élevées.",
        "tache_complexe": tache,
        "criteres_evaluation": ["Qualité technique de l'exécution", "Expressivité et interprétation artistique", "Créativité et originalité"],
        "savoirs_essentiels": ["Techniques avancées spécifiques", "Principes de composition artistique", "Interprétation et expression"],
        "progression": [
            {"phase": "Échauffement", "duree": "8 min", "activite": f"Échauffement technique ciblé pour {moyen.lower()}", "role_enseignant": "Diriger l'échauffement, cibler les muscles et articulations sollicités"},
            {"phase": "Apprentissage", "duree": "15 min", "activite": f"Approfondissement technique et artistique en {moyen.lower()}", "role_enseignant": "Enseigner, démontrer, corriger, différencier selon les niveaux"},
            {"phase": "Mise en action", "duree": "25 min", "activite": f"Création, répétition et préparation de la présentation en {moyen.lower()}", "role_enseignant": "Accompagner la création, offrir des rétroactions, préparer les présentations"},
            {"phase": "Retour au calme", "duree": "5 min", "activite": "Étirements et bilan réflexif approfondi", "role_enseignant": "Guider les étirements, animer la réflexion critique, encourager l'autoévaluation"}
        ],
        "materiel": ["Matériel spécialisé selon l'activité", "Système de son de qualité", "Tapis et équipement de sécurité"],
        "espace": "Gymnase",
        "tags": ["expression", moyen.lower(), "1er cycle secondaire"]
    })

# ============================================================
# 2e CYCLE SECONDAIRE (14-16 ans) — 24 SAÉ (EXPB-117 to EXPB-140)
# ============================================================

sec2_data = [
    (117, "Chorégraphie de spectacle de fin d'année", "Création chorégraphique", 2, "60 min",
     "Les élèves conçoivent et répètent une chorégraphie pour le spectacle de fin d'année. Ils gèrent tous les aspects : concept, musique, costumes, éclairage, formations.",
     "L'équipe produit une chorégraphie de 4 minutes prête pour le spectacle avec concept, costumes et éclairage planifiés."),
    (118, "Théâtre physique — création originale", "Mime", 2, "60 min",
     "Les élèves créent une pièce de théâtre physique originale de 5 minutes abordant un enjeu social. Intégration de mime, danse, acrobatie et manipulation.",
     "L'équipe présente une pièce de théâtre physique de 5 minutes sur un enjeu social avec un impact émotionnel fort."),
    (119, "Danses du monde — danse orientale", "Danse folklorique", 2, "60 min",
     "Les élèves découvrent la danse orientale : ondulations du torse, shimmies, mouvements des hanches, port de bras élégant. Connaissance culturelle et technique.",
     "L'élève exécute une chorégraphie de danse orientale de 48 temps avec ondulations, shimmies et port de bras."),
    (120, "Acrosport — création libre de haut niveau", "Acrosport", 2, "60 min",
     "Les élèves créent une routine d'acrosport de compétition de 4 minutes avec figures complexes, pyramides, portés dynamiques et chorégraphie de transition.",
     "L'équipe de 6 présente une routine de 4 minutes avec au moins 6 figures complexes et des transitions chorégraphiées."),
    (121, "GR — solo de compétition", "Gymnastique rythmique", 2, "60 min",
     "Les élèves composent et présentent un solo de GR de compétition de 90 secondes. Maîtrise technique de l'engin, chorégraphie et expression artistique.",
     "L'élève présente un solo de GR de 90 secondes avec maîtrise technique, musicalité et expression artistique."),
    (122, "Gymnastique au sol — routine de compétition", "Gymnastique au sol", 2, "60 min",
     "Les élèves composent une routine de gymnastique au sol de 90 secondes de niveau compétitif. Éléments acrobatiques avancés, chorégraphie et expression.",
     "L'élève présente une routine au sol de 90 secondes sur musique avec au moins 10 éléments techniques de difficulté variée."),
    (123, "Danse hip-hop — chorégraphie de crew", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves forment un crew de danse hip-hop et créent une chorégraphie de compétition de 3 minutes. Synchronisation, formations, solos et énergie de groupe.",
     "Le crew présente une chorégraphie de 3 minutes avec formations dynamiques, passages solos et synchronisation de haut niveau."),
    (124, "Cirque — spectacle de troupe complet", "Cirque", 2, "60 min",
     "Les élèves montent un spectacle de cirque complet de 10 minutes en troupe. Scénario, numéros variés, transitions, musique et mise en scène.",
     "La troupe présente un spectacle de cirque de 10 minutes avec scénario, au moins 5 numéros variés et des transitions scéniques."),
    (125, "Danse contemporaine — solo d'interprétation", "Danse contemporaine", 2, "60 min",
     "Chaque élève crée et présente un solo de danse contemporaine de 2 minutes sur un thème personnel. Authenticité, vulnérabilité et qualité de mouvement.",
     "L'élève présente un solo de 2 minutes de danse contemporaine avec une interprétation authentique et une qualité de mouvement élevée."),
    (126, "Expression corporelle — performance immersive", "Expression corporelle", 2, "60 min",
     "Les élèves créent une performance immersive où le public est intégré à l'œuvre. Déambulation, interaction avec les spectateurs, environnement sonore et visuel.",
     "Le groupe crée une performance immersive de 10 minutes avec interaction du public et environnement multisensoriel."),
    (127, "Danse créative — le processus de création", "Danse créative", 2, "60 min",
     "Les élèves vivent le processus de création complet d'une pièce de danse : recherche, exploration, composition, répétition, présentation. Documentation par journal de bord.",
     "L'élève crée une pièce de danse de 2 minutes en documentant son processus créatif dans un journal de bord."),
    (128, "Yoga et conditionnement mental pour la performance", "Relaxation créative", 2, "60 min",
     "Les élèves apprennent des techniques de préparation mentale pour la performance artistique : yoga pour artistes, respiration anti-trac, visualisation de la performance.",
     "L'élève applique une routine de préparation mentale de 15 minutes avant une performance et en évalue l'impact."),
    (129, "Danses du monde — tango argentin", "Danse folklorique", 2, "60 min",
     "Les élèves découvrent le tango argentin : la marche, la connexion poitrine à poitrine, les ochos, le croisé. Élégance, connexion et musicalité.",
     "L'élève exécute les pas de base du tango argentin en couple avec la marche, les ochos et le croisé."),
    (130, "Acrosport et danse — la fusion", "Acrosport", 2, "60 min",
     "Les élèves créent une routine fusionnant acrosport et danse contemporaine. Les figures acrobatiques naissent du mouvement dansé et y retournent sans rupture.",
     "L'équipe présente une routine fusion acrosport-danse de 3 minutes où les figures émergent naturellement du mouvement dansé."),
    (131, "Mime contemporain — Lecoq et le mouvement", "Mime", 2, "60 min",
     "Les élèves découvrent le mime contemporain inspiré de Jacques Lecoq : le jeu du masque neutre, les 7 niveaux de tension, les éléments. Profondeur expressive.",
     "L'élève présente un exercice du masque neutre démontrant les 7 niveaux de tension en transition fluide."),
    (132, "GR — duo synchronisé", "Gymnastique rythmique", 2, "60 min",
     "Les élèves créent un duo de GR synchronisé avec le même engin. Travail de miroir, échanges d'engin entre partenaires et composition musicale.",
     "Le duo présente un enchaînement synchronisé de 90 secondes avec le même engin, incluant au moins 2 échanges."),
    (133, "Danse contemporaine — atelier de création collective", "Danse contemporaine", 2, "60 min",
     "Les élèves participent à un atelier de création collective dirigé par un processus démocratique. Chaque élève contribue du matériel chorégraphique à l'œuvre commune.",
     "La classe présente une œuvre collective de 8 minutes où chaque élève a contribué au moins une phrase de mouvement."),
    (134, "Hip-hop et culture urbaine — le showcase", "Danse hip-hop / moderne", 2, "60 min",
     "Les élèves organisent un showcase de danse urbaine : chaque crew ou soliste présente son numéro. Évaluation par les pairs selon des critères établis ensemble.",
     "L'élève ou le crew présente un numéro de 2-3 minutes lors du showcase et évalue les autres selon les critères établis."),
    (135, "Cirque — spécialisation et coaching", "Cirque", 2, "60 min",
     "Chaque élève se spécialise dans une discipline de cirque et devient le coach de ses pairs dans cette discipline. Pédagogie par les pairs.",
     "L'élève présente son numéro de spécialité de 3 minutes et enseigne les bases de sa discipline à un groupe de pairs."),
    (136, "Gymnastique au sol — création artistique sur musique", "Gymnastique au sol", 2, "60 min",
     "Les élèves créent une routine au sol où la musique guide chaque mouvement. Interprétation musicale, synchronisation et expression personnelle.",
     "L'élève présente une routine de 90 secondes démontrant une interprétation musicale fine et une expression personnelle."),
    (137, "Expression corporelle — le manifeste dansé", "Expression corporelle", 2, "60 min",
     "Les élèves créent un manifeste dansé sur un sujet qui leur tient à cœur : environnement, justice sociale, santé mentale. L'art comme outil de changement.",
     "L'équipe présente un manifeste dansé de 4 minutes avec un message social clair et un impact émotionnel sur le public."),
    (138, "Danse folklorique — création contemporaine sur musique trad", "Danse folklorique", 2, "60 min",
     "Les élèves créent une chorégraphie contemporaine sur de la musique traditionnelle québécoise. Fusion entre l'héritage folklorique et l'expression contemporaine.",
     "L'équipe présente une chorégraphie de 3 minutes fusionnant mouvement contemporain et musique traditionnelle québécoise."),
    (139, "Création chorégraphique — le portfolio de l'artiste", "Création chorégraphique", 2, "60 min",
     "Les élèves compilent un portfolio d'artiste incluant leurs meilleures créations chorégraphiques de l'année. Réflexion sur leur parcours artistique.",
     "L'élève présente son portfolio contenant 3 extraits chorégraphiques de 1 minute chacun et une réflexion écrite sur son évolution."),
    (140, "Relaxation créative — enseigner aux autres", "Relaxation créative", 1, "60 min",
     "Les élèves conçoivent et animent une séance de relaxation créative de 15 minutes pour un groupe de plus jeunes. Pédagogie par les aînés et leadership.",
     "L'élève anime une séance de relaxation de 15 minutes pour un groupe de plus jeunes avec calme, clarté et bienveillance.")
]

for cid, titre, moyen, dur, dur_p, desc, tache in sec2_data:
    sae_list.append({
        "id": mid(cid), "titre": titre,
        "cycle": "2e cycle secondaire", "niveau": "14-16 ans",
        "duree_periodes": dur, "duree_par_periode": dur_p,
        "moyen_action": moyen,
        "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
        "description": desc,
        "contexte_apprentissage": f"L'enseignant agit comme guide et mentor, offrant aux élèves du 2e cycle secondaire l'autonomie nécessaire pour approfondir {moyen.lower()} à un niveau avancé.",
        "tache_complexe": tache,
        "criteres_evaluation": ["Excellence technique", "Profondeur de l'interprétation artistique", "Autonomie et leadership dans le processus créatif"],
        "savoirs_essentiels": ["Maîtrise technique avancée", "Processus de création artistique", "Autoévaluation et pensée critique"],
        "progression": [
            {"phase": "Échauffement", "duree": "10 min", "activite": f"Échauffement autonome ciblé pour {moyen.lower()} avec activation complète", "role_enseignant": "Superviser l'échauffement autonome, intervenir au besoin"},
            {"phase": "Apprentissage", "duree": "15 min", "activite": f"Perfectionnement technique et exploration créative avancée en {moyen.lower()}", "role_enseignant": "Offrir un enseignement différencié, mentorat individuel et collectif"},
            {"phase": "Mise en action", "duree": "25 min", "activite": f"Création autonome, répétition et peaufinage de la présentation en {moyen.lower()}", "role_enseignant": "Accompagner la création avec rétroactions critiques, préparer les présentations"},
            {"phase": "Retour au calme", "duree": "10 min", "activite": "Étirements et réflexion critique approfondie sur le processus et le produit artistique", "role_enseignant": "Faciliter la réflexion critique, encourager l'autoévaluation et l'ouverture aux commentaires"}
        ],
        "materiel": ["Matériel spécialisé de qualité", "Système de son professionnel", "Équipement de sécurité adapté"],
        "espace": "Gymnase",
        "tags": ["expression", moyen.lower(), "2e cycle secondaire"]
    })

# ============================================================
# BUILD FINAL JSON
# ============================================================

output = {
    "domaine": "Expression — Bonification",
    "total_sae": len(sae_list),
    "programme": "PFEQ — Éducation physique et à la santé",
    "sae": sae_list
}

with open("/Users/admin/PROJETS_CLAUDE/app-sae/data/sae/expression_bonus.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Generated {len(sae_list)} SAÉ successfully.")

# Verify distribution
from collections import Counter
cycles = Counter(s["cycle"] for s in sae_list)
for c, n in sorted(cycles.items()):
    print(f"  {c}: {n}")
