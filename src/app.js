import { appConfig } from '../../config/app.config.js';
import { metrics, initiatives, backlog, roadmap, team } from './data/mockData.js';

const app = document.querySelector('#app');

const renderMetricCard = (metric) => `
  <article class="metric-card ${metric.tone}">
    <div class="metric-header">
      <span>${metric.label}</span>
      <span class="dot"></span>
    </div>
    <strong>${metric.value}</strong>
    <small>${metric.trend}</small>
  </article>
`;

const renderInitiative = (initiative) => `
  <div class="initiative-item">
    <div class="initiative-topline">
      <h3>${initiative.title}</h3>
      <span class="status-badge">${initiative.status}</span>
    </div>
    <div class="initiative-meta">
      <span>${initiative.owner}</span>
      <span>${initiative.percent}%</span>
    </div>
    <div class="progress-bar">
      <span style="width: ${initiative.percent}%"></span>
    </div>
  </div>
`;

const renderRoadmap = (item) => `
  <li class="roadmap-item">
    <span class="phase">${item.phase}</span>
    <div>
      <strong>${item.text}</strong>
      <small>${item.date}</small>
    </div>
  </li>
`;

const renderTeam = (member) => `
  <div class="team-card">
    <div class="avatar">${member.name.charAt(0)}</div>
    <div>
      <strong>${member.name}</strong>
      <small>${member.role}</small>
    </div>
  </div>
`;

app.innerHTML = `
  <header class="topbar">
    <div class="brand">
      <img src="../assets/logo.svg" alt="Logo GitHub-Schools" />
      <div>
        <span class="eyebrow">Projet PFE</span>
        <h1>${appConfig.appName}</h1>
      </div>
    </div>
    <nav>
      <a href="#overview">Vue d'ensemble</a>
      <a href="#tasks">Tâches</a>
      <a href="#roadmap">Roadmap</a>
      <a href="#team">Équipe</a>
    </nav>
    <button class="primary-btn">Démarrer</button>
  </header>

  <main class="layout">
    <section class="hero panel" id="overview">
      <div class="hero-copy">
        <span class="badge">Plateforme de gestion GitHub</span>
        <h2>Un projet d'entreprise, prêt pour la soutenance.</h2>
        <p>
          GitHub-Schools centralise les objectifs pédagogiques, les tâches, les livrables et
          la documentation d'un projet réel afin de faciliter le pilotage et la présentation.
        </p>
        <div class="hero-actions">
          <button class="primary-btn">Voir le tableau de bord</button>
          <button class="secondary-btn">Documentation</button>
        </div>
      </div>
      <div class="hero-visual">
        <img src="../assets/hero-dashboard.svg" alt="Aperçu de dashboard GitHub-Schools" />
      </div>
    </section>

    <section class="metrics-grid">
      ${metrics.map(renderMetricCard).join('')}
    </section>

    <section class="content-grid">
      <article class="panel" id="tasks">
        <div class="section-header">
          <h3>Initiatives actives</h3>
          <span>Ce sprint</span>
        </div>
        ${initiatives.map(renderInitiative).join('')}
      </article>

      <article class="panel">
        <div class="section-header">
          <h3>Backlog produit</h3>
          <span>Priorités</span>
        </div>
        <ul class="backlog-list">
          ${backlog.map((item) => `<li>${item}</li>`).join('')}
        </ul>
      </article>
    </section>

    <section class="bottom-grid">
      <article class="panel" id="roadmap">
        <div class="section-header">
          <h3>Roadmap</h3>
          <span>Evolution</span>
        </div>
        <ul class="timeline">
          ${roadmap.map(renderRoadmap).join('')}
        </ul>
      </article>

      <article class="panel" id="team">
        <div class="section-header">
          <h3>Équipe</h3>
          <span>Rôles</span>
        </div>
        <div class="team-grid">
          ${team.map(renderTeam).join('')}
        </div>
      </article>
    </section>
  </main>
`;
