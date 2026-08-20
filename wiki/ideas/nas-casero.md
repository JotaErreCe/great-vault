---
type: idea
date: 2026-08-20
tags:
  - idea
  - tema/infraestructura
  - tema/finanzas-personales
  - prioridad/baja
---

# NAS casero — análisis de viabilidad

Análisis de costo-beneficio de armar un NAS doméstico para reemplazar iCloud+ y suscripciones de streaming. Hecho 2026-08-20 con precios reales de esa fecha.

**Estado: NO ejecutar todavía.** Ver [[#Gatillo de decisión]].

---

## Punto de partida

- Mac Pro al **95% de capacidad**: 393 GB usados de 460 GB. Solo 24 GB libres. 83 GB de eso está en `~/Downloads`.
- **No existe backup** de ninguna de las dos Macs. Riesgo real y no cubierto.
- Data total estimada (ambas Macs + iCloud): **1–2 TB**.
- Internet de casa: **250 Mbps de bajada / 20 Mbps de subida**.

---

## Qué reemplazaría (precios Guatemala, agosto 2026)

| Servicio | Mensual USD | Anual USD |
|---|---|---|
| Netflix Estándar | 9.99 | 120 |
| Disney+ Standard | 10.99 | 132 |
| Apple TV+ | *sin confirmar* | — |
| iCloud+ 2 TB | 9.99 | 120 |

**Total reemplazable estimado: ~USD 41/mes ≈ Q3,770/año.**

> Pendiente: confirmar qué planes tiene contratados y el monto real de Apple TV+. Ver [[suscripciones]].

---

## Restricción crítica: la subida de 20 Mbps

| Escenario | Viable |
|---|---|
| 4K **en casa** (por LAN) | Sí — el internet no interviene |
| 1080p fuera de casa, 1 stream | Sí, apenas (consume 8–15 de 20) |
| 1080p fuera de casa, 2 streams | No |
| **4K fuera de casa** | **Imposible** — pide 25–50 Mbps |
| 720p fuera (transcodificado), 2–3 streams | Sí |

**Consecuencias de diseño:**
- El 4K vive dentro de la casa. Para fuera hay que transcodificar → obliga a un CPU con Intel Quick Sync.
- Un backup inicial de 2 TB hacia la nube tomaría **~11 días** de subida saturada. Sembrarlo por disco físico, no por internet.

---

## Dimensionamiento

Proyección a 5 años:

| Concepto | Espacio |
|---|---|
| Buffer de media (rotativo, ~15 pelis + series) | ~1 TB |
| Datos actuales | 2 TB |
| Crecimiento de fotos (~150 GB/año) | ~1 TB |
| Time Machine de las dos Macs | ~2.5 TB |
| **Total** | **~6.5 TB** |

Regla: nunca pasar del 80% de ocupación. En espejo no se puede ampliar barato — hay que reemplazar ambos discos.

**Recomendación: 2 × 14 TB en espejo → 14 TB usables** (46% de ocupación al año 5).

---

## Especificación recomendada

| Componente | Elección | Razón |
|---|---|---|
| Equipo | **UGREEN NASync DXP2800** (Intel N100, 8 GB DDR5) | El N100 trae Quick Sync — obligatorio por la subida de 20 Mbps |
| Discos | **2 × 14 TB enterprise recertificado** (Exos / Ultrastar / Toshiba MG) con garantía | Los discos nuevos cuestan 2.5× y matan el payback |
| Arreglo | Espejo (RAID 1) | Tolera la falla de un disco |
| Software de media | **Jellyfin, no Plex** | Plex Pass subió a USD 749.99 lifetime / 69.99 anual el 2026-07-01 y la transcodificación por hardware lo exige. Jellyfin lo hace gratis |
| Tarjeta gráfica | **No** | El N100 ya trae Quick Sync (3–5 transcodes 4K simultáneos, 6 W). El cuello de botella es el internet, no el CPU. El DXP2800 tampoco tiene ranura PCIe |
| Clientes | Apple TV 4K por televisor | Reproduce nativo → elimina el transcoding en casa |

---

## Números

| Escenario de discos | Inversión (con ~27% de casillero + IVA) | Payback |
|---|---|---|
| **Recertificados** | **≈ Q9,000** | **2.6 años** ✓ |
| Nuevos | ≈ Q15,400 | 4.5 años ✗ |

Ahorro neto anual: Q3,770 − Q315 de electricidad = **Q3,455/año**.

**El proyecto solo cierra con discos recertificados.** Con discos nuevos el payback excede la vida útil del disco.

### Costos que casi nadie cuenta
- **Electricidad:** ~20 W constantes ≈ Q315/año
- **Amortización de discos:** vida útil ~5 años ≈ Q660/año
- **Backup off-site:** un NAS en casa **no es backup**. Incendio o robo se lleva todo. Sigue haciendo falta.
- **Tiempo:** a la tarifa de [[amc-legal]] (USD 90/hr), el ahorro de USD 41/mes compra **27 minutos mensuales**. Armar una biblioteca son 40–80 horas iniciales (Q28,000–55,000 de costo de oportunidad). **Solo se justifica si ese tiempo es ocio disfrutado, no trabajo desplazado.**

---

## Rotación automática de media

Sí es posible. La herramienta es **Maintainerr** (gratis, open source, compatible con Plex/Jellyfin/Emby): lee el historial de reproducción, aplica reglas cada 8 horas, manda lo que califica a una colección visible "Leaving Soon", espera un período de gracia (ej. 14 días) y borra. Si alguien lo ve durante la gracia, el contador se reinicia.

**Advertencia:** exige correr Jellyfin + Radarr + Sonarr + Tautulli + Maintainerr — cinco servicios que mantener.

**Decisión tomada: no automatizar al inicio.** Comprando 14 TB no hace falta rotar por años. Por ~USD 100 más de disco se evita un sistema entero de mantenimiento. Si en dos años aprieta el espacio, se monta Maintainerr entonces.

> Nota: la regla intuitiva "borra la #1 cuando llegue la #16" es la peor versión — ordena por fecha de descarga y borraría películas que [[monica]] no ha visto. Las reglas correctas van por *visto + antigüedad*, con exclusión de watchlist y de una colección "Conservar".

---

## Gatillo de decisión

**No comprar hoy.** El payback contra iCloud solo (sin streaming) es de 10.7 años. Ejecutar cuando se cumpla **cualquiera** de estas:

1. **Cruzar los 2 TB reales** — iCloud salta al escalón de 6 TB (USD 29.99/mes = Q2,772/año) y el payback baja a 2.6 años
2. **[[amc-legal]] o [[propi]] necesitan repositorio compartido** con control de acceso por usuario
3. **Aparece tiempo de ocio real** para el media server, asumido como hobby y no como ahorro

---

## Plan por etapas (lo que sí hacer ya)

| Fase | Acción | Costo |
|---|---|---|
| **0** | Limpiar los 83 GB de `~/Downloads` | Q0 |
| **1** | Disco externo 4–6 TB + Time Machine en ambas Macs | ~Q900 |
| **2** | Mantener iCloud — Q924/año por sync sin fricción y off-site automático es barato | — |
| **3** | Comprar el NAS cuando se dispare el gatillo | ~Q9,000 |

La Fase 1 resuelve el 80% del riesgo real al 14% del costo del NAS.

---

## Consideración legal

[[propi]] es Persona Obligada con deber de conservación documental. Si el NAS llega a alojar expedientes, **el backup off-site deja de ser opcional**: un robo o incendio en casa dejaría a la entidad incumpliendo su obligación de conservar registros. Ver [[propi-aml-compliance]].

---

## Pendientes

- [ ] Confirmar planes reales de Netflix, Disney+ y Apple TV+ → actualiza el ahorro
- [ ] Cotizar proveedores de discos recertificados que envíen a Guatemala (precio + garantía)
- [ ] Cotizar envío por casillero y aduana real para cerrar el número exacto (hoy es ±27%)
- [ ] Medir consumo exacto de iCloud para saber qué tan cerca está del umbral de 2 TB

---

## Relacionado

- [[suscripciones]] — los gastos fijos que este proyecto atacaría
- [[amc-legal]] — la tarifa que define el costo de oportunidad
- [[propi]] — obligación de conservación documental
- [[wiki/index]]
