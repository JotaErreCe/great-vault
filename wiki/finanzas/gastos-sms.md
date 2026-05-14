---
type: resource
date: 2026-05-07
last-touched: 2026-05-07
tags:
  - finanzas
  - tema/gastos
  - fuente/sms
---

# Gastos por SMS

Análisis agregado de consumos detectados en SMS bancarios locales. No guardar SMS crudos, credenciales ni números completos de cuenta; solo agregados y decisiones.

---

## Corte 2026-05-07 — Banco GTC

Fuente: SMS locales de Banco GTC / BancoGTC, consumos de tarjeta de crédito. Cobertura principal: cargos con formato `Consumo tarjeta credito`. No incluye efectivo, transferencias, cargos sin SMS ni otros bancos si no aparecen con formato parseable.

Archivo generado:

- `/Users/jr/.openclaw/workspace/outputs/geoffrey-analisis-gastos-sms-2026-05-07.pptx`

### Resumen

| Métrica | Valor |
|---------|------:|
| Rango | 2025-08-14 a 2026-05-07 |
| Transacciones | 742 |
| Total GTQ | Q190,581.76 |
| Total USD | USD 12,606.67 |
| Promedio mensual completo aprox. | Q21,656.21 + USD 1,481.96 |

Promedio mensual calculado sobre meses completos sep 2025–abr 2026; mayo 2026 es parcial.

### Rubros GTQ principales

| Rubro | Total | Cargos |
|-------|------:|------:|
| Comida / supermercado | Q51,899.33 | 172 |
| Otros | Q42,127.80 | 201 |
| Salud / seguros | Q27,849.84 | 27 |
| Hogar / muebles | Q27,545.50 | 20 |
| Transporte / carro | Q11,387.37 | 51 |
| Mascotas | Q7,022.05 | 13 |
| Servicios / telecom | Q6,750.91 | 18 |
| Educación | Q5,964.00 | 1 |

### Rubros USD principales

| Rubro | Total | Cargos |
|-------|------:|------:|
| Compras online | USD 6,087.55 | 26 |
| Otros | USD 2,804.22 | 70 |
| Salud / seguros | USD 894.06 | 2 |
| Viajes | USD 845.08 | 1 |
| Suscripciones / digital | USD 747.69 | 67 |
| Comida / supermercado | USD 663.32 | 14 |
| Transporte / carro | USD 471.24 | 10 |

### Métodos de pago detectados

Inferido desde el texto del SMS.

| Método | GTQ | Cargos GTQ | USD | Cargos USD |
|--------|----:|-----------:|----:|-----------:|
| Tarjeta física / no especificado | Q105,758.19 | 190 | USD 3,567.91 | 68 |
| Apple Pay | Q78,218.66 | 331 | USD 1,806.47 | 41 |
| Online / cargo recurrente | Q6,604.91 | 24 | USD 7,232.29 | 88 |

### Tarjetas / cuentas por últimos 4 dígitos

Detalle movido a `_sensitive.md`. Mantener fuera del wiki operativo para no exponer identificadores financieros.

---

## Criterio de mejora

- Separar gastos extraordinarios de gastos operativos mensuales: hogar/muebles, salud, educación y viajes no deben leerse igual que supermercado/comida.
- Priorizar control semanal sobre comida/supermercado, porque combina monto alto y frecuencia alta.
- Auditar suscripciones y cargos online mensualmente; muchos cargos pequeños se vuelven invisibles.
- Mantener Apple Pay por seguridad, pero monitorear su total semanal por la facilidad con que reduce fricción de gasto.
- Si Master JR lo aprueba, Geoffrey puede generar reporte mensual automático desde SMS nuevos.

## Relacionado

- [[finanzas]]
- [[egresos]]
- [[suscripciones]]
- [[patrimonio]]
