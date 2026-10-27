# Guide d'installation

## Objectif

Ce document décrit les étapes nécessaires pour installer, lancer et utiliser le projet GitHub-Schools dans un environnement de développement local ou de démonstration.

## Prérequis

- Node.js version 18 ou supérieure
- npm version 9 ou supérieure
- Un navigateur moderne (Chrome, Edge, Firefox)

## Installation locale

```bash
git clone https://github.com/imaneoujoua/GitHub-Schools.git
cd GitHub-Schools
npm install
```

## Lancer le projet

```bash
npm run dev
```

Le serveur démarre par défaut sur :

```text
http://localhost:5173
```

## Build de production

```bash
npm run build
```

La version de production est générée dans le dossier `dist/`.

## Vérification

1. Ouvrir le navigateur à l'adresse locale.
2. Vérifier l'affichage du tableau de bord principal.
3. Vérifier la compatibilité visuelle sur écran 1440x1024.

## Dépannage

- Si `npm install` échoue, vérifier la version de Node.js.
- Si le port 5173 est occupé, modifier le fichier `vite.config.js`.
- Vérifier la présence du dossier `node_modules` après installation.
