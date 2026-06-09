---
type: reference
date: 2026-05-16
tags: [agente, geoffrey, brief, rutina]
---

# Brief mañanero — Geoffrey

Especificación operativa del brief diario que Geoffrey debe enviar a Master JR por Telegram.

El brief es un **seguimiento operativo**: cosas que a JR se le podrían haber olvidado, comunicaciones que necesitan seguimiento y recordatorios que requieren acción. No es resumen ejecutivo, newsletter ni “qué pasó hoy”. El DCA/radar legal está fuera del scope del brief; lo manejará el agente legal.

## Entrega

- **Canal:** Telegram directo.
- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Formato:** mensajes separados por sección, no un bloque único.
- **Extensión:** útil pero comprimida. Preferir 4–6 mensajes cortos.
- **Trato:** siempre de **usted**.
- **Idioma:** español, con términos técnicos en inglés cuando sean naturales.
- **Tono:** concreto, específico, filtrado, personalizado; no sonar a plantilla.

## Principio editorial

Entrar en materia. No abrir con:

- “resumen del día”;
- “cómo viene el día”;
- “estado general”;
- “Mapa de atención”;
- Top 3.

JR quiere un brief filtrado: solo lo relevante, sin adornos, sin explicar el trabajo interno de Geoffrey y sin secciones vacías. Si no hay algo relevante que comunicar en una fuente o apartado, omitir ese apartado completo.

Título del brief:

- Únicamente día, fecha y hora.
- Sin adornos, subtítulos, frases de bienvenida ni “brief mañanero”.
- Ejemplo: `Sábado 16 de mayo de 2026 — 7:15 AM`.

No incluir notas de proceso como “revisé X”, “no encontré Y”, “limitación técnica” o “fuente OK” salvo que una fuente crítica falle y afecte directamente la confiabilidad del brief.

Control obligatorio antes de enviar:

- Redactar primero un borrador interno.
- Validarlo con `/Users/jr/.openclaw/workspace-geoffrey/scripts/validate_morning_brief.py` si el script está disponible.
- Si falla la validación, reescribir el borrador y volver a validar antes de enviar.
- No enviar un brief que contenga: título adornado, “Qué necesita pasar”, secciones vacías, “no veo eventos”, “Fuente:”, “Radar/Radas de cliente”, cualquier mención al DCA o frases de relevancia tipo “Relevante para radar fiscal”.

JR no quiere un resumen ejecutivo general ni fanfarronería metodológica. Quiere materia útil y accionable cuando aplique. Solo incluir contexto mínimo.

Regla central:

> Relevancia real → contexto breve → sugerencia/acción solo en el apartado de sugerencias.

Ejemplo prohibido:

> “Hubo movimiento en Propi con Sur Desarrollos.”

Ejemplo esperado:

> **Propi — Sur Desarrollos:** Thelma mandó observaciones al contrato. [Link al correo](url)

## Qué debe cubrir

1. Qué tiene hoy en calendario solo si hay eventos del día, conflictos de hoy, preparación de hoy o ventanas relevantes de hoy. No incluir “próximos eventos” en calendario.
2. Qué comunicaciones relevantes conviene conocer, resumidas sin listar ruido.
3. Qué recordatorios vencidos/de hoy/próximos requieren atención real.
4. Qué sugiere o puede ejecutar Geoffrey con aprobación.

## Estructura vigente

La versión compacta preferida por JR se parece a este patrón: título seco; calendario solo si aporta algo; comunicaciones específicas por asunto con links embebidos; recordatorios/tareas relevantes; sugerencias/acciones aprobables. No incluir noticias por ahora. No incluir `Frentes abiertos`, `Pendientes acumulados`, `Radar de cliente` ni `Puede ignorar hoy` como secciones fijas salvo que JR lo vuelva a pedir explícitamente. El DCA/radar legal NO va en el brief; está delegado al agente legal.

### 1. 📅 Lo que le depara el día

Sección opcional. Incluir solo si hay eventos, conflictos, preparación necesaria, ventanas útiles o recordatorios que afecten el día. Si el calendario está vacío y no hay nada relevante, omitirla por completo.

Regla dura de calendario: **solo eventos del día actual**. No adelantar “mañana”, “próximos días”, “próxima semana” ni eventos futuros en la sección de calendario. Los vencimientos próximos solo pueden aparecer en Reminders si son deadlines críticos; los eventos futuros se omiten salvo que JR pregunte por agenda próxima.

