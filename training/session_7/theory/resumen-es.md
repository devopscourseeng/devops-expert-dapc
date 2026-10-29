# Session 7: resumen en español con ejemplos sencillos

Referencia para el entrenador (Sesión 7). Resume las diapositivas 129 a 153 del material oficial, con ejemplos de la Summit Cafe API. Los ejemplos son nuestros, no vienen del material oficial. Los números de página son los del PDF oficial V072021A.

## Lanzamientos de alto riesgo y despliegue de autoservicio (diapositivas 129 a 134, 138 a 141)

**Idea:** lo que importa son los resultados. Un despliegue debe ser un evento de "presionar un botón", de bajo riesgo, que se puede ejecutar cuando se necesite. Un despliegue manual, poco frecuente y distinto en cada servidor es peligroso.

**Caso:** Knight Capital (2012). Había ocho servidores y el código nuevo se copió a mano. Un servidor quedó sin actualizar y el código viejo reaccionó mal a las órdenes nuevas. La empresa perdió unos 440 millones de dólares en unos 45 minutos y nadie pudo volver atrás rápido. Este caso es nuestro ejemplo; no está en las páginas oficiales con esas cifras.

**El pipeline de despliegue** (diapositivas 131 y 138): desplegar de la misma manera en todos los entornos, hacer una prueba de humo después de cada despliegue, mantener entornos consistentes, y registrar qué comandos se ejecutaron, en qué máquinas, cuándo, quién autorizó y cuál fue la salida.

**Autoservicio** (diapositivas 133 y 134): construir, probar y desplegar sin pasos manuales ni traspasos. El desarrollador despliega y corrige sin abrir un ticket a Operaciones.

**Entrega continua y despliegue continuo** (diapositivas 130 y 139): en la entrega continua cada cambio está listo y una persona presiona el botón. En el despliegue continuo nadie presiona el botón. La integración continua va primero.

**Despliegue no es liberación** (diapositivas 140 y 141): desplegar es instalar una versión en un entorno. Liberar es ofrecer una funcionalidad a todos los clientes o a una parte de ellos.

**Ejemplo:** el martes desplegamos la versión 1.2, pero los pedidos programados siguen ocultos. El jueves los activamos. El despliegue fue el martes; la liberación fue el jueves.

**Ejemplo con los scripts:** `./deploy/deploy-to-environment.sh prod 1.2` pone la versión 1.2 en el contenedor canario con 0 % de las llamadas. La liberación llega después, con `./deploy/set-weight.sh 10`.

## Patrones basados en el entorno (diapositivas 142 a 150)

**Idea:** hay dos o más entornos, pero solo uno recibe tráfico de clientes. El código nuevo se despliega en un entorno sin clientes y la liberación se hace moviendo el tráfico (diapositivas 142 y 143). Se evitan los despliegues de madrugada o de fin de semana (diapositiva 145).

**Azul-verde** (diapositiva 146): dos entornos de producción, azul y verde. Solo uno sirve a los clientes. Se despliega en el que está libre, se prueba y se cambia el enrutador. Para volver atrás, se cambia de nuevo.

**Cambios de base de datos** (diapositiva 147): dos versiones de la aplicación con una base de datos común pueden romperse entre sí. Dos caminos: dos bases de datos, o separar los cambios de base de datos de los cambios de la aplicación. El segundo se llama expandir y contraer: primero se agregan objetos nuevos, y más tarde se quitan los viejos.

**Ejemplo:** para cambiar el nombre de la columna `name` a `title`, primero se agrega `title` y se escriben las dos. Cuando ninguna versión usa `name`, se quita.

**Canario** (diapositivas 148 y 149): se libera a un grupo pequeño, se observa el resultado y solo después se pasa a un grupo mayor. Si algo parece mal, se vuelve atrás. El nombre viene de los canarios que llevaban los mineros. Facebook usó grupos así: un conjunto pequeño de usuarios, sus empleados y después la mayoría de los usuarios.

**Ejemplo:** `./deploy/set-weight.sh 10`, luego `50`, luego `100`. Con `curl http://localhost:8200/version` se ve qué versión respondió. Para volver atrás: `./deploy/set-weight.sh 0`.

**Sistema inmune del clúster** (diapositiva 150): amplía el canario conectando el monitoreo de producción con el proceso de liberación y automatizando la reversión. Dos beneficios: protege contra defectos difíciles de encontrar y reduce el tiempo para detectar y responder a un mal desempeño.

**Ejemplo:** un skill lee el runbook, mira los errores y propone la reversión. En la práctica, una persona dice sí.

## Patrones basados en la aplicación (diapositivas 151 a 153)

**Idea:** se modifica la aplicación para exponer funcionalidades de forma selectiva con pequeños cambios de configuración. Da más flexibilidad, pero exige más disciplina y participación de Desarrollo (diapositiva 151).

**Feature toggles** (diapositiva 152): un mecanismo para activar o desactivar una funcionalidad sin desplegar código de producción. Permite volver atrás fácilmente, degradar el servicio de forma controlada y ser más resistente.

**Lanzamiento oculto, o dark launch** (diapositiva 153): la funcionalidad completa está en producción pero los clientes no pueden verla. Se puede probar con carga real. En cambios grandes o riesgosos se hace durante semanas antes de la liberación.

**Ejemplo:** la versión 1.2 trae `SCHEDULED_ORDERS=off`. Con `off`, el campo `pickup_time` se ignora y la API se comporta como la 1.1. Con `on`, un pedido guarda la hora de recogida, por ejemplo `14:30`. El mismo contenedor se reinicia con `-e SCHEDULED_ORDERS=on`; la imagen no cambia.

**Consejo nuestro (no oficial):** quitar los toggles viejos cuando la funcionalidad ya está liberada para todos.

## Pregunta para cerrar

¿Qué patrón elegirían para cada riesgo: una versión rota, un error que afecta a todos a la vez, una funcionalidad dudosa dentro de una versión buena?

| Riesgo | Patrón | Cómo se vuelve atrás |
|---|---|---|
| Una versión nueva rota | Azul-verde | Volver al entorno anterior |
| Dañar a todos los usuarios a la vez | Canario | Enviar 0 % a la versión nueva |
| Una funcionalidad mala dentro de una versión buena | Feature toggle | Apagar el interruptor |
| Sorpresas con carga real | Lanzamiento oculto | Detener el trabajo oculto |
