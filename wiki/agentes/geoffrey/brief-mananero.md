---
type: reference
date: 2026-05-08
tags: [agente, geoffrey, brief, rutina]
---

# Brief mañanero — Geoffrey

Especificación operativa del brief diario que Geoffrey debe enviar a Master JR por Telegram. Criterio central: **útil en menos de 5 minutos**, con contexto suficiente para decidir; no una lista escueta de fuentes revisadas.

## Entrega

- **Canal:** Telegram directo.
- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Formato:** mensajes separados por sección, no un bloque único.
- **Extensión:** cada sección breve, pero con suficiente contexto práctico. No sacrificar utilidad por brevedad.
- **Trato:** siempre de **usted**.
- **Idioma:** español, con términos técnicos en inglés cuando sean naturales.

## Principio de calidad

El brief debe contestar cuatro preguntas:

1. **¿Qué requiere mi atención hoy?**
2. **¿Qué cambió desde ayer?**
3. **¿Qué riesgo o oportunidad puedo perder si no actúo?**
4. **¿Qué puede hacer Geoffrey con mi aprobación?**

Si una sección solo dice “sin acceso” o “no encontré”, Geoffrey debe intentar una fuente alternativa antes de reportar fallo. Un brief sin hallazgos debe explicar **qué se revisó** y **por qué no hay acción**, no quedarse vacío.

## Fuentes autorizadas / previstas

- Calendario del día.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail autorizado según [[geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda, conversación diaria y notas relevantes.
- Web: Diario de Centro América, noticias Guatemala, noticias internacionales, AI/tech y mercados generales.

## Diario de Centro América / legal-regulatorio

El Diario de Centro América es fuente prioritaria para Master JR por su valor legal/regulatorio. **No depender solo de la portada `dca.gob.gt`.** Usar el portal legal cuando la portada no entregue resultados útiles.

### Fuentes DCA en orden

1. Portal legal: `https://legal.dca.gob.gt/`.
2. API/búsqueda del portal legal:
   - `GET /GestionDocumento/EstructuraPublicacionesDCA` para categorías.
   - `POST /GestionDocumento/BusquedaDocumento` con fechas `DD/MM/YYYY`.
   - Para documentos encontrados: `GET /GestionDocumento/VisualizarDocumento?...&doc=ID` y PDF en `/GestionDocumento/DescargarPDFDocumento?idDocumento=ID` cuando haga falta ver contenido.
3. Portada editorial: `https://dca.gob.gt/`.
4. Web search restringido a `site:dca.gob.gt` o `site:legal.dca.gob.gt`.
5. Si todo falla: noticias legales/regulatorias de fuentes secundarias confiables, indicando que no son DCA.

### Categorías mínimas a revisar en portal legal

- Organismo Legislativo: decretos, acuerdos, disposiciones varias.
- Organismo Ejecutivo: decretos gubernativos, acuerdos gubernativos, acuerdos ministeriales, disposiciones varias.
- Organismo Judicial: acuerdos, resoluciones, disposiciones varias.
- Otras instituciones: acuerdos/resoluciones varias, acuerdos municipales, avisos si parecen relevantes.
- Convocatorias: licitaciones, subastas, balances/estados si hay relación con clientes o proyectos.

### Cómo resumir DCA

Para cada hallazgo relevante:

- **Qué es:** tipo de publicación + emisor + identificador si existe.
- **Qué cambió:** una línea práctica.
- **A quién afecta:** JR/AMC Legal/clientes/proyectos/Guatemala general.
- **Acción:** revisar, archivar, responder a cliente, monitorear o ignorar.
- **Fuente:** enlace o ruta de búsqueda cuando sea posible.

Si hay muchos resultados, priorizar legal/regulatorio y decir “hay N publicaciones menores omitidas”. Si no hay nada material, decir: “DCA legal revisado en categorías X/Y/Z; sin acción material hoy.”

## Estructura del brief

### Mensajes fijos

1. **🌅 Saludo + Top 3 del día**
   - Día de semana y fecha.
   - Top 3 prioridades con razón breve.
   - Estado general del día: liviano/cargado/con riesgos.
   - Cualquier conflicto crítico sube aquí.

2. **📅 Agenda + ventanas reales**
   - Mañana / tarde / noche.
   - Cada evento: hora · título · ubicación/link · duración.
   - Si no hay agenda, decirlo y convertirlo en oportunidad: “bloque útil para X”.
   - Marcar conflictos, reuniones consecutivas o falta de buffer.

3. **🚨 Urgentes / acción requerida**
   - Reminders vencidos o de hoy.
   - Correos de últimas 24h con urgencia/deadline explícito.
   - SMS pendientes de respuesta de familia, clientes activos o contactos VIP.
   - Clasificar: **Hoy**, **Esta semana**, **Puede esperar**.

4. **✨ Acciones sugeridas + cierre**
   - 3–7 acciones concretas, priorizadas.
   - Formato aprobable: “Sí a 1, 3, 5”.
   - Cierre obligatorio: “¿Aprueba alguna acción sugerida o necesita profundizar en algo?”

### Mensajes condicionales pero esperados si hay contenido

- **📧 Correos accionables** — máximo 5 hilos; no listar newsletters. Para cada uno: remitente · asunto · por qué importa · siguiente acción.
- **⚖️ DCA / legal-regulatorio** — usar protocolo robusto anterior.
- **💼 Proyectos vivos** — solo cambios o bloqueos en Propi, UK, tesis, AMC Legal, Crisol u otros activos.
- **💰 Finanzas / cobros / gastos** — solo anomalías, pagos vencidos o cosas que requieran decisión; no portafolio personal por ahora.
- **📰 Noticias relevantes** — 3–5 bullets máximo, con “por qué le importa a JR”.
- **💭 Criterio de Geoffrey** — opcional: una observación útil, no frase motivacional.

## Reglas de priorización

1. Urgencia manda: deadline hoy > mañana > esta semana > importante sin fecha.
2. Utilidad manda sobre brevedad: mejor 8 líneas útiles que 3 vacías.
3. Si una fuente falla, intentar una alternativa antes de reportarlo.
4. Si hay conflicto crítico de agenda o deadline, va en el primer mensaje.
5. Para correo: incluir solo si Master JR debe responder, decidir, agendar, delegar o revisar.
6. Para SMS: incluir solo conversaciones con respuesta pendiente o señal relevante; no transcribir mensajes crudos salvo necesidad explícita.
7. Propi se trata como AMC Legal cuando el asunto sea legal; como proyecto solo si no es jurídico.
8. Roamy, Diplomado de Autismo y Outlander se omiten salvo evento real relevante.
9. No llenar el brief con “fuentes sin novedad”; agruparlas en una línea de verificación.

## Estándar mínimo de salida

Aunque haya poca información, el brief debe incluir:

- Top 3 razonado.
- Agenda o ventana recomendada si no hay eventos.
- Urgentes separados por prioridad.
- DCA/legal: hallazgos o verificación robusta.
- 3 acciones sugeridas.

Si no puede cumplir esto por fallo técnico, debe decir exactamente qué fuente falló y qué alternativa intentó.

## Privacidad y ejecución

- No ejecutar acciones sin confirmación explícita.
- No enviar correos, SMS ni mensajes sin aprobación por acción.
- No marcar mensajes/correos como leídos ni archivar sin aprobación.
- No incluir montos, composición ni rendimiento del portafolio personal en Telegram por ahora.
- Resumir información confidencial sin transcribir verbatim.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/reminders|Reminders — Geoffrey]] · [[imsg]]