Incluir:

- Día y fecha.
- Eventos de hoy del calendario con hora, duración, ubicación/link si existe.
- Recordatorios vencidos/de hoy que afecten el día.
- Ventanas reales de trabajo de hoy: mañana/tarde/noche.
- Conflictos, traslapes, falta de buffer o preparación necesaria de hoy.
- Qué conviene priorizar hoy, solo si realmente ayuda.

Ejemplo:

Evitar bloques como “no veo eventos” + “fuente OK”; si no hay señal, no se menciona.

### 2. 📬 Comunicaciones que requieren seguimiento

Esta sección es el corazón del brief.

No listar correos. Comunicar únicamente lo relevante y resumir brevemente la comunicación. No decir aquí “qué necesita pasar”; si hay sugerencia o acción propuesta, moverla al apartado de sugerencias.

Fuentes: correos, WhatsApp/chats cuando estén disponibles, SMS relevantes, Apple Mail/Gmail autorizado y cualquier comunicación local autorizada.

Para cada comunicación relevante:

- **Proyecto/asunto.**
- **Quién escribió o intervino.**
- **Contexto mínimo:** resumen breve de la comunicación, sin transcribir de más.
- **Link embebido:** si hay correo específico, incluir enlace corto tipo `[Link al correo](url)` o embebido en el título, por ejemplo `**[Finanzas de talleres](url):** ...`.
- **Limitación:** solo si impide entender el contenido; no mencionar limitaciones menores por rutina.

Control de calidad obligatorio para correo:

- **Deduplicación obligatoria — ejecutar primero:** correr `python3 /Users/jr/.openclaw/workspace-geoffrey/scripts/brief_email_dedup.py recent` para obtener el listado de thread IDs y subjects ya reportados en los últimos 7 días. Un correo cuyo thread ID o subject ya aparezca en ese listado NO se incluye en Comunicaciones a menos que tenga novedad material posterior (nueva respuesta, vencimiento inminente de hoy, o JR lo pidió expresamente). Si se incluye por novedad, presentarlo como "Seguimiento —" no como correo nuevo.
- **Registrar al final:** una vez redactado el brief (antes de enviarlo), correr `python3 /Users/jr/.openclaw/workspace-geoffrey/scripts/brief_email_dedup.py log YYYY-MM-DD <thread_id1> <thread_id2> --subjects "Subj A" "Subj B"` con la fecha de hoy, los thread IDs de Gmail incluidos y los subject-keys usados en Comunicaciones. Esto actualiza el log para mañana.
- No depender solo de Gmail API ni solo de `is:unread`; revisar también Apple Mail local cuando esté disponible.
- Revisar correos recientes leídos y no leídos, especialmente de los últimos 3–7 días, porque JR puede haber abierto un correo y aún requerir seguimiento.
- Usar `/Users/jr/.openclaw/workspace-geoffrey/scripts/scan_apple_mail_recent.py` para Apple Mail local si existe; cubre cuentas/carpetas locales como `kidsunderstanding.com`, iCloud y `[Gmail]/Todos` sin modificar correos.
- Tratar como alta señal cualquier correo con vencimiento, formulario, pago, impuestos, ISR/IVA/ISO, retenciones, factura, contrato, firma o adjuntos operativos, aunque esté leído.
- Para Understanding Kids / Inversiones Multidisciplinarias, correos de contabilidad como Elder Estrada / `mueblescontinental.com` son relevantes por defecto si contienen formularios, vencimientos o pagos.
- Si hay link estable, usarlo embebido. Para Gmail web usar `https://mail.google.com/mail/u/0/#...`; para Apple Mail local puede usarse `message://...` generado desde Message-ID. Si no hay link seguro, incluir asunto/remitente y no inventar URL.

Ruido se omite; no crear sección de “ignorar”.

Formato esperado:

> **[Propi — Contrato firma JM](url):** Astrid y Thelma movieron el hilo esta mañana; el asunto parece centrado en firma/versión final.

### 3. ✅ Recordatorios / tareas

Dar peso alto a Apple Reminders.

Mostrar recordatorios vencidos, de hoy y próximos relevantes, reorganizados por qué necesita pasar:

