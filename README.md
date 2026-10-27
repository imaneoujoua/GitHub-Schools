# GitHub-Schools

GitHub-Schools est une plateforme de gestion pédagogique et de suivi des projets GitHub, pensée pour accompagner les étudiants, enseignants et équipes projets dans l'organisation, la collaboration et le suivi des livrables académiques.

Ce dépôt a été repensé en une base projet de qualité professionnelle, conforme à une démarche de développement en environnement réel, avec une architecture claire, une documentation de soutenance et une interface moderne et responsive.

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Architecture du projet](#architecture-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Documentation](#documentation)
- [Captures d'écran](#captures-d'écran)
- [Roadmap](#roadmap)
- [Licence](#licence)

## Présentation

GitHub-Schools aide à structurer le suivi de projets informatiques autour de GitHub, de la gestion des tâches, de la documentation technique et de la préparation de soutenances PFE. Le système met en place une vue globale sur le statut des initiatives, les métriques de progression, les rôles d'équipe et les jalons du projet.

## Fonctionnalités

- Tableau de bord d'initiative avec indicateurs clés
- Gestion des sprint et des livrables
- Suivi des tâches techniques et pédagogiques
- Vue de la roadmap projet et des jalons
- Interface responsive pour écran 1440x1024 et mobile
- Documentation complète pour soutenance
- Architecture professionnelle avec dossiers src, docs, assets et config

## Architecture du projet

```text
GitHub-Schools/
├── src/
│   ├── index.html
│   ├── app.js
│   ├── data/
│   │   └── mockData.js
│   ├── styles.css
│   └── assets/
│       └── logo.svg
├── public/
├── assets/
│   ├── logo.svg
│   └── hero-dashboard.svg
├── config/
│   └── app.config.js
├── docs/
│   ├── installation.md
│   ├── usage-guide.md
│   ├── scrum/
│   │   ├── product-backlog.md
│   │   └── sprints.md
│   └── uml/
│       ├── use-case.md
│       ├── class-diagram.md
│       └── sequence-diagram.md
├── .gitignore
├── LICENSE
├── README.md
├── package.json
├── vite.config.js
└── dist/
```

## Installation

### Prérequis

- Node.js >= 18
- npm >= 9

### Étapes

```bash
git clone https://github.com/imaneoujoua/GitHub-Schools.git
cd GitHub-Schools
npm install
npm run dev
```

Le projet est ensuite accessible sur : http://localhost:5173

## Utilisation

1. Lancez le projet avec `npm run dev`.
2. Ouvrez l'application dans le navigateur.
3. Consultez le tableau de bord principal, les indicateurs, la roadmap et les livrables.
4. Utilisez les documents dans `docs/` pour la documentation de soutenance.

## Documentation

- Guide d'installation : `docs/installation.md`
- Guide d'utilisation : `docs/usage-guide.md`
- Product Backlog : `docs/scrum/product-backlog.md`
- Sprints S1-S6 : `docs/scrum/sprints.md`
- UML Use Case : `docs/uml/use-case.md`
- UML Class Diagram : `docs/uml/class-diagram.md`
- UML Sequence Diagram : `docs/uml/sequence-diagram.md`

## Captures d'écran

### Aperçu de la landing dashboard

![Dashboard GitHub-Schools](assets/hero-dashboard.svg)

## Roadmap

- S1 : Analyse du besoin, cadrage et architecture
- S2 : Prototype de l'interface et maquettes
- S3 : Développement du tableau de bord principal
- S4 : Intégration avancée et navigation
- S5 : Documentation technique et qualité
- S6 : Validation, préparation de la soutenance

## Licence

Ce projet est distribué sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.
