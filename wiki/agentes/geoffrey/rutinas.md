---
type: reference
date: 2026-05-13
tags: [agente, geoffrey, rutinas, brief]
---

# Rutinas — Geoffrey

Procedimientos recurrentes de Geoffrey. Este archivo define cómo ejecutar tareas repetidas; [[geoffrey/AGENT|AGENT]] define reglas operativas generales.

## Brief mañanero

Objetivo: enviar a Master JR un brief diario corto, específico y accionable por Telegram. La especificación canónica vive en [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]].

### Entrega

- **Canal:** Telegram directo a JR.
- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Automatización:** cron de OpenClaw, no heartbeat genérico.
- **Formato:** compacto, Telegram-friendly, secciones claras.
- **Trato:** siempre de **usted**.

### Automatización activa

El brief debe ejecutarse con un cron diario:

- Nombre esperado: `Geoffrey Morning Brief`
- Cron: `15 7 * * *`
- Zona horaria: `America/Guatemala`
- Sesión: `isolated`
- Delivery: `announce` por Telegram directo a JR.

El heartbeat no debe duplicar el brief. Si se usa `HEARTBEAT.md`, debe servir solo como guardia/recordatorio, no como disparador principal del brief diario.

### Fuentes previstas

- Calendario del día.
- Apple Reminders: vencidos, hoy y próximos; ver [[geoffrey/reminders|Reminders — Geoffrey]] y [[resources/apple-reminders-manual|Manual operativo — Apple Reminders de JR]].
- Correo: ver [[geoffrey/integraciones|Integraciones — Geoffrey]] (`joserca95@gmail.com`, `jcastaneda@kidsunderstanding.com`, `joserca95@icloud.com`; UFM excluida por defecto).
- SMS vía [[imsg]] cuando aplique; lectura local minimizada, sin envío ni marcar como leído sin aprobación.
- Radar legal/regulatorio: Diario de Centro América, Congreso, SAT, SIB/IVE, Banguat, CC/CSJ/OJ y fuentes oficiales relevantes.
- Great Vault: dashboard/proyectos/notas relevantes si aportan seguimiento real.

### Orden vigente del brief

El orden canónico vive en [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]]. Versión vigente:

1. 📅 Lo que le depara el día.
2. 📬 Comunicaciones relevantes.
3. ⚖️ Radar legal Guatemala / DCA.
4. 🧑‍💼 Radar de cliente, solo si aplica.
5. ✅ Reminders / qué haceres.
6. ✅ Puedo ejecutar con aprobación.

No incluir como secciones fijas:

- Noticias.
- Frentes abiertos.
- Pendientes acumulados.
- Puede ignorar hoy.
- Riesgo de arrastre.
- Top 3 / Mapa de Atención / “cómo viene el día”.

### Reglas de edición

- Entrar directo con `📅 Lo que le depara el día`.
- Omitir secciones vacías.
- Comunicaciones: quién / qué pasó / qué necesita pasar.
- DCA: no basta decir que existe un acuerdo; debe decir qué regula, aprueba, modifica, adjudica, reconoce o dispone.
- Reminders: enfocarse en qué hacer, confirmar, reprogramar o convertir en acción.
- Finanzas personales y portafolio quedan fuera por ahora, salvo solicitud explícita de JR.
- Usar links a fuentes cuando existan.
- No enviar correos, mensajes ni acciones externas sin aprobación explícita.
- El cron está autorizado a enviar el brief; las acciones dentro del brief siguen requiriendo aprobación de JR.

### Verificación operativa

Para auditar que el envío diario está activo:

```bash
openclaw cron list
openclaw cron show <job-id>
openclaw cron runs --id <job-id>
openclaw status
```

Debe existir un job diario habilitado para `Geoffrey Morning Brief`. Si no existe, el formato puede estar documentado pero el envío diario no está garantizado.

## Pendientes operativos

- Mejorar acceso a Apple Calendar si vuelve a fallar con `Calendar got an error: Application isn’t running. (-600)`.
- Mejorar extracción de cuerpo/links de Apple Mail (`message://...`) para comunicaciones relevantes.
- Mejorar extracción DCA cuando el endpoint PDF devuelva PDFs vacíos.
- Organizar labels/filtros de Gmail para separar AMC Legal de correo personal en `joserca95@gmail.com`; JR aprobó la idea, pero pidió dejarlo para después y enfocarse primero en el brief.

## Relacionado

- [[geoffrey/SOUL|SOUL — Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|integraciones]] · [[geoffrey/reminders|reminders]] · [[resources/apple-reminders-manual|Manual operativo — Apple Reminders de JR]]
