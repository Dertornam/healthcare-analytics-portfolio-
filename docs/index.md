
---
layout: default
title: Healthcare Analytics Portfolio
---

<style>
/* Simple enhancements for Cayman */
.hero { padding: 2.5rem 1rem; background: linear-gradient(135deg,#0ea5e9 0%, #10b981 100%);
        color: #fff; border-radius: 12px; text-align: center; margin-bottom: 1.5rem; }
.hero h1 { margin: 0 0 .25rem 0; font-size: 2.0rem; }
.btn-row { margin-top: 1rem; display: inline-flex; gap: .75rem; flex-wrap: wrap; }
.btn { display:inline-block; padding:.6rem 1rem; border-radius:999px; text-decoration:none; font-weight:600; }
.btn.primary { background:#fff; color:#0f172a; }
.btn.ghost { border:2px solid #fff; color:#fff; }
.grid { display:grid; gap:1rem; }
@media(min-width:900px){ .grid.cols-2 { grid-template-columns: 1fr 1fr; } }
.card { background:#fff; border-radius:12px; padding:1rem; box-shadow:0 2px 12px rgba(0,0,0,.06); }
.caption { font-size:.95rem; color:#475569; margin:.5rem 0 0 0; }
.kpis { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; }
.kpi { background:#ecfeff; border:1px solid #cffafe; border-radius:10px; padding:.5rem .75rem; font-weight:600; }
.badges span { display:inline-block; background:#f1f5f9; border-radius:999px; padding:.35rem .7rem; margin:.25rem; }
figure { margin:0; }
figure img { width:100%; border-radius:10px; }
figcaption { font-size:.95rem; color:#475569; margin-top:.35rem; }
footer.small { margin-top:1.5rem; font-size:.9rem; color:#64748b; }
</style>

<div class="hero">
  <h1>Turning Healthcare Data into Actionable Insights</h1>
  <p>From messy sources to clear decisions—cleaning, analysis, and automated reporting.</p>
  <div class="btn-row">
    <a class="btn primary" href="#work">Explore My Projects</a>
    <a class="btn ghost" href="https://github.com/{{ site.github.owner_name }}/{{ site.github.repository_name }}">View on GitHub</a>
  </div>
  <div class="kpis" style="margin-top:1rem;">
    <div class="kpi">Synthetic, anonymized datasets</div>
    <div class="kpi">Reproducible Python workflows</div>
    <div class="kpi">Auto-generated weekly report</div>
  </div>
</div>

## Overview
Imagine hospital feedback, readmission flags, and claim lines—organized and decision-ready.  
This portfolio shows how I clean, analyze, and visualize **healthcare** data to surface insights fast.

**Process**: Raw Data → Cleaning → Analysis → Visualization → Insights

---

## Why Healthcare Analytics?
- Improve patient experience and communication.  
- Reduce 30-day readmissions and length of stay.  
- Standardize claims data for reliable cost/volume views.

---

## Featured visuals {#work}

<div class="grid cols-2">
  <div class="card">
    <figure>
      <img src="./fig_1.png" alt="Patient experience means by department">
      <figcaption><strong>Patient Experience by Department.</strong> Highlights where communication and cleanliness lead—and where to focus.</figcaption>
    </figure>
  </div>
  <div class="card">
    <figure>
      <img src="./fig_2.png" alt="Readmission rate by risk decile">
      <figcaption><strong>Readmission Rate by Risk Decile.</strong> Calibrates risk; higher deciles show expected lift for targeted intervention.</figcaption>
    </figure>
  </div>
</div>

<p class="caption">
See also: <a href="./report.md">Weekly Insights (Markdown)</a> · <a href="./cleaned.csv">Cleaned claims CSV</a>
</p>

---

## Mini case study: From signal to action
**Challenge:** Identify drivers of patient satisfaction and readmission risk.  
**Approach:** Cleaned 500–800 synthetic records, visualized department-level means and risk deciles, automated a weekly report.  
**Impact:** Clear priorities for unit leaders and quality teams; reproducible pipeline for ongoing monitoring.

---

## Skills & Tools
<div class="badges">
  <span>Python</span><span>Pandas</span><span>Matplotlib</span><span>SPSS</span>
  <span>Markdown automation</span><span>Data cleaning</span><span>Visualization</span>
</div>

---

## What I bring to your team
- Data cleaning & reproducibility you can trust.  
- Patient-experience and readmissions analytics.  
- Automated reporting workflows.  
- Clear, actionable insights for leaders.

<footer class="small">
  All datasets here are synthetic and anonymized.
</footer>