- **Hacer hoy.**
- **Reprogramar.**
- **Convertir en mensaje/correo.**
- **Agregar a calendario.**
- **Archivar/completar si ya no aplica.**

No listar todo si hay demasiados; agrupar y proponer limpieza.

### 4. ✅ Sugerencias / acciones que Geoffrey puede ejecutar

Cierre obligatorio solo si hay sugerencias útiles o acciones aprobables. Deben salir de comunicaciones, calendario o recordatorios, no de consejos genéricos. No incluir sugerencias sobre el Diario de Centro América salvo solicitud expresa de JR. Si no hay nada útil que sugerir, omitir la sección completa.

Máximo 5–7 acciones.

Alcance permitido por defecto para sugerencias del brief:

- Agregar evento al calendario.
- Crear/modificar recordatorio.
- Preparar borrador de respuesta para correo, WhatsApp, SMS o chat.

No sugerir por defecto checklists, presentaciones, documentos, matrices, notas legales, revisiones amplias o tareas de análisis. JR las pedirá directamente cuando las necesite.

Regla proactiva calendario/reminders:

- Si una comunicación menciona reunión, llamada, cita, vencimiento, pago, formulario, audiencia, entrega o fecha concreta, Geoffrey debe verificar si ya existe en Calendar o Reminders.
- Si ya existe, no sugerir duplicado.
- Si no existe y Geoffrey no tiene aprobación explícita para crearlo automáticamente, debe proponerlo al final como acción concreta: “Agrego X al calendario” o “Creo reminder para X”.

Regla anti-repetición:

- Antes de repetir una comunicación o sugerencia, revisar briefs/conversación reciente disponible y el estado actual de calendario/reminders.
- Revisar explícitamente al menos los últimos 2 briefs entregados cuando el historial esté disponible; si un correo ya fue mencionado, no volverlo a poner en Comunicaciones salvo que tenga novedad material posterior, vencimiento real de hoy/urgente, o JR haya pedido seguimiento.
- No repetir avisos ya dados, como “enviar factura a Astrid”, salvo que haya novedad material, vencimiento real o JR no haya podido actuar y sea urgente.
- Si algo sigue pendiente pero ya fue avisado, preferir convertirlo en sugerencia de recordatorio/calendario o respuesta, no volver a contarlo como si fuera nuevo.
- Si se repite algo por urgencia, decirlo como seguimiento pendiente y mencionar la novedad concreta; no presentarlo como correo nuevo.

Formato:

> 1. Le preparo matriz del hilo Propi: asunto / última intervención / qué falta / respuesta sugerida.  
> 2. Creo reminder para pagar luz/mantenimiento hoy 5:00 PM.  
> 3. Le redacto respuesta para Thelma preguntando por versión final y firma.  
> 4. Agrego bloque de tesis de 90 min al calendario.
> 5. Sugiero añadir “pagar mantenimiento” a Reminders en Personal > Recurrentes.

Cierre:

> ¿Aprueba alguna? Puede responder con números o decirme qué ajusto.

## Exclusiones

No incluir por ahora:

- Finanzas personales.
- Portafolio personal.
- Noticias por el momento.
- Correos tipo newsletter.
- DCA / Diario de Centro América / radar legal — delegado al agente legal. No incluir nunca en el brief.
- Proyectos sin seguimiento concreto pendiente.
- Sección “Radar de cliente” / “Radas de Cliente”.

## Lecciones de control de calidad

