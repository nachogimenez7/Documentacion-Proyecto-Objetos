# Documentación del proyecto TRAIDORES

Documentación del juego de deducción social **TRAIDORES**, para la materia **Desarrollo de Sistemas Orientado a Objetos**.

**Alumno:** Ignacio Giménez

**Fecha de incorporación de los documentos al repositorio:** 14 de octubre de 2026.

## Documentos

| Documento | Fecha de referencia | Descripción breve |
|---|---|---|
| [Análisis y diseño](documentacion/analisis-y-diseno.pdf) | 26/08/2026 | Documento principal: historias de usuario actualizadas, casos de uso y diagramas de clases. Describe el alcance del juego en su versión de agosto. |
| [Diagramas de secuencia](documentacion/diagramas-de-secuencia.pdf) | 16/09/2026 | Seis flujos centrales: crear sala, unirse, iniciar partida, realizar acciones, votar y recuperar la continuidad online. Borrador en revisión. |
| [Diagramas de estados](documentacion/diagramas-de-estados.pdf) | 23/09/2026 | Cambios de estado de la sala, la partida, la participación del jugador y la votación. Borrador en revisión. |
| [DER y mapeo ORM](documentacion/der-y-mapeo-orm.pdf) | 13/10/2026 | Propuesta resumida de entidades, relaciones y persistencia. Su planteo relacional deberá ajustarse a la adaptación con Firebase aceptada para el proyecto. |
| [Historias de usuario — primera entrega](documentacion/historico/historias-de-usuario-julio-2026.pdf) | Julio de 2026; entrega: 17/07/2026 | Antecedente histórico. Algunas funciones que aquí eran futuras aparecen implementadas en la versión de agosto. |

La fecha de análisis y diseño y la referencia de la primera entrega figuran en los documentos. Las fechas de secuencia, estados y DER corresponden a la creación registrada en los metadatos de cada PDF, no a una aprobación ni a una entrega formal.

## Alcance y próxima etapa

El juego actual está desarrollado para Android con Kotlin y Firebase. El documento de agosto es la referencia principal del alcance funcional; la entrega de julio se conserva como antecedente. La documentación seguirá ajustándose para mantener coherencia entre las reglas, los casos de uso y los diagramas.

Más adelante se realizará una **implementación académica exclusivamente en Python del funcionamiento de una partida**, con un alcance acotado. Su propósito será representar y explicar la **lógica del modelo de negocio**, mediante clases, atributos, métodos y relaciones: participantes, roles, acciones, votación y resolución de la partida. El código será desarrollado por el alumno como parte de su aprendizaje y para poder explicar sus decisiones de diseño.

También quedan para una etapa posterior el **manual de usuario** y el **manual técnico**.
