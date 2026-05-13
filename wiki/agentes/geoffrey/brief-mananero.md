---
type: reference
date: 2026-05-13
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

JR no quiere saber “qué pasó” como noticia. Quiere saber **qué necesita pasar**. Solo incluir qué pasó como contexto mínimo para explicar qué debe pasar después.

Regla central:

> Contexto breve → acción/seguimiento necesario.

Ejemplo prohibido:

> “Hubo movimiento en Propi con Sur Desarrollos.”

Ejemplo esperado:

> **Propi — Sur Desarrollos:** Thelma mandó observaciones al contrato; falta que usted defina si acepta los cambios o si quiere que prepare respuesta con contraobservaciones.

## Qué debe cubrir

1. Qué tiene hoy en calendario y qué ventanas reales tiene.
2. Qué comunicaciones necesita contestar, revisar o recordar.
3. Qué seguimiento nace de correos, WhatsApp/chats u otras comunicaciones.
4. Qué recordatorios vencidos/de hoy/próximos requieren acción o reprogramación.
5. Qué cambios del DCA/radar legal debe conocer para mantenerse actualizado en su rubro.
6. Qué puede ejecutar Geoffrey con aprobación.

## Estructura vigente

La versión compacta preferida por JR se parece a este patrón: calendario/ventanas + pendientes vencidos visibles; comunicaciones específicas por asunto; DCA en bullets con instrumento linkeado y materia concreta; recordatorios/tareas; acciones aprobables. No incluir noticias por ahora. No incluir `Frentes abiertos`, `Pendientes acumulados` ni `Puede ignorar hoy` como secciones fijas salvo que JR lo vuelva a pedir explícitamente.

### 1. 📅 Lo que le depara el día

Primera sección obligatoria. Empezar aquí.

Incluir:

- Día y fecha.
- Eventos del calendario con hora, duración, ubicación/link si existe.
- Recordatorios vencidos/de hoy que afecten el día.
- Ventanas reales de trabajo: mañana/tarde/noche.
- Conflictos, traslapes, falta de buffer o preparación necesaria.
- Qué necesita pasar hoy, no solo qué está agendado.

Ejemplo:

> No veo reuniones fijas antes de las 11:00; esa ventana debería usarse para cerrar Propi o avanzar tesis. Si se va en correos sueltos, el pendiente vuelve a arrastrarse.

### 2. 📬 Comunicaciones que requieren seguimiento

Esta sección es el corazón del brief.

No listar correos. Decir qué necesita atención y qué debe pasar después.

Fuentes: correos, WhatsApp/chats cuando estén disponibles, SMS relevantes, Apple Mail/Gmail autorizado y cualquier comunicación local autorizada.

Para cada comunicación relevante:

- **Proyecto/asunto.**
- **Quién escribió o intervino.**
- **Contexto mínimo:** qué pasó, solo lo necesario para entender el seguimiento.
- **Qué necesita pasar:** contestar, revisar, pedir documento, aprobar, calendarizar, crear reminder, esperar, delegar.
- **Si JR no contestó:** marcarlo como seguimiento pendiente.
- **Limitación:** si solo se pudo ver asunto/remitente o no cuerpo/adjuntos, decirlo.

Clasificación sugerida:

- **Contestar / resolver hoy.**
- **Revisar para decidir.**
- **Agregar a recordatorio/calendario.**
- **Esperar / sin acción por ahora.**
- **Ignorar / ruido.**

Formato esperado:

> **Propi — Contrato firma JM**  
> Astrid y Thelma movieron el hilo esta mañana. Solo pude verificar remitentes/asunto, no el cuerpo ni adjuntos.  
> **Qué necesita pasar:** abrir el hilo y confirmar si falta firma, versión final o instrucción a José Mario. Si quiere, preparo matriz del hilo.

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

> **[Instrumento / DocumentID](url):** una oración sobre qué pasó.

No basta decir “acuerdo publicado” o “resolución institucional”: debe decir qué regula, aprueba, modifica, adjudica, reconoce o dispone. Si solo se obtiene miniatura/primera página, extraer al menos emisor, número y materia visible. Si no se puede saber qué es, omitirlo o marcar “no identificado”, no rellenar con metadata vacía.

No explicar “por qué importa” salvo que sea alta relevancia directa para AMC Legal, Propi, SAT/IVE/AML, inmobiliario, clientes o decisión inmediata. La profundidad se ofrece bajo demanda.

Si hay muchos hallazgos, máximo 3–5 principales; el resto se agrupa:

> Omití X licitaciones/avisos sin conexión clara con clientes o proyectos.

Si no hay algo fuerte:

> DCA revisado con criterio SAT/IVE/inmobiliario/sociedades/laboral; no encontré publicaciones de alta relevancia. Omití avisos administrativos, convocatorias sin conexión clara y publicaciones sin impacto para su práctica.

No decir “sin acción inmediata” como conclusión principal.

### 4. 🧑‍💼 Radar de cliente

Incluir solo si hay señal real.

Objetivo: anticipar consultas de clientes o ángulos útiles para AMC Legal.

Ejemplos:

- SAT cambia registro de contadores → clientes con contabilidad externa.
- IVE/AML → Propi, inmobiliarias, sujetos obligados, clientes corporativos.
- Presupuesto/lictitaciones → contratistas, proveedores del Estado, ejecución pública.
- Municipalidad/licencias → inmobiliario, construcción, locales comerciales.
- Laboral/IGSS → clientes con planillas o contratación.

