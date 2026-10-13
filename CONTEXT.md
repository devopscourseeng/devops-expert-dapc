# CONTEXT.md — Curso DAPC (DevOps Advanced Professional Certification)

Archivo de contexto compartido. Su objetivo es que cualquier persona (o cualquier sesión de Claude) que abra este repositorio entienda el curso, su estado y las reglas de trabajo sin depender del historial de un chat.

> Mantenimiento: actualiza este archivo mediante PR cuando cambie el estado del curso o una decisión. Si algo aquí contradice otro documento del repo, este archivo describe el **estado vigente** y debe corregirse.

## 1. El curso

| Dato | Valor |
|---|---|
| Curso | DevOps Advanced Professional Certification (DAPC) · "DevOps Expert" |
| Entidad certificadora | CertiProf (material base V072021A) |
| Modalidad | Virtual sincrónica (videollamada, salas de grupos, pizarra Excalidraw) |
| Carga | 16 sesiones de 4 h = 64 h, una sesión por semana, más 2–3 h semanales de trabajo autónomo |
| Participantes | 6, en dos equipos de 3 para las dinámicas |
| Examen de certificación | 40 preguntas de selección múltiple, 60 min, se aprueba con 80 % (32/40) |
| Nota del curso | 0–100; aprueba con 70 o más y 80 % de asistencia (13 de 16 sesiones) |

## 2. Estado actual

- **Sesiones 1–4:** ya preparadas por el instructor anterior (guiones, laboratorios y prácticas). Resumen en la sección 4.
- **Desde la sesión 5:** el curso lo toma un nuevo instructor (el propietario de este repo). Aquí se prepara todo lo que falta.
- **Plan global original (v1.0, oct 2026)** del instructor anterior: cubre las 16 sesiones. Es la referencia de partida, no necesariamente el plan final.
- **Nuevo plan global (v0.1, sesiones 5–16):** borrador solo con títulos y descripciones breves. Lo seguirá mejorando el instructor durante los próximos días. Hasta que se publique aquí, el plan v1.0 es la referencia.
- **Sesión 5:** será el *kickoff* del nuevo instructor: conocer a la audiencia, configurar herramientas de IA, Jira y GitHub, y empezar a recorrer el material DAPC.

## 3. Objetivos y enfoque del nuevo instructor

- Cubrir el contenido de CertiProf usando **IA como herramienta principal de los estudiantes** para aprender haciendo.
- Reducir el tiempo de exposición del instructor (no le gustan las clases magistrales) y aumentar el tiempo de práctica de los estudiantes.
- Trabajar con **GitLab o GitHub** (el que resulte más fácil para MCPs y herramientas DevOps) más **Jira**: los estudiantes reciben tickets, suben cambios y tienen CI/CD integrado.
- Que los estudiantes **creen skills**.
- Un proyecto completo como hilo del curso, alojado en este repo (ver sección 5).

## 4. Qué se vio en las sesiones 1–4

Resumen del plan v1.0. Las diapositivas son páginas del PDF del instructor CertiProf.

| Sesión | Tema | Diap. | Práctica principal |
|---|---|---|---|
| S1 | Origen de DevOps, conceptos base (CD, IaC, Kata, WIP, lead time, deuda técnica, bimodal), CALMS, organización | 1–47 | Lab 1 GitHub (repo, ramas, PR, conflicto, Actions, protección de `main`, tag) · Lab 2 Docker (imágenes, capas, Dockerfile, registro). Tarea T1 «Cafetería Yungas» |
| S2 | Team Topologies, equipos autogestionados, Ops en Dev, DevOps Topologies | 48–63 | Cafetería Yungas resuelta por tres métodos; consigna «Chocolatería Alto Beni»; dinámica Ruta Salar / Cooperativa Illimani. T2 opcional |
| S3 | Las Tres Formas y cimientos del pipeline | 64–98 | Dinámica Flowban; entorno completo con Compose en un comando (taller 98). T3 |
| S4 | **Evaluación 1** y pruebas automatizadas | 99–109 | Práctica de evaluación «Heladería Sajama»; pytest + cobertura + CI que bloquea `main`. T4 |