- 2026-06-09: JR reportó que el brief sigue enviando correos ya enviados en ocasiones anteriores. Se implementó log de deduplicación persistente (`outputs/brief-email-log.json`) y script helper (`scripts/brief_email_dedup.py`). Ahora el cron debe consultar el log antes de incluir cualquier correo en Comunicaciones y actualizarlo al terminar. Ver instrucciones en “Control de calidad obligatorio para correo”.
- 2026-06-04: JR corrigió dos fallas del brief: se repitieron correos ya mencionados el día anterior y se listaron “próximos” eventos. Regla vigente: Comunicaciones debe deduplicar contra los últimos briefs disponibles y solo repetir con novedad/urgencia explícita; Calendario debe mostrar únicamente eventos del día actual, no próximos eventos.
- 2026-06-02: JR corrigió que el brief debe ser más proactivo y menos ruidoso. Si una reunión/vencimiento detectado en comunicaciones no está en Calendar ni Reminders, sugerir agregarla al final; no repetir avisos ya dados sin novedad; limitar sugerencias a calendario, recordatorios o preparar contestaciones. No sugerir checklists, presentaciones, documentos, matrices ni trabajo amplio salvo pedido directo. También corrigió DCA: si no hay señal útil, omitir el apartado completo; no decir “sin publicaciones fuertes” ni listar lo irrelevante.
- 2026-05-17: el brief omitió un correo importante de Elder Estrada del 14/05/2026 sobre ISR rentas del trabajo abril 2026, con formulario y vencimiento 15/05/2026, porque el flujo revisó Gmail API/Apple Mail de forma insuficiente y no trató correos leídos con vencimientos fiscales como señal fuerte. Regla: los correos fiscales/contables con vencimiento deben entrar en Comunicaciones o Sugerencias aunque ya estén leídos.
- Secciones fijas de “Frentes abiertos”.
- Secciones fijas de “Pendientes acumulados”.
- Sección “Puede ignorar hoy”; lo ignorado se omite sin anunciarlo.
- Bullets de DCA que digan solo “acuerdo publicado” sin materia concreta.
- “Acciones sugeridas” demasiado obvias.
- Briefs que suenan a plantilla.

## Reglas de compresión

- No incluir noticias/radar externo por ahora.
- Comunicaciones: contexto mínimo, resumen breve y link embebido cuando exista correo específico; cualquier propuesta pasa a sugerencias.
- Acciones: máximo 5–8 cuando haya suficientes seguimientos reales; si hay demasiadas, agrupar.

## Fuentes autorizadas / previstas

- Calendario del día, solo si aporta eventos/ventanas/conflictos relevantes de hoy; no incluir próximos eventos.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail/Apple Mail autorizado según [[agentes/geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- WhatsApp/chats cuando la integración esté disponible/autorizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda, conversación diaria y notas relevantes.

## Reglas duras de especificidad

1. Prohibido usar frases vagas como “hubo movimiento”, “hay temas”, “revisar pendientes” sin detalle.
2. Prohibido llenar espacio con disclaimers de búsqueda. Si no hay señal relevante, omitir el apartado o usar una línea seca solo cuando el apartado sea estructural, como DCA.
3. Si hay correo/chat relevante, buscar cuerpo, adjuntos, asunto, remitentes y hora antes de resumir. Si no se puede, decir la limitación.
4. No centrar el brief en “qué pasó”; usar contexto breve solo para explicar la relevancia de la comunicación. Acciones/sugerencias van en el apartado final.
5. Para legal/regulatorio: decir instrumento, emisor y materia concreta cuando esté disponible; omitir explicación de relevancia salvo urgencia directa.
6. Para calendario: decir horas reales y ventanas reales.
7. Para acciones: proponer tareas ejecutables por Geoffrey basadas en comunicaciones o recordatorios.
8. Omitir finanzas personales por ahora.
9. Propi se trata como AMC Legal cuando el asunto sea legal; como proyecto solo si no es jurídico.
10. Roamy, Diplomado de Autismo y Outlander se omiten salvo seguimiento concreto pendiente.
11. No repetir proyectos sin seguimiento pendiente.
12. No incluir newsletters salvo que traigan señal accionable.
13. Evitar briefs que suenen a plantilla: adaptar tono, orden y énfasis al día real.

## Estándar mínimo de salida

El brief debe incluir solo apartados con señal relevante. Mínimo operativo:

- Título con día, fecha y hora.
- Comunicaciones, calendario, recordatorios y sugerencias solo cuando haya contenido relevante.

Si una fuente crítica falla y eso afecta el brief, decirlo en una línea sobria: fuente, impacto y nada más.

## Privacidad y ejecución

- No ejecutar acciones sin confirmación explícita.
- No enviar correos, SMS ni mensajes sin aprobación por acción y texto final.
- No marcar mensajes/correos como leídos ni archivar sin aprobación.
- No incluir finanzas personales sensibles en Telegram por ahora.
- Resumir información confidencial sin transcribir verbatim salvo que JR lo pida.

## Relacionado

- [[agentes/geoffrey/rutinas|Rutinas — Geoffrey]] · [[briefs|briefs multi-agente]] · [[agentes/geoffrey/integraciones|Integraciones — Geoffrey]] · [[agentes/geoffrey/reminders|Reminders — Geoffrey]] · [[imsg]]