Formato:

> **Radar de cliente:** si alguien de Propi pregunta por IVE/AML, conviene responder desde sujeto obligado y debida diligencia, no como trámite administrativo.

### 5. ✅ Recordatorios / tareas

Dar peso alto a Apple Reminders.

Mostrar recordatorios vencidos, de hoy y próximos relevantes, reorganizados por qué necesita pasar:

- **Hacer hoy.**
- **Reprogramar.**
- **Convertir en mensaje/correo.**
- **Agregar a calendario.**
- **Archivar/completar si ya no aplica.**

No listar todo si hay demasiados; agrupar y proponer limpieza.

### 6. ✅ Acciones que Geoffrey puede ejecutar

Cierre obligatorio. Las acciones deben salir de comunicaciones y recordatorios, no de consejos genéricos.

Máximo 5–7 acciones.

Incluir opciones como:

- Agregar evento al calendario.
- Crear/modificar recordatorio.
- Mover o sugerir mover cita.
- Preparar borrador de correo, WhatsApp o mensaje.
- Enviar mensaje/correo solo si JR aprueba texto final.
- Ordenar un hilo de correos en matriz.
- Profundizar en DCA/SAT/SIB/Congreso.
- Preparar nota legal breve para cliente/proyecto.
- Revisar un sistema o archivo local.

Formato:

> 1. Le preparo matriz del hilo Propi: asunto / última intervención / qué falta / respuesta sugerida.  
> 2. Creo reminder para pagar luz/mantenimiento hoy 5:00 PM.  
> 3. Le redacto respuesta para Thelma preguntando por versión final y firma.  
> 4. Agrego bloque de tesis de 90 min al calendario.

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
- Secciones fijas de “Frentes abiertos”.
- Secciones fijas de “Pendientes acumulados”.
- Sección “Puede ignorar hoy”; lo ignorado se omite sin anunciarlo.
- Bullets de DCA que digan solo “acuerdo publicado” sin materia concreta.
- “Acciones sugeridas” demasiado obvias.
- Briefs que suenan a plantilla.

## Reglas de compresión

- DCA: una oración + link/DocumentID. Expandir solo si es claramente crítico.
- Noticias/radar externo: máximo 3, cada una con una línea de “por qué le importa”.
- Por ahora, no incluir noticias; esta regla queda suspendida hasta nueva instrucción.
- Comunicaciones: contexto mínimo; foco en qué necesita pasar.
- Acciones: máximo 5–8 cuando haya suficientes seguimientos reales; si hay demasiadas, agrupar.
- Evitar repetir “por qué importa” cuando el siguiente movimiento ya lo deja claro.

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

- Calendario del día.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail/Apple Mail autorizado según [[geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- WhatsApp/chats cuando la integración esté disponible/autorizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda, conversación diaria y notas relevantes.
- Web: DCA, Congreso, SAT, SIB/IVE, Banguat, CC/CSJ/OJ, municipalidades relevantes.

## Reglas duras de especificidad

1. Prohibido usar frases vagas como “hubo movimiento”, “hay temas”, “revisar pendientes” sin detalle.
2. Prohibido decir “no encontré nada relevante” sin explicar criterio mínimo de búsqueda/descarte.
3. Si hay correo/chat relevante, buscar cuerpo, adjuntos, asunto, remitentes y hora antes de resumir. Si no se puede, decir la limitación.
4. No centrar el brief en “qué pasó”; usar contexto breve solo para explicar qué necesita pasar.
5. Para legal/regulatorio: decir instrumento, emisor, materia y relevancia cuando esté disponible.
6. Para calendario: decir horas reales y ventanas reales.
7. Para acciones: proponer tareas ejecutables por Geoffrey basadas en comunicaciones o recordatorios.
8. Omitir finanzas personales por ahora.
9. Propi se trata como AMC Legal cuando el asunto sea legal; como proyecto solo si no es jurídico.
10. Roamy, Diplomado de Autismo y Outlander se omiten salvo seguimiento concreto pendiente.
11. No repetir proyectos sin seguimiento pendiente.
12. No incluir newsletters salvo que traigan señal accionable.
13. Evitar briefs que suenen a plantilla: adaptar tono, orden y énfasis al día real.

## Estándar mínimo de salida

Aunque haya poca información, el brief debe incluir:

- Lo que le depara el día.
- Comunicaciones que requieren seguimiento o criterio claro de descarte.
- DCA/radar legal Guatemala compacto.
- Recordatorios/tareas relevantes.
- Acciones ejecutables por Geoffrey, máximo 5–7.

Si una fuente falla, decir exactamente qué fuente falló, qué alternativa se intentó y qué impacto tiene en la calidad del brief.

## Privacidad y ejecución

- No ejecutar acciones sin confirmación explícita.
- No enviar correos, SMS ni mensajes sin aprobación por acción y texto final.
- No marcar mensajes/correos como leídos ni archivar sin aprobación.
- No incluir finanzas personales sensibles en Telegram por ahora.
- Resumir información confidencial sin transcribir verbatim salvo que JR lo pida.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/reminders|Reminders — Geoffrey]] · [[imsg]]
