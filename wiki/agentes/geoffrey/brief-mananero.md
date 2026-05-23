---
type: reference
date: 2026-05-16
tags: [agente, geoffrey, brief, rutina]
---

# Brief mañanero — Geoffrey

Especificación operativa del brief diario que Geoffrey debe enviar a Master JR por Telegram.

El brief es un **seguimiento operativo**: cosas que a JR se le podrían haber olvidado, comunicaciones que necesitan seguimiento, recordatorios que requieren acción y actualización compacta del Diario de Centro América / radar legal. No es resumen ejecutivo, newsletter ni “qué pasó hoy”.

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
- No enviar un brief que contenga: título adornado, “Qué necesita pasar”, secciones vacías, “no veo eventos”, “Fuente:”, “Radar/Radas de cliente”, explicaciones de proceso del DCA o frases de relevancia tipo “Relevante para radar fiscal”.

JR no quiere un resumen ejecutivo general ni fanfarronería metodológica. Quiere materia útil y accionable cuando aplique. Solo incluir contexto mínimo.

Regla central:

> Relevancia real → contexto breve → sugerencia/acción solo en el apartado de sugerencias.

Ejemplo prohibido:

> “Hubo movimiento en Propi con Sur Desarrollos.”

Ejemplo esperado:

> **Propi — Sur Desarrollos:** Thelma mandó observaciones al contrato. [Link al correo](url)

## Qué debe cubrir

1. Qué tiene hoy en calendario solo si hay eventos, conflictos, preparación o ventanas relevantes.
2. Qué comunicaciones relevantes conviene conocer, resumidas sin listar ruido.
3. Qué recordatorios vencidos/de hoy/próximos requieren atención real.
4. Qué cambios del DCA/radar legal debe conocer para mantenerse actualizado en su rubro.
5. Qué sugiere o puede ejecutar Geoffrey con aprobación.

## Estructura vigente

La versión compacta preferida por JR se parece a este patrón: título seco; calendario solo si aporta algo; comunicaciones específicas por asunto con links embebidos; DCA en bullets con link al diario/instrumento y materia concreta; recordatorios/tareas relevantes; sugerencias/acciones aprobables. No incluir noticias por ahora. No incluir `Frentes abiertos`, `Pendientes acumulados`, `Radar de cliente` ni `Puede ignorar hoy` como secciones fijas salvo que JR lo vuelva a pedir explícitamente.

### 1. 📅 Lo que le depara el día

Sección opcional. Incluir solo si hay eventos, conflictos, preparación necesaria, ventanas útiles o recordatorios que afecten el día. Si el calendario está vacío y no hay nada relevante, omitirla por completo.

Incluir:

- Día y fecha.
- Eventos del calendario con hora, duración, ubicación/link si existe.
- Recordatorios vencidos/de hoy que afecten el día.
- Ventanas reales de trabajo: mañana/tarde/noche.
- Conflictos, traslapes, falta de buffer o preparación necesaria.
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

- No depender solo de Gmail API ni solo de `is:unread`; revisar también Apple Mail local cuando esté disponible.
- Revisar correos recientes leídos y no leídos, especialmente de los últimos 3–7 días, porque JR puede haber abierto un correo y aún requerir seguimiento.
- Usar `/Users/jr/.openclaw/workspace-geoffrey/scripts/scan_apple_mail_recent.py` para Apple Mail local si existe; cubre cuentas/carpetas locales como `kidsunderstanding.com`, iCloud y `[Gmail]/Todos` sin modificar correos.
- Tratar como alta señal cualquier correo con vencimiento, formulario, pago, impuestos, ISR/IVA/ISO, retenciones, factura, contrato, firma o adjuntos operativos, aunque esté leído.
- Para Understanding Kids / Inversiones Multidisciplinarias, correos de contabilidad como Elder Estrada / `mueblescontinental.com` son relevantes por defecto si contienen formularios, vencimientos o pagos.
- Si hay link estable, usarlo embebido. Para Gmail web usar `https://mail.google.com/mail/u/0/#...`; para Apple Mail local puede usarse `message://...` generado desde Message-ID. Si no hay link seguro, incluir asunto/remitente y no inventar URL.

Ruido se omite; no crear sección de “ignorar”.

