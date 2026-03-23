#!/usr/bin/env python3
import json, random

random.seed(42)

sae_list = []

# Define cycles
cycles = [
    ("Maternelle", "4-5 ans", "30 min"),
    ("1er cycle primaire", "6-7 ans", "30 min"),
    ("2e cycle primaire", "8-9 ans", "45 min"),
    ("3e cycle primaire", "10-11 ans", "45 min"),
    ("1er cycle secondaire", "12-13 ans", "60 min"),
    ("2e cycle secondaire", "14-16 ans", "60 min"),
]

# Distribution: 23,23,23,23,24,24 = 140
counts = [23, 23, 23, 23, 24, 24]

# Moyens d'action templates per cycle
moyens = [
    "Équilibre statique",
    "Équilibre dynamique",
    "Gainage",
    "Yoga",
    "Gymnastique",
    "Souplesse",
    "Coordination",
    "Acrosport",
    "Force",
    "Conditionnement physique",
    "Relaxation",
    "Proprioception",
]

# Detailed SAÉ definitions per moyen and cycle
# We'll create unique content for each

titles_by_moyen = {
    "Équilibre statique": [
        ("Les Statues du Parc", "Explorer l'immobilité en adoptant des postures de statues variées, en maintenant l'équilibre sur différentes parties du corps."),
        ("Le Flamant Rose", "Développer l'équilibre unipodal en imitant le flamant rose, avec des variations de positions de bras et de jambe libre."),
        ("Les Gardiens de la Tour", "Maintenir des positions d'équilibre statique sur des surfaces surélevées (bancs suédois, blocs de mousse)."),
        ("Immobile comme un Arbre", "Tenir des postures d'équilibre sur un pied en s'inspirant de la nature (arbre, héron, champignon)."),
        ("Les Équilibristes du Cirque", "Reproduire des postures d'équilibre inspirées du cirque sur des surfaces stables et instables."),
        ("Défis d'Équilibre en Duo", "Réaliser des postures d'équilibre statique en duo, en se soutenant mutuellement pour maintenir la stabilité."),
        ("Le Parcours des Statues", "Enchaîner des déplacements et des arrêts en posture d'équilibre à différentes stations."),
        ("Équilibre et Concentration", "Développer l'attention et la concentration par des défis d'équilibre statique de durée croissante."),
        ("Les Piliers du Temple", "Maintenir des postures de gainage debout inspirées de l'architecture, en variant les appuis."),
        ("Stabilité sur Surfaces Variées", "Explorer l'équilibre statique sur des coussins d'équilibre, demi-ballons et tapis pliés."),
        ("Le Défi des 30 Secondes", "Progresser dans la durée de maintien de postures d'équilibre statique avec chronomètre."),
        ("Équilibre les Yeux Fermés", "Développer la proprioception en réalisant des postures d'équilibre avec privation visuelle progressive."),
    ],
    "Équilibre dynamique": [
        ("Le Pont de Singe", "Se déplacer sur des poutres basses et des lignes tracées au sol en maintenant l'équilibre."),
        ("La Rivière aux Crocodiles", "Traverser un parcours d'équilibre dynamique composé de bancs, poutres et surfaces étroites."),
        ("Marche sur la Poutre", "Apprendre à marcher avant, arrière et latéralement sur la poutre basse avec assurance."),
        ("Le Funambule", "Progresser sur des lignes étroites (ruban adhésif, corde au sol, poutre) avec des objets en équilibre."),
        ("Parcours Ninja", "Enchaîner des éléments d'équilibre dynamique dans un parcours inspiré des courses à obstacles."),
        ("La Slackline au Sol", "S'initier à la marche sur sangle tendue près du sol, avec aide puis de façon autonome."),
        ("Les Chemins Suspendus", "Réaliser un parcours d'équilibre en hauteur (bancs retournés, poutres, échelles horizontales)."),
        ("Équilibre en Mouvement", "Intégrer des actions motrices (lancer, attraper) tout en se déplaçant en équilibre sur des surfaces étroites."),
        ("Le Déménageur Acrobate", "Transporter des objets variés en marchant sur des surfaces d'équilibre sans les faire tomber."),
        ("Relais Équilibre", "Compétition par équipes sur un parcours d'équilibre dynamique avec passages de relais."),
        ("Le Labyrinthe Instable", "Naviguer un parcours en zigzag sur des surfaces variées (mousses, coussins, planches)."),
        ("Danse sur la Poutre", "Créer et exécuter une courte chorégraphie sur la poutre basse avec des éléments variés."),
    ],
    "Gainage": [
        ("La Planche Musicale", "Maintenir la position de la planche pendant la durée d'une chanson, avec des variations rythmiques."),
        ("Le Défi Gainage", "Réaliser un circuit de gainage avec des positions variées (planche, latéral, dorsal) tenues progressivement."),
        ("Les Animaux Forts", "Reproduire des positions de gainage inspirées des animaux (ours, crocodile, lézard, cobra)."),
        ("Superman et ses Amis", "Explorer les positions de gainage dorsal (superman, nageur, pont) de façon ludique."),
        ("Le Circuit des Guerriers", "Enchaîner des stations de gainage dans un circuit chronométré avec des défis progressifs."),
        ("Gainage en Duo", "Réaliser des exercices de gainage en duo avec contacts (tapes, passages dessous/dessus)."),
        ("Le Bûcheron Solide", "Développer le gainage fonctionnel à travers des mouvements inspirés du travail forestier."),
        ("Planche et Créativité", "Inventer de nouvelles positions de gainage en combinant appuis sur mains et pieds."),
        ("Le Défi de la Minute", "Progresser vers le maintien d'une planche complète pendant 60 secondes avec bonne technique."),
        ("Gainage Dynamique", "Intégrer des mouvements dans les positions de gainage (mountain climbers, planche marchée)."),
        ("Le Core Challenge", "Circuit de renforcement du tronc avec exercices variés adaptés au niveau des élèves."),
        ("Gainage et Stabilité", "Combiner gainage et surfaces instables pour un défi de stabilisation complet."),
    ],
    "Yoga": [
        ("Le Yoga des Saisons", "Découvrir des séquences de yoga inspirées des quatre saisons du Québec."),
        ("Salutation au Soleil Junior", "Apprendre la séquence de la salutation au soleil adaptée aux enfants."),
        ("Le Yoga des Animaux", "Pratiquer des postures de yoga nommées d'après les animaux avec histoires guidées."),
        ("Respiration et Postures", "Coordonner la respiration avec les mouvements de yoga pour développer la conscience corporelle."),
        ("Le Jardin de Yoga", "Créer un enchaînement de postures inspirées de la nature (arbre, fleur, montagne, rivière)."),
        ("Yoga en Duo", "Réaliser des postures de yoga à deux pour développer la confiance et la coopération."),
        ("Le Yoga Sportif", "Intégrer des postures de yoga comme complément d'entraînement pour améliorer la performance."),
        ("Relaxation Guidée", "Pratiquer une séance complète de yoga incluant postures, respiration et relaxation finale."),
        ("Yoga et Équilibre", "Se concentrer sur les postures d'équilibre du yoga (arbre, aigle, danseur, guerrier III)."),
        ("Le Flow Créatif", "Créer son propre enchaînement de yoga fluide en utilisant les postures apprises."),
        ("Yoga et Pleine Conscience", "Combiner le yoga avec des exercices de pleine conscience et de méditation guidée."),
        ("Le Power Yoga", "Séance de yoga dynamique axée sur la force et l'endurance musculaire."),
    ],
    "Gymnastique": [
        ("La Roulade Avant", "Apprendre la technique de la roulade avant avec progression pédagogique adaptée."),
        ("Les Appuis Manuels", "Développer la confiance en appui sur les mains (trépied, appui tendu renversé avec aide)."),
        ("Mini-Enchaînement Gym", "Créer un court enchaînement gymnastique combinant roulades, équilibres et sauts."),
        ("La Chandelle", "Maîtriser la position de la chandelle avec une progression par étapes sécuritaires."),
        ("La Roue Latérale", "Apprendre la roue latérale avec des exercices préparatoires et une progression adaptée."),
        ("Gymnastique au Sol", "Explorer les éléments de base de la gymnastique au sol dans un parcours guidé."),
        ("Les Figures Acrobatiques", "Réaliser des figures gymniques simples en combinant roulades, sauts et équilibres."),
        ("Le Parcours Gymnique", "Enchaîner des éléments gymniques sur un parcours avec différents appareils."),
        ("Gym et Créativité", "Composer un enchaînement gymnique libre en respectant des contraintes imposées."),
        ("Les Sauts Gymniques", "Maîtriser différents types de sauts gymniques (extension, groupé, écart, demi-tour)."),
        ("Enchaînement Évalué", "Préparer et présenter un enchaînement gymnique complet évalué selon des critères précis."),
        ("Gymnastique Acrobatique", "Réaliser des éléments acrobatiques avancés avec parade et sécurité."),
    ],
    "Souplesse": [
        ("Les Étirements Rigolos", "Découvrir les principaux étirements sous forme de jeu avec des images d'animaux."),
        ("Le Circuit Souplesse", "Réaliser un circuit d'étirements pour tous les groupes musculaires principaux."),
        ("Souplesse et Mobilité", "Explorer l'amplitude articulaire à travers des mouvements guidés et progressifs."),
        ("Le Grand Écart Progressif", "Travailler la souplesse des jambes avec une progression vers le grand écart."),
        ("Étirements Dynamiques", "Pratiquer des étirements en mouvement pour préparer le corps à l'activité physique."),
        ("Flexibilité Totale", "Séance complète de développement de la flexibilité de la tête aux pieds."),
        ("Souplesse en Musique", "Réaliser une routine d'étirements chorégraphiée sur une musique relaxante."),
        ("Le Défi Souplesse", "Mesurer et améliorer sa souplesse avec des tests standardisés et des objectifs personnels."),
        ("Mobilité Articulaire", "Explorer les mouvements de chaque articulation pour développer une mobilité complète."),
        ("Stretching et Récupération", "Apprendre des routines d'étirements pour la récupération après l'effort."),
        ("La Souplesse du Gymnaste", "Développer la souplesse spécifique à la gymnastique (ponts, grands écarts, cambrés)."),
        ("Souplesse Active", "Travailler la souplesse par des contractions musculaires (PNF) et des étirements actifs."),
    ],
    "Coordination": [
        ("Les Mains et les Pieds", "Développer la coordination mains-pieds à travers des jeux de dissociation simple."),
        ("Le Rythme dans la Peau", "Coordonner des mouvements avec différents rythmes musicaux et percussions corporelles."),
        ("Jonglerie Débutant", "S'initier à la jonglerie avec des foulards puis des balles pour développer la coordination œil-main."),
        ("Multi-Tâches Motrices", "Réaliser deux actions motrices simultanées de complexité croissante."),
        ("La Danse Coordonnée", "Apprendre une chorégraphie simple qui sollicite la coordination globale du corps."),
        ("Le Parcours Coordination", "Enchaîner des actions motrices variées dans un parcours sollicitant la coordination."),
        ("Coordination et Rythme", "Synchroniser ses mouvements avec un partenaire sur des rythmes imposés."),
        ("Le Cirque des Habiletés", "Explorer des habiletés de cirque (assiettes chinoises, bâton du diable, diabolo)."),
        ("Défis de Dissociation", "Réaliser des mouvements différents avec le haut et le bas du corps simultanément."),
        ("La Corde à Sauter", "Maîtriser différentes techniques de saut à la corde (simple, croisé, double)."),
        ("Coordination Avancée", "Combiner des actions complexes sollicitant la coordination fine et globale."),
        ("Le Défi Ambidextre", "Développer l'habileté du côté non dominant à travers des exercices bilatéraux."),
    ],
    "Acrosport": [
        ("Les Petites Pyramides", "Découvrir les bases de l'acrosport en réalisant des figures simples à deux."),
        ("Figures à Trois", "Construire des figures acrosportives à trois avec des rôles définis (porteur, voltigeur, pareur)."),
        ("L'Acrosport en Équipe", "Créer des pyramides collectives en respectant les règles de sécurité."),
        ("Portés et Équilibres", "Apprendre les techniques de portés simples avec une progression sécuritaire."),
        ("Le Spectacle Acrosport", "Préparer un enchaînement acrosportif en groupe pour une présentation."),
        ("Acrosport et Musique", "Synchroniser un enchaînement acrosportif avec une trame musicale choisie."),
        ("Les Rôles en Acrosport", "Explorer les trois rôles (porteur, voltigeur, pareur) et développer les compétences de chacun."),
        ("Figures Dynamiques", "Intégrer des transitions et des éléments dynamiques entre les figures acrosportives."),
        ("Le Défi Pyramide", "Construire des pyramides de complexité croissante en respectant les principes de sécurité."),
        ("Acrosport Créatif", "Inventer de nouvelles figures acrosportives originales en duo ou trio."),
        ("Enchaînement Acrosport", "Composer et présenter un enchaînement complet incluant figures, transitions et éléments gymniques."),
        ("Acrosport Avancé", "Réaliser des figures acrosportives complexes avec éléments de voltige."),
    ],
    "Force": [
        ("Les Muscles Rigolos", "Découvrir les principaux muscles du corps par des exercices de renforcement ludiques."),
        ("Le Circuit des Costauds", "Réaliser un circuit de renforcement musculaire adapté avec le poids du corps."),
        ("Force et Jeux", "Développer la force à travers des jeux de traction, poussée et transport."),
        ("Les Super-Héros Musclés", "Exercices de renforcement inspirés des super-héros avec des postures de force."),
        ("Le Parcours de Force", "Enchaîner des stations de renforcement musculaire dans un parcours varié."),
        ("Musculation au Poids du Corps", "Apprendre les exercices de base au poids du corps (pompes, squats, fentes, tractions)."),
        ("Force et Endurance", "Combiner des exercices de force et d'endurance musculaire dans un circuit."),
        ("Le Cross-Training Junior", "Séance de cross-training adaptée aux jeunes avec exercices fonctionnels variés."),
        ("Renforcement et Prévention", "Développer la force musculaire ciblée pour la prévention des blessures."),
        ("Force du Haut du Corps", "Circuit spécifique pour le renforcement des bras, épaules et dos."),
        ("Force du Bas du Corps", "Circuit spécifique pour le renforcement des jambes et du bassin."),
        ("Force Fonctionnelle", "Développer la force à travers des mouvements fonctionnels et sportifs."),
    ],
    "Conditionnement physique": [
        ("Le Parcours Actif", "Réaliser un parcours d'activités physiques variées pour développer la condition physique."),
        ("Bouge ton Corps", "Séance d'activité physique globale avec exercices cardiovasculaires et musculaires adaptés."),
        ("Le Mini-Tabata", "S'initier au format Tabata avec des exercices simples et des temps adaptés aux jeunes."),
        ("Le Circuit Cardio", "Circuit d'exercices cardiovasculaires variés pour développer l'endurance."),
        ("HIIT Adapté", "Séance d'entraînement par intervalles de haute intensité adaptée au niveau des élèves."),
        ("Le Bootcamp Scolaire", "Séance d'entraînement de type bootcamp adaptée au contexte scolaire."),
        ("Tabata Challenge", "Séance Tabata complète avec 8 exercices différents en format 20s/10s."),
        ("Le Test de Condition", "Évaluer et améliorer les différentes composantes de la condition physique."),
        ("Cardio et Musculation", "Alterner exercices cardiovasculaires et musculaires dans un circuit complet."),
        ("Le Programme Personnel", "Créer son propre programme de conditionnement physique selon ses objectifs."),
        ("HIIT et Performance", "Séance HIIT avancée pour améliorer la capacité anaérobie et la puissance."),
        ("Conditionnement Complet", "Séance complète travaillant toutes les qualités physiques (force, endurance, souplesse, vitesse)."),
    ],
    "Relaxation": [
        ("Le Nuage Magique", "Séance de relaxation guidée avec visualisation pour apprendre à se détendre."),
        ("Respire et Calme-toi", "Découvrir différentes techniques de respiration pour gérer le stress et les émotions."),
        ("Le Corps au Repos", "Explorer la relaxation musculaire progressive de Jacobson adaptée aux enfants."),
        ("La Bulle de Calme", "Créer son espace de calme intérieur par des techniques de respiration et de visualisation."),
        ("Relaxation Musculaire", "Pratiquer la relaxation musculaire progressive en contractant puis relâchant chaque groupe musculaire."),
        ("Pleine Conscience Active", "Combiner des mouvements lents et conscients avec des techniques de respiration."),
        ("Le Voyage Intérieur", "Séance de visualisation guidée pour développer la conscience corporelle et le calme."),
        ("Respiration et Performance", "Apprendre des techniques de respiration pour optimiser la performance sportive."),
        ("Le Scan Corporel", "Pratiquer le scan corporel complet pour développer la conscience de chaque partie du corps."),
        ("Gestion du Stress", "Apprendre des techniques de relaxation pour gérer le stress en contexte sportif et scolaire."),
        ("Relaxation et Récupération", "Intégrer la relaxation dans une routine de récupération après l'effort."),
        ("Méditation et Sport", "Explorer la méditation de pleine conscience comme outil d'amélioration de la performance."),
    ],
    "Proprioception": [
        ("Les Pieds Malins", "Explorer les sensations sous les pieds en marchant sur différentes textures et surfaces."),
        ("L'Aveugle et le Guide", "Développer la proprioception en se déplaçant les yeux fermés avec l'aide d'un partenaire."),
        ("Équilibre sans les Yeux", "Réaliser des exercices d'équilibre avec privation visuelle progressive."),
        ("Les Surfaces Surprises", "Explorer l'équilibre et la stabilité sur des surfaces instables variées."),
        ("Le Parcours Sensoriel", "Traverser un parcours pieds nus sur des surfaces de textures et densités variées."),
        ("Proprioception et Sport", "Développer la proprioception spécifique à différentes disciplines sportives."),
        ("Le Défi des Sens", "Combiner privation visuelle et surfaces instables pour un défi proprioceptif complet."),
        ("Équilibre Réactif", "Développer les réactions d'équilibre face à des perturbations externes."),
        ("Proprioception Avancée", "Circuit de proprioception avancé avec exercices sur plateaux instables et bossu."),
        ("Le Corps Intelligent", "Développer la conscience corporelle et la proprioception par des exercices de perception."),
        ("Stabilité Dynamique", "Combiner mouvements et surfaces instables pour développer la stabilité en action."),
        ("Proprioception et Prévention", "Utiliser des exercices proprioceptifs pour la prévention des blessures articulaires."),
    ],
}

