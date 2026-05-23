---
type: proyecto
date: 2026-04-27
estado: activo
fecha-inicio: 2026-04-27
tags:
  - proyecto
  - estado/activo
  - tema/tecnologia
  - tema/tcg
  - tema/fintech
---

# Crisol TCG

Crisol TCG es el proyecto principal de [[jr]]: el primer marketplace integral y centralizado de Guatemala diseñado exclusivamente para juegos de cartas coleccionables (TCG). Su propósito es profesionalizar el hobby en la región centroamericana, eliminando los riesgos de las transacciones informales (estafas, asaltos, disputas). Como de 2026-04.

---

## 📝 Descripción

Plataforma digital multivendedor donde compradores y vendedores de TCG (Yu-Gi-Oh!, Pokémon, Magic: The Gathering, One Piece, accesorios) operan sobre una infraestructura centralizada. El diferenciador clave: un **catálogo maestro** administrado por la plataforma — los vendedores no crean cartas, solo crean **listados** sobre fichas ya existentes.

**Arquetipo de marca:** "El Facilitador Eficiente".

---

## 🎯 Objetivos

1. Ser la referencia de precios TCG en Guatemala
2. Proveer infraestructura segura de compra/venta con escrow
3. Democratizar los pagos (Visacuotas para piezas de alto valor)
4. Escalar a nivel regional centroamericano

---

## 🏛️ Tres pilares

1. **Seguridad transaccional** — escrow: 5 días para despachar + 48h para disputar
2. **Eficiencia logística** — envío ciego (solo IDs de orden), método "sándwich"
3. **Democratización de pagos** — tarjetas locales + Visacuotas

---

## 🛠️ Stack técnico

### Implementación actual (producción)
| Capa | Tecnología |
|------|-----------|
| CMS / tienda | WordPress + WooCommerce en `crisoltcg.com` |
| Base de datos cartas | YGOPRODeck API (sync automatizado con Python) |
| Catálogo Yu-Gi-Oh | CSV/JSON por set exportados a WooCommerce |
| Automatización precios | `actualizar_precios.py` — consulta YGOPro y actualiza WooCommerce via REST API |

### Stack objetivo (planeado / en desarrollo)
| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js + React + Tailwind CSS |
| Animaciones | Framer Motion |
| Gráficas | Recharts |
| Backend / DB / Auth | Supabase |

---

## 🚀 MVP — alcance definido

- [x] Catálogo maestro
- [x] Registro de usuarios
- [x] Creación de listados por vendedores
- [x] Catálogo público navegable
- [x] Ficha de producto
- [x] Carrito multi-vendedor
- [x] Checkout
- [x] Integración PagaloGT + Visacuotas
- [x] Panel básico de vendedor
- [x] Panel administrativo
- [x] Control de órdenes

**Post-MVP:** análisis avanzado de precios, gráficos dinámicos, estadísticas mensuales.

---

## 🔐 Sistema de usuarios (KYC estricto para vendedores)

- Vendedores requieren: validación SMS + DPI/NIT + cruce SAT + recibo de servicios + declaración jurada
- Sanciones por fraude: expulsión de por vida, bloqueo por DPI/NIT
- Política de cero privilegios internos

---

## 🎮 Gamificación de vendedores

| Nivel | Retiro | Beneficios |
|-------|--------|-----------|
| Básico | 7 días | Límites estrictos |
| Fase 1 | Reducido | Carga masiva Excel |
| Fase 2 | Reducido | Más herramientas |
| EX (Power Sellers) | 2 días | Sin límites |

---

## 📌 Decisiones clave

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-04-27 | Stack: Next.js + React + Tailwind + Supabase + Framer + Recharts | Definido en contexto ChatGPT |
| 2026-04-27 | Escrow: 5 días despacho + 48h disputa | Versión Gemini es autoritativa sobre versión ChatGPT |
| 2026-04-27 | Kits de empaque oficial con margen oculto como fondo de garantía | Jugada financiera inteligente |
| 2026-04-27 | Envío ciego — solo IDs de orden, sin nombres reales | Privacidad de usuarios |

---

## 🎨 Identidad visual

| Elemento | Valor |
|----------|-------|
| Color principal (Ink) | `#111827` (gris casi negro) |
| Color acento (Amber) | `#F59E0B` |
| Fondo oscuro sugerido | `#0B1020` |
| Tipografía | Inter / Space Grotesk / Manrope |
| Logos | Horizontal pill, Horizontal alt, Stacked, Inverso (blanco sobre `#0B1020`) |
| Isotipos | C monograma, cartas apiladas, crisol gota |
| Archivos SVG | `~/Downloads/Crisol_TCG_Logotipo_SVG/` + `Crisol_TCG_Isotipos_SVG/` |

---

## ⚠️ Pendientes

- [ ] Estado exacto: WooCommerce en producción vs. migración a Next.js/Supabase
- [ ] Couriers / partners logísticos (Cargo Expreso, Guatex, Forza, etc.)
- [ ] Pasarela de pago final: PagaloGT vs Visacuotas
- [ ] Definir equipo: ¿solo JR? ¿hay socios o desarrollador?
- [ ] Flujo completo de disputas y reputación de vendedores

---

## ✅ Próximos pasos

- [ ] Confirmar estado actual del proyecto
- [ ] Definir pasarela de pago final
- [ ] Integrar contexto adicional de ChatGPT/Gemini

---

## 🔗 Relacionado

- [[roamy|Roamy]] — otro proyecto de JR (app distinta)
- [[understanding-kids]] — proyecto de Mónica
- [[wiki/IDENTITY]] — metas de JR vinculadas a Crisol

## Relacionado

- [[wiki/index]]