Formato esperado:

> **[Propi — Contrato firma JM](url):** Astrid y Thelma movieron el hilo esta mañana; el asunto parece centrado en firma/versión final.

### 3. ⚖️ Diario de Centro América / radar legal Guatemala

Esta sección no busca acciones inmediatas. Sirve para mantener a JR actualizado como abogado/empresario sobre cómo van cambiando leyes, acuerdos, resoluciones, criterios e instituciones.

Debe revisarse diario, pero con criterio. No listar todo el DCA.

Subfuentes prioritarias:

1. Diario de Centro América / portal legal.
2. Congreso: iniciativas, dictámenes, reformas relevantes.
3. SAT: acuerdos, resoluciones, criterios, registros, cumplimiento tributario.
4. SIB / IVE / AML.
5. Banguat / Junta Monetaria.
6. CC / CSJ / Organismo Judicial.
7. Municipalidades si afecta inmuebles, licencias, construcción, operación o clientes.

Temas siempre relevantes:

- SAT, impuestos, facturación, registros tributarios, compliance.
- IVE/AML, sujetos obligados, prevención de lavado.
- Inmobiliario, licencias, municipalidades, construcción, arrendamientos.
- Sociedades, Registro Mercantil, gobierno corporativo, representación legal.
- Contratación pública, licitaciones, presupuesto estatal si afecta clientes o negocio.
- Laboral, IGSS, Ministerio de Trabajo.
- Banca/SIB, pagos, crédito, regulación financiera.
- Congreso cuando impacte legal, fiscal, inmobiliario, empresarial o seguridad jurídica.
- Educación/terapias si afecta Understanding Kids.
- Tecnología, AI, e-commerce o pagos si afecta Crisol, UK o productividad de JR.

Formato normal — compacto por defecto:

Encabezado del apartado:

> **Diario de Centro América — 15/05/2026** · [Leer diario](url)

> **[Instrumento / DocumentID](url):** una oración sobre qué pasó.

No basta decir “acuerdo publicado” o “resolución institucional”: debe decir qué regula, aprueba, modifica, adjudica, reconoce o dispone. Si solo se obtiene miniatura/primera página, extraer al menos emisor, número y materia visible. Si no se puede saber qué es, omitirlo o marcar “no identificado”, no rellenar con metadata vacía.

No explicar “por qué importa” y no agregar coletillas tipo “Relevante para radar fiscal”. La profundidad se ofrece bajo demanda.

Omitir acuerdos ministeriales, reconocimientos, nombramientos o publicaciones relacionadas con iglesias evangélicas salvo que JR lo pida expresamente o exista conexión legal/cliente concreta.

No mencionar frases de proceso como “el portal devolvió 0 documentos”, “revisé el último día hábil”, “PDF requirió sesión”, “extraje de primera página” o similares. Si el día publicado no coincide con el día actual, el encabezado ya comunica la fecha revisada.

Si hay muchos hallazgos, máximo 3–5 principales; el resto se agrupa:

> Omití X licitaciones/avisos sin conexión clara con clientes o proyectos.

Si no hay algo fuerte:

> **Diario de Centro América — 15/05/2026** · [Leer diario](url)  
> Sin publicaciones de alta relevancia para SAT/IVE/inmobiliario/sociedades/laboral.

No decir “sin acción inmediata” como conclusión principal.

### 4. ✅ Recordatorios / tareas

Dar peso alto a Apple Reminders.

Mostrar recordatorios vencidos, de hoy y próximos relevantes, reorganizados por qué necesita pasar:

- **Hacer hoy.**
- **Reprogramar.**
- **Convertir en mensaje/correo.**
- **Agregar a calendario.**
- **Archivar/completar si ya no aplica.**

No listar todo si hay demasiados; agrupar y proponer limpieza.

### 5. ✅ Sugerencias / acciones que Geoffrey puede ejecutar

Cierre obligatorio si hay sugerencias útiles o acciones aprobables. Deben salir de comunicaciones, calendario o recordatorios, no de consejos genéricos. No incluir sugerencias sobre el Diario de Centro América salvo solicitud expresa de JR.

Máximo 5–7 acciones.

Incluir opciones como:

