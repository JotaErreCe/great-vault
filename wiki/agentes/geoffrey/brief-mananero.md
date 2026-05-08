---
type: reference
date: 2026-05-08
tags: [agente, geoffrey, brief, rutina]
---

# Brief mañanero — Geoffrey

Especificación operativa del brief diario que Geoffrey debe enviar a Master JR por Telegram. El brief no es un resumen ejecutivo ni una lista de fuentes: es una **lectura concreta de qué le depara el día a JR**, con radar legal, comunicaciones relevantes y acciones que Geoffrey puede ejecutar con aprobación.

## Entrega

- **Canal:** Telegram directo.
- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Formato:** mensajes separados por sección, no un bloque único.
- **Extensión:** suficiente para ser útil; no rellenar por cumplir.
- **Trato:** siempre de **usted**.
- **Idioma:** español, con términos técnicos en inglés cuando sean naturales.

## Principio editorial

El brief debe entrar en materia. No abrir con “resumen del día”, “estado general” ni Top 3. JR quiere saber directamente:

1. **Qué tiene hoy en calendario y qué ventanas reales tiene.**
2. **Qué comunicaciones/proyectos se movieron, exactamente.**
3. **Qué cambios legales/regulatorios debe tener en radar.**
4. **Qué pendientes o riesgos se están arrastrando.**
5. **Qué puede hacer Geoffrey con aprobación: calendario, recordatorios, mensajes, correos, investigación, organización.**

Regla de oro: **no decir “hubo movimiento” sin explicar el movimiento.** Cada item relevante debe decir quién hizo qué, sobre qué documento/asunto, qué cambió y qué queda pendiente.

Ejemplo prohibido:

> “Hubo movimiento en Propi con Sur Desarrollos.”

Ejemplo esperado:

> “Thelma envió versión revisada del contrato de Sur Desarrollos; Astrid quedó copiada para coordinar firma; falta que usted confirme si acepta la cláusula X / si responde con observaciones.”

Si Geoffrey no puede ver el contenido suficiente para ser específico, debe decirlo: “solo pude ver remitente/asunto, no cuerpo/adjuntos”, y sugerir revisar el hilo.

## Fuentes autorizadas / previstas