# Echauffement activities per cycle
echauffements = {
    "Maternelle": [
        "Jeu de tag doux avec déplacements variés (marcher comme un ours, sautiller comme un lapin).",
        "Ronde musicale avec mouvements de locomotion variés au son de la musique.",
        "Jeu du miroir : imiter les mouvements de l'enseignant (s'étirer, tourner, se pencher).",
        "Danse libre sur une musique entraînante avec consignes de mouvement.",
        "Jeu des animaux : se déplacer en imitant différents animaux nommés par l'enseignant.",
    ],
    "1er cycle primaire": [
        "Course légère autour du gymnase avec arrêts en position d'équilibre au signal.",
        "Jeu de la statue musicale avec positions de stabilisation imposées.",
        "Exercices de mobilisation articulaire guidés en cercle (cou, épaules, hanches, chevilles).",
        "Tag-équilibre : les joueurs touchés doivent tenir une posture d'équilibre 5 secondes.",
        "Parcours de locomotion avec des zones d'équilibre à traverser.",
    ],
    "2e cycle primaire": [
        "Course progressive avec exercices de mobilité articulaire intégrés (talons-fesses, montées de genoux).",
        "Jeu d'activation cardio-musculaire avec exercices au signal (jumping jacks, squats, fentes).",
        "Échauffement en duo avec exercices de mobilisation et d'étirements dynamiques.",
        "Parcours d'activation avec stations de mobilité et d'équilibre.",
        "Jeu du chef d'orchestre : un élève propose des mouvements d'échauffement que tous imitent.",
    ],
    "3e cycle primaire": [
        "Course d'activation avec exercices intégrés (pas chassés, carioca, talons-fesses, skipping).",
        "Circuit d'échauffement de 4 stations avec exercices de mobilisation spécifiques.",
        "Échauffement autonome guidé par une fiche avec exercices de mobilité articulaire.",
        "Jeu de poursuite avec contraintes de déplacement et arrêts en position de gainage.",
        "Routine d'échauffement dynamique en musique avec étirements balistiques contrôlés.",
    ],
    "1er cycle secondaire": [
        "Échauffement cardio progressif suivi d'exercices de mobilité articulaire dynamique.",
        "Routine d'activation musculaire avec bandes élastiques et exercices de stabilisation.",
        "Circuit d'échauffement spécifique incluant mobilité, activation et équilibre.",
        "Course progressive avec gammes athlétiques et exercices de coordination.",
        "Échauffement en autonomie avec routine personnalisée validée par l'enseignant.",
    ],
    "2e cycle secondaire": [
        "Échauffement auto-dirigé avec routine de mobilité et activation musculaire spécifique.",
        "Circuit d'activation neuromusculaire avec exercices de proprioception et stabilisation.",
        "Échauffement spécifique à la séance avec exercices progressifs ciblés.",
        "Routine de mobilité dynamique complète (foam roller, bandes, exercices articulaires).",
        "Échauffement en groupe avec leadership rotatif et exercices imposés par un élève.",
    ],
}

