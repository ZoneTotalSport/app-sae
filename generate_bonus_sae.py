#!/usr/bin/env python3
"""
Générateur de SAÉ bonus pour l'app-sae.
Génère 6 fichiers JSON × 140 SAÉ = 840 SAÉ au total.
Catégories: Manipulation, Locomotion, Stabilisation, Opposition, Coopération, Expression.
"""

import json
import os
import random
import itertools

random.seed(42)  # Reproductibilité

OUTPUT_DIR = "/Users/admin/PROJETS_CLAUDE/app-sae/data/sae"

# ============================================================
# CYCLES & NIVEAUX
# ============================================================
CYCLES = [
    {"cycle": "Maternelle", "niveau": "4-5 ans", "duree_par_periode": "30 min", "duree_periodes": 1,
     "echauffement": "5 min", "apprentissage": "10 min", "mise_en_action": "10 min", "retour": "5 min"},
    {"cycle": "1er cycle primaire", "niveau": "6-7 ans", "duree_par_periode": "30 min", "duree_periodes": 1,
     "echauffement": "5 min", "apprentissage": "10 min", "mise_en_action": "10 min", "retour": "5 min"},
    {"cycle": "2e cycle primaire", "niveau": "8-9 ans", "duree_par_periode": "45 min", "duree_periodes": 1,
     "echauffement": "5 min", "apprentissage": "15 min", "mise_en_action": "15 min", "retour": "5 min"},  # was missing 5
    {"cycle": "3e cycle primaire", "niveau": "10-11 ans", "duree_par_periode": "45 min", "duree_periodes": 1,
     "echauffement": "5 min", "apprentissage": "15 min", "mise_en_action": "20 min", "retour": "5 min"},
    {"cycle": "1er cycle secondaire", "niveau": "12-13 ans", "duree_par_periode": "60 min", "duree_periodes": 1,
     "echauffement": "10 min", "apprentissage": "15 min", "mise_en_action": "25 min", "retour": "10 min"},
    {"cycle": "2e cycle secondaire", "niveau": "14-16 ans", "duree_par_periode": "60 min", "duree_periodes": 2,
     "echauffement": "10 min", "apprentissage": "15 min", "mise_en_action": "25 min", "retour": "10 min"},
]

# 24 per cycle (first 4 get 23, last 2 get 24) => 23*4 + 24*2 = 140... actually let's do 23,23,24,23,24,23=140
SAE_PER_CYCLE = [23, 23, 24, 23, 24, 23]  # = 140

# ============================================================
# COMPETENCES PFEQ
# ============================================================
COMP_AGIR = "Agir dans divers contextes de pratique d'activités physiques"
COMP_INTERAGIR = "Interagir dans divers contextes de pratique d'activités physiques"
COMP_ADOPTER = "Adopter un mode de vie sain et actif"


def pick(lst):
    """Pick a random item from a list."""
    return random.choice(lst)


def pick_n(lst, n):
    """Pick n unique items from a list (with cycling if needed)."""
    if n <= len(lst):
        return random.sample(lst, n)
    result = list(lst)
    random.shuffle(result)
    while len(result) < n:
        result.extend(random.sample(lst, min(n - len(result), len(lst))))
    return result[:n]


# ============================================================
# CATEGORY DEFINITIONS
# ============================================================

# ------ MANIPULATION ------
MANIPULATION = {
    "file": "manipulation_bonus.json",
    "prefix": "MANB",
    "domaine": "Manipulation d'objets — Bonification",
    "competence": COMP_AGIR,
    "moyens_action": [
        "Lancer", "Attraper", "Dribler", "Frapper (raquette)",
        "Frapper (bâton)", "Jongler", "Corde à sauter", "Cerceau",
        "Cirque", "Volleyball", "Basketball manipulation", "Hockey"
    ],
    "title_templates": [
        "Le cirque des {obj}", "Festival de {action}", "Défi {action} extrême",
        "La ronde des {obj}", "Mission {action}", "Les artistes du {obj}",
        "Parcours {action}", "Tournoi des {obj}", "L'atelier du {action}",
        "Les magiciens du {obj}", "Aventure {action}", "Le grand {action}",
        "Les acrobates du {obj}", "Champion de {action}", "La quête du {obj}",
        "Les virtuoses du {action}", "Expédition {obj}", "Le labo du {action}",
        "Les explorateurs du {obj}", "Course aux {obj}", "Le défi des {obj}",
        "Les jongleurs de {obj}", "La danse des {obj}", "Les lanceurs d'élite",
    ],
    "title_objects": [
        "ballons", "balles", "cerceaux", "quilles", "anneaux", "foulards",
        "raquettes", "bâtons", "poches de sable", "frisbees", "diabolos",
        "assiettes chinoises", "cordes", "rubans", "massues",
    ],
    "title_actions": [
        "lancer", "jonglerie", "driblage", "frappe", "réception",
        "manipulation", "contrôle", "acrobatie", "précision", "adresse",
        "coordination", "agilité", "passes", "rebonds", "attrapés",
    ],
    "materiel_bank": [
        "Ballons en mousse", "Balles de tennis", "Cônes", "Cerceaux",
        "Poches de sable", "Raquettes de badminton", "Bâtons de hockey",
        "Sifflet", "Dossards", "Quilles", "Cordes à sauter", "Foulards",
        "Paniers de basketball", "Anneaux", "Frisbees", "Filet de volleyball",
        "Cibles murales", "Ballons de volleyball", "Ballons de basketball",
        "Ruban adhésif pour lignes", "Chronomètre", "Balles de jonglage",
    ],
    "criteres_bank": [
        "Précision du lancer vers la cible", "Fluidité du mouvement de manipulation",
        "Coordination œil-main lors de la réception", "Contrôle de l'objet en mouvement",
        "Adaptation du geste à la distance", "Rythme régulier dans la manipulation",
        "Variété des techniques utilisées", "Transfert de poids lors du lancer",
        "Capacité à ajuster la force du geste", "Positionnement du corps face à la cible",
        "Réception souple avec amortissement", "Enchaînement fluide de deux actions",
        "Maintien du contrôle sous pression", "Utilisation des deux mains",
        "Anticipation de la trajectoire de l'objet",
    ],
    "savoirs_bank": [
        "Prise de l'objet adaptée", "Trajectoire de lancer", "Positionnement des mains pour la réception",
        "Transfert de poids avant-arrière", "Coordination œil-main", "Rythme et tempo",
        "Dosage de la force", "Utilisation de l'espace", "Amortissement à la réception",
        "Rotation du poignet", "Suivi visuel de l'objet", "Équilibre dynamique",
        "Placement des pieds", "Phases du mouvement (préparation, exécution, suivi)",
        "Sécurité avec le matériel",
    ],
    "echauffement_bank": {
        "young": [
            "Jeu du chat-souris avec une balle en mousse — les enfants se passent la balle pour éviter le chat",
            "Course libre avec un ballon en mousse : le tenir, le lancer en l'air et le rattraper en marchant",
            "Manipulation libre de balles : rouler, lancer doucement, faire rebondir au sol",
            "Jeu du facteur avec des poches de sable — déposer et ramasser en courant",
            "Marche en cercle en se passant un ballon de main en main autour du corps",
        ],
        "mid": [
            "Échauffement avec balle : jongler à une main, lancer-rattraper en marchant, passes murales",
            "Circuit de manipulation : 30 s de drible, 30 s de lancer-cible, 30 s de jonglage",
            "Passes en duo en se déplaçant dans le gymnase — varier les types de passes",
            "Jeu de la bombe : se passer la balle rapidement en cercle au signal du sifflet",
            "Exercices de coordination : lancer une balle, frapper des mains, rattraper",
        ],
        "old": [
            "Échauffement technique : 2 minutes de drible dominant, 2 minutes non-dominant, 2 minutes d'alternance",
            "Passes en déplacement par groupes de 3 avec changement de direction au signal",
            "Routine de manipulation progressive : sol, taille, épaule, au-dessus de la tête",
            "Travail de passes murales en variant distances et angles — 3 séries de 10",
            "Jeu de rapidité : lancer et rattraper avant que la balle rebondisse 2 fois",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Exploration des lancers : par en dessous, par-dessus, à deux mains vers une grande cible murale",
            "Atelier de réception : l'enseignant lance doucement, l'enfant attrape avec les deux mains formant un panier",
            "Jeu de roulade : faire rouler une balle vers un partenaire assis à 3 mètres, alterner",
            "Manipulation de foulards : lancer en l'air et rattraper avant qu'ils touchent le sol",
            "Dribler un ballon léger en marchant entre des cônes espacés",
        ],
        "mid": [
            "Travail en ateliers tournants : lancer précis, drible slalom, réception en mouvement, frappe de raquette",
            "Pratique de passes à rebond et passes directes en duo — 10 de chaque type",
            "Exercice de précision : lancer dans des cerceaux posés au sol à distances croissantes",
            "Apprentissage de la jonglerie : cascade à 2 balles, progression étape par étape",
            "Technique de frappe avec raquette : coup droit de base, position latérale, suivi du geste",
        ],
        "old": [
            "Perfectionnement technique : analyse vidéo du geste de lancer et correction par les pairs",
            "Ateliers de manipulation avancée : jonglage 3 objets, drible des deux mains, passes longues précises",
            "Travail tactique : choisir le type de passe en fonction de la situation de jeu (simulation)",
            "Exercices de précision sous pression : atteindre des cibles en mouvement ou avec décompte",
            "Technique de frappe au bâton : transfert de poids, rotation des hanches, suivi du regard",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Jeu du trésor : les enfants lancent des poches de sable dans des cerceaux-coffres pour marquer des points",
            "Parcours de manipulation : lancer dans un cerceau, dribler entre cônes, rouler vers un partenaire",
            "Match de passes : en équipes, se faire 10 passes sans échapper la balle pour gagner un point",
            "Le bowling humain : lancer une balle pour faire tomber des quilles placées en triangle",
            "Jeu de la cible magique : chaque zone de couleur donne un nombre de points différent",
        ],
        "mid": [
            "Tournoi de précision : compétition amicale de lancers vers des cibles à différentes distances",
            "Mini-match de volleyball adapté avec ballon en mousse — service par en dessous obligatoire",
            "Jeu de la balle au capitaine : réussir 5 passes pour marquer, l'adversaire tente d'intercepter",
            "Relais de manipulation : drible-slalom, lancer-cible, réception-course — équipes de 4",
            "Match de hockey avec balles en mousse : mini-matchs de 3 contre 3 sur terrain réduit",
        ],
        "old": [
            "Matchs de volleyball 4 contre 4 avec rotation obligatoire et statistiques individuelles",
            "Tournoi de badminton en simple : matchs de 11 points avec arbitrage par les pairs",
            "Situation de jeu complexe : 4 contre 4 avec contraintes tactiques (3 passes minimum avant le tir)",
            "Match de basketball 3 contre 3 : demi-terrain avec règles adaptées et rôles définis",
            "Défi d'adresse chrono : circuit de 6 stations techniques, meilleur temps cumulé",
        ],
    },
    "retour_bank": {
        "young": [
            "En cercle, rouler doucement une balle vers le centre tout en respirant calmement",
            "Étirements doux en imitant des animaux qui s'étirent (chat, chien, tortue) avec la balle à côté",
            "Assis en cercle, nommer une chose qu'on a aimée et une chose qu'on a trouvée difficile",
            "Respiration profonde : gonfler un ballon imaginaire avec le ventre, le dégonfler lentement",
        ],
        "mid": [
            "Étirements en duo avec le matériel utilisé comme appui — discussion sur les réussites du cours",
            "Retour verbal : chaque élève nomme une technique améliorée aujourd'hui",
            "Relaxation au sol : respiration abdominale, relâchement progressif de chaque partie du corps",
            "Jeu calme de passes lentes en cercle avec un compliment à chaque réception",
        ],
        "old": [
            "Étirements complets guidés par un élève volontaire — 30 secondes par groupe musculaire",
            "Retour réflexif : journal d'apprentissage — noter 2 points forts et 1 objectif d'amélioration",
            "Discussion tactique : analyse de séquences de jeu observées pendant le cours",
            "Relaxation guidée avec musique calme — visualisation de gestes techniques réussis",
        ],
    },
}