- Calendario del día.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail/Apple Mail autorizado según [[geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda, conversación diaria y notas relevantes.
- Web: Diario de Centro América, Congreso, SAT, SIB/IVE, Banguat, noticias Guatemala, AI/tech y fuentes relevantes a proyectos.

## Estructura del brief

### 1. 📅 Lo que le depara el día

Primera sección obligatoria. Entrar directo:

- Día y fecha.
- Eventos del calendario con hora, duración, ubicación/link si existe.
- Recordatorios vencidos/de hoy que afecten el día.
- Ventanas reales de trabajo: mañana/tarde/noche.
- Conflictos, traslapes, falta de buffer o preparación necesaria.

Si no hay agenda fuerte, decir qué oportunidad crea:

> “No veo reuniones fijas antes de las 11:00; eso deja una ventana limpia para revisar contratos de Propi.”

### 2. 📬 Comunicaciones relevantes

Solo incluir comunicaciones que merecen atención. No newsletters ni ruido. Clasificar por proyecto/asunto, no por bandeja.

Para cada hilo o conversación:

- **Quién:** remitente/persona.
- **Qué pasó exactamente:** documento enviado, respuesta recibida, pregunta planteada, cambio de versión, coordinación solicitada, deadline, adjunto, etc.
- **Por qué importa:** impacto concreto en JR/AMC Legal/proyecto/familia.
- **Siguiente movimiento:** responder, leer, agendar, delegar, esperar, ignorar.
- **Limitación:** si solo se pudo ver asunto/remitente, indicarlo claramente.

Formato esperado:

> **Propi — Contrato Alianza Intense Group**  
> Astrid envió/reenviió el hilo “Contrato Alianza Intense Group”; Thelma y Andres también intervinieron en las últimas 24h. Falta revisar si el último correo trae versión final, observaciones del abogado de Intense o coordinación de firma.  
> **Siguiente movimiento:** revisar hilo y separar: versión actual / puntos abiertos / quién debe responder.

### 3. ⚖️ Radar legal Guatemala

Esta sección no busca solo acciones inmediatas. Su función es mantener a JR actualizado como abogado/empresario sobre acuerdos, reformas, decretos, resoluciones y cambios regulatorios.

Subfuentes prioritarias:

1. Diario de Centro América / portal legal.
2. Congreso: iniciativas, dictámenes, reformas relevantes.
3. SAT: acuerdos, resoluciones, criterios, registros, cumplimiento tributario.
4. SIB / IVE / AML: prevención de lavado, banca, cumplimiento financiero.
5. Banguat / Junta Monetaria cuando afecte economía, pagos, crédito o tipo de cambio.
6. CC / CSJ / Organismo Judicial cuando haya resoluciones o acuerdos relevantes.
7. Municipalidades si afecta inmuebles, licencias, construcción, operación o clientes.

### DCA — protocolo robusto

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

Cómo resumir cada hallazgo legal:

- **Instrumento:** Acuerdo/Decreto/Resolución + número + emisor.
- **Contenido específico:** qué regula, modifica, autoriza o publica.
- **Relevancia para JR:** alta/media/baja y por qué.
- **Conexión:** AMC Legal, Propi/inmobiliario, fiscal/SAT, IVE/AML, sociedades, contratación pública, laboral, consumidor, banca/SIB, municipal, etc.
- **Seguimiento sugerido:** guardar en radar, investigar, preparar nota, avisar a cliente, crear recordatorio, ignorar.
- **Fuente:** enlace o `DocumentID`.

No decir “sin acción material” como cierre principal. Si no hay nada fuerte, decir: “sin hallazgos de alta relevancia; dejo X/Y/Z como radar de baja/media relevancia”.

### 4. 💼 Proyectos y frentes abiertos

Solo incluir proyectos con cambio nuevo, bloqueo persistente o deadline cercano. Para cada uno:

- **Qué cambió desde ayer o desde la última revisión.**
- **Qué está bloqueado.**
- **Qué decisión o trabajo corresponde.**
- **Qué puede hacer Geoffrey.**

Proyectos de referencia:

- AMC Legal / Propi.
- Understanding Kids.
- Tesis.
- Crisol TCG.
- Altezza / inmuebles / casa.
- Familia/logística cuando afecte agenda o decisiones.

No repetir descripciones estáticas salvo que ayuden a decidir.

### 5. 🧨 Riesgos de arrastre / pendientes que se están pudriendo

Separar de “urgentes” para que JR vea lo que no explota hoy pero se deteriora si se ignora.

Ejemplos:

- Tesis sin bloque semanal.
- Checkout UK roto.
- Contratos con contraparte esperando respuesta.
- Pagos o trámites recurrentes vencidos.
- Recordatorios que ya pasaron y siguen sin cierre.

Cada item debe tener “próximo paso mínimo”.

### 6. 📰 Noticias relevantes para JR

Máximo 3–5, seleccionadas por perfil de JR. No política genérica salvo impacto legal, regulatorio, económico o de negocio.

Temas preferentes:

- Guatemala legal/regulatorio.
- Economía real: tipo de cambio, remesas, inflación, crédito, banca, impuestos.
- Inmobiliario/construcción/municipalidades.
- IVE/AML y cumplimiento.
- Educación, clínica, terapias o marketing si afecta UK.
- AI/productividad/automatización si puede servir a JR.
- E-commerce/marketplaces si afecta Crisol o UK.

Cada noticia debe decir:

- **Qué pasó.**
- **Por qué le importa a JR.**
- **Si debe quedar en radar o merece acción.**

### 7. ✅ Acciones que Geoffrey puede ejecutar

Cierre obligatorio. No solo “acciones sugeridas”; deben ser acciones aprobables y ejecutables por Geoffrey.

Incluir opciones como:

- Agregar evento al calendario.
- Crear/modificar recordatorio.
- Mover o sugerir mover cita.
- Preparar borrador de correo o mensaje.
- Enviar mensaje/correo solo si JR aprueba texto final.
- Ordenar un hilo de correos en matriz.
- Profundizar en DCA/SAT/SIB/Congreso.
- Preparar nota legal breve para cliente/proyecto.
- Actualizar una página del Vault.
- Revisar un sistema o archivo local.

Formato:

> 1. Creo recordatorio para X el lunes 9:00.  
> 2. Le preparo matriz de Propi: contrato / versión / contraparte / pendiente / respuesta sugerida.  
> 3. Hago nota radar sobre SAT Acuerdo 3-2026.  
> 4. Redacto mensaje para Thelma preguntando por versión final y firma.

Cierre:

> ¿Aprueba alguna? Puede responder con números o decirme qué ajusto.

## Reglas de especificidad

1. Prohibido usar frases vagas como “hubo movimiento”, “hay temas”, “revisar pendientes” sin detalle.
2. Si hay correo/mensaje relevante, buscar cuerpo, adjuntos, asunto, remitentes y hora antes de resumir. Si no se puede, decir la limitación.
3. Para proyectos: decir el cambio concreto o el bloqueo concreto.
4. Para legal/regulatorio: decir número de instrumento, emisor y materia cuando esté disponible.
5. Para calendario: decir horas reales y ventanas reales.
6. Para acciones: proponer tareas que Geoffrey pueda ejecutar, no consejos genéricos.
7. Omitir finanzas personales por ahora, salvo que JR lo pida explícitamente.
8. No incluir portafolio personal, montos financieros sensibles ni composición patrimonial en Telegram.
9. Propi se trata como AMC Legal cuando el asunto sea legal; como proyecto solo si no es jurídico.
10. Roamy, Diplomado de Autismo y Outlander se omiten salvo evento real relevante.

## Estándar mínimo de salida

Aunque haya poca información, el brief debe incluir:

- Lo que le depara el día: agenda, recordatorios y ventanas.
- Comunicaciones relevantes con movimiento específico o limitación clara.
- Radar legal Guatemala con DCA y, cuando aplique, Congreso/SAT/SIB.
- Proyectos/frentes abiertos solo si hay cambio, bloqueo o deadline.
- Riesgos de arrastre.
- Noticias relevantes filtradas para JR.
- Acciones ejecutables por Geoffrey.

Si no puede cumplir por fallo técnico, debe decir exactamente qué fuente falló y qué alternativa intentó.

## Privacidad y ejecución

- No ejecutar acciones sin confirmación explícita.
- No enviar correos, SMS ni mensajes sin aprobación por acción y texto final.
- No marcar mensajes/correos como leídos ni archivar sin aprobación.
- No incluir finanzas personales en Telegram por ahora.
- Resumir información confidencial sin transcribir verbatim salvo que JR lo pida.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/reminders|Reminders — Geoffrey]] · [[imsg]]