roles_enseignant = {
    "Échauffement": [
        "Dirige l'échauffement et s'assure de la participation de tous.",
        "Modélise les mouvements et encourage les élèves à bouger.",
        "Observe la participation et ajuste l'intensité selon le groupe.",
        "Circule et corrige les postures pendant l'échauffement.",
        "Anime l'échauffement avec énergie et dynamisme.",
    ],
    "Apprentissage": [
        "Démontre les techniques et fournit des rétroactions individuelles.",
        "Explique les consignes et vérifie la compréhension.",
        "Circule entre les élèves pour corriger et encourager.",
        "Propose des adaptations selon les niveaux des élèves.",
        "Guide les apprentissages par questionnement et démonstration.",
    ],
    "Mise en action": [
        "Supervise la pratique et intervient pour assurer la sécurité.",
        "Observe et évalue les élèves en action.",
        "Encourage l'effort et la persévérance des élèves.",
        "Ajuste les défis selon la progression des élèves.",
        "Facilite l'organisation et gère les transitions.",
    ],
    "Retour au calme": [
        "Guide le retour au calme avec une voix posée.",
        "Anime le bilan et questionne les élèves sur leurs apprentissages.",
        "Dirige les étirements et la relaxation finale.",
        "Fait un retour sur les objectifs de la séance et les progrès.",
        "Félicite les efforts et annonce la prochaine séance.",
    ],
}

