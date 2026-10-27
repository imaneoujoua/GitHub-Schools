# Diagramme UML - Cas d'utilisation

```mermaid
flowchart LR
    User[Utilisateur] --> UC1[Consulter le tableau de bord]
    User --> UC2[Voir les KPI]
    User --> UC3[Suivre les tâches]
    User --> UC4[Consulter la roadmap]
    User --> UC5[Lire la documentation]
    User --> UC6[Préparer une soutenance]

    Admin[Chef de projet] --> UC7[Valider les livrables]
    Team[Membre de l'équipe] --> UC8[Mettre à jour les tâches]
```

## Description

Le système permet à un utilisateur de visualiser le statut global du projet, de consulter les tâches, la roadmap et la documentation associée. Les rôles administrateur et membre de l'équipe complètent la logique de contribution et de validation.
