<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="840" alt="Udit Parihar. I build machine learning models I can measure, and the APIs, web apps and tests around them. Frankfurt am Main. M.Sc. Global Software Development, Hochschule Fulda.">
</picture>

**Open to Werkstudent, internship and part-time roles in Germany:** ML and AI engineering, Java and Python backend, full-stack, QA and test automation, data and automation.

## Projects, one measured result each

<p align="center">
  <a href="https://github.com/Uditp11/cifar10-from-scratch"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-cifar10-dark.svg"><img src="assets/card-cifar10-light.svg" width="400" alt="cifar10-from-scratch: 96.06% test top-1, evaluated once. ResNet-18 written from scratch in PyTorch. 10,000 held-out images. Every recipe choice tested in a logged ablation."></picture></a>
  <a href="https://github.com/Uditp11/applytrack"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-applytrack-dark.svg"><img src="assets/card-applytrack-light.svg" width="400" alt="applytrack: 86 tests, 0 skipped in CI. Java and Spring Boot API. A status state machine refuses illegal moves. Kubernetes deploy in CI, Terraform deploy to Azure."></picture></a>
  <a href="https://github.com/Uditp11/vectordb-from-scratch"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-vectordb-dark.svg"><img src="assets/card-vectordb-light.svg" width="400" alt="vectordb-from-scratch: 3 search algorithms, by hand. HNSW, KD-Tree and brute force in Python and NumPy. Tests prove KD-Tree matches brute force exactly. Recall and latency benchmarked, local RAG."></picture></a>
  <a href="https://github.com/Uditp11/solar-inspect"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-solar-inspect-dark.svg"><img src="assets/card-solar-inspect-light.svg" width="400" alt="solar-inspect, v1.0: 5 modules, each test split read once. Solar panel inspection in PyTorch: U-Net from scratch, YOLOv8 detection, Kalman and SORT, defect classifier, plant analytics with SQL."></picture></a>
  <a href="https://github.com/Uditp11/shift-log"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-shift-log-dark.svg"><img src="assets/card-shift-log-light.svg" width="400" alt="shift-log, live: end-to-end tested in 2 browsers. Offline-first phone app my friends and I use. Playwright in WebKit and Chromium, one branch per task, tests run before every deploy."></picture></a>
  <a href="https://github.com/Uditp11/Shree_Shyam_Constructions"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-shree-shyam-dark.svg"><img src="assets/card-shree-shyam-light.svg" width="400" alt="Shree_Shyam_Constructions, live: website for a paying client, in English and Hindi. Next.js, TypeScript, Tailwind CSS."></picture></a>
</p>

Tests run on every push:

| applytrack | cifar10 | vectordb | shift-log | einkaufzentrum |
|:---:|:---:|:---:|:---:|:---:|
| [![applytrack CI](https://github.com/Uditp11/applytrack/actions/workflows/ci.yml/badge.svg)](https://github.com/Uditp11/applytrack/actions/workflows/ci.yml) | [![cifar10 CI](https://github.com/Uditp11/cifar10-from-scratch/actions/workflows/ci.yml/badge.svg)](https://github.com/Uditp11/cifar10-from-scratch/actions/workflows/ci.yml) | [![vectordb tests](https://github.com/Uditp11/vectordb-from-scratch/actions/workflows/tests.yml/badge.svg)](https://github.com/Uditp11/vectordb-from-scratch/actions/workflows/tests.yml) | [![shift-log test and deploy](https://github.com/Uditp11/shift-log/actions/workflows/pages.yml/badge.svg)](https://github.com/Uditp11/shift-log/actions/workflows/pages.yml) | [![einkaufzentrum tests](https://github.com/Uditp11/einkaufzentrum/actions/workflows/tests.yml/badge.svg)](https://github.com/Uditp11/einkaufzentrum/actions/workflows/tests.yml) |

## Pick your lane

<details>
<summary><b>ML and AI engineering</b></summary>

- [solar-inspect](https://github.com/Uditp11/solar-inspect): five-stage solar panel inspection in PyTorch. U-Net segmentation written from scratch, YOLOv8 detection with IoU, NMS and AP written by hand, Kalman and SORT tracking checked on synthetic flyovers, defect classification with calibration and distillation, and analytics on real plant data. Each of the three image test splits read once. Open the [headline results](https://github.com/Uditp11/solar-inspect#headline-results)
- [cifar10-from-scratch](https://github.com/Uditp11/cifar10-from-scratch): ResNet-18 written from scratch, 96.06% test accuracy. Open the [ablation ledger](https://github.com/Uditp11/cifar10-from-scratch/blob/main/docs/EXPERIMENTS.md)
- [vectordb-from-scratch](https://github.com/Uditp11/vectordb-from-scratch): HNSW and KD-Tree written by hand, local RAG with Ollama. Open the [benchmark](https://github.com/Uditp11/vectordb-from-scratch/blob/main/docs/BENCHMARK.md)
- [RAG_Adaptive](https://github.com/Uditp11/RAG_Adaptive) (team project): LangGraph chatbot that routes each question to documents, the LLM or web search, then grades and retries retrieval

</details>

<details>
<summary><b>Java and Python backend</b></summary>

- [applytrack](https://github.com/Uditp11/applytrack): Java and Spring Boot API, PostgreSQL with Flyway migrations, a status state machine that refuses illegal moves, statistics computed in SQL
- [vectordb-from-scratch](https://github.com/Uditp11/vectordb-from-scratch): async FastAPI layer over a hand-written vector index
- [einkaufzentrum](https://github.com/Uditp11/einkaufzentrum) (team course project): Flask and SQLAlchemy API with JWT roles and integration tests in CI

</details>

<details>
<summary><b>Full-stack</b></summary>

- [Shree_Shyam_Constructions](https://github.com/Uditp11/Shree_Shyam_Constructions): live website for a paying client, in English and Hindi. [Open the site](https://shree-shyam-constructions.vercel.app/)
- [shift-log](https://github.com/Uditp11/shift-log): offline-first phone app (service worker, IndexedDB), English and German. [Open the app](https://uditp11.github.io/shift-log/)
- [einkaufzentrum](https://github.com/Uditp11/einkaufzentrum) (team course project): React frontend on a Flask API

</details>

<details>
<summary><b>QA and test automation</b></summary>

- [shift-log](https://github.com/Uditp11/shift-log): Playwright end-to-end tests in WebKit at iPhone size and Chromium at Android size, run before every deploy. Open [playwright.config.js](https://github.com/Uditp11/shift-log/blob/main/playwright.config.js)
- [applytrack](https://github.com/Uditp11/applytrack): JUnit 5, Mockito and Testcontainers against a real PostgreSQL
- [cifar10-from-scratch](https://github.com/Uditp11/cifar10-from-scratch): pytest on a Python 3.10 and 3.12 CI matrix
- [solar-inspect](https://github.com/Uditp11/solar-inspect): 232 pytest tests, checked against hand-computed values and against torchvision and statsmodels
- [einkaufzentrum](https://github.com/Uditp11/einkaufzentrum) (team course project): three integration suites, run in CI

</details>

<details>
<summary><b>Data and automation</b></summary>

- [applytrack](https://github.com/Uditp11/applytrack): response rate and status counts computed in SQL
- [solar-inspect](https://github.com/Uditp11/solar-inspect): regression on real solar plant data with Newey-West errors, and five SQLite queries with window functions, each checked against pandas. Open [sql/](https://github.com/Uditp11/solar-inspect/tree/main/sql)
- [einkaufzentrum](https://github.com/Uditp11/einkaufzentrum) (team course project): SQL layer through SQLAlchemy, SQLite and MySQL
- Automation (n8n, Power Automate, Python and JavaScript scripts) was used at work
- Private, not public: my own job-hunt agents, built with Claude, collect postings every day, score them and file them in Notion. I also wrote Claude Code skills and my own MCP server

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="840" alt="">
</picture>

## Stack

Every badge below is used in a public repo on this profile.

**ML and AI** &nbsp;
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-7FC8FF?logo=langchain&logoColor=black)

**Backend and data** &nbsp;
![Java](https://img.shields.io/badge/Java-000000?logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?logo=springboot&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3BABC3?logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?logo=nodedotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

**Frontend** &nbsp;
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white)

**Testing** &nbsp;
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![JUnit 5](https://img.shields.io/badge/JUnit%205-25A162?logo=junit5&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33)

**Cloud and delivery** &nbsp;
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

## How I work

| Habit | Where to see it |
|---|---|
| Measure before I claim | [cifar10 ablation ledger](https://github.com/Uditp11/cifar10-from-scratch/blob/main/docs/EXPERIMENTS.md): every recipe choice tested against a measured noise floor |
| Touch the test set once | [solar-inspect eval script](https://github.com/Uditp11/solar-inspect/blob/main/scripts/eval_test_d1.py) refuses to run until the config is committed |
| Write decisions down | Decision records in [cifar10](https://github.com/Uditp11/cifar10-from-scratch/blob/main/docs/ADR.md) (retractions kept) and [solar-inspect](https://github.com/Uditp11/solar-inspect/tree/main/docs/adr) |
| One branch per task, tests before deploy | [shift-log workflow](https://github.com/Uditp11/shift-log/blob/main/.github/workflows/pages.yml): deploy waits for the tests |

## Where my skills come from

| Area | Built in public (open the repos above) | Used at work (Kidz Brain Academy, 2023 to 2024) | Coursework (graded, M.Sc. and B.Tech) |
|---|---|---|---|
| ML and AI | PyTorch, NumPy, computer vision (segmentation, detection with YOLOv8, tracking with Kalman and SORT, classification), knowledge distillation, statistics (regression, Newey-West errors, bootstrap intervals), model evaluation (ablations, calibration, leakage checks), vector search, LangGraph, LangChain, OpenAI API, Ollama | OpenAI API in internal tools, with output checks | Classical ML and statistics with scikit-learn, PySpark, Hugging Face |
| Backend and data | Java, Spring Boot, PostgreSQL with Flyway migrations, SQLite with window functions, pandas, FastAPI, Flask, SQLAlchemy, REST APIs, JWT | Node.js and Python services, REST APIs, SQL, data cleaning | Thymeleaf, NestJS |
| Frontend | React, Next.js, TypeScript, Tailwind CSS, offline web apps (service worker, IndexedDB) | React | Vue 3, Angular |
| Testing | pytest, JUnit 5, Mockito, Testcontainers, Playwright | Test cases, manual testing, Postman | Two graded testing courses |
| Cloud and delivery | Docker, Docker Compose, Kubernetes (kind), Terraform on Azure, GitHub Actions, Prometheus and Grafana | | Jenkins |
| Automation | Nothing public yet | n8n, Power Automate, Python and JavaScript scripts | |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img src="assets/divider-light.svg" width="840" alt="">
</picture>

## Background

- M.Sc. Global Software Development, Hochschule Fulda (ongoing)
- B.Tech Computer Science, CGPA 9.06 / 10 · GATE qualified 2022 and 2023
- Full Stack Developer Intern at Kidz Brain Academy, an education business (Feb 2023 to Aug 2024)
- English fluent, Hindi native, German A2/B1 (actively improving, uncertified)

<details>
<summary>Show as a timeline</summary>

```mermaid
timeline
    2019 to 2023 : B.Tech Computer Science, CGPA 9.06 / 10
                 : GATE qualified 2022 and 2023
    2023 to 2024 : Full Stack Developer Intern, Kidz Brain Academy, an education business
    2024 onward  : M.Sc. Global Software Development, Hochschule Fulda
    2025         : Team projects, einkaufzentrum and RAG_Adaptive
    2026         : ApplyTrack, cifar10, vectordb, shift-log, solar-inspect
```

</details>

## Contact

[Email](mailto:pariharudit03@gmail.com) · [LinkedIn](https://www.linkedin.com/in/uditparihar11/)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://uditp11.github.io/Uditp11/snake-dark.svg">
  <img src="https://uditp11.github.io/Uditp11/snake-light.svg" width="840" alt="A snake eating my GitHub contribution graph, redrawn every week">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img src="assets/footer-light.svg" width="840" alt="A small planet with a football orbiting it">
</picture>

<p align="center"><sub>Outside code: football and astrophysics.</sub></p>