# ------ LOCOMOTION ------
LOCOMOTION = {
    "file": "locomotion_bonus.json",
    "prefix": "LOCB",
    "domaine": "Locomotion — Bonification",
    "competence": COMP_AGIR,
    "moyens_action": [
        "Courir (vitesse)", "Courir (endurance)", "Sauter", "Ramper / grimper",
        "Esquiver", "Relais", "Parcours d'obstacles", "Déplacements variés",
        "Course d'orientation", "Athlétisme", "Poursuite / tag", "Danse locomotrice"
    ],
    "title_templates": [
        "La course des {obj}", "Parcours {action}", "Défi {action}",
        "Le marathon des {obj}", "Mission {action}", "L'aventure {action}",
        "Le grand relais des {obj}", "Sprint {action}", "Le labyrinthe des {obj}",
        "Rallye {action}", "La jungle des {obj}", "L'expédition {action}",
        "Les coureurs de {obj}", "Le sentier des {obj}", "La traversée {action}",
        "Les ninjas de {action}", "La piste des {obj}", "Les sprinters du {obj}",
        "Course folle des {obj}", "Le circuit des {obj}", "Les gazelles du gymnase",
        "Défi vitesse {action}", "Le parcours du combattant", "L'obstacle course des {obj}",
    ],
    "title_objects": [
        "obstacles", "cônes", "cerceaux", "tapis", "bancs", "cordes",
        "haies", "échelles", "tunnels", "tremplins", "sentiers", "montagnes",
        "forêts", "volcans", "étoiles",
    ],
    "title_actions": [
        "locomotion", "sprint", "endurance", "sauts", "esquive",
        "agilité", "exploration", "poursuite", "course", "relais",
        "vitesse", "obstacles", "orientation", "déplacements", "acrobatique",
    ],
    "materiel_bank": [
        "Cônes", "Cerceaux", "Tapis de gymnastique", "Bancs suédois",
        "Cordes à sauter", "Haies basses", "Échelle d'agilité", "Sifflet",
        "Chronomètre", "Dossards", "Plots", "Rubans de marquage",
        "Ballons", "Sacs de fèves", "Craies", "Cartes d'orientation",
        "Boussoles", "Drapeaux de couleur", "Bâtons de relais", "Tremplins",
    ],
    "criteres_bank": [
        "Fluidité des déplacements", "Vitesse d'exécution", "Coordination des mouvements",
        "Enchaînement sans interruption", "Réception stable après un saut",
        "Adaptation du rythme de course", "Utilisation de l'espace disponible",
        "Respect de la technique de course", "Synchronisation dans le relais",
        "Changement de direction rapide et contrôlé", "Endurance maintenue durant l'activité",
        "Technique de saut (appel, envol, réception)", "Orientation dans l'espace",
        "Réaction rapide au signal", "Placement du pied à l'appel",
    ],
    "savoirs_bank": [
        "Technique de course (bras, posture)", "Foulée adaptée à la vitesse",
        "Phases du saut (élan, appel, envol, réception)", "Rythme respiratoire en endurance",
        "Déplacements latéraux et arrière", "Changement de direction",
        "Coordination bras-jambes", "Répartition de l'effort", "Prise d'élan",
        "Proprioception en mouvement", "Conscience spatiale", "Lecture de carte simple",
        "Transmission du bâton de relais", "Gainage en mouvement",
        "Sécurité lors des sauts et réceptions",
    ],
    "echauffement_bank": {
        "young": [
            "Jeu du feu rouge / feu vert : courir au vert, marcher au jaune, s'arrêter au rouge",
            "Imiter des animaux qui se déplacent : galoper comme un cheval, sauter comme un lapin, ramper comme un serpent",
            "Course en cercle en changeant de direction au coup de sifflet",
            "Marche rapide puis trot léger avec arrêts-statues sur commande",
            "Sauter par-dessus des lignes au sol comme des grenouilles sur des nénuphars",
        ],
        "mid": [
            "Course progressive : 1 minute marche, 1 minute trot, 1 minute course légère",
            "Échauffement par ateliers : sauts sur place, pas chassés, genoux hauts, talons-fesses",
            "Jeu de l'épervier simplifié : traverser le gymnase sans se faire toucher",
            "Course en slalom entre les cônes avec changements de rythme au signal",
            "Exercices de coordination : pas croisés, galop latéral, course arrière",
        ],
        "old": [
            "Course continue 5 minutes avec variations d'allure toutes les minutes",
            "Échauffement technique d'athlétisme : montées de genoux, talons-fesses, pas chassés, accélérations",
            "Parcours dynamique : haies basses, slalom, sprint 20 m, retour en trottinant",
            "Activation musculaire ciblée : squats, fentes, mollets, rotations de chevilles",
            "Jeu de réaction : sprints courts sur signal visuel ou sonore depuis différentes positions",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Explorer différentes façons de se déplacer : en avant, en arrière, de côté, à quatre pattes",
            "Sauter à pieds joints par-dessus des cordes posées au sol à différentes hauteurs",
            "Courir à petits pas rapides puis à grands pas lents — sentir la différence",
            "Apprendre à ramper sous des obstacles (bancs, cordes tendues) comme des soldats",
            "Pratiquer le galop et le saut en longueur avec élan de 3 pas",
        ],
        "mid": [
            "Technique de course : position du corps, mouvement des bras, poussée du pied",
            "Apprentissage du saut en longueur : élan, appel un pied, envol, réception deux pieds",
            "Travail de relais : passage du bâton en zone, synchronisation des vitesses",
            "Parcours technique : enchaîner course, saut, roulade, sprint dans le bon ordre",
            "Exercices d'esquive : feinter à gauche, partir à droite en situation de 1 contre 1",
        ],
        "old": [
            "Perfectionnement de la foulée de sprint : analyse par les pairs, corrections en binôme",
            "Technique de haies : passage de la jambe d'attaque et de la jambe de rappel",
            "Travail d'endurance avec gestion d'allure : courir à une fréquence cardiaque cible",
            "Parcours d'orientation avec carte du gymnase — trouver 6 balises dans l'ordre",
            "Technique de départ (starting blocks simulés) : réaction, poussée, accélération",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Parcours d'aventure : ramper dans le tunnel, sauter sur les îles (cerceaux), courir au trésor",
            "Jeu du loup-garou : le loup poursuit les villageois, les maisons (cerceaux) protègent temporairement",
            "Relais des animaux : chaque membre de l'équipe se déplace comme un animal différent",
            "Course de grenouilles : sauter d'un nénuphar (cerceau) à l'autre sans tomber dans l'eau",
            "Le grand déménagement : transporter des objets d'un bout à l'autre du gymnase en courant",
        ],
        "mid": [
            "Relais navette par équipes de 4 : course aller-retour avec passage du bâton",
            "Parcours chronométré : 8 stations d'obstacles variés à compléter le plus vite possible",
            "Tag éliminatoire : les joueurs touchés deviennent des obstacles statiques à contourner",
            "Mini-triathlon adapté : course, sauts, parcours d'obstacles — 3 épreuves enchaînées",
            "Jeu de territoire : conquérir les zones adverses en courant plus vite que les défenseurs",
        ],
        "old": [
            "Course contre la montre individuelle sur 400 m avec gestion d'allure et chronométrage",
            "Compétition de relais 4 × 100 m avec zones de passage réglementaires",
            "Parcours du combattant chronométré : 10 obstacles variés en intensité maximale",
            "Course d'orientation en équipe sur le terrain de l'école : 10 balises, carte et boussole",
            "Défi d'endurance : course progressive (paliers de vitesse croissante) type bip-test",
        ],
    },
    "retour_bank": {
        "young": [
            "Marche lente en cercle en respirant comme un ballon qui se gonfle et se dégonfle",
            "Les animaux fatigués s'étirent : imiter le chat, le chien, la girafe pour s'étirer",
            "Assis en cercle, montrer avec le pouce si on a aimé (pouce en haut / milieu / bas)",
            "S'allonger au sol et écouter les battements de son cœur ralentir",
        ],
        "mid": [
            "Étirements des jambes guidés : quadriceps, ischio-jambiers, mollets — 20 s chaque",
            "Retour verbal en équipe : nommer la stratégie de course qui a le mieux fonctionné",
            "Marche de récupération avec respiration profonde — inspirer 4 temps, expirer 6 temps",
            "Discussion : qu'avez-vous appris sur votre façon de courir aujourd'hui?",
        ],
        "old": [
            "Étirements complets : 30 s par groupe musculaire, guidés par un élève volontaire",
            "Journal de bord : noter sa performance, ses sensations, un objectif pour la prochaine fois",
            "Analyse de la gestion d'allure : comparer son plan de course avec le résultat réel",
            "Relaxation au sol avec musique — visualisation d'une course parfaite",
        ],
    },
}