materiel_by_moyen = {
    "Équilibre statique": ["Cônes", "Blocs de mousse", "Chronomètre", "Bancs suédois", "Demi-ballons d'équilibre", "Coussins d'équilibre", "Cerceaux"],
    "Équilibre dynamique": ["Poutres basses", "Bancs suédois", "Cônes", "Ruban adhésif", "Cordes", "Tapis de gymnastique", "Planches d'équilibre"],
    "Gainage": ["Tapis de sol", "Chronomètre", "Sifflet", "Musique", "Cônes", "Dés d'exercices", "Fiches d'exercices"],
    "Yoga": ["Tapis de yoga", "Musique relaxante", "Clochette", "Fiches de postures", "Coussins de méditation", "Couvertures"],
    "Gymnastique": ["Tapis de gymnastique", "Tremplin", "Poutre basse", "Cerceaux", "Cônes", "Fiches techniques"],
    "Souplesse": ["Tapis de sol", "Musique relaxante", "Bandes élastiques", "Blocs de yoga", "Chronomètre", "Fiches d'étirements"],
    "Coordination": ["Foulards de jonglerie", "Balles de tennis", "Cordes à sauter", "Cônes", "Musique rythmée", "Cerceaux", "Bâtons"],
    "Acrosport": ["Tapis de gymnastique épais", "Fiches de figures", "Musique", "Appareil photo/tablette", "Cônes de délimitation"],
    "Force": ["Tapis de sol", "Cônes", "Chronomètre", "Ballons médicinaux", "Bandes élastiques", "Bancs suédois", "Fiches d'exercices"],
    "Conditionnement physique": ["Chronomètre/minuteur", "Cônes", "Musique motivante", "Tapis de sol", "Cordes à sauter", "Cerceaux", "Sifflet"],
    "Relaxation": ["Tapis de sol", "Musique relaxante", "Couvertures", "Clochette ou bol tibétain", "Lumière tamisée (si possible)", "Coussins"],
    "Proprioception": ["Coussins d'équilibre", "Demi-ballons (Bosu)", "Plateaux d'équilibre", "Tapis texturés", "Bandeaux pour les yeux", "Cônes"],
}

