# Simulateur de domotique — Python / Tkinter

**Application de bureau simulant la gestion de l'éclairage et de la température dans trois pièces d'une maison.**

Développé en **Python** avec **Tkinter**, ce projet propose une interface graphique interactive pour sélectionner une pièce, modifier l'état de sa lumière et ajuster sa température. Chaque pièce conserve ses propres valeurs tant que l'application reste ouverte.

> **Périmètre :** il s'agit d'une simulation logicielle. L'application ne communique pas avec des ampoules, thermostats ou autres équipements physiques.

## Fonctionnalités

- **Trois pièces indépendantes :** cuisine, salon et chambre.
- **Gestion de l'éclairage :** passage de `OFF` à `ON`, et inversement, pour la pièce sélectionnée.
- **Réglage de la température :** augmentation ou diminution par pas de **1 °C**, dans l'intervalle **16–30 °C**.
- **Affichage dynamique :** actualisation de l'état de la lumière et de la température après chaque action.
- **Conservation des états par pièce :** le passage d'une pièce à une autre permet de retrouver ses dernières valeurs pendant la session.

**État initial :** la cuisine est sélectionnée ; les trois pièces ont une lumière éteinte et une température de **20 °C**.

## Technologies

| Technologie | Utilisation |
| --- | --- |
| Python 3 | Logique de l'application et gestion des états |
| Tkinter | Fenêtre, boutons, libellés et interactions graphiques |
| Dictionnaires Python | Stockage en mémoire des paramètres de chaque pièce |

Aucune bibliothèque Python tierce n'est nécessaire : Tkinter fait partie de la bibliothèque standard sur les installations Python Windows habituelles.

## Lancer l'application

### Prérequis

- **Python 3** avec Tkinter ;
- **Windows recommandé**, car le code utilise `fenetre.state("zoomed")` pour maximiser la fenêtre.

### Exécution

1. Télécharger ou cloner ce dépôt.
2. Ouvrir un terminal dans le dossier du projet.
3. Exécuter :

```powershell
python Domotique.py
```

Sur Windows, si la commande `python` n'est pas reconnue, essayer :

```powershell
py Domotique.py
```

### Utilisation

1. Sélectionner **Cuisine**, **Salon** ou **Chambre**.
2. Cliquer sur **Allumer** ou **Éteindre** pour changer l'état de la lumière.
3. Cliquer sur **+** ou **−** pour ajuster la température.
4. Changer de pièce pour consulter ou modifier ses paramètres indépendants.

## Fonctionnement technique

Les états sont regroupés dans un dictionnaire Python `etats`. Chaque pièce possède deux propriétés : `lumiere` et `temperature`.

Les principales fonctions sont :

- `choisir_piece()` : sélectionne la pièce active et met à jour l'affichage ;
- `allumer()` / `eteindre()` : modifient l'état de son éclairage ;
- `augmenter_temperature()` / `diminuer_temperature()` : modifient la température en respectant les limites ;
- `mettre_a_jour_affichage()` : synchronise les libellés avec les valeurs en mémoire.

L'interface s'appuie notamment sur `Button`, `Label`, `Frame` et `StringVar` de Tkinter.

## Structure du dépôt

```text
smart-home-simulator-tkinter/
├── Domotique.py
├── Projet _ Application-de-Domotique.pdf
├── README.md
└── .gitignore
```

Le [document de conception](Projet%20_%20Application-de-Domotique.pdf) détaille le noyau fonctionnel, les commandes utilisateur, les états du système, les réponses de l'interface et une **maquette réalisée sur Canva** (page 5). Cette maquette n'est pas une capture d'écran de l'application exécutée.

## Limites et améliorations possibles

**Dans la version actuelle :**

- les états sont conservés uniquement en mémoire et sont réinitialisés au redémarrage ;
- aucun équipement domotique réel n'est connecté ;
- l'apparence des boutons « Allumer » et « Éteindre » ne se resynchronise pas automatiquement avec l'état lumineux lors du changement de pièce ;
- le comportement de maximisation de la fenêtre est prévu pour Windows.

**Évolutions envisageables :**

- enregistrer et restaurer les paramètres des pièces ;
- synchroniser systématiquement le style des boutons avec les états ;
- séparer davantage la logique métier de l'interface pour faciliter les tests ;
- adapter l'affichage à différents systèmes d'exploitation.

---

*Projet de programmation et de conception d'interface graphique — simulation de gestion domotique.*