# ------ STABILISATION ------
STABILISATION = {
    "file": "stabilisation_bonus.json",
    "prefix": "STAB",
    "domaine": "Stabilisation — Bonification",
    "competence": COMP_AGIR,
    "moyens_action": [
        "Équilibre statique", "Équilibre dynamique", "Gainage", "Yoga",
        "Gymnastique", "Souplesse", "Coordination", "Acrosport",
        "Force", "Conditionnement", "Relaxation", "Proprioception"
    ],
    "title_templates": [
        "Le yoga des {obj}", "Défi {action}", "Mission {action}",
        "Les acrobates du {obj}", "L'équilibre des {obj}", "Le circuit {action}",
        "Les statues de {obj}", "Le parcours {action}", "Les funambules du {obj}",
        "Le temple du {action}", "La forêt de {action}", "Zen et {action}",
        "Les gymnastes de {obj}", "Le défi des {obj}", "La pyramide {action}",
        "Les guerriers du {action}", "Le laboratoire {action}", "L'île de {action}",
        "Les champions de {action}", "Le secret de {action}", "Les maîtres du {action}",
        "La montagne de {action}", "Le sentier {action}", "Les équilibristes du {obj}",
    ],
    "title_objects": [
        "tapis", "poutres", "bancs", "cerceaux", "ballons suisses",
        "élastiques", "cordes", "briques", "cônes", "coussins",
        "blocs", "anneaux", "bandes", "planches", "demi-sphères",
    ],
    "title_actions": [
        "équilibre", "stabilité", "souplesse", "gainage", "coordination",
        "force", "yoga", "gymnastique", "acrosport", "relaxation",
        "proprioception", "posture", "concentration", "contrôle", "harmonie",
    ],
    "materiel_bank": [
        "Tapis de gymnastique", "Poutre basse", "Banc suédois", "Cônes",
        "Cerceaux", "Ballons suisses", "Élastiques de résistance", "Cordes",
        "Blocs de yoga", "Chronomètre", "Musique de relaxation", "Sifflet",
        "Bandes élastiques", "Coussins d'équilibre", "Planches d'équilibre",
        "Demi-sphères d'équilibre", "Espaliers", "Barres parallèles basses",
    ],
    "criteres_bank": [
        "Maintien de l'équilibre pendant 10 secondes", "Alignement postural correct",
        "Fluidité des transitions entre les positions", "Gainage du tronc pendant l'exercice",
        "Amplitude articulaire complète", "Synchronisation dans les figures de groupe",
        "Contrôle de la respiration pendant l'effort", "Stabilité sur une surface instable",
        "Coordination des mouvements complexes", "Maîtrise de la posture de base",
        "Régularité du rythme respiratoire", "Engagement musculaire approprié",
        "Maintien de la concentration", "Qualité de la figure gymnique",
        "Sécurité dans les portés (acrosport)",
    ],
    "savoirs_bank": [
        "Centre de gravité et base de support", "Alignement postural",
        "Respiration abdominale", "Gainage abdominal et dorsal",
        "Amplitude articulaire", "Proprioception et conscience corporelle",
        "Sécurité en gymnastique (parade)", "Positions de yoga de base",
        "Figures d'acrosport (base, voltigeur, pareur)", "Relaxation musculaire progressive",
        "Équilibre sur surfaces instables", "Souplesse passive et active",
        "Tonus musculaire adapté", "Coordination multi-segments",
        "Règles de sécurité pour les portés",
    ],
    "echauffement_bank": {
        "young": [
            "Les arbres dans le vent : se balancer doucement d'un pied à l'autre comme des arbres",
            "Jeu des statues : danser librement et se figer en équilibre au signal",
            "Marche sur une ligne au sol comme un funambule au cirque",
            "Imiter des animaux en équilibre : flamant rose, grue, chat sur un mur",
            "Rouler comme une bûche sur les tapis, puis se lever en équilibre sur un pied",
        ],
        "mid": [
            "Parcours d'équilibre simplifié : marcher sur les lignes, sur un banc renversé, sur un pied",
            "Échauffement articulaire progressif : chevilles, genoux, hanches, épaules, cou",
            "Jeu de la tortue : se déplacer à quatre pattes avec un coussin sur le dos sans le faire tomber",
            "Étirements dynamiques en cercle guidés par l'enseignant",
            "Course légère avec arrêts en position d'équilibre (avion, flamant, chandelle)",
        ],
        "old": [
            "Mobilisation articulaire complète : 30 s par articulation, de bas en haut",
            "Salutation au soleil adaptée : enchaînement de yoga dynamique (3 répétitions)",
            "Parcours d'activation : fentes, squats, planche, pont — circuit de 4 stations",
            "Exercices de proprioception : yeux fermés, marche talon-orteil, appui unipodal",
            "Échauffement musculaire ciblé : gainage ventral 30 s, latéral 20 s par côté, dorsal 30 s",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Apprendre à tenir en équilibre sur un pied : poser le pied sur le genou comme un flamant rose",
            "Roulade avant sur plan incliné : descendre la pente douce en se roulant en boule",
            "Faire le pont : dos au sol, pousser les hanches vers le ciel avec les pieds et mains au sol",
            "Marcher sur le banc suédois en tenant les bras en croix pour l'équilibre",
            "Exercices de souplesse ludiques : toucher ses orteils, faire le papillon, l'étoile de mer",
        ],
        "mid": [
            "Technique de roulade avant et arrière sur tapis : départ accroupi, menton sur poitrine",
            "Apprentissage de 4 positions de yoga : arbre, guerrier, chien tête en bas, cobra",
            "Exercices de gainage : planche sur les mains (10 s), planche latérale (8 s par côté)",
            "Équilibre sur surfaces variées : sol, banc, coussin, poutre basse — progression",
            "Figures d'acrosport en duo : base couchée, voltigeur debout sur les pieds — avec pareur",
        ],
        "old": [
            "Perfectionnement des éléments gymniques : ATR contre le mur, roue, rondade",
            "Séquence de yoga Vinyasa : 8 postures enchaînées avec transitions fluides",
            "Travail de gainage avancé : planche avec variations (lever un bras, une jambe, opposés)",
            "Figures d'acrosport en trio : pyramide de base, portés simples avec consignes de sécurité",
            "Exercices de proprioception avancés : yeux fermés sur coussin, squats sur demi-sphère",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Parcours gymnique : roulade, marche sur banc, saut depuis un mini-tremplin, pose finale",
            "Jeu du yoga des animaux : piger une carte d'animal et faire la posture correspondante",
            "Construction de statues en duo : créer 3 poses d'équilibre différentes ensemble",
            "Le sol est de la lave : se déplacer sur les tapis et les bancs sans toucher le sol",
            "Spectacle de cirque : chaque enfant présente sa meilleure figure d'équilibre",
        ],
        "mid": [
            "Enchaînement gymnique de 4 éléments au choix — présentation devant un petit groupe",
            "Circuit de 6 stations de stabilisation : 1 min par station avec rotation au signal",
            "Défi d'acrosport en duo : créer une séquence de 3 figures en 5 minutes, la présenter",
            "Parcours de poutre et banc : traversée avec obstacles (enjamber, passer dessous, demi-tour)",
            "Yoga flow en groupe : l'enseignant guide un enchaînement de 10 postures maintenues",
        ],
        "old": [
            "Création d'un enchaînement gymnique au sol de 30 secondes avec 5 éléments minimum",
            "Épreuve d'acrosport en trio ou quatuor : chorégraphie de 4 figures avec transitions musicales",
            "Challenge de gainage : qui tiendra la planche le plus longtemps? (record personnel)",
            "Circuit training de conditionnement : 8 stations, 40 s travail / 20 s repos, 2 tours",
            "Séance de yoga complète : salutations au soleil, postures debout, au sol, méditation finale",
        ],
    },
    "retour_bank": {
        "young": [
            "S'allonger comme une étoile de mer et respirer doucement en sentant son ventre monter et descendre",
            "Étirements animaux : s'étirer comme un chat, un chien, une tortue qui rentre dans sa carapace",
            "Assis en cercle, montrer sa figure d'équilibre préférée en version mini",
            "Relaxation guidée : imaginer qu'on est un nuage qui flotte doucement dans le ciel",
        ],
        "mid": [
            "Séquence d'étirements statiques : 20 s par muscle, respiration profonde",
            "Retour sur les postures de yoga apprises : nommer et refaire sa préférée",
            "Exercice de respiration : 4 temps inspiration, 4 temps rétention, 6 temps expiration",
            "Discussion : quelle figure a été la plus difficile? Comment l'améliorer?",
        ],
        "old": [
            "Étirements complets 30 s par muscle : quadriceps, ischio-jambiers, psoas, épaules, dos",
            "Relaxation progressive de Jacobson : contracter puis relâcher chaque groupe musculaire",
            "Journal de bord : noter les figures maîtrisées et celles à travailler",
            "Méditation guidée de 3 minutes avec musique zen — focus sur la respiration",
        ],
    },
}

# ------ OPPOSITION ------
OPPOSITION = {
    "file": "opposition_bonus.json",
    "prefix": "OPPB",
    "domaine": "Opposition — Bonification",
    "competence": COMP_INTERAGIR,
    "moyens_action": [
        "Dodgeball", "Ballon chasseur", "Lutte éducative", "Duel de territoire",
        "Tag / Poursuite", "Escrime adaptée", "Capture du drapeau", "Sports de combat adaptés",
        "Flag football", "Ultimate", "Badminton duel"
    ],
    "title_templates": [
        "Le tournoi des {obj}", "Duel {action}", "Combat de {obj}",
        "La bataille des {obj}", "Les guerriers du {obj}", "Défi {action}",
        "L'arène des {obj}", "Mission {action}", "Les gladiateurs du {obj}",
        "Le chasseur de {obj}", "La forteresse des {obj}", "Attaque {action}",
        "Les chevaliers du {obj}", "Le duel des {obj}", "La conquête {action}",
        "Les défenseurs du {obj}", "Le piège des {obj}", "L'embuscade {action}",
        "Les duellistes du {obj}", "La chasse aux {obj}", "Les corsaires du {obj}",
        "Le siège des {obj}", "L'affrontement des {obj}", "La joute {action}",
    ],
    "title_objects": [
        "ballons", "dossards", "drapeaux", "épées", "boucliers",
        "territoires", "châteaux", "trésors", "zones", "camps",
        "cibles", "foulards", "cônes", "bases", "forteresses",
    ],
    "title_actions": [
        "opposition", "esquive", "stratégie", "poursuite", "combat",
        "défense", "attaque", "duel", "tactique", "feinte",
        "confrontation", "capture", "conquête", "résistance", "évasion",
    ],
    "materiel_bank": [
        "Ballons en mousse", "Dossards de couleur", "Cônes", "Foulards",
        "Drapeaux", "Cerceaux", "Tapis de lutte", "Raquettes de badminton",
        "Volants de badminton", "Sifflet", "Chronomètre", "Bâtons en mousse",
        "Épées en mousse", "Ballons de dodgeball", "Plots", "Filet",
        "Ceintures de flag football", "Frisbees", "Ballons de football",
    ],
    "criteres_bank": [
        "Utilisation de feintes pour tromper l'adversaire", "Réaction rapide aux actions de l'opposant",
        "Respect des règles de jeu et de sécurité", "Choix tactique adapté à la situation",
        "Esquive efficace avec changement de direction", "Anticipation des actions adverses",
        "Gestion de l'espace (attaque/défense)", "Contrôle de la force dans le contact",
        "Communication avec les coéquipiers", "Adaptabilité de la stratégie en cours de jeu",
        "Précision du lancer/frappe vers l'adversaire", "Positionnement défensif approprié",
        "Fair-play et esprit sportif", "Prise de décision sous pression",
        "Capacité à lire le jeu de l'adversaire",
    ],
    "savoirs_bank": [
        "Feinte et changement de direction", "Lecture du jeu adverse",
        "Zones d'attaque et de défense", "Règles de sécurité en opposition",
        "Stratégie individuelle et collective", "Esquive et déplacement latéral",
        "Contrôle de la force", "Anticipation et réaction",
        "Communication en situation d'opposition", "Notion de territoire",
        "Prise de décision rapide", "Fair-play et respect de l'adversaire",
        "Gestion du stress en compétition", "Tactiques de base (1 contre 1, zone)",
        "Règles sportives de base",
    ],
    "echauffement_bank": {
        "young": [
            "Jeu du chat et de la souris : un chat poursuit les souris dans un espace délimité",
            "Course avec arrêts en position de garde : pieds écartés, genoux fléchis, mains devant",
            "Jeu du miroir en duo : imiter les déplacements du partenaire (avant, arrière, côtés)",
            "Les petits soldats : marcher, courir, s'arrêter, se cacher au signal",
            "Sauts sur place en changeant de direction au coup de sifflet",
        ],
        "mid": [
            "Échauffement en duo : jeu de touches aux épaules — toucher l'épaule du partenaire en protégeant les siennes",
            "Course avec feintes : courir en ligne droite puis changer de direction au signal",
            "Jeu de l'ombre : un élève mène, l'autre le suit en imitant ses déplacements",
            "Exercices d'esquive : éviter des ballons roulés doucement par un partenaire",
            "Pas chassés et déplacements défensifs : avant, arrière, latéral en position basse",
        ],
        "old": [
            "Échauffement spécifique combat : déplacements en garde, esquives, feintes — 3 minutes",
            "Activation musculaire : squats, fentes, gainage, pompes — circuit rapide de 4 minutes",
            "Jeu de rapidité en duo : toucher les genoux du partenaire sans se faire toucher",
            "Course avec variations tactiques : sprint, esquive de cônes, changements de direction",
            "Échauffement spécifique badminton : échanges en douceur, déplacements sur le terrain",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Apprendre à esquiver un ballon en mousse lancé doucement : pas de côté, se baisser",
            "Jeu de la queue de renard en duo : attraper le foulard du partenaire en protégeant le sien",
            "Exercice de poursuite : courir vers un refuge avant d'être touché — notion de vitesse de réaction",
            "Apprendre à lancer avec précision pour toucher une cible mobile (partenaire qui marche)",
            "Les gardiens : apprendre à défendre un objet (cône) contre un attaquant",
        ],
        "mid": [
            "Technique de dodgeball : attraper, esquiver, lancer avec précision — rotation en trio",
            "Apprentissage des feintes : fausse direction du regard, faux départs, leurres",
            "Jeu du drapeau : stratégies de base (diversion, couverture, attaque rapide)",
            "Exercice de lutte éducative : pousser/tirer un partenaire hors d'un cerceau (à genoux)",
            "Tactique de jeu 2 contre 1 : comment créer et exploiter le surnombre",
        ],
        "old": [
            "Stratégie de dodgeball avancée : positionnement, couverture d'équipe, attaques coordonnées",
            "Technique de badminton : service court, service long, dégagé, amorti — exercices ciblés",
            "Tactique de flag football : tracés de course, couverture de zone, lecture défensive",
            "Lutte éducative au sol : positions de contrôle, retournements, sorties sécuritaires",
            "Analyse vidéo de situations d'opposition : identifier les choix tactiques optimaux",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Jeu du ballon chasseur simplifié : lancer des ballons en mousse pour toucher les adversaires en dessous des épaules",
            "Tag collectif : 3 chasseurs tentent de toucher les autres, le touché devient chasseur",
            "La rivière aux crocodiles : traverser le gymnase sans se faire toucher par les crocodiles",
            "Le gardien du trésor : défendre son cône contre les attaquants (1 gardien, 3 attaquants)",
            "Jeu de la queue du loup : attraper le plus de foulards possible en 2 minutes",
        ],
        "mid": [
            "Match de dodgeball 6 contre 6 : règles officielles adaptées, rotation toutes les 5 minutes",
            "Capture du drapeau : 2 équipes, chacune protège un drapeau et tente de capturer celui adverse",
            "Tournoi de lutte éducative : combats de 1 minute, système de points (poussée hors du cercle)",
            "Mini-matchs de badminton en simple : 11 points, rotation des adversaires",
            "Jeu du roi de la montagne : défendre son territoire (cerceau) contre les challengers",
        ],
        "old": [
            "Tournoi de dodgeball avec stratégies d'équipe imposées : attaque en V, défense en ligne",
            "Matchs de badminton en double avec rotations et analyse des placements",
            "Simulation de flag football : attaque 5 contre 5 avec jeux planifiés et audibles",
            "Compétition de capture du drapeau avec rôles spécialisés (attaquants, défenseurs, éclaireurs)",
            "Tournoi multi-sports d'opposition : 3 disciplines, classement individuel cumulé",
        ],
    },
    "retour_bank": {
        "young": [
            "Les guerriers fatigués se reposent : étirements doux assis en cercle, respiration calme",
            "Serrer la main de 3 adversaires et dire « beau match! »",
            "S'allonger au sol et écouter son cœur battre de plus en plus lentement",
            "Discussion en cercle : qu'est-ce qui fait un bon joueur? (écouter les réponses)",
        ],
        "mid": [
            "Étirements en duo face à face : jambes, dos, épaules — 20 s chaque",
            "Retour sur les stratégies : qu'est-ce qui a bien fonctionné? Qu'est-ce qu'on changerait?",
            "Jeu calme du « respect » : nommer un geste de fair-play observé chez un camarade",
            "Relaxation au sol : 2 minutes de respiration profonde avec musique calme",
        ],
        "old": [
            "Étirements complets autonomes : chaque élève étire les muscles sollicités",
            "Discussion tactique : analyse collective des situations de jeu clés",
            "Journal de bord : auto-évaluation de son fair-play, sa stratégie et son engagement",
            "Retour sur les valeurs sportives : respect, persévérance, contrôle de soi",
        ],
    },
}