- “¿Le doy sugerencias de respuesta a estos correos?”
- “Sugiero añadir X a Reminders en Personal > Recurrentes.”
- Agregar evento al calendario.
- Crear/modificar recordatorio.
- Mover o sugerir mover cita.
- Preparar borrador de correo, WhatsApp o mensaje.
- Enviar mensaje/correo solo si JR aprueba texto final.
- Ordenar un hilo de correos en matriz.
- Preparar nota legal breve para cliente/proyecto.
- Revisar un sistema o archivo local.

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
- Listas largas de DCA sin relevancia.
- Proyectos sin seguimiento concreto pendiente.
- Sección “Radar de cliente” / “Radas de Cliente”.

## Lecciones de control de calidad

- 2026-05-17: el brief omitió un correo importante de Elder Estrada del 14/05/2026 sobre ISR rentas del trabajo abril 2026, con formulario y vencimiento 15/05/2026, porque el flujo revisó Gmail API/Apple Mail de forma insuficiente y no trató correos leídos con vencimientos fiscales como señal fuerte. Regla: los correos fiscales/contables con vencimiento deben entrar en Comunicaciones o Sugerencias aunque ya estén leídos.
- Secciones fijas de “Frentes abiertos”.
- Secciones fijas de “Pendientes acumulados”.
- Sección “Puede ignorar hoy”; lo ignorado se omite sin anunciarlo.
- Bullets de DCA que digan solo “acuerdo publicado” sin materia concreta.
- “Acciones sugeridas” demasiado obvias.
- Briefs que suenan a plantilla.

## Reglas de compresión

- DCA: una oración + link/DocumentID. Expandir solo si es claramente crítico.
- No incluir noticias/radar externo por ahora. Si JR lo vuelve a pedir, máximo 3 y cada una debe explicar por qué le importa.
- Comunicaciones: contexto mínimo, resumen breve y link embebido cuando exista correo específico; cualquier propuesta pasa a sugerencias.
- Acciones: máximo 5–8 cuando haya suficientes seguimientos reales; si hay demasiadas, agrupar.
- Evitar explicar “por qué importa” en DCA; el brief debe entrar en materia y dejar la profundidad para demanda posterior.

## DCA — protocolo robusto

No depender solo de la portada `dca.gob.gt`. Usar:

1. Portal legal: `https://legal.dca.gob.gt/`.
2. API/búsqueda del portal legal:
   - `GET /GestionDocumento/EstructuraPublicacionesDCA` para categorías.
   - `POST /GestionDocumento/BusquedaDocumento` con fechas `DD/MM/YYYY`.
   - Helper local si está disponible: `~/.openclaw/workspace/scripts/dca_legal_search.py DD/MM/YYYY`.
   - Para documentos encontrados: `GET /GestionDocumento/VisualizarDocumento?...&doc=ID` y PDF en `/GestionDocumento/DescargarPDFDocumento?idDocumento=ID` cuando haga falta ver contenido.
3. Portada editorial: `https://dca.gob.gt/`.
4. Web search restringido a `site:dca.gob.gt` o `site:legal.dca.gob.gt`.
5. Si todo falla: fuentes secundarias confiables, marcadas como no-DCA.

Categorías mínimas DCA:

- Organismo Legislativo: decretos, acuerdos, disposiciones varias.
- Organismo Ejecutivo: decretos gubernativos, acuerdos gubernativos, acuerdos ministeriales, disposiciones varias.
- Organismo Judicial: acuerdos, resoluciones, disposiciones varias.
- Otras instituciones: acuerdos/resoluciones varias, acuerdos municipales, avisos si parecen relevantes.
- Convocatorias: licitaciones, subastas, balances/estados solo si tienen relevancia pública, legal o para clientes/proyectos.

## Fuentes autorizadas / previstas

- Calendario del día, solo si aporta eventos/ventanas/conflictos relevantes.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail/Apple Mail autorizado según [[agentes/geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- WhatsApp/chats cuando la integración esté disponible/autorizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda, conversación diaria y notas relevantes.
- Web: DCA, Congreso, SAT, SIB/IVE, Banguat, CC/CSJ/OJ, municipalidades relevantes.

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
- DCA/radar legal Guatemala compacto con link al diario, salvo fallo total de acceso.
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
