---
name: dapc-examen-test
description: Genera un examen tipo test del banco DAPC por sesiones y número de preguntas, lo presenta pregunta a pregunta y, al terminar, crea el reporte y un merge request en la carpeta students.
---

# Examen tipo test DAPC

Usa esta skill cuando una persona quiera hacer un examen de práctica del banco de preguntas DAPC. Puede llamarla cualquier participante, así que lo primero es saber quién es.

## 1. Identificar a la persona

Antes de nada, pregunta:
- Nombre completo.
- Usuario de GitHub (login). Si no lo conoces, pide el nombre y genera un identificador en minúsculas con guiones (por ejemplo, `ana-perez`).

El identificador se usa para la carpeta `students/<identificador>/`. Nunca mezcles resultados de dos personas. Si la persona no quiere dar su nombre, usa `anonimo-<fecha>` y dilo en el reporte.

## 2. Parámetros del examen

- **Sesiones (obligatorio).** Pregunta siempre qué sesiones debe cubrir el examen, del 1 al 16, por ejemplo `1-4` o `8, 9, 10, 11`. No asumas un valor. Si la persona pide la simulación completa, usa las sesiones 1 a 16.
- **Número de preguntas.** Por defecto, 40. Úsalo si la persona no indica otro.

Comprueba que hay preguntas suficientes para las sesiones elegidas. Si no las hay, dilo y propone el número máximo posible.

## 3. Cargar el banco

El banco está en el repositorio, en la misma carpeta que esta skill: `training/skills/dapc-examen-test/dapc-es-bank.json`. Léelo desde esa ruta. No pidas el banco a la persona.

El archivo tiene un campo `questions` con la lista de preguntas. Cada pregunta tiene: `id`, `sesiones` (lista), `difficulty`, `type` (`single` o `multiple`), `question`, `options`, `answer` (lista de letras), `explanation`.

Antes de seguir, confirma que el archivo existe y que tiene ese formato. Si falta algún campo o el archivo no existe, avisa y no generes el examen.

## 4. Seleccionar las preguntas

- Filtra por las sesiones elegidas: una pregunta entra si alguna de sus sesiones está en la lista.
- No repitas preguntas.
- Reparto de dificultad aproximado: 25 % fácil, 50 % medio, 25 % difícil. Si una dificultad no alcanza, completa con las otras.
- Mantén el orden de las opciones; la letra de la respuesta correcta depende de él.

## 5. Presentar el examen en la interfaz

Crea una página HTML (artefacto) con estas reglas, sin excepción:
- Una pregunta por pantalla, con el número de pregunta y el total.
- Arriba de cada pregunta de **una respuesta** se muestra la indicación «Una respuesta». En las preguntas de **varias respuestas** no se muestra ninguna indicación en la parte superior. No se muestran la sesión ni la dificultad.
- En preguntas de una respuesta, las opciones son de selección única. En preguntas de varias respuestas, se pueden marcar varias opciones.
- El botón **Siguiente** está deshabilitado hasta que haya al menos una opción seleccionada. No hay forma de saltar una pregunta.
- No se puede volver a una pregunta anterior.
- En la última pregunta el botón dice **Ver resultado**.
- Durante el examen no se muestran la explicación, la fuente ni la respuesta correcta.
- Idioma: español.

## 6. Reporte al terminar

Al pulsar **Ver resultado** en la última pregunta, la página muestra:
- Puntuación en porcentaje y número de correctas.
- Aprobado si la puntuación es 80 % o más, no aprobado en otro caso.
- Una fila por pregunta: si acertó, respuesta marcada, respuesta correcta, sesión y explicación.
- Un bloque JSON con el reporte completo y un botón para copiarlo.

Una pregunta de varias respuestas solo cuenta como correcta si están marcadas exactamente las letras correctas.

La página no puede crear el merge request por sí sola. Pide a la persona que copie el reporte y lo envíe en el chat.

## 7. Crear el merge request

Cuando recibas el reporte en el chat:
1. Confirma con la persona su identificador.
2. Crea la rama `feature/examen-<identificador>-<AAAAMMDD>` desde `develop`.
3. Crea `students/<identificador>/examen-<AAAAMMDD>/report.json` con el reporte recibido y `students/<identificador>/examen-<AAAAMMDD>/report.md` con un resumen legible: nombre, fecha, sesiones, puntuación, aprobado o no, y la tabla de preguntas.
4. Haz commit con el mensaje `test(students): examen DAPC de <identificador>`.
5. Sube la rama y abre un pull request hacia `develop` con título `Examen DAPC: <nombre>`. Si `gh pr create` devuelve 403, usa `gh api repos/devopscourseeng/devops-expert-dapc/pulls -X POST`.
6. No hagas merge del pull request. Devuelve a la persona el enlace del pull request.

Al final de los mensajes de commit y del cuerpo del pull request, incluye las líneas de atribución indicadas por el entorno.

## Reglas

- No inventes preguntas ni cambies respuestas del banco.
- Si el banco y el reporte no coinciden en IDs, avisa antes de crear el merge request.
- El banco incluye las respuestas y explicaciones, y está en el repositorio. Por eso este examen es de práctica: no es válido para evaluar a alguien que ya conoce el banco.
- Un examen real no debe incluir las respuestas en el código de la página. Para uso real, la corrección se hace en Claude a partir de las respuestas enviadas, y la página solo muestra las preguntas.