# ------ COOPÉRATION ------
COOPERATION = {
    "file": "cooperation_bonus.json",
    "prefix": "COOB",
    "domaine": "Coopération — Bonification",
    "competence": COMP_INTERAGIR,
    "moyens_action": [
        "Basketball", "Volleyball", "Handball", "Flag-football",
        "Ultimate frisbee", "Soccer / futsal", "Kin-Ball",
        "Jeux coopératifs", "Sports adaptés (tchoukball, goalball)",
        "Relais coopératifs", "Spikeball"
    ],
    "title_templates": [
        "L'équipe des {obj}", "Mission {action} collective", "Le grand match des {obj}",
        "Alliance {action}", "Les coéquipiers du {obj}", "Défi {action} en équipe",
        "Le tournoi des {obj}", "Ensemble pour {action}", "La victoire des {obj}",
        "Le rallye des {obj}", "Coéquipiers de {action}", "Le clan des {obj}",
        "La chaîne des {obj}", "L'union des {obj}", "Le relais des {obj}",
        "La stratégie des {obj}", "Les alliés du {obj}", "Le cercle des {obj}",
        "La passe des {obj}", "Les champions de {action}", "Le défi des {obj}",
        "Le réseau des {obj}", "L'esprit d'équipe des {obj}", "La coupe des {obj}",
    ],
    "title_objects": [
        "ballons", "paniers", "filets", "buts", "frisbees",
        "drapeaux", "cônes", "cerceaux", "équipiers", "champions",
        "étoiles", "lions", "aigles", "faucons", "loups",
    ],
    "title_actions": [
        "coopération", "passes", "stratégie", "coordination", "communication",
        "tactique", "placement", "attaque", "défense", "collaboration",
        "solidarité", "entraide", "synchronisation", "organisation", "création",
    ],
    "materiel_bank": [
        "Ballons de basketball", "Ballons de volleyball", "Ballons de handball",
        "Ballons de soccer", "Frisbees", "Cônes", "Dossards de couleur",
        "Filet de volleyball", "Paniers de basketball", "Buts (mini-soccer)",
        "Sifflet", "Chronomètre", "Kin-Ball", "Ballons en mousse",
        "Ceintures de flag-football", "Plots", "Chasubles", "Cerceaux",
        "Spikeball (filet et balle)", "Ballon de tchoukball",
    ],
    "criteres_bank": [
        "Communication efficace avec les coéquipiers", "Passes précises et adaptées à la situation",
        "Placement sur le terrain en attaque et en défense", "Respect du rôle assigné dans l'équipe",
        "Encouragement et soutien des coéquipiers", "Prise de décision collective",
        "Adaptation de la stratégie en cours de match", "Démarquage et appel de balle",
        "Respect des règles et de l'arbitre", "Participation active de tous les membres",
        "Transitions rapides attaque-défense", "Couverture de l'espace collectif",
        "Qualité technique des gestes sportifs", "Esprit d'équipe et fair-play",
        "Gestion des émotions en situation de compétition",
    ],
    "savoirs_bank": [
        "Passes et réceptions (types variés)", "Démarquage et création d'espace",
        "Rôles en attaque et en défense", "Communication verbale et non-verbale",
        "Stratégie d'équipe de base", "Règles des sports collectifs",
        "Positionnement sur le terrain", "Transition offensive/défensive",
        "Soutien du porteur de balle", "Notion de surnombre",
        "Gestion de l'espace collectif", "Leadership sportif",
        "Arbitrage et fair-play", "Analyse du jeu adverse",
        "Échauffement spécifique au sport collectif",
    ],
    "echauffement_bank": {
        "young": [
            "Jeu des déménageurs : transporter des objets en duo d'un bout à l'autre du gymnase",
            "Ronde musicale : se déplacer en cercle et se passer un ballon au rythme de la musique",
            "Course en duo main dans la main : suivre un parcours de cônes ensemble sans se lâcher",
            "Jeu du parachute : tenir le parachute en groupe et faire rebondir des ballons dessus",
            "Les trains : en file indienne, le premier guide les wagons dans le gymnase",
        ],
        "mid": [
            "Passes en déplacement par groupes de 3 : passe et suit en trottinant",
            "Jeu de la balle brûlante : se passer le ballon le plus vite possible en cercle",
            "Échauffement en duo : exercices synchronisés (squats face à face, étirements dos à dos)",
            "Jeu des 10 passes : réussir 10 passes d'équipe sans que l'adversaire intercepte",
            "Course en relais de passes : transporter le ballon par passes d'un bout à l'autre",
        ],
        "old": [
            "Échauffement spécifique sport collectif : passes et déplacements par groupes de 4",
            "Exercice 3 contre 1 (taureau) : 3 passeurs gardent le ballon, 1 défenseur intercepte",
            "Activation musculaire avec ballon : squats-passes, fentes-passes, gainage en duo",
            "Jeu de conservation : 5 contre 2, garder le ballon le plus longtemps possible",
            "Échauffement tactique : 4 contre 4 demi-terrain avec objectif de passes minimum",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Apprendre à se passer un ballon en duo : à deux mains, par en dessous, en roulant au sol",
            "Jeu coopératif du cerceau musical : quand la musique s'arrête, tout le monde entre dans les cerceaux restants",
            "Exercice de communication : guide verbal d'un partenaire les yeux bandés dans un parcours",
            "Apprendre à jouer ensemble : exercice de passes en triangle avec ballon en mousse",
            "Jeu de construction collective : bâtir une tour de cônes en équipe dans un temps limité",
        ],
        "mid": [
            "Technique de passe à deux mains (basketball) : passe poitrine, passe à rebond, passe baseball",
            "Apprentissage du démarquage : se libérer de son défenseur pour recevoir une passe",
            "Exercice de handball : tir au but en pivot avec opposition passive d'un défenseur",
            "Stratégie de base : attaque en triangle, rôles (porteur, soutien, appel)",
            "Technique de manchette et touche de volleyball en duo : 10 échanges consécutifs",
        ],
        "old": [
            "Tactique de basketball : pick and roll, give and go — exercices en 3 contre 3",
            "Volleyball : montée de balle (réception, passe, attaque) en trio avec rotation",
            "Handball : circulation de balle 5 contre 5 avec pivot, ailiers et arrières",
            "Ultimate : techniques de lancer (backhand, forehand) et coupes (in-cut, deep-cut)",
            "Analyse tactique : visionner un schéma de jeu et le reproduire sur le terrain",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Jeu du parachute coopératif : soulever ensemble pour faire flotter un ballon le plus haut possible",
            "Match de passes en cercle : combien de passes l'équipe peut-elle réussir en 2 minutes?",
            "Jeu du ballon-château : protéger ensemble des cônes-châteaux avec des ballons en mousse",
            "Relais coopératifs : transporter un ballon en duo de différentes façons (dos à dos, front à front)",
            "Mini-match de soccer adapté : les buts ne comptent que si tous les joueurs ont touché le ballon",
        ],
        "mid": [
            "Match de basketball 4 contre 4 adapté : 3 passes minimum avant le tir, tout le monde touche le ballon",
            "Tournoi de volleyball en équipes de 4 : matchs de 15 points avec rotation",
            "Jeu du Kin-Ball : 3 équipes s'affrontent avec le ballon géant — service et réception",
            "Match de handball 5 contre 5 : terrain réduit, tirs interdits hors de la zone",
            "Relais sportif par équipes : chaque membre fait une épreuve différente (drible, passes, tir)",
        ],
        "old": [
            "Matchs de basketball 5 contre 5 avec système de jeu imposé et rotations",
            "Tournoi d'ultimate frisbee : matchs de 9 points avec esprit du jeu",
            "Match de volleyball 6 contre 6 avec arbitrage par les pairs et statistiques",
            "Compétition inter-équipes de flag football : attaques planifiées avec audibles",
            "Tournoi multi-sports coopératif : 3 sports, classement par points cumulés",
        ],
    },
    "retour_bank": {
        "young": [
            "En cercle, chaque enfant dit merci à un coéquipier en nommant ce qu'il a bien fait",
            "Étirements en ronde : se tenir les mains et s'étirer ensemble comme une étoile",
            "Respiration collective : inspirer et expirer tous ensemble au même rythme",
            "Discussion : qu'est-ce qu'une bonne équipe? (recueillir les idées des enfants)",
        ],
        "mid": [
            "Étirements en équipe : chaque joueur propose un étirement que tout le monde fait",
            "Retour tactique : qu'est-ce qui a bien fonctionné dans notre jeu d'équipe?",
            "Caucus d'équipe : nommer 2 forces et 1 aspect à améliorer pour le prochain match",
            "Relaxation au sol en écoutant une musique calme — récupération après l'effort",
        ],
        "old": [
            "Étirements autonomes ciblés selon le sport pratiqué — 5 minutes",
            "Analyse collective du match : points forts, erreurs tactiques, ajustements",
            "Journal de bord d'équipe : chaque joueur évalue sa contribution et celle de l'équipe",
            "Discussion sur le leadership : qui a bien dirigé le jeu? Comment améliorer la communication?",
        ],
    },
}

