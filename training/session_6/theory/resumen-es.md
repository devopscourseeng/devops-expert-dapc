# Session 6: resumen en español con ejemplos sencillos

Referencia para el entrenador (Sesión 6). Resume las diapositivas 99 a 127 del material oficial, con ejemplos de la Summit Cafe API. Los ejemplos son nuestros, no vienen del material oficial. Los números de página son los del PDF oficial V072021A.

## Pruebas automatizadas rápidas y fiables (diapositivas 99 y 100)

**Idea:** los desarrolladores deben recibir información sobre la calidad de su trabajo en minutos. Encontrar los errores lo antes posible, ejecutar las pruebas rápido (en paralelo si hace falta) y escribir las pruebas antes que el código.

**Ejemplo:** cada cambio en `src/summit-cafe-api/` ejecuta `ruff` y `pytest` en CI. Si una prueba falla, el cambio no entra.

**Pulsar la cuerda andon** (diapositivas 100 y 113): en una fábrica, cualquiera tira de la cuerda cuando una máquina se detiene, y la línea no sigue hasta que el problema esté resuelto. En software, cuando un cambio rompe la compilación o las pruebas, no entra trabajo nuevo hasta corregirlo. Si alguien necesita ayuda, se trae la ayuda que haga falta.

**Ejemplo:** un PR rompe `pytest`. Nadie abre otro PR hasta que la prueba esté arreglada.

**Pruebas lentas o inestables** (diapositiva 7 de la presentación; diapositivas 99 y 110 del material oficial): una prueba que a veces falla sin razón hace que el equipo deje de confiar en la suite. Las pruebas lentas, a su vez, acaban sin ejecutarse. Por eso las pruebas deben ser rápidas y confiables.
- Ejemplo de prueba inestable: una prueba que llama a un servicio externo y a veces tarda demasiado. Se arregla usando datos fijos en la prueba, o se quita si no aporta nada.
- Ejemplo de prueba lenta: una prueba que espera 5 segundos sin motivo. Se cambia por una espera corta o se reemplaza por una prueba unitaria.
- Pregunta para el grupo: ¿qué prueba inestable han visto alguna vez, y qué hicieron con ella?

## Tipos de pruebas y pirámide (diapositivas 102, 105, 106, 107 y 110)

**Idea:** hay pruebas unitarias (la unidad más pequeña), de integración (las piezas funcionando juntas) y de aceptación. Lo ideal es una pirámide: muchas pruebas unitarias abajo, pocas pruebas manuales o de interfaz arriba. El "cono de helado" (muchas pruebas manuales) es un antipatrón.

**Ejemplo:**
- Unitaria: el total de un pedido es 2 × 3,50 + 1 × 2,80 = 9,80. Sin servidor ni HTTP.
- De API: `POST /orders` devuelve 201 y el total correcto.
- Manual: una persona revisa el menú en el navegador. Pocas, y solo cuando hacen falta.

**Regla importante** (diapositiva 106): si una prueba de aceptación o de integración encuentra un error, hay que crear una prueba unitaria que lo encuentre antes, más rápido y más barato.

**Acoplamiento** (diapositiva 107): si cambiar un módulo rompe otros, o si las pruebas unitarias son difíciles de escribir, el diseño está demasiado acoplado. Hay que separar los módulos para poder probarlos por separado.

**Pocas pruebas confiables** (diapositiva 110): es mejor tener pocas pruebas automatizadas y confiables que muchas que fallan sin razón. Se empieza con pocas y se agregan con el tiempo.

## TDD: desarrollo orientado por pruebas (diapositiva 108)

**Idea:** primero se escribe una prueba automatizada que describe el comportamiento esperado. Luego se escribe el código que la pasa. Por último, se limpia el código sin cambiar lo que hace.

**Los tres pasos** (Kent Beck, *Extreme Programming*, 1990): el material oficial los numera 2, 3 y 4. La numeración habitual es 1, 2 y 3:
1. Hacer que la prueba falle (rojo).
2. Escribir el código mínimo para que pase (verde).
3. Refactorizar el código nuevo y el antiguo, manteniendo las pruebas en verde.

**Ejemplo:** `DELETE /orders/{id}` devuelve 204 para un pedido existente. Primero se escribe la prueba (falla), luego la ruta mínima (pasa), luego se ordena el código (sigue pasando).

**ATDD:** lo mismo, pero partiendo de pruebas de aceptación, es decir, del comportamiento que pide el cliente.

## Integración continua y trunk (diapositivas 115 a 123)

**Idea:** integrar seguido. Las ramas que viven mucho tiempo hacen que la fusión sea cada vez más difícil y costosa (diapositiva 116).

**El modelo oficial** (diapositivas 121 a 123): los desarrolladores registran su código en el *trunk* (tronco) al menos una vez al día. Un cambio llega al tronco solo si todas las pruebas automatizadas pasan ("confirmaciones bloqueadas", diapositiva 122).

**Nuestro curso:** usamos el mismo objetivo con otro tronco, `develop`. Cada ticket tiene una rama corta desde `develop`, que vuelve con un pull request, CI en verde y la revisión de un compañero. Es decir, no es el modelo oficial de tronco, porque tenemos la rama `develop` y no confirmamos en ella directamente. Hay que decirlo así cuando se explique.

**Definición de "listo"** (diapositiva 123): al final de cada intervalo, el código está integrado, probado, funcionando, potencialmente utilizable, construido desde el tronco con un solo clic y validado con pruebas automatizadas.

**Ejemplo de la fusión difícil:** una rama de "pedidos" que vive dos semanas choca con tres cambios al fusionarse. Con nuestro flujo, una rama de un día entra por PR cuando `Checks` está en verde.

**Caso del material** (diapositivas 118 a 120): un equipo de firmware con 400 desarrolladores solo sacaba dos versiones al año, y el 5 % del tiempo se iba en funciones nuevas. Lo que los sacó de ahí fue la integración continua, el trabajo basado en tronco y la inversión en automatizar pruebas.

## Shift left (diapositivas 103 y 124)

**Idea:** la atención a la calidad debe moverse hacia la izquierda, hacia la planificación, el diseño y el desarrollo, en vez de concentrarse solo en las pruebas y la publicación (diapositiva 124).

**Ejemplo:** revisar en el PR, antes de integrar, un cambio que pueda romper el pedido. Así el problema aparece al principio y cuesta poco.

## Automatizar el despliegue (diapositivas 125 a 127)

**Idea:** documentar las etapas del despliegue, simplificar y automatizar los pasos manuales, reducir los tiempos de entrega y el número de traspasos entre personas. Este es el punto de partida de la sesión 7.

## Cómo se relacionan los conceptos

- Las pruebas rápidas y confiables hacen posible el TDD.
- El TDD y la integración frecuente hacen que la cuerda andon se use pocas veces y temprano.
- El desplazamiento a la izquierda (*shift left*) es el resultado de todo lo anterior: el error se encuentra cuando todavía es barato de corregir.
