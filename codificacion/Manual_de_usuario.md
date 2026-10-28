# TRAIDORES - Manual de usuario

**Autor:** Ignacio Giménez  
**Materia:** Desarrollo de Sistemas Orientado a Objetos  
**Fecha de elaboración:** 28 de octubre de 2026  
**Estado:** guía basada en el diseño documentado de la beta móvil; pasos, nombres de botones y requisitos pendientes de comprobar en la aplicación.

## 1. ¿Qué es Traidores?

Traidores es un juego de deducción social para Android. Cada participante recibe un rol secreto, usa las habilidades que le correspondan, debate y vota para ayudar a cumplir el objetivo de su equipo. La documentación describe una beta con una modalidad local contra inteligencia artificial y otra online.

Este repositorio no contiene la aplicación instalable ni su código. Las funciones y recorridos siguientes proceden de los documentos del proyecto; no se pudieron verificar las pantallas ni la versión actual de la beta. La simulación en Python prevista en la guía es un trabajo académico separado y todavía no está programada en este repositorio.

## 2. Antes de comenzar

Necesitás un dispositivo Android compatible y acceso a una copia de la aplicación. Para jugar online se necesita conexión y otros participantes. La versión mínima de Android, el enlace de descarga y los pasos exactos de instalación deben completarse cuando se disponga de la aplicación.

La documentación distingue jugador invitado y registrado. El invitado puede jugar contra IA y unirse a salas existentes; para crear una sala online y conservar perfil, historial y estadísticas se describe una cuenta registrada. El registro se documenta mediante correo y contraseña o proveedores disponibles en la aplicación; verificar las opciones en la versión utilizada.

## 3. Comenzar una partida local

1. Abrí la aplicación y elegí la opción de jugar localmente contra IA.
2. Revisá y ajustá la configuración disponible antes de iniciar.
3. Iniciá la partida y consultá tu rol y objetivo. Conservá esa información en secreto.
4. Seguí las fases que muestre el juego: noche, debate y votación, hasta el resultado final.

Los nombres exactos de los controles y las opciones dependen de la versión de la aplicación.

## 4. Jugar online

**Crear una sala:** ingresá con una cuenta registrada, elegí crear una partida online y configurá la sala. Compartí su código con quienes quieras invitar. Como anfitrión, revisá a los participantes y la configuración e iniciá cuando se cumplan las condiciones que indique el juego.

**Unirse a una sala:** buscá una sala pública disponible o ingresá el código que te compartieron. Si la sala está llena, cerrada o no existe, el ingreso puede rechazarse. Una vez en el lobby, seguí las indicaciones para prepararte y esperar el inicio.

**Durante el lobby:** la documentación contempla preparación de jugadores, selección o votación de mapa, comunicación e interacciones. Las opciones concretas y sus controles deben verificarse en la beta.

## 5. Desarrollo de la partida

- **Rol:** consultá tu equipo, objetivo y habilidad. No todos los roles actúan en todas las fases.
- **Noche:** si tu rol tiene una acción disponible, elegí un objetivo permitido y confirmala siguiendo la pantalla. El sistema debería rechazar acciones duplicadas o inválidas.
- **Día:** participá del debate si estás habilitado. Luego elegí y confirmá tu voto; cada jugador habilitado registra un voto por votación.
- **Desempate:** seguí la indicación del juego si varios candidatos reciben la misma cantidad de votos. La guía de la simulación describe los casos con y sin Alcalde revelado.
- **Eliminación:** la documentación indica que un jugador eliminado puede observar sin intervenir en acciones restringidas.
- **Resultado:** al cumplirse una condición de victoria se muestra el resultado. En online la documentación contempla volver al lobby o preparar una revancha.

### Ejemplo de roles de la simulación académica

La guía plantea una partida de 12: cinco Aldeanas, Detective, Médico y Alcalde para el Pueblo; Asesino, Espía y Mercenario para los Traidores; y Bufón neutral. El Detective investiga, el Médico protege, el Alcalde puede revelarse y el Mercenario restringe a un jugador durante el día siguiente. El Bufón obtiene una victoria individual si es expulsado por votación, pero la partida continúa. Esta composición corresponde al ejemplo de la guía y no necesariamente a todas las configuraciones de la aplicación.

En ese ejemplo gana el Pueblo si no quedan Asesino ni Espía; los Traidores ganan si aún queda alguno y su cantidad de vivos iguala o supera a la del Pueblo. El Bufón no cuenta como integrante de esos bandos. Algunas reglas de detalle siguen pendientes de definición en la guía.

## 6. Perfil y convivencia

La documentación describe personalización de perfil, consulta de historial y estadísticas para cuentas registradas, así como opciones para silenciar o bloquear jugadores y mecanismos de expulsión en sala. Usá las opciones disponibles en la aplicación y seguí sus mensajes de confirmación. Las pantallas y condiciones concretas todavía deben verificarse.

## 7. Problemas frecuentes

- **No puedo entrar a una sala:** comprobá la conexión, el código y que la sala siga abierta y tenga lugar. Pedí al anfitrión que revise su estado.
- **No puedo iniciar una sala:** la documentación reserva la creación al jugador registrado; comprobá también que se cumplan los requisitos de jugadores y configuración que informe el juego.
- **No puedo actuar o votar:** revisá la fase, si seguís en juego y si tu rol o una restricción te habilita. En el ejemplo, el jugador afectado por el Mercenario no vota ese día.
- **Perdí la conexión:** recuperá la conexión y buscá la opción de reingreso. La documentación prevé recuperar el estado si la sala sigue disponible, pero no garantiza que siempre sea posible.
- **No aparece el historial:** comprobá que usás una cuenta registrada; la documentación contempla un estado vacío cuando no hay partidas registradas.