# ------ EXPRESSION ------
EXPRESSION = {
    "file": "expression_bonus.json",
    "prefix": "EXPB",
    "domaine": "Expression — Bonification",
    "competence": COMP_AGIR,
    "moyens_action": [
        "Danse créative", "Danse folklorique", "Danse contemporaine",
        "Mime", "Acrosport", "Gymnastique rythmique",
        "Gymnastique au sol", "Cirque", "Expression corporelle",
        "Chorégraphie", "Hip-hop"
    ],
    "title_templates": [
        "La danse des {obj}", "Le spectacle {action}", "Les artistes du {obj}",
        "Festival {action}", "Création {action}", "Les danseurs de {obj}",
        "Le bal des {obj}", "Scène {action}", "Les performers du {obj}",
        "L'atelier {action}", "Le gala des {obj}", "Rythme et {action}",
        "Les étoiles de {action}", "Le studio {action}", "L'expression des {obj}",
        "Les créateurs de {action}", "La troupe des {obj}", "Le mouvement des {obj}",
        "La scène des {obj}", "Les interprètes du {obj}", "Le tableau {action}",
        "Les chorégraphes du {obj}", "La piste des {obj}", "Le récital {action}",
    ],
    "title_objects": [
        "rubans", "foulards", "masques", "cerceaux", "étoiles",
        "lumières", "ombres", "saisons", "émotions", "couleurs",
        "éléments", "rêves", "vagues", "fleurs", "papillons",
    ],
    "title_actions": [
        "expression", "danse", "mime", "chorégraphie", "création",
        "rythme", "mouvement", "interprétation", "imaginaire", "contemporain",
        "folklorique", "artistique", "acrobatique", "corporel", "musical",
    ],
    "materiel_bank": [
        "Rubans de gymnastique", "Foulards de couleur", "Tambourin",
        "Musique variée (CD/bluetooth)", "Tapis de gymnastique", "Cerceaux",
        "Masques de mime", "Balles de jonglage", "Costumes simples",
        "Système de son", "Lumières d'ambiance", "Cordes à sauter",
        "Chapeaux", "Bâton du diable", "Assiettes chinoises",
        "Images plastifiées (émotions/animaux)", "Craies de couleur",
    ],
    "criteres_bank": [
        "Créativité et originalité des mouvements", "Utilisation des niveaux dans l'espace (haut, moyen, bas)",
        "Expressivité corporelle et faciale", "Synchronisation avec la musique",
        "Fluidité des enchaînements de mouvements", "Variété des formes corporelles",
        "Qualité de la présentation au public", "Mémorisation de la chorégraphie",
        "Utilisation de l'espace scénique", "Travail en synchronisation avec les partenaires",
        "Interprétation du thème choisi", "Qualité technique des éléments (sauts, tours, équilibres)",
        "Transitions harmonieuses entre les séquences", "Engagement et énergie dans la performance",
        "Capacité à s'adapter au rythme musical",
    ],
    "savoirs_bank": [
        "Niveaux dans l'espace (haut, moyen, bas)", "Qualités de mouvement (fluide, saccadé, lourd, léger)",
        "Rythme et tempo musical", "Formes corporelles (droite, courbe, torsion)",
        "Relations spatiales (près, loin, ensemble, séparé)", "Expression des émotions par le corps",
        "Composition chorégraphique (début, milieu, fin)", "Écoute musicale et synchronisation",
        "Techniques de base de danse (pas chassé, pivot, tour)", "Éléments de mime (mur, corde, boîte)",
        "Posture de scène et regard", "Figures d'acrosport et sécurité",
        "Histoire des danses folkloriques", "Éléments de cirque (jonglerie, équilibre, acrobatie)",
        "Vocabulaire de la danse et du mouvement",
    ],
    "echauffement_bank": {
        "young": [
            "Danse libre sur musique enjouée : les enfants bougent comme ils veulent dans le gymnase",
            "Jeu du miroir : en duo, imiter les mouvements du partenaire au ralenti",
            "Marche de personnages : marcher comme un géant, une souris, un robot, une fée",
            "Les animaux dansent : bouger au rythme de la musique en imitant un animal choisi",
            "Les bulles de savon : se déplacer léger et doux comme une bulle qui flotte",
        ],
        "mid": [
            "Échauffement rythmique : frapper des mains, des pieds, claquer des doigts en suivant un rythme",
            "Isolation corporelle : bouger une seule partie du corps à la fois (tête, épaules, hanches)",
            "Étirements dansés : enchaîner des positions de yoga en musique de façon fluide",
            "Marche scénique : se déplacer dans l'espace en variant les rythmes et les directions",
            "Jeu des émotions : marcher en exprimant la joie, la colère, la surprise, la peur",
        ],
        "old": [
            "Échauffement danse : isolations, ondulations, pliés, tendus, dégagés — routine de 5 minutes",
            "Étirements actifs avec musique : mobilisation de toutes les articulations en rythme",
            "Routine de hip-hop basique : bounce, rock, step touch — 4 mouvements de base enchaînés",
            "Échauffement contemporain : travail de sol, spirales, swings, chutes contrôlées",
            "Activation créative : improvisation guidée sur thème — 3 minutes libre",
        ],
    },
    "apprentissage_bank": {
        "young": [
            "Exploration des niveaux : danser très haut sur la pointe des pieds, moyen, très bas au sol",
            "Création de formes : faire des formes avec son corps (rond, pointu, large, étroit)",
            "Mime guidé : mimer des actions du quotidien (se laver, manger, se brosser les dents)",
            "Apprendre un pas de danse folklorique simple : la ronde, le galop, la farandole",
            "Explorer les foulards : vagues, cercles, spirales en se déplaçant dans l'espace",
        ],
        "mid": [
            "Apprentissage d'une séquence de 8 temps de danse hip-hop avec décomposition",
            "Technique de mime : le mur, la corde, la boîte, la marche contre le vent",
            "Création chorégraphique en trio : choisir 4 mouvements et les enchaîner en canon",
            "Apprentissage de la roue et de la roulade dans un enchaînement gymnique expressif",
            "Danse folklorique : apprendre les pas de base d'une danse traditionnelle québécoise",
        ],
        "old": [
            "Technique de danse contemporaine : contraction-release, spirale, chute et récupération",
            "Création chorégraphique en groupe : processus de composition (thème, exploration, sélection, mise en forme)",
            "Acrosport : création de figures à 3-4 avec portés, transitions et éléments individuels",
            "Apprentissage d'un enchaînement hip-hop de 32 temps avec variations de niveau et d'énergie",
            "Technique de cirque : jonglerie à 3 balles, équilibre sur rolla bolla, diabolo",
        ],
    },
    "mise_en_action_bank": {
        "young": [
            "Spectacle de fin de cours : chaque enfant présente sa danse du papillon / du robot / de l'animal",
            "Fresque collective : les enfants créent ensemble un tableau vivant sur le thème de la nature",
            "Défilé de personnages : chaque enfant marche devant les autres comme un personnage inventé",
            "Danse collective : ronde chantée avec gestes et mouvements appris pendant le cours",
            "Le cirque des tout-petits : chaque enfant montre son numéro préféré au groupe",
        ],
        "mid": [
            "Présentation des chorégraphies de trio devant la classe — rétroaction constructive des pairs",
            "Mini-spectacle : chaque équipe présente un numéro de 1 minute sur un thème imposé",
            "Battle de danse amicale : chaque élève montre son meilleur mouvement dans le cercle",
            "Performance de mime : présentation de scènes mimées en duo devant le groupe",
            "Festival de danse folklorique : enchaîner toutes les danses apprises dans un grand bal",
        ],
        "old": [
            "Présentation de la chorégraphie de groupe (3-5 min) devant la classe avec évaluation par les pairs",
            "Spectacle de fin d'unité : chaque groupe performe sa création avec musique et éclairage",
            "Battle de hip-hop structurée : passages individuels et en crew, jury d'élèves",
            "Festival d'acrosport : enchaînements de 2 minutes avec figures, transitions et musique",
            "Performance de cirque : numéros variés (jonglerie, acrobatie, mime) dans un spectacle collectif",
        ],
    },
    "retour_bank": {
        "young": [
            "Les danseurs s'endorment : s'allonger et respirer au son d'une berceuse douce",
            "Chaque enfant fait un mouvement très lent comme un nuage qui disparaît",
            "En cercle, dire avec un geste silencieux ce qu'on a préféré aujourd'hui",
            "Étirements de danseur : bras au ciel, toucher le sol, s'enrouler comme un escargot",
        ],
        "mid": [
            "Retour réflexif : nommer un élément réussi dans sa performance et un à améliorer",
            "Étirements guidés en musique : 20 s par position en respirant profondément",
            "Ronde de compliments : dire un commentaire positif sur la performance d'un camarade",
            "Relaxation au sol en visualisant sa chorégraphie dans sa tête",
        ],
        "old": [
            "Étirements de danseur complets : quadriceps, ischio-jambiers, dos, épaules — 30 s chacun",
            "Analyse critique constructive : chaque groupe donne et reçoit une rétroaction sur sa performance",
            "Journal créatif : dessiner ou décrire sa chorégraphie, noter les intentions artistiques",
            "Relaxation guidée avec musique : scanner corporel de 3 minutes, relâchement total",
        ],
    },
}

# ============================================================
# ALL CATEGORIES
# ============================================================
ALL_CATEGORIES = [MANIPULATION, LOCOMOTION, STABILISATION, OPPOSITION, COOPERATION, EXPRESSION]


def generate_title(cat, moyen, idx, used_titles):
    """Generate a unique creative title."""
    template = pick(cat["title_templates"])
    obj = pick(cat["title_objects"])
    action = pick(cat["title_actions"])
    title = template.format(obj=obj, action=action)

    # Ensure uniqueness
    attempts = 0
    while title in used_titles and attempts < 100:
        template = pick(cat["title_templates"])
        obj = pick(cat["title_objects"])
        action = pick(cat["title_actions"])
        title = template.format(obj=obj, action=action)
        attempts += 1

    if title in used_titles:
        # Fallback: append a qualifier
        qualifiers = [
            "niveau supérieur", "édition spéciale", "version 2.0", "le retour",
            "la suite", "remix", "évolution", "pro", "expert", "défi ultime",
            "nouvelle vague", "grand format", "hors-série", "aventure extrême",
        ]
        title = f"{title} — {pick(qualifiers)}"

    used_titles.add(title)
    return title


def get_age_key(cycle_info):
    """Return 'young', 'mid', or 'old' based on cycle."""
    cycle = cycle_info["cycle"]
    if cycle in ("Maternelle", "1er cycle primaire"):
        return "young"
    elif cycle in ("2e cycle primaire", "3e cycle primaire"):
        return "mid"
    else:
        return "old"