savoirs_by_moyen = {
    "Équilibre statique": [
        ["Centre de gravité et base de sustentation", "Alignement corporel", "Contrôle postural"],
        ["Muscles stabilisateurs du tronc", "Regard fixe pour l'équilibre", "Respiration en posture statique"],
        ["Ajustement postural", "Tonus musculaire", "Concentration et équilibre"],
    ],
    "Équilibre dynamique": [
        ["Transfert de poids", "Déplacement du centre de gravité", "Ajustement postural en mouvement"],
        ["Coordination pieds-regard", "Rythme de déplacement", "Sécurité sur surfaces étroites"],
        ["Équilibre et vitesse", "Adaptation posturale", "Gestion de la hauteur"],
    ],
    "Gainage": [
        ["Position neutre de la colonne", "Engagement du transverse", "Respiration en gainage"],
        ["Muscles du tronc (abdominaux, dorsaux)", "Alignement corporel", "Endurance musculaire"],
        ["Progression en gainage", "Variantes de positions", "Auto-évaluation de la technique"],
    ],
    "Yoga": [
        ["Postures fondamentales du yoga", "Respiration abdominale", "Conscience corporelle"],
        ["Enchaînement de postures", "Coordination souffle-mouvement", "Relaxation"],
        ["Bienfaits du yoga sur le corps et l'esprit", "Philosophie du bien-être", "Pleine conscience"],
    ],
    "Gymnastique": [
        ["Éléments gymniques de base", "Règles de sécurité en gymnastique", "Roulade avant et arrière"],
        ["Appui tendu renversé", "Enchaînement gymnique", "Postures et alignements"],
        ["Figures acrobatiques", "Composition chorégraphique", "Critères de qualité d'exécution"],
    ],
    "Souplesse": [
        ["Principaux groupes musculaires", "Étirements statiques et dynamiques", "Respiration pendant l'étirement"],
        ["Amplitude articulaire", "Techniques d'étirement sécuritaires", "Échauffement avant étirement"],
        ["Souplesse active vs passive", "PNF et étirements avancés", "Programme de flexibilité"],
    ],
    "Coordination": [
        ["Dissociation segmentaire", "Coordination œil-main", "Rythme et tempo"],
        ["Latéralité et ambidextrie", "Coordination globale", "Synchronisation"],
        ["Coordination complexe", "Multi-tâches motrices", "Automatisation des gestes"],
    ],
    "Acrosport": [
        ["Rôles en acrosport (porteur, voltigeur, pareur)", "Règles de sécurité", "Communication entre partenaires"],
        ["Figures de base à 2 et 3", "Transitions entre figures", "Montage et démontage sécuritaire"],
        ["Composition acrosportive", "Éléments de liaison", "Critères esthétiques"],
    ],
    "Force": [
        ["Principaux groupes musculaires", "Techniques d'exercices au poids du corps", "Sécurité en musculation"],
        ["Surcharge progressive", "Récupération musculaire", "Exercices de renforcement ciblés"],
        ["Programme de musculation", "Principes d'entraînement", "Prévention des blessures"],
    ],
    "Conditionnement physique": [
        ["Fréquence cardiaque", "Composantes de la condition physique", "Intensité de l'effort"],
        ["Entraînement par intervalles", "Zone d'entraînement cible", "Récupération"],
        ["Planification d'entraînement", "Tests de condition physique", "Objectifs personnels"],
    ],
    "Relaxation": [
        ["Techniques de respiration", "Relaxation musculaire progressive", "Gestion du stress"],
        ["Visualisation guidée", "Conscience corporelle", "Bienfaits de la relaxation"],
        ["Pleine conscience", "Méditation", "Autorégulation émotionnelle"],
    ],
    "Proprioception": [
        ["Récepteurs sensoriels", "Équilibre et vision", "Surfaces d'appui"],
        ["Proprioception et prévention des blessures", "Ajustements posturaux réflexes", "Conscience corporelle"],
        ["Entraînement proprioceptif avancé", "Stabilité articulaire", "Réathlétisation"],
    ],
}

