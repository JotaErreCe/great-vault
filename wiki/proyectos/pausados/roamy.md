---
type: proyecto
date: 2026-04-27
estado: pausado
fecha-inicio: 2026-04-27
tags:
  - proyecto
  - estado/pausado
  - tema/tecnologia
  - tema/app-movil
---

# Roamy

Roamy es una app móvil de location-sharing temporal para grupos — pensada para coordinar personas durante eventos, viajes, conciertos o cualquier actividad en la que el grupo se mueve junto. Iniciada por [[jr]] usando Claude Design. Como de 2026-04.

**Estado:** ⏸ **PAUSADO** — proyecto en pausa. Solo JR en el equipo. Retomar cuando haya tiempo/energía disponible.

**Diferencia importante:** Roamy ≠ [[crisol-tcg]]. Son proyectos completamente distintos.

---

## 📝 Descripción

App para que grupos de personas que se mueven juntas puedan verse en un mapa en tiempo real, sin necesidad de llamadas constantes. La app no es vigilancia permanente — es una herramienta útil y temporal. La privacidad es pilar de diseño.

**Lema:** *Moverse libremente, pero seguir juntos.*

---

## 🎯 Objetivos

1. Lanzar MVP funcional en iOS y Android
2. Posicionarla como herramienta de coordinación grupal (no rastreo)
3. Modelo freemium: base gratis, features premium de pago
4. Alcance global: español + inglés desde el inicio

---

## 🛠️ Stack técnico

| Capa | Tecnología |
|------|-----------|
| App móvil | Flutter (iOS + Android) |
| Backend / Auth / DB / Realtime | Supabase |
| Mapas y navegación | Google Maps |
| Notificaciones push | Firebase Cloud Messaging |
| Desarrollo | Cursor + Claude AI |

**Nota:** una sola persona desarrolla (JR con asistencia de IA).

---

## 🚀 MVP definido

- [x] Autenticación por correo
- [x] Creación de grupos (temporal y permanente)
- [x] Unirse por enlace o código
- [x] Mapa grupal en tiempo real
- [x] Alerta de separación (distancia configurable)
- [x] Punto de reunión con navegación
- [x] Alerta de batería baja (20%)
- [x] Última ubicación conocida
- [x] Botón SOS con confirmación
- [x] Soporte ES/EN
- [x] Sin chat en V1 — alertas predefinidas del admin

---

## 📌 Decisiones clave

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-04-27 | Flutter para iOS y Android | Una sola base de código |
| 2026-04-27 | Supabase como backend | Misma elección que Crisol |
| 2026-04-27 | Sin chat en V1, solo alertas predefinidas | Foco en coordinación, no mensajería |
| 2026-04-27 | Historial limitado a 30-60 min | Privacidad + costos |

---

## ⚠️ Pendientes

- [ ] Estado actual del diseño en Claude Design (JR comparte más tarde)
- [ ] Branding visual: logo, colores, tipografía
- [ ] Mecanismo para pausar sharing sin salir del grupo (¿modo invisible?)
- [ ] Comportamiento ante pérdida de señal (¿distinto de batería baja?)
- [ ] Modo offline / cache de última ubicación al recuperar señal

---

## ✅ Próximos pasos

- [ ] JR comparte estado del diseño en Claude Design
- [ ] Definir branding visual

---

## 🔗 Relacionado

- [[crisol-tcg]] — otro proyecto de JR (marketplace TCG, distinto)
- [[IDENTITY]] — metas de JR

## Relacionado

- [[index]]