def generate_sae(cat, idx, cycle_info, used_titles):
    """Generate a single SAÉ entry with 1000+ words of rich content."""
    prefix = cat["prefix"]
    moyen = pick(cat["moyens_action"])
    age_key = get_age_key(cycle_info)
    m = moyen.lower()

    title = generate_title(cat, moyen, idx, used_titles)

    # Pick content from banks — more items for richer content
    criteres = pick_n(cat["criteres_bank"], 5)
    savoirs = pick_n(cat["savoirs_bank"], 5)
    materiel = pick_n(cat["materiel_bank"], random.randint(5, 8))

    echauffement_act = pick(cat["echauffement_bank"][age_key])
    apprentissage_act = pick(cat["apprentissage_bank"][age_key])
    mise_en_action_act = pick(cat["mise_en_action_bank"][age_key])
    retour_act = pick(cat["retour_bank"][age_key])

    # ======== ROLE ENSEIGNANT (expanded) ========
    roles_echauffement = [
        f"Donner les consignes clairement et s'assurer que tous les élèves participent activement. Circuler dans l'espace pour vérifier la compréhension des consignes. Encourager les élèves plus réservés à s'engager dans l'activité. Ajuster le rythme selon l'énergie du groupe et la température ambiante.",
        f"Animer avec enthousiasme en utilisant un ton dynamique et encourageant. Observer attentivement les élèves et corriger les postures inadéquates pour prévenir les blessures. Proposer des alternatives pour les élèves qui éprouvent des difficultés. Maintenir un rythme soutenu tout en respectant les capacités de chacun.",
        f"Démontrer les mouvements attendus de façon claire et visible par tous. Circuler activement dans le gymnase et encourager les élèves timides ou moins confiants à participer. Utiliser le renforcement positif pour valoriser les efforts. S'assurer que l'espace est sécuritaire et que le matériel est bien disposé.",
        f"Gérer le rythme et les transitions entre les exercices de façon fluide. Assurer la sécurité en vérifiant l'espacement entre les élèves. Utiliser des signaux sonores ou visuels clairs pour les changements d'activité. Adapter l'intensité selon les besoins observés dans le groupe.",
    ]
    roles_apprentissage = [
        f"Démontrer la technique de façon détaillée en décomposant les mouvements. Offrir des rétroactions individuelles précises et constructives. Utiliser des mots-clés simples pour guider l'exécution. Prévoir des ateliers de niveaux différents pour respecter le rythme d'apprentissage de chaque élève. Observer attentivement et noter les progrès pour l'évaluation formative.",
        f"Circuler parmi les ateliers en accordant une attention particulière aux élèves en difficulté. Corriger les gestes techniques avec bienveillance et valoriser les progrès, même petits. Proposer des défis supplémentaires aux élèves qui maîtrisent déjà les éléments de base. Documenter les observations pour le suivi des apprentissages.",
        f"Expliquer les critères de réussite de façon explicite en donnant des exemples concrets et des contre-exemples. Utiliser des démonstrations visuelles et des repères spatiaux. Permettre aux élèves de s'autoévaluer à l'aide de grilles simples. Encourager l'entraide entre pairs pour favoriser l'apprentissage coopératif.",
        f"Guider les exercices étape par étape en vérifiant la compréhension à chaque transition. Adapter le niveau de difficulté en temps réel selon les réponses des élèves. Utiliser le questionnement pour amener les élèves à réfléchir sur leurs actions. Proposer des situations de complexité croissante pour maintenir la motivation.",
    ]
    roles_mise_en_action = [
        f"Arbitrer les activités de façon juste et cohérente. Gérer les rotations entre les équipes ou les ateliers pour maximiser le temps d'engagement moteur. S'assurer que les règles sont comprises et respectées par tous. Intervenir rapidement en cas de conflit ou de situation d'insécurité. Encourager l'esprit sportif et le fair-play.",
        f"Observer les stratégies utilisées par les élèves et noter les comportements significatifs. Encourager la communication verbale et non verbale entre coéquipiers. Proposer des ajustements tactiques ou techniques lorsque nécessaire. Valoriser la créativité et la prise d'initiative dans les solutions proposées par les élèves.",
        f"Superviser la sécurité de façon constante en anticipant les situations à risque. Offrir des défis bonus aux équipes ou individus qui terminent rapidement. Maintenir un niveau d'engagement élevé en variant les consignes. Prendre des notes d'observation structurées pour l'évaluation formative et sommative.",
        f"Circuler dans tout l'espace de jeu pour avoir une vue d'ensemble. Encourager la participation active de tous les élèves, incluant ceux qui tendent à rester en retrait. Adapter les règles si nécessaire pour maintenir l'équilibre entre les équipes. Utiliser le chronomètre pour structurer les périodes de jeu et de repos.",
    ]
    roles_retour = [
        f"Guider les étirements en nommant les groupes musculaires sollicités et en expliquant leur importance. Animer une discussion de retour en posant des questions ouvertes sur les apprentissages réalisés. Créer une atmosphère calme et respectueuse pour favoriser la réflexion. Féliciter le groupe pour les efforts et les comportements positifs observés.",
        f"Poser des questions de réflexion variées pour amener les élèves à verbaliser ce qu'ils ont appris. Valoriser les apprentissages observés en donnant des exemples concrets tirés de la séance. Encourager les élèves à identifier un élément qu'ils souhaitent améliorer à la prochaine séance. Faire le lien entre l'activité vécue et la vie quotidienne.",
        f"Créer une ambiance calme propice à la récupération physique et mentale. Guider la respiration et la relaxation en utilisant des exercices de retour au calme progressifs. Inviter les élèves à évaluer leur propre performance sur une échelle simple. Annoncer brièvement le contenu de la prochaine séance pour maintenir la motivation.",
        f"Faire un bilan verbal structuré en revenant sur les objectifs de la séance. Demander aux élèves de partager un moment fort ou une difficulté rencontrée. Annoncer les objectifs de la prochaine séance et faire un lien avec ce qui a été appris aujourd'hui. Superviser le rangement du matériel en le transformant en activité éducative.",
    ]

    # ======== DESCRIPTION (expanded to 5+ sentences) ========
    desc_templates_young = [
        f"Les enfants découvrent le {m} à travers des activités ludiques et imaginaires qui stimulent leur curiosité naturelle. Ils développent leurs habiletés motrices de base dans un contexte sécurisant et amusant, où chaque enfant peut progresser à son propre rythme. L'enseignant crée un environnement bienveillant qui favorise l'exploration libre et la prise de risques calculés. Les consignes sont données sous forme de jeux et d'histoires pour capter l'attention des tout-petits. L'accent est mis sur le plaisir de bouger, la socialisation et la construction d'une image positive de l'activité physique. Chaque enfant est encouragé à essayer, à persévérer et à célébrer ses réussites, aussi petites soient-elles.",
        f"Dans un univers imaginaire soigneusement préparé par l'enseignant, les élèves explorent le {m} en variant les approches et les solutions motrices. L'activité est conçue pour stimuler tous les sens et encourager la créativité dans le mouvement. Les enfants apprennent à écouter leur corps, à respecter celui des autres et à coopérer avec leurs camarades. L'accent est mis sur le plaisir de bouger et la découverte de nouvelles façons de s'exprimer par le mouvement. Des repères visuels colorés et du matériel adapté à la taille des enfants sont utilisés pour faciliter la compréhension des tâches. L'enseignant valorise chaque tentative et guide doucement vers l'acquisition des habiletés fondamentales.",
        f"Activité ludique de {m} spécialement adaptée aux tout-petits, où le jeu est le principal vecteur d'apprentissage. Les enfants explorent, essaient et découvrent à leur rythme dans un climat de confiance et de bienveillance. L'environnement est aménagé de façon à offrir différentes zones de complexité croissante. Les transitions entre les activités sont fluides et accompagnées de comptines ou de signaux musicaux. L'enseignant utilise le renforcement positif abondamment et adapte ses interventions au niveau de développement de chaque enfant. La séance se termine par un moment calme qui aide les enfants à faire le bilan de leurs découvertes.",
    ]
    desc_templates_mid = [
        f"Les élèves approfondissent leurs habiletés en {m} à travers des exercices structurés et des situations de jeu authentiques adaptées à leur niveau de développement. L'accent est mis sur la technique, la progression et l'acquisition de stratégies efficaces. Des ateliers de niveaux différents permettent à chaque élève de travailler dans sa zone proximale de développement. L'enseignant utilise des démonstrations, des rétroactions ciblées et des grilles d'autoévaluation pour guider les apprentissages. Les élèves sont amenés à verbaliser leurs choix et à justifier leurs stratégies auprès de leurs pairs. La séance intègre des moments de pratique individuelle, en dyade et en petit groupe pour varier les contextes d'apprentissage.",
        f"Séance de {m} soigneusement planifiée, combinant apprentissage technique rigoureux et mises en situation motivantes. Les élèves développent leur autonomie et leur capacité à s'autoévaluer grâce à des critères de réussite explicites. L'enseignant propose des défis progressifs qui maintiennent un haut niveau de motivation tout en assurant un taux de réussite suffisant. Les élèves apprennent à recevoir et donner des rétroactions constructives à leurs pairs. Des outils visuels (affiches, pictogrammes, vidéos) soutiennent la compréhension des éléments techniques clés. La coopération et l'esprit sportif sont valorisés tout au long de la séance.",
        f"Par des ateliers variés de {m}, les élèves renforcent leurs compétences motrices tout en développant leur esprit sportif, leur sens de la coopération et leur capacité à résoudre des problèmes moteurs. L'enseignant structure la séance de façon à offrir un temps d'engagement moteur maximal. Les transitions sont efficaces et les consignes claires pour minimiser les temps d'attente. Chaque atelier présente un défi adapté avec des possibilités de régulation. Les élèves sont encouragés à expérimenter différentes approches et à identifier celles qui sont les plus efficaces pour eux.",
    ]
    desc_templates_old = [
        f"Séance avancée de {m} intégrant des dimensions tactiques, stratégiques et réflexives qui préparent les élèves à devenir des pratiquants autonomes et engagés. Les élèves font preuve d'autonomie dans leur apprentissage et leur évaluation, en utilisant des grilles critériées et des outils d'autoévaluation sophistiqués. L'enseignant adopte un rôle de facilitateur et de coach, laissant plus de responsabilités aux élèves dans la gestion de leur pratique. Les situations proposées sont complexes et requièrent la mobilisation simultanée de plusieurs compétences. Les élèves analysent leurs performances à l'aide de données objectives et ajustent leurs stratégies en conséquence. La dimension éthique du sport et de l'activité physique est abordée à travers des discussions et des mises en situation.",
        f"Les élèves perfectionnent leurs habiletés en {m} dans des situations complexes et authentiques qui simulent les exigences de la pratique sportive réelle. L'analyse critique, la prise de décision rapide et l'autorégulation sont au cœur de la séance. L'enseignant propose des situations-problèmes qui obligent les élèves à mobiliser leurs connaissances théoriques et pratiques. Le travail d'équipe est valorisé et les rôles sont distribués de façon à développer le leadership partagé. Les élèves documentent leur progression et fixent des objectifs personnels réalistes. La séance inclut des moments de réflexion métacognitive sur les processus d'apprentissage utilisés.",
        f"Activité de {m} de niveau avancé avec objectifs de performance individuels et collectifs ambitieux mais réalistes. Les élèves développent leur leadership, leur esprit critique et leur capacité à coacher leurs pairs. L'enseignant crée un environnement d'apprentissage qui valorise la prise de risques calculés et l'innovation dans les solutions motrices. Les données de performance sont collectées et analysées pour guider la planification des séances suivantes. Les élèves sont invités à concevoir des variantes d'exercices et à proposer des améliorations. La dimension santé et bien-être est intégrée à travers la compréhension des principes d'entraînement et de récupération.",
    ]

    if age_key == "young":
        desc = pick(desc_templates_young)
    elif age_key == "mid":
        desc = pick(desc_templates_mid)
    else:
        desc = pick(desc_templates_old)

    # ======== CONTEXTE (expanded) ========
    contexte_templates = [
        f"En contexte de {m}, les élèves vivent des situations d'apprentissage progressives soigneusement adaptées à leur niveau de développement moteur, cognitif et social. L'enseignant a préparé l'environnement de façon à maximiser le temps d'engagement moteur et à minimiser les temps d'attente. Les consignes sont claires, concises et accompagnées de démonstrations visuelles. Le matériel est disposé de manière stratégique pour faciliter les transitions entre les activités. L'atmosphère est positive et encourage la prise de risques calculés dans un cadre sécuritaire.",
        f"L'activité se déroule dans un environnement soigneusement structuré et sécuritaire où les élèves peuvent explorer le {m} de façon stimulante et progressive. L'enseignant a identifié les prérequis nécessaires et a planifié des activités de complexité croissante. Le climat d'apprentissage favorise l'entraide, le respect mutuel et la valorisation des différences individuelles. Les élèves sont informés des objectifs de la séance et des critères de réussite dès le début. Des adaptations sont prévues pour répondre aux besoins particuliers de certains élèves.",
        f"Les élèves sont amenés à développer leurs compétences en {m} à travers des défis adaptés, des situations authentiques et des jeux structurés qui donnent du sens aux apprentissages. L'enseignant utilise une approche pédagogique différenciée qui tient compte des forces et des défis de chaque élève. Le regroupement des élèves varie au cours de la séance pour favoriser différents types d'interactions. L'évaluation formative est intégrée de façon continue pour ajuster l'enseignement en temps réel.",
    ]

    # ======== TÂCHE COMPLEXE (expanded) ========
    tache_templates_young = [
        f"L'élève réalise un parcours de {m} en enchaînant au moins 3 actions différentes avec fluidité. Il doit démontrer qu'il comprend les consignes en adaptant ses mouvements à chaque station. L'enseignant observe la qualité de l'exécution, la capacité à maintenir l'effort et le respect des règles de sécurité. L'élève est invité à nommer les actions qu'il réalise et à identifier celles qu'il préfère.",
        f"L'élève participe activement à une activité de {m} en respectant les consignes données et en variant ses mouvements de façon créative. Il explore différentes façons de réaliser la tâche et choisit celles qui lui conviennent le mieux. L'enseignant évalue la participation, l'engagement et la variété des réponses motrices. L'élève démontre sa capacité à coopérer avec ses pairs et à attendre son tour.",
        f"L'élève explore le {m} en essayant au moins 3 façons différentes de bouger et en identifiant verbalement ses préférences. Il démontre sa capacité à utiliser le matériel de façon sécuritaire et appropriée. L'enseignant note la créativité, la persévérance et la capacité de l'élève à s'adapter aux consignes changeantes. L'élève partage ses découvertes avec un camarade et écoute les idées des autres.",
    ]
    tache_templates_mid = [
        f"L'élève exécute une séquence de {m} en démontrant la maîtrise d'au moins 3 éléments techniques clés avec précision et contrôle. Il adapte sa performance en fonction des rétroactions reçues de l'enseignant et de ses pairs. L'évaluation porte sur la qualité d'exécution, la capacité d'autoévaluation et la progression démontrée au cours de la séance. L'élève utilise une grille d'observation pour évaluer un camarade et offrir des conseils constructifs.",
        f"L'élève adapte ses actions de {m} à différentes situations de jeu en faisant des choix tactiques éclairés et en justifiant ses décisions. Il démontre sa capacité à lire le jeu, à anticiper les actions des autres et à réagir de façon appropriée. L'enseignant évalue la pertinence des choix tactiques, la communication avec les coéquipiers et la capacité à ajuster sa stratégie. L'élève fait un retour réflexif sur ses performances et identifie des pistes d'amélioration.",
        f"L'élève participe à une situation complexe de {m} en combinant habiletés techniques, prise de décision et communication efficace avec ses coéquipiers. Il démontre sa compréhension des principes de jeu et sa capacité à les appliquer dans des contextes variés. L'évaluation porte sur la qualité technique, l'efficacité tactique et la contribution au jeu collectif. L'élève remplit une fiche d'autoévaluation après l'activité.",
    ]
    tache_templates_old = [
        f"L'élève analyse et adapte sa stratégie de {m} en fonction des réponses de l'adversaire ou de l'environnement, démontrant une pensée tactique avancée. Il documente sa démarche d'amélioration en utilisant des outils d'analyse (vidéo, statistiques, grilles). L'évaluation porte sur la profondeur de l'analyse, la pertinence des ajustements et la capacité à transférer ses apprentissages dans de nouveaux contextes. L'élève prend en charge l'échauffement ou le retour au calme d'un sous-groupe.",
        f"L'élève crée et présente un enchaînement de {m} intégrant des éléments techniques avancés, des transitions fluides et une dimension esthétique ou stratégique. Il justifie ses choix en s'appuyant sur des principes biomécaniques et tactiques. L'évaluation tient compte de l'originalité, de la maîtrise technique, de la capacité d'analyse et de la qualité de la présentation. L'élève offre des rétroactions structurées à ses pairs en utilisant un vocabulaire technique approprié.",
        f"L'élève démontre une maîtrise avancée du {m} en situation complexe avec prise de décision autonome et autorégulation. Il assume un rôle de leader en guidant ses coéquipiers et en proposant des ajustements stratégiques. L'évaluation porte sur l'autonomie, le leadership, la qualité d'exécution et la capacité à gérer la pression. L'élève établit un plan d'entraînement personnel pour poursuivre sa progression en dehors des cours.",
    ]

    if age_key == "young":
        tache = pick(tache_templates_young)
    elif age_key == "mid":
        tache = pick(tache_templates_mid)
    else:
        tache = pick(tache_templates_old)

    # ======== VARIANTES (3-5 per SAÉ) ========
    variantes_bank_young = [
        f"Simplifier la tâche en réduisant le nombre d'actions à enchaîner ou en augmentant la taille des cibles. Utiliser des repères visuels au sol (cônes colorés, lignes) pour guider les déplacements.",
        f"Ajouter un thème imaginaire (animaux de la jungle, astronautes, pirates) pour stimuler la motivation et la créativité dans les réponses motrices.",
        f"Proposer l'activité en musique en variant le tempo pour explorer différentes vitesses d'exécution. Alterner entre mouvements lents et rapides.",
        f"Remplacer le matériel standard par des objets inusités (foulards, ballons de baudruche, rubans) pour varier les sensations et les défis moteurs.",
        f"Organiser l'activité en parcours à stations avec des durées courtes (2-3 minutes) pour maintenir l'attention et la motivation des tout-petits.",
        f"Intégrer des pauses actives sous forme de jeux de devinettes motrices ou de statues pour travailler l'équilibre et l'écoute.",
        f"Permettre aux enfants de créer leur propre parcours en choisissant parmi le matériel disponible, favorisant ainsi l'autonomie et la prise de décision.",
    ]
    variantes_bank_mid = [
        f"Augmenter la complexité en ajoutant des contraintes (utiliser seulement la main non dominante, yeux fermés pour certains exercices d'équilibre, temps limité).",
        f"Introduire un système de points ou de défis à relever pour stimuler la motivation intrinsèque et l'engagement des élèves dans la tâche.",
        f"Proposer une version coopérative où les élèves doivent synchroniser leurs mouvements ou atteindre un objectif commun, favorisant la communication.",
        f"Organiser un tournoi amical avec des règles adaptées pour développer l'esprit sportif, la gestion des émotions et le respect de l'adversaire.",
        f"Offrir des choix de niveaux de difficulté (vert = facile, jaune = intermédiaire, rouge = avancé) pour favoriser l'autodifférenciation et l'autonomie.",
        f"Intégrer un rôle d'observateur-coach où un élève observe un pair et lui offre des rétroactions à partir d'une grille simple d'observation.",
        f"Varier les formations (individuel, en dyade, en petit groupe de 4, en grand groupe) pour développer différentes compétences sociales et motrices.",
    ]
    variantes_bank_old = [
        f"Proposer aux élèves de concevoir et d'arbitrer leur propre version du jeu en modifiant les règles, les dimensions du terrain ou le système de pointage.",
        f"Introduire l'analyse vidéo où les élèves filment leurs performances et les analysent en identifiant les forces et les points à améliorer.",
        f"Ajouter des contraintes tactiques complexes (nombre limité de touches, zones interdites, rôles spécialisés) pour développer l'adaptabilité et la lecture du jeu.",
        f"Proposer un défi de coaching par les pairs où chaque élève prépare et anime un exercice de 5 minutes pour un petit groupe, développant le leadership.",
        f"Organiser une compétition intercycle ou interclasse avec un comité d'organisation élève pour développer les compétences organisationnelles et le leadership.",
        f"Intégrer des éléments de préparation mentale (visualisation, gestion du stress, concentration) pour enrichir l'expérience sportive et préparer à la compétition.",
        f"Proposer un projet d'entraînement sur plusieurs séances avec un carnet de bord où l'élève planifie, exécute et évalue sa progression personnelle.",
    ]

    if age_key == "young":
        variantes = pick_n(variantes_bank_young, random.randint(3, 4))
    elif age_key == "mid":
        variantes = pick_n(variantes_bank_mid, random.randint(3, 5))
    else:
        variantes = pick_n(variantes_bank_old, random.randint(4, 5))

    # ======== ADAPTATIONS HDAA ========
    adaptation_hdaa = {
        "Trouble du spectre de l'autisme (TSA)": pick([
            f"Utiliser un horaire visuel avec pictogrammes pour présenter les étapes de la séance de {m}. Réduire les stimuli sensoriels (baisser la musique, limiter le bruit ambiant). Offrir un espace de retrait calme si nécessaire. Prévenir l'élève des transitions à l'avance (minuterie visuelle). Utiliser des consignes courtes et concrètes accompagnées de démonstrations. Maintenir une routine stable d'une séance à l'autre.",
            f"Placer l'élève à proximité de l'enseignant pour faciliter la communication et la régulation. Utiliser un système de renforcement positif personnalisé (jetons, autocollants). Permettre l'utilisation d'objets sensoriels pendant les temps d'attente. Jumeler l'élève avec un pair aidant qui modélise les comportements attendus. Découper les tâches complexes en étapes simples et séquentielles. Utiliser un langage visuel et concret plutôt qu'abstrait.",
        ]),
        "Handicap physique ou moteur": pick([
            f"Adapter la hauteur, la distance ou la taille des cibles selon les capacités de l'élève. Proposer des rôles actifs alternatifs (arbitre, marqueur, stratège, chronométreur) lorsque la participation physique directe est limitée. Utiliser du matériel adapté (ballons plus légers, raquettes avec poignées modifiées, surfaces antidérapantes). Modifier les règles pour assurer l'inclusion (passes obligatoires, zones protégées). Consulter l'intervenant en adaptation scolaire pour les adaptations spécifiques.",
            f"Aménager l'espace pour assurer l'accessibilité (rampes, surfaces planes, espace de manœuvre suffisant). Permettre l'utilisation d'aides techniques (fauteuil roulant, déambulateur, orthèses). Proposer des exercices en position assise ou couchée comme alternatives. Adapter le temps de réalisation et les critères de réussite. Valoriser l'effort et la participation plutôt que la performance pure. Impliquer l'élève dans le choix de ses adaptations pour favoriser l'autonomie.",
        ]),
        "Trouble déficitaire de l'attention (TDA/H)": pick([
            f"Structurer la séance avec des périodes courtes et variées pour maintenir l'attention. Utiliser des signaux clairs et multisensoriels (visuels, auditifs, kinesthésiques) pour les transitions. Placer l'élève à proximité de l'enseignant, loin des distractions. Donner une responsabilité spéciale (distribuer le matériel, être le capitaine) pour canaliser l'énergie. Répéter les consignes individuellement et demander à l'élève de les reformuler. Proposer des moments de mouvement libre entre les activités plus structurées.",
            f"Utiliser un système de gestion du comportement positif avec des objectifs réalistes et atteignables. Prévoir des activités à haute intensité physique pour permettre une dépense d'énergie constructive. Alterner entre activités dynamiques et moments de concentration plus calmes. Offrir des choix dans les activités pour favoriser l'engagement. Établir des routines claires et prévisibles. Utiliser un minuteur visuel pour aider l'élève à gérer le temps.",
        ]),
        "Difficulté d'apprentissage": pick([
            f"Simplifier les consignes en utilisant un vocabulaire de base et en les accompagnant de démonstrations visuelles. Décomposer les tâches complexes en étapes simples et progressives avec des repères concrets. Offrir plus de temps de pratique pour chaque habileté. Utiliser le tutorat par les pairs en jumelant l'élève avec un camarade patient et compétent. Fournir des repères visuels permanents (affiches, pictogrammes, couleurs) pour soutenir la mémorisation. Célébrer les progrès individuels plutôt que de comparer aux autres.",
            f"Proposer des activités multisensorielles qui sollicitent la vue, l'ouïe et le toucher pour renforcer les apprentissages. Réduire le nombre de consignes données simultanément à 2-3 maximum. Utiliser des démonstrations entre pairs pour modéliser les comportements attendus. Prévoir des périodes de révision et de consolidation régulières. Adapter les critères d'évaluation en maintenant des attentes élevées mais réalistes. Communiquer les progrès aux parents pour renforcer la motivation.",
        ]),
    }

    # ======== ENRICHISSEMENT ========
    enrichissement_bank = [
        f"Les élèves avancés peuvent créer un mini-parcours d'obstacles intégrant les habiletés travaillées et le présenter à un groupe de plus jeunes. Ils expliquent les règles, démontrent les mouvements et accompagnent les participants, développant ainsi leur leadership pédagogique.",
        f"Proposer un défi de création chorégraphique ou de séquence de mouvements en lien avec le {m}, à présenter lors d'un spectacle de classe ou d'une journée portes ouvertes. Les élèves travaillent en équipe pour concevoir, répéter et peaufiner leur présentation.",
        f"Inviter les élèves à tenir un journal d'apprentissage sportif dans lequel ils documentent leur progression, dessinent les mouvements clés et notent leurs objectifs personnels. Ce journal peut être utilisé lors des conférences parents-enseignant pour illustrer les apprentissages.",
        f"Organiser un projet interdisciplinaire où les élèves fabriquent du matériel sportif à partir de matériaux recyclés (raquettes en carton, cibles, obstacles) et l'utilisent dans une séance adaptée. Ce projet intègre les arts plastiques, les sciences et l'éducation physique.",
        f"Proposer aux élèves de documenter l'activité par la photographie ou la vidéo (avec supervision) pour créer un album ou une présentation numérique sur les apprentissages réalisés en {m}. Ce projet développe les compétences numériques et la communication.",
        f"Inviter un athlète local, un entraîneur bénévole ou un parent sportif à venir partager son expertise et sa passion pour enrichir l'expérience des élèves. Préparer des questions d'entrevue avec les élèves pour structurer la visite.",
    ]
    enrichissement = pick(enrichissement_bank)

    # ======== INTERDISCIPLINARITÉ ========
    interdisciplinarite_bank = [
        f"Mathématiques : Calculer les distances parcourues, les scores, les moyennes de performance, les angles de lancer ou les statistiques de jeu. Utiliser des graphiques pour visualiser la progression individuelle ou collective au fil des séances.",
        f"Français : Rédiger un compte-rendu de la séance en utilisant le vocabulaire technique approprié. Pratiquer la communication orale en expliquant les règles d'un jeu à un camarade ou en présentant sa stratégie à l'équipe.",
        f"Sciences et technologie : Explorer les principes physiques en jeu (force, vitesse, trajectoire, gravité, frottement) et les relier aux mouvements pratiqués. Observer l'effet de la force appliquée sur la trajectoire d'un objet.",
        f"Arts : Intégrer des éléments esthétiques dans les mouvements (grâce, rythme, harmonie, expression corporelle). Créer une affiche illustrant les règles du jeu ou les mouvements clés de la séance avec des dessins et des couleurs.",
        f"Éthique et culture religieuse : Discuter des valeurs sportives (respect, persévérance, entraide, humilité, dépassement de soi) et de leur application dans la vie quotidienne. Explorer les origines culturelles de différents sports et jeux traditionnels.",
        f"Géographie et univers social : Découvrir l'origine géographique du sport ou du jeu pratiqué et les traditions qui y sont associées. Situer sur une carte les pays où ce type d'activité est populaire et comprendre son contexte culturel.",
    ]
    interdisciplinarite = pick_n(interdisciplinarite_bank, random.randint(2, 3))

    # ======== NOTES ENSEIGNANT ========
    notes_bank = [
        f"S'assurer de vérifier l'état du matériel avant chaque séance pour prévenir les brisures et les blessures. Prévoir du matériel supplémentaire en cas de perte ou de défectuosité. Ranger le matériel de façon systématique pour faciliter la préparation des prochaines séances.",
        f"Prévoir un plan B en cas de pluie ou d'indisponibilité du gymnase. Avoir des activités alternatives qui travaillent les mêmes compétences dans un espace réduit (corridor, classe). Adapter les consignes en conséquence pour maintenir la qualité pédagogique.",
        f"Documenter les observations pour le bulletin en notant les progrès significatifs et les défis persistants de chaque élève. Utiliser une grille d'observation avec les critères du PFEQ pour assurer la cohérence et l'objectivité de l'évaluation.",
        f"Communiquer avec les parents des élèves HDAA pour connaître les adaptations qui fonctionnent à la maison et en classe. Collaborer avec l'orthopédagogue et le TES pour assurer la cohérence des interventions. Tenir un dossier d'adaptation pour chaque élève.",
        f"Planifier les groupements d'élèves à l'avance pour favoriser les interactions positives et éviter les conflits récurrents. Varier les compositions d'équipes d'une séance à l'autre. Utiliser des méthodes de formation d'équipes rapides et équitables.",
        f"Intégrer la dimension santé en discutant brièvement de l'importance de l'hydratation, du sommeil, de la nutrition et de l'activité physique quotidienne. Faire le lien entre les activités de la séance et les habitudes de vie saine.",
        f"Filmer occasionnellement la séance (avec les autorisations parentales) pour fins d'autoévaluation professionnelle et pour montrer aux élèves leurs progrès lors de visionnements. Cet outil est précieux pour le portfolio professionnel et les communications aux parents.",
    ]
    notes = " | ".join(pick_n(notes_bank, 3))

    # ======== GRILLE D'ÉVALUATION ========
    grille_evaluation = {
        "Très bien": pick([
            f"L'élève exécute les habiletés de {m} avec fluidité, précision et constance. Il fait preuve d'initiative et adapte ses actions de façon autonome aux situations rencontrées. Il participe activement, respecte les règles et encourage ses pairs.",
            f"L'élève démontre une maîtrise assurée des éléments techniques de {m}. Il anticipe les situations, prend des décisions éclairées et communique efficacement avec ses coéquipiers. Son engagement est exemplaire et constant tout au long de la séance.",
        ]),
        "Bien": pick([
            f"L'élève exécute les habiletés de {m} avec une qualité technique satisfaisante et un niveau de contrôle adéquat. Il participe de façon régulière et respecte généralement les consignes. Il démontre une progression par rapport à ses performances antérieures.",
            f"L'élève maîtrise les éléments de base du {m} et commence à les combiner dans des situations plus complexes. Sa participation est active et il fait des efforts visibles pour s'améliorer. Il accepte les rétroactions et tente de les appliquer.",
        ]),
        "En développement": pick([
            f"L'élève est en voie d'acquérir les habiletés de base en {m} et nécessite un soutien accru de l'enseignant. Il participe avec encouragement et démontre de la volonté à s'améliorer. Des adaptations sont mises en place pour favoriser sa progression et maintenir sa motivation.",
            f"L'élève éprouve des difficultés avec certains éléments techniques du {m} mais montre des signes de progression avec l'aide apportée. Il a besoin de temps supplémentaire et de pratique répétée. L'enseignant offre un soutien individualisé et des situations simplifiées pour favoriser la réussite.",
        ]),
    }

    # ======== VALEURS ÉDUCATIVES ========
    valeurs_bank = [
        "Respect de soi et des autres",
        "Persévérance et dépassement de soi",
        "Coopération et entraide",
        "Esprit sportif et fair-play",
        "Autonomie et responsabilisation",
        "Engagement et participation active",
        "Créativité et ouverture d'esprit",
        "Plaisir de bouger et mode de vie actif",
        "Gestion des émotions et résilience",
        "Communication et écoute active",
    ]
    valeurs = pick_n(valeurs_bank, random.randint(3, 5))

    # ======== CONSEILS DE SÉCURITÉ ========
    securite_bank = [
        f"Vérifier que les élèves portent des chaussures de sport appropriées avec des semelles non marquantes et des lacets bien attachés.",
        f"S'assurer que l'espace de jeu est libre d'obstacles et que les surfaces sont propres et non glissantes. Baliser les zones de jeu clairement.",
        f"Rappeler les règles de sécurité spécifiques au {m} avant le début de chaque activité. Insister sur le contrôle de soi et le respect de l'espace personnel.",
        f"Avoir une trousse de premiers soins accessible et connaître les allergies et conditions médicales des élèves. Garder un téléphone à proximité.",
        f"Établir un signal d'arrêt clair (sifflet, mot-clé, geste) que tous les élèves connaissent et respectent immédiatement.",
        f"Adapter l'intensité des activités à la condition physique des élèves et prévoir des moments de récupération et d'hydratation suffisants.",
        f"Superviser de façon active en se positionnant pour avoir une vue d'ensemble de tout le groupe. Ne jamais laisser les élèves sans surveillance.",
    ]
    securite = pick_n(securite_bank, random.randint(3, 4))

    # ======== EXPANDED PROGRESSION (longer activity descriptions) ========
    echauffement_expanded = f"{echauffement_act} L'enseignant s'assure que tous les élèves sont actifs et que le rythme cardiaque augmente progressivement. Il propose des variations pour maintenir l'intérêt : changer de direction, varier la vitesse, ajouter des défis moteurs simples. Les élèves qui le souhaitent peuvent proposer des mouvements au groupe."
    apprentissage_expanded = f"{apprentissage_act} L'enseignant décompose les habiletés en éléments simples et propose une progression du plus facile au plus difficile. Il utilise des démonstrations, des repères visuels et des mots-clés pour faciliter l'apprentissage. Les élèves pratiquent d'abord individuellement, puis en dyade pour obtenir des rétroactions de leurs pairs."
    mise_en_action_expanded = f"{mise_en_action_act} L'enseignant structure l'activité pour maximiser le temps d'engagement moteur de chaque élève. Il utilise des rotations rapides, des équipes de taille appropriée et des règles claires. Il observe et note les comportements significatifs pour l'évaluation. Des ajustements sont faits en temps réel pour maintenir le niveau de défi optimal."
    retour_expanded = f"{retour_act} L'enseignant guide un retour au calme progressif qui inclut des étirements ciblés, une discussion réflexive et un moment de gratitude. Les élèves partagent ce qu'ils ont appris et identifient un objectif pour la prochaine séance. Le rangement du matériel est organisé de façon efficace et responsable."

    # Tags
    domaine_tag = cat["domaine"].split(" —")[0].lower()
    tags = [domaine_tag, moyen.lower().replace(" / ", "-").replace(" ", "-"),
            cycle_info["cycle"].lower().replace(" ", "-")]
    extra_tags = ["pfeq", "éducation-physique", "gymnase", "actif", "santé",
                  "motricité", "habileté", "plaisir", "mouvement", "sport"]
    tags.extend(pick_n(extra_tags, 3))

    # Espace
    espaces = ["Gymnase", "Gymnase", "Gymnase", "Gymnase", "Gymnase double",
               "Cour extérieure", "Salle polyvalente"]
    espace = pick(espaces)

    sae = {
        "id": f"{prefix}-{idx:03d}",
        "titre": title,
        "cycle": cycle_info["cycle"],
        "niveau": cycle_info["niveau"],
        "duree_periodes": cycle_info["duree_periodes"],
        "duree_par_periode": cycle_info["duree_par_periode"],
        "moyen_action": moyen,
        "competence_pfeq": cat["competence"],
        "description": desc,
        "contexte_apprentissage": pick(contexte_templates),
        "tache_complexe": tache,
        "criteres_evaluation": criteres,
        "savoirs_essentiels": savoirs,
        "progression": [
            {
                "phase": "Échauffement",
                "duree": cycle_info["echauffement"],
                "activite": echauffement_expanded,
                "role_enseignant": pick(roles_echauffement),
            },
            {
                "phase": "Apprentissage",
                "duree": cycle_info["apprentissage"],
                "activite": apprentissage_expanded,
                "role_enseignant": pick(roles_apprentissage),
            },
            {
                "phase": "Mise en action",
                "duree": cycle_info["mise_en_action"],
                "activite": mise_en_action_expanded,
                "role_enseignant": pick(roles_mise_en_action),
            },
            {
                "phase": "Retour au calme",
                "duree": cycle_info["retour"],
                "activite": retour_expanded,
                "role_enseignant": pick(roles_retour),
            },
        ],
        "materiel": materiel,
        "espace": espace,
        "tags": tags,
        "variantes": variantes,
        "adaptation_hdaa": adaptation_hdaa,
        "enrichissement": enrichissement,
        "interdisciplinarite": interdisciplinarite,
        "notes": notes,
        "grille_evaluation": grille_evaluation,
        "valeurs_educatives": valeurs,
        "securite": securite,
    }
    return sae