criteria_by_moyen = {
    "Équilibre statique": [
        "Maintient la posture d'équilibre pendant la durée demandée",
        "Adopte un alignement corporel adéquat",
        "Utilise son regard pour stabiliser son équilibre",
        "Contrôle sa respiration en posture statique",
        "Ajuste sa posture en fonction de la surface d'appui",
    ],
    "Équilibre dynamique": [
        "Se déplace avec fluidité sur les surfaces d'équilibre",
        "Maintient son centre de gravité au-dessus de sa base de sustentation",
        "Adapte sa vitesse de déplacement à la surface",
        "Utilise ses bras pour maintenir son équilibre en mouvement",
        "Traverse le parcours sans chuter ni poser le pied au sol",
    ],
    "Gainage": [
        "Maintient l'alignement tête-épaules-hanches-chevilles en position de planche",
        "Engage les muscles du tronc de façon visible et soutenue",
        "Respire régulièrement pendant les exercices de gainage",
        "Tient les positions pendant la durée prescrite",
        "Effectue les transitions entre positions avec contrôle",
    ],
    "Yoga": [
        "Reproduit les postures avec une forme reconnaissable",
        "Coordonne sa respiration avec ses mouvements",
        "Maintient chaque posture avec stabilité",
        "Respecte l'atmosphère calme et concentrée de la séance",
        "Crée un enchaînement fluide entre les postures",
    ],
    "Gymnastique": [
        "Exécute les éléments gymniques avec une technique sécuritaire",
        "Maintient un alignement corporel adéquat pendant les figures",
        "Enchaîne les éléments avec fluidité",
        "Respecte les règles de sécurité en tout temps",
        "Présente son enchaînement avec assurance et contrôle",
    ],
    "Souplesse": [
        "Réalise les étirements avec une technique appropriée",
        "Respecte ses limites personnelles de souplesse",
        "Maintient chaque étirement pendant la durée demandée",
        "Respire de façon régulière pendant les étirements",
        "Progresse dans son amplitude articulaire au fil des séances",
    ],
    "Coordination": [
        "Coordonne efficacement les mouvements du haut et du bas du corps",
        "Synchronise ses mouvements avec le rythme donné",
        "Exécute les tâches motrices avec précision",
        "Adapte ses mouvements à différents tempos",
        "Réalise des actions motrices simultanées avec contrôle",
    ],
    "Acrosport": [
        "Assume son rôle (porteur, voltigeur ou pareur) avec responsabilité",
        "Respecte les règles de sécurité lors des montages et démontages",
        "Communique efficacement avec ses partenaires",
        "Maintient les figures avec stabilité et contrôle",
        "Contribue activement à la création de l'enchaînement du groupe",
    ],
    "Force": [
        "Exécute les exercices de renforcement avec une technique appropriée",
        "Maintient un alignement corporel sécuritaire pendant les exercices",
        "Dose son effort selon ses capacités personnelles",
        "Complète le circuit avec persévérance et engagement",
        "Respire adéquatement pendant les exercices de force",
    ],
    "Conditionnement physique": [
        "Maintient une intensité d'effort appropriée pendant la séance",
        "Exécute les exercices avec une technique correcte",
        "Gère son effort sur la durée de la séance",
        "Respecte les temps de travail et de repos prescrits",
        "Démontre de l'engagement et de la persévérance",
    ],
    "Relaxation": [
        "Adopte une attitude calme et respectueuse pendant la séance",
        "Applique les techniques de respiration enseignées",
        "Détend progressivement chaque partie de son corps",
        "Reste immobile et concentré pendant les exercices de relaxation",
        "Identifie les bienfaits de la relaxation sur son corps et son esprit",
    ],
    "Proprioception": [
        "Maintient son équilibre sur des surfaces instables",
        "Ajuste sa posture en réponse aux déséquilibres",
        "Réalise les exercices les yeux fermés avec contrôle",
        "Progresse dans la difficulté des exercices proprioceptifs",
        "Décrit ses sensations corporelles pendant les exercices",
    ],
}

