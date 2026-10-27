# Diagramme UML - Diagramme de classes

```mermaid
classDiagram
    class User {
        +id: string
        +name: string
        +role: string
    }

    class Project {
        +id: string
        +name: string
        +status: string
        +timeline: string
    }

    class KPI {
        +progressPercent: number
        +teamSize: number
        +completedTasks: number
    }

    class Task {
        +id: string
        +title: string
        +priority: string
        +status: string
    }

    class Sprint {
        +id: string
        +label: string
        +startDate: date
        +endDate: date
    }

    User --> Project
    Project --> KPI
    Project --> Task
    Project --> Sprint
    Task --> Sprint
```

## Description

Le modèle met en évidence les relations entre les utilisateurs, les projets, les tâches et les sprints. Il permet de structurer le suivi d'avancement et le pilotage du projet sur plusieurs itérations.