def generate_category(cat):
    """Generate 140 SAÉ for one category."""
    sae_list = []
    used_titles = set()
    idx = 1

    for cycle_idx, cycle_info in enumerate(CYCLES):
        count = SAE_PER_CYCLE[cycle_idx]
        for _ in range(count):
            sae = generate_sae(cat, idx, cycle_info, used_titles)
            sae_list.append(sae)
            idx += 1

    return sae_list


def write_file(cat, sae_list):
    """Write the JSON file for a category."""
    output = {
        "domaine": cat["domaine"],
        "total_sae": len(sae_list),
        "programme": "PFEQ — Éducation physique et à la santé",
        "sae": sae_list,
    }

    filepath = os.path.join(OUTPUT_DIR, cat["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    return filepath


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total = 0
    for cat in ALL_CATEGORIES:
        sae_list = generate_category(cat)
        filepath = write_file(cat, sae_list)
        count = len(sae_list)
        total += count
        print(f"✓ {cat['file']:30s} → {count} SAÉ générées → {filepath}")

    print(f"\n{'='*60}")
    print(f"TOTAL : {total} SAÉ générées dans {len(ALL_CATEGORIES)} fichiers")
    print(f"{'='*60}")

    # Verification
    print("\nVérification des fichiers :")
    for cat in ALL_CATEGORIES:
        filepath = os.path.join(OUTPUT_DIR, cat["file"])
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        n = len(data["sae"])
        first_id = data["sae"][0]["id"]
        last_id = data["sae"][-1]["id"]
        # Check unique titles
        titles = [s["titre"] for s in data["sae"]]
        unique_titles = len(set(titles))
        # Check cycle distribution
        cycles = {}
        for s in data["sae"]:
            cycles[s["cycle"]] = cycles.get(s["cycle"], 0) + 1
        cycle_dist = ", ".join(f"{c}: {n}" for c, n in sorted(cycles.items()))
        # Word count
        word_counts = []
        for s in data["sae"]:
            text = json.dumps(s, ensure_ascii=False)
            wc = len(text.split())
            word_counts.append(wc)
        avg_wc = sum(word_counts) // len(word_counts)
        min_wc = min(word_counts)
        max_wc = max(word_counts)

        status = "OK" if n == 140 else "ERREUR"
        dup_status = f"({unique_titles} uniques)" if unique_titles < n else "(tous uniques)"
        print(f"  [{status}] {cat['file']:30s} — {n} SAÉ, IDs {first_id}..{last_id}, titres {dup_status}")
        print(f"         Distribution : {cycle_dist}")
        print(f"         Mots : moy={avg_wc}, min={min_wc}, max={max_wc}")


if __name__ == "__main__":
    main()