idx = 0
for ci, (cycle, niveau, duree) in enumerate(cycles):
    n = counts[ci]
    # Distribute moyens across this cycle
    for j in range(n):
        moyen_idx = j % len(moyens)
        moyen = moyens[moyen_idx]

        # Pick title/desc from the moyen's list
        title_idx = (ci * 2 + j // len(moyens)) % len(titles_by_moyen[moyen])
        title, desc = titles_by_moyen[moyen][title_idx]

        # Make titles more unique by adding cycle-specific suffixes if needed
        cycle_suffix = {
            "Maternelle": " — Éveil",
            "1er cycle primaire": " — Initiation",
            "2e cycle primaire": " — Exploration",
            "3e cycle primaire": " — Consolidation",
            "1er cycle secondaire": " — Approfondissement",
            "2e cycle secondaire": " — Maîtrise",
        }

        # Only add suffix if title would be duplicate
        full_title = title + cycle_suffix[cycle]

        idx += 1
        sae_id = f"STAB-{idx:03d}"

        duree_min = duree
        if duree == "30 min":
            total_min = 30
        elif duree == "45 min":
            total_min = 45
        else:
            total_min = 60

        # Phase durations
        if total_min == 30:
            phases_dur = [("5 min", "10 min", "10 min", "5 min")]
        elif total_min == 45:
            phases_dur = [("7 min", "15 min", "15 min", "8 min")]
        else:
            phases_dur = [("8 min", "20 min", "22 min", "10 min")]

        pd = phases_dur[0]

        ech_list = echauffements[cycle]
        ech_act = ech_list[j % len(ech_list)]

        role_ech = roles_enseignant["Échauffement"][j % len(roles_enseignant["Échauffement"])]
        role_app = roles_enseignant["Apprentissage"][j % len(roles_enseignant["Apprentissage"])]
        role_mise = roles_enseignant["Mise en action"][j % len(roles_enseignant["Mise en action"])]
        role_ret = roles_enseignant["Retour au calme"][j % len(roles_enseignant["Retour au calme"])]

        # Build specific apprentissage and mise en action activities
        apprentissage_templates = {
            "Équilibre statique": [
                f"Les élèves explorent différentes postures d'équilibre sur un pied, sur la pointe des pieds et sur des surfaces variées. L'enseignant présente 4 à 5 postures à reproduire et à maintenir.",
                f"Introduction des positions d'équilibre statique avec progression : deux pieds, un pied, yeux ouverts puis fermés. Les élèves pratiquent en ateliers.",
            ],
            "Équilibre dynamique": [
                f"Les élèves s'exercent à marcher sur des lignes au sol, puis sur des bancs suédois retournés. Progression : marche avant, arrière, latérale.",
                f"Présentation du parcours d'équilibre avec démonstration de chaque station. Les élèves pratiquent par vagues de 3-4.",
            ],
            "Gainage": [
                f"L'enseignant présente les positions de gainage (planche, planche latérale, superman). Les élèves pratiquent chaque position avec des temps progressifs.",
                f"Apprentissage des positions de base du gainage avec attention portée à l'alignement corporel et à la respiration.",
            ],
            "Yoga": [
                f"Introduction de 5 à 6 postures de yoga avec démonstration et pratique guidée. Chaque posture est tenue 3 à 5 respirations.",
                f"Les élèves apprennent un enchaînement de postures de yoga en suivant les indications de l'enseignant.",
            ],
            "Gymnastique": [
                f"Progression pédagogique vers l'élément gymnique ciblé avec exercices préparatoires et éducatifs. Travail en ateliers avec parade.",
                f"Démonstration de la technique puis pratique guidée en ateliers. L'enseignant circule pour corriger et sécuriser.",
            ],
            "Souplesse": [
                f"Les élèves apprennent les techniques d'étirement appropriées pour chaque groupe musculaire ciblé. L'enseignant insiste sur la respiration.",
                f"Présentation d'une routine d'étirements complète avec explications sur les muscles étirés et les consignes de sécurité.",
            ],
            "Coordination": [
                f"Les élèves s'exercent à réaliser des mouvements de coordination progressifs, d'abord simples puis de plus en plus complexes.",
                f"Ateliers de coordination avec des exercices ciblés. Les élèves progressent à leur rythme dans la difficulté.",
            ],
            "Acrosport": [
                f"Présentation des rôles (porteur, voltigeur, pareur) et des règles de sécurité. Apprentissage des figures de base en duo ou trio.",
                f"Les élèves apprennent les techniques de montage et démontage sécuritaires avec des figures adaptées à leur niveau.",
            ],
            "Force": [
                f"L'enseignant présente les exercices de renforcement au poids du corps avec démonstration de la bonne technique pour chacun.",
                f"Apprentissage des exercices de renforcement musculaire ciblés avec correction individuelle de la technique.",
            ],
            "Conditionnement physique": [
                f"Présentation du circuit d'entraînement avec démonstration de chaque exercice. Les élèves pratiquent chaque station à faible intensité.",
                f"Les élèves apprennent le format de la séance (travail/repos) et les exercices prescrits avec la bonne technique.",
            ],
            "Relaxation": [
                f"L'enseignant guide les élèves dans l'apprentissage d'une technique de relaxation (respiration, relaxation musculaire, visualisation).",
                f"Introduction des techniques de respiration et de détente avec pratique guidée étape par étape.",
            ],
            "Proprioception": [
                f"Les élèves explorent les surfaces instables et apprennent à maintenir leur équilibre en ajustant leur posture.",
                f"Présentation des exercices proprioceptifs avec progression : yeux ouverts sur surface stable, puis surface instable, puis yeux fermés.",
            ],
        }

        mise_action_templates = {
            "Équilibre statique": [
                f"Défi d'équilibre : les élèves tentent de maintenir différentes postures le plus longtemps possible. Travail en duo avec observation et rétroaction.",
                f"Circuit de stations d'équilibre statique avec des défis de durée et de complexité croissante.",
            ],
            "Équilibre dynamique": [
                f"Les élèves réalisent le parcours d'équilibre complet en enchaînant les éléments. Défi de fluidité et de contrôle.",
                f"Relais par équipes sur le parcours d'équilibre. Les élèves s'encouragent et s'entraident.",
            ],
            "Gainage": [
                f"Circuit de gainage avec 4 à 6 stations. Les élèves travaillent en duo (un travaille, l'autre chronomètre et corrige).",
                f"Défi collectif de gainage : accumuler le plus de secondes possible en équipe avec des positions variées.",
            ],
            "Yoga": [
                f"Les élèves créent leur propre enchaînement de 5 postures et le présentent à un partenaire ou au groupe.",
                f"Pratique autonome de la séquence de yoga apprise avec possibilité d'ajouter des postures personnelles.",
            ],
            "Gymnastique": [
                f"Les élèves pratiquent l'enchaînement ou l'élément gymnique ciblé de façon autonome avec parade d'un pair.",
                f"Présentation de l'élément gymnique travaillé devant un petit groupe avec rétroaction des pairs.",
            ],
            "Souplesse": [
                f"Les élèves réalisent la routine d'étirements de façon autonome en duo. L'un s'étire, l'autre vérifie la posture.",
                f"Circuit de souplesse avec stations ciblant différents groupes musculaires. Auto-évaluation de la progression.",
            ],
            "Coordination": [
                f"Défis de coordination en ateliers avec progression dans la difficulté. Les élèves tentent de maîtriser le niveau suivant.",
                f"Jeu ou parcours intégrant les habiletés de coordination pratiquées. Travail individuel ou en équipe.",
            ],
            "Acrosport": [
                f"Les groupes créent un enchaînement de 3 à 4 figures acrosportives avec des transitions. Répétitions et ajustements.",
                f"Présentation des figures acrosportives devant le groupe avec évaluation par les pairs.",
            ],
            "Force": [
                f"Circuit de renforcement musculaire complet. Les élèves passent d'une station à l'autre au signal.",
                f"Défi de force en duo : les élèves se motivent mutuellement et notent leurs résultats.",
            ],
            "Conditionnement physique": [
                f"Réalisation du circuit complet à l'intensité prescrite. Les élèves gèrent leur effort sur la durée de la séance.",
                f"Séance d'entraînement par intervalles avec exercices variés. Les élèves travaillent à leur intensité cible.",
            ],
            "Relaxation": [
                f"Pratique autonome des techniques de relaxation apprises. Les élèves identifient celles qui leur conviennent le mieux.",
                f"Séance de relaxation guidée complète avec musique douce et lumière tamisée.",
            ],
            "Proprioception": [
                f"Parcours proprioceptif complet avec stations de difficulté progressive. Les élèves notent leur niveau atteint.",
                f"Défis proprioceptifs en duo : un élève crée un défi d'équilibre que l'autre doit relever.",
            ],
        }

        retour_calme_templates = [
            f"Étirements légers des principaux groupes musculaires sollicités. Retour en cercle pour un bilan verbal de la séance.",
            f"Relaxation guidée au sol avec respiration profonde. Discussion sur les apprentissages réalisés.",
            f"Marche lente autour du gymnase avec respiration consciente. Bilan de la séance et annonce de la suivante.",
            f"Étirements en duo et partage des réussites de la séance. L'enseignant fait un retour sur les objectifs.",
            f"Exercices de respiration et retour au calme progressif. Les élèves identifient ce qu'ils ont appris.",
        ]

        app_act = apprentissage_templates[moyen][j % len(apprentissage_templates[moyen])]
        mise_act = mise_action_templates[moyen][j % len(mise_action_templates[moyen])]
        ret_act = retour_calme_templates[j % len(retour_calme_templates)]

        # Context
        contextes = [
            f"Les élèves sont invités à développer leur stabilité corporelle à travers des activités de {moyen.lower()} adaptées à leur niveau.",
            f"Dans un contexte ludique et sécuritaire, les élèves explorent les possibilités de stabilisation de leur corps par le {moyen.lower()}.",
            f"L'enseignant propose une situation d'apprentissage centrée sur le {moyen.lower()} pour développer la compétence de stabilisation.",
        ]
        contexte = contextes[j % len(contextes)]

        # Tâche complexe
        taches = {
            "Équilibre statique": "L'élève doit démontrer sa capacité à maintenir au moins 3 postures d'équilibre statique pendant une durée minimale, en utilisant des stratégies d'ajustement postural.",
            "Équilibre dynamique": "L'élève doit traverser un parcours d'équilibre dynamique en maintenant une posture stable et en adaptant ses déplacements aux surfaces rencontrées.",
            "Gainage": "L'élève doit réaliser un circuit de gainage en maintenant un alignement corporel adéquat et en respectant les temps de maintien prescrits.",
            "Yoga": "L'élève doit exécuter un enchaînement de postures de yoga en coordonnant sa respiration avec ses mouvements et en maintenant chaque posture avec stabilité.",
            "Gymnastique": "L'élève doit réaliser un enchaînement gymnique comprenant les éléments travaillés en respectant les critères techniques et de sécurité.",
            "Souplesse": "L'élève doit démontrer sa capacité à réaliser une routine d'étirements complète en respectant les techniques appropriées et ses limites personnelles.",
            "Coordination": "L'élève doit exécuter des tâches de coordination de complexité croissante en démontrant sa capacité à dissocier et synchroniser ses mouvements.",
            "Acrosport": "L'élève doit participer à la création et à la présentation d'un enchaînement acrosportif en assumant ses rôles avec responsabilité et sécurité.",
            "Force": "L'élève doit compléter un circuit de renforcement musculaire en démontrant une technique d'exécution sécuritaire et un engagement soutenu.",
            "Conditionnement physique": "L'élève doit réaliser la séance d'entraînement en maintenant une intensité appropriée et en exécutant les exercices avec une technique correcte.",
            "Relaxation": "L'élève doit démontrer sa capacité à appliquer les techniques de relaxation enseignées et à identifier leurs effets sur son corps et son esprit.",
            "Proprioception": "L'élève doit réaliser des exercices proprioceptifs de difficulté progressive en démontrant sa capacité à ajuster sa posture et maintenir son équilibre.",
        }

        savoirs = savoirs_by_moyen[moyen][j % len(savoirs_by_moyen[moyen])]
        criteres = random.sample(criteria_by_moyen[moyen], 3)
        mat = random.sample(materiel_by_moyen[moyen], min(4, len(materiel_by_moyen[moyen])))

        tags = ["stabilisation", moyen.lower().replace("é", "e").replace("è", "e").replace("ê", "e")]
        if moyen in ["Yoga", "Relaxation"]:
            tags.append("bien-être")
        elif moyen in ["Gainage", "Force", "Conditionnement physique"]:
            tags.append("renforcement")
        elif moyen in ["Équilibre statique", "Équilibre dynamique", "Proprioception"]:
            tags.append("équilibre")
        elif moyen in ["Gymnastique", "Acrosport"]:
            tags.append("acrobatie")
        else:
            tags.append("motricité")

        duree_periodes = 1 if total_min <= 45 else random.choice([1, 2])

        sae_entry = {
            "id": sae_id,
            "titre": full_title,
            "cycle": cycle,
            "niveau": niveau,
            "duree_periodes": duree_periodes,
            "duree_par_periode": duree_min,
            "moyen_action": moyen,
            "competence_pfeq": "Agir dans divers contextes de pratique d'activités physiques",
            "description": desc,
            "contexte_apprentissage": contexte,
            "tache_complexe": taches[moyen],
            "criteres_evaluation": criteres,
            "savoirs_essentiels": savoirs,
            "progression": [
                {"phase": "Échauffement", "duree": pd[0], "activite": ech_act, "role_enseignant": role_ech},
                {"phase": "Apprentissage", "duree": pd[1], "activite": app_act, "role_enseignant": role_app},
                {"phase": "Mise en action", "duree": pd[2], "activite": mise_act, "role_enseignant": role_mise},
                {"phase": "Retour au calme", "duree": pd[3], "activite": ret_act, "role_enseignant": role_ret},
            ],
            "materiel": mat,
            "espace": "Gymnase",
            "tags": tags,
        }

        sae_list.append(sae_entry)

# Now make all titles truly unique
seen_titles = {}
for s in sae_list:
    t = s["titre"]
    if t in seen_titles:
        seen_titles[t] += 1
        s["titre"] = t + f" (variante {seen_titles[t]})"
    else:
        seen_titles[t] = 0

output = {
    "domaine": "Stabilisation — Bonification",
    "total_sae": 140,
    "programme": "PFEQ — Éducation physique et à la santé",
    "sae": sae_list
}

with open("/Users/admin/PROJETS_CLAUDE/app-sae/data/sae/stabilisation_bonus.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Generated {len(sae_list)} SAÉ entries")
# Verify distribution
from collections import Counter
cycle_counts = Counter(s["cycle"] for s in sae_list)
moyen_counts = Counter(s["moyen_action"] for s in sae_list)
print("\nDistribution par cycle:")
for c, n in sorted(cycle_counts.items()):
    print(f"  {c}: {n}")
print("\nDistribution par moyen d'action:")
for m, n in sorted(moyen_counts.items()):
    print(f"  {m}: {n}")
print("\nTitres uniques:", len(set(s["titre"] for s in sae_list)))
