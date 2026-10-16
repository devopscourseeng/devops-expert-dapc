# Las Tres Vías de DevOps: resumen en español con ejemplos sencillos

Referencia para el entrenador (Sesión 5). Resume las diapositivas 64 a 76 con ejemplos de una cafetería. Los ejemplos son nuestros, no vienen del material oficial.

## Contexto (diapositivas 64 a 68)

- La Parte 2 se apoya en dos libros: *The Phoenix Project* y *The DevOps Handbook*.
- Idea central: DevOps no es una tecnología, es un problema de negocio.
- DevOps se entiende mejor con tres principios: pensamiento sistémico, retroalimentación, y experimentación y aprendizaje continuo.
- La diapositiva 76 no es teoría: es la actividad de equipos "Dinámica Flowban". Las tres vías se explican en las diapositivas 69 a 75.

## Primera Vía: Flujo (diapositivas 69 a 71)

**Idea:** el trabajo debe fluir rápido y sin trabas, de izquierda a derecha (de Desarrollo a Operaciones y al cliente). Se mira el rendimiento de todo el sistema, no el de un solo departamento.

| # | Competencia | Qué significa | Ejemplo sencillo |
|---|---|---|---|
| 1 | Identificar las cadenas de valor | Ver todos los pasos de un pedido, de principio a fin | Un cliente pide un café: se toma el pedido, se prepara, se cobra y se entrega. Todo ese recorrido es la cadena de valor |
| 2 | Hacer visible nuestro trabajo | Que todos vean qué se está haciendo | Un tablero con los pedidos pendientes, en preparación y entregados |
| 3 | Limitar el trabajo en proceso (WIP) | No empezar demasiadas cosas a la vez | El barista prepara máximo 3 cafés a la vez. Con 10 a medias, ninguno sale bien ni rápido |
| 4 | Reducir el número de transferencias (handoffs) | Menos veces que el trabajo pasa de una persona a otra | Una sola persona toma el pedido y prepara el café. Con cuatro personas se pierde tiempo y se confunden los datos |
| 5 | Eliminar obstáculos y desperdicios | Quitar lo que no aporta valor | Si el barista camina 2 minutos a buscar la leche, se acerca la nevera a la máquina |
| 6 | Identificar y elevar las restricciones | Encontrar el paso más lento y mejorarlo | Si la máquina de café es lo más lento, se compra una segunda máquina |
| 7 | Reducir el tamaño de los lotes | Trabajar en partes pequeñas | Se prepara un pedido a la vez, no se espera a juntar 50 |

**En nuestro curso:** una rama corta por ticket y un pull request pequeño por cambio.

## Segunda Vía: Retroalimentación (diapositivas 72 y 73)

**Idea:** las respuestas deben volver rápido, de derecha a izquierda (de Operaciones y el cliente hacia Desarrollo). Así se corrige pronto, cuando el problema aún es pequeño y barato de arreglar.

| # | Competencia | Qué significa | Ejemplo sencillo |
|---|---|---|---|
| 1 | Ver los problemas a medida que ocurren | Enterarse del problema en el momento | Un sensor avisa que la nevera está caliente, antes de que la leche se eche a perder |
| 2 | Trabajar de manera segura con sistemas complejos | Hacer cambios de modo que un error no tumbe todo | Se prueba una receta nueva con 5 clientes, no con toda la cafetería |
| 3 | "Swarm" (enjambre): resolver problemas y construir conocimiento | Varias personas se juntan de inmediato a resolver un problema y aprenden de él | Se rompe la máquina en hora pico: baristas y encargado se juntan, la arreglan y anotan cómo evitar que se repita |
| 4 | Seguir presionando la calidad más cerca de la fuente | Detectar y corregir el error donde nace, no al final | El barista prueba el café antes de entregarlo, no espera la queja del cliente |
| 5 | Habilitar la optimización para los centros de trabajo downstream | Pensar en quien recibe tu trabajo después | La cocina deja los pedidos ordenados y con la mesa anotada, para que el mesero no pierda tiempo |

**Dos términos que suelen confundir**

- **Swarm:** es "hacer enjambre". Cuando aparece un problema, varias personas se juntan de inmediato, en vez de dejarlo a una sola persona o pasarlo a otro equipo. Se relaciona con la cuerda Andon: quien detecta el problema avisa, el trabajo nuevo se detiene y se junta la ayuda que haga falta.
- **Calidad más cerca de la fuente:** la fuente es quien escribe el código o toma la decisión. Se trata de detectar el error lo más cerca y lo más pronto posible (pruebas automáticas, revisión de código, programación en pares), porque un error corregido en el momento cuesta mucho menos que uno encontrado en producción.

**En nuestro curso:** los tests automáticos (CI) avisan en minutos si algo se rompió, y el compañero que revisa tu pull request también es retroalimentación.

## Tercera Vía: Experimentación y aprendizaje continuos (diapositivas 74 y 75)

**Idea:** crear una cultura donde se prueba, se falla sin miedo, se aprende y se practica una y otra vez. El conocimiento individual se convierte en conocimiento del equipo y de la organización.

| # | Competencia | Qué significa | Ejemplo sencillo |
|---|---|---|---|
| 1 | Habilitar el aprendizaje organizacional y una cultura segura | Que nadie tema equivocarse; los errores sirven para aprender, no para culpar | Si alguien derrama un café, se pregunta "¿cómo evitamos que pase otra vez?", no "¿quién fue?" |
| 2 | Institucionalizar la mejora del trabajo diario | Reservar tiempo fijo para mejorar | Cada viernes, 30 minutos para mejorar un proceso de la cafetería |
| 3 | Transformar descubrimientos locales en mejoras globales | Lo que aprende uno lo aprenden todos | Un barista descubre cómo hacer espuma más rápido y lo enseña a todo el equipo y a otras sucursales |
| 4 | Inyectar patrones de resiliencia en el trabajo diario | Practicar fallas a propósito para estar preparados | Se apaga la máquina 10 minutos a propósito, para ver si el equipo sabe qué hacer |
| 5 | Los líderes refuerzan la cultura de aprendizaje | Los jefes dan el ejemplo y apoyan | El encargado cuenta sus propios errores y premia a quien propone una mejora |

**En nuestro curso:** el comentario de cierre en el ticket (qué se hizo y qué se aprendió) y los problemas de setup que anotamos para convertirlos después en skills.

## Cómo se relacionan las tres vías

- **Primera Vía:** que el trabajo fluya rápido.
- **Segunda Vía:** que las respuestas vuelvan rápido.
- **Tercera Vía:** que el equipo aprenda y mejore de forma continua, lo que hace crecer a las otras dos.

La calidad en la fuente evita muchos problemas. Cuando uno se escapa y se detecta, el enjambre lo resuelve entre todos y deja un aprendizaje.
