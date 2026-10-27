# Diagramme UML - Diagramme de séquence

```mermaid
sequenceDiagram
    actor User
    participant Dashboard as Dashboard GitHub-Schools
    participant Data as Mock Data
    participant App as Application

    User->>Dashboard: Ouvre la page d'accueil
    Dashboard->>App: Demande le chargement des données
    App->>Data: Récupère KPI, tâches, roadmap
    Data-->>App: Renvoie les informations structurées
    App-->>Dashboard: Affiche les cards, listes et roadmap
    User->>Dashboard: Consulte les indicateurs
    User->>Dashboard: Consulte la documentation de soutenance
```

## Description

Ce diagramme représente le flux de chargement des données depuis le modèle de données vers le tableau de bord. Il montre la logique simple et claire d'un système de démonstration avec un design professionnel.