> Nota: el plan v1.0 indica que solo S1 y S2 estaban dictadas al momento de redactarse; el nuevo instructor retoma desde S5. Verifica con el instructor qué parte de S3–S4 se llegó a impartir antes de planificar repasos.

## 5. Proyecto hilo conductor: «Café Cumbre en línea»

Sistema que cada participante construye y opera durante el curso: una API en Flask más un sitio nginx, orquestados con Docker Compose. Sesión a sesión se le añaden capacidades (según el plan v1.0):

| Sesiones | Capacidad que se añade | Forma |
|---|---|---|
| S1–S2 | Repo con CI y publicación; imagen del sitio versionada (1.0 → 1.1) | Flujo |
| S3 | API de pedidos y Compose: entorno completo en un comando | Flujo |
| S4 | Pruebas unitarias y de API; job de pruebas que bloquea la integración | Flujo |
| S5 | Funcionalidad por TDD; pipeline de análisis, pruebas, build y publicación en GHCR | Flujo |
| S6 | Despliegue de autoservicio, azul-verde, canario y feature toggles | Flujo |
| S7 | Servicio de inventario extraído con patrón estrangulador; mapa de flujo de valor | Flujo |
| S8 | Métricas en Prometheus y paneles en Grafana | Feedback |
| S9 | Logs estructurados con id de correlación, radiador y alertas | Feedback |
| S10 | Canario vigilado con retorno automático; lista LRR | Feedback |
| S11 | Experimento A/B; plantilla de PR, CODEOWNERS y revisión cruzada | Feedback |
| S12 | Plantilla de postmortem sin culpa | Aprendizaje |
| S13 | Timeouts, reintentos y runbooks probados en un Game Day (Toxiproxy) | Aprendizaje |
| S14 | Workflow reutilizable y plantilla de repo compartidos | Aprendizaje |
| S15 | Controles de seguridad (gitleaks, pip-audit, Trivy), SBOM y registro automático del cambio | Seguridad y cambio |

Con el nuevo enfoque (IA + Jira + tickets), este reparto puede cambiar. El nuevo plan v0.1 lo redefine para S5–S16.

## 6. Temario oficial (6 unidades)

1. Introducción (diap. 18–63)
2. Principios: las Tres Formas (64–76)
3. La Primera Forma: flujo (77–159)
4. La Segunda Forma: feedback (160–216)
5. La Tercera Forma: aprendizaje (217–252)
6. Seguridad, cambio y cumplimiento (253–273)

Evaluaciones: E1 en S4, E2 en S8, E3 en S12, evaluación final con simulacro en S16. Peso: E1–E3 15 % c/u, final 25 %, tareas 20 %, participación 10 %.

## 7. Herramientas y stack

Git y GitHub (Actions, GHCR), Docker y Compose, Flask, pytest, ruff, nginx, Prometheus, Grafana, k6, Toxiproxy, gitleaks, pip-audit, Trivy (SBOM CycloneDX), Dependabot. Nuevo: Jira y asistentes de IA para los estudiantes. Pizarra: Excalidraw.

## 8. Convenciones de este repositorio

- Idioma de los materiales: **español**.
- Estructura prevista: `plan/` (planes globales), `session_N/` (guion, consignas, soluciones y `recursos/` por sesión), `cafe-cumbre-en-linea/` (proyecto hilo conductor), `recursos/` (material compartido).
- Los cambios entran **por pull request**, uno por tema, con una descripción breve de qué cambia y por qué.
- Los secretos que aparezcan en prácticas son siempre **falsos** (patrones de prueba); nunca credenciales reales.
- Los PDF originales de CertiProf (material del instructor y del estudiante, brochure, examen de muestra) **no se suben** a este repo público: son material con derechos de autor. Se citan por número de diapositiva.

## 9. Decisiones abiertas

- [ ] Elegir GitHub o GitLab como plataforma de los estudiantes y cómo integrar Jira.
- [ ] Publicar el nuevo plan global (v0.1) en `plan/` cuando esté listo.
- [ ] Decidir si «Café Cumbre en línea» vive en este repo (subcarpeta) o en un repo propio.
- [ ] Definir cómo se evaluará el uso de IA por los estudiantes (el plan v1.0 lo prohíbe en las evaluaciones prácticas y lo permite declarado en tareas; es una propuesta a revisar).
