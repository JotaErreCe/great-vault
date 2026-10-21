---
type: project
date: 2026-10-20
tags: [understanding-kids, finanzas, costos, precios]
---

# Finanzas de UK: costo real, caja y criterios

Base de números que arma el agente `finanzas-uk` (ver [[agentes/claude/subagentes]]). Detalle y fórmulas fuera del Vault: `~/Claude/pendiente-vault/finanzas-uk/` (`criterios.md`, `costo-real-2026/`, `utilidad-vs-efectivo-2026/`).

## Reglas de JR (20-oct-2026)
- Dos sedes: zona 14 y CAES (= Carretera a El Salvador). Mismos precios ([[understanding-kids]]).
- Régimen General de IVA (12%) e ISR sobre utilidades (25%).
- Gastos compartidos entre sedes por % de clientes de cada sede.
- Margen mínimo 20% = (Precio − Costo) / Precio.
- El vehículo de 2025 se separa de la operación.

## Hallazgos (ene-sep 2026; criterios sin aprobar del todo)
- **Las terapeutas son pequeño contribuyente:** su IVA no se acredita.
- **Fijo por sesión:** zona 14 Q246.71, CAES Q220.22, contando el pago de Magoo como dirección. Sin ese pago: Q184 y Q179.
- **Margen a precio de lista:** ninguna terapia llega a 20%. Zona 14: Q350 −21%, Q400 −6%. CAES: Q400 +1%. Margen de contribución (después de la terapeuta): 58% a 63%.
- **Caja:** Q205,750 (dic-2025) contra Q193,137 (sep-2026). La sostienen la formación (unos Q20k al mes de subsidio a la clínica) y el colchón de 2025 (unos USD 19k). El puente utilidad-caja de ene-jun cuadra a Q0 con el contador.
- **Riesgos de caja:** IVA en efectivo desde sep-2026 (se acabó el crédito del carro), aguinaldo de dic (unos Q14.8k), cuota del carro Q4,233 al mes.
- **Pendientes con el contador:** cómo se arma el pago de Magoo (sueldo más facturas de gastos personales, con riesgo fiscal); los intereses del préstamo del carro no se deducen; estados financieros de jul-sep.
- **La publicidad de Facebook entre sedes NO está duplicada:** es una factura partida 50/50.

## Relacionado
- [[understanding-kids]] · [[agentes/claude/subagentes]]
- **Pago de Magoo (criterio aprobado por JR, 21-oct-2026):** los ~Q20k/mes son su sueldo de directora y **cuentan como costo de la clínica** para precios (costo fijo por sesión zona 14 ~Q247). Mecánica: se cubre en parte con facturas de gastos personales que entran como reembolso, no como sueldo, para no generar pasivo laboral. Para el costeo se toma el total, sin importar la forma de pago; el riesgo fiscal de la mecánica sigue pendiente con el contador.
- **Talleres y diplomados (JR, 21-oct-2026):** los presenciales usan la clínica y absorben parte de renta y gastos; los en línea o pregrabados no. Lista a confirmar con JR.
- **Colchón en USD (~USD 19k, de 2025)** (JR, 21-oct-2026): es todo a la vez: dinero de los socios pensado para invertir en algún porcentaje (aún no se ha hecho) y reserva para meses bajos. En el análisis va separado de la caja operativa, como reserva disponible.
- **Préstamo de apertura de la clínica** (JR, 21-oct-2026): lo sacaron JR y Magoo para abrir la clínica la primera vez. Tasa del 25%. Saldo aproximado Q29,000; termina en julio de 2027. Es aparte del préstamo del carro. La cuota sale de las cuentas de UK por transferencia a la cuenta personal de JR, que paga el banco. Está a nombre de JR. La transferencia de UK a JR es solo la cuota (sin mezclar con sueldo ni reembolsos); el monto lo saca finanzas-uk de los estados de cuenta. Tratamiento: pago de deuda (capital + interés), no gasto de operación.
- **Decisión JR (21-oct-2026):** no perseguir tasa ni plazo de los préstamos; trabajar con las cuotas que salen en los estados de cuenta (p. ej. Q4,233/mes del carro) como pago de deuda.
- **Préstamo G&T del vehículo, condiciones (JR, 21-oct-2026):** financiado Q220,054.50 (Q216,900 vehículo + Q175 administración + Q2,979.50 gastos legales); enganche Q100,000; 84 meses; tasa nominal 8.50% fija (TAE 8.84%). Cuota calculada de capital + interés: Q3,484.89/mes. Lo que sale de la cuenta (~Q4,233) incluiría otros cargos (p. ej. seguro), por confirmar en estados de cuenta.
- **Préstamo G&T del vehículo:** el contrato firmado no está digitalizado (búsqueda completa en el Drive de las dos cuentas y en el Vault, 21-oct-2026). Sí están el acta de asamblea y el acta notarial del 17-oct-2025 (Mitsubishi, crédito G&T con garantía mobiliaria y fiduciaria, sin plazo ni tasa), los formularios en `Documentos contables…/08 Créditos y formularios bancarios/2025` y los comprobantes de pago en el correo (p. ej. Q3,346.57 el 4-dic-2025).

## Costo real 12 meses, v3 (oct-2025 a sep-2026; 21-oct-2026)
- Reglas de JR (21-oct): dirección Q16,653.43/mes (Q20k menos la cuota de apertura), 100% a terapias; publicidad de Meta de cada diplomado es costo directo del diplomado; plataforma repartida por lo que factura cada línea (62.6% terapias); talleres presenciales usan la clínica, los en línea no.
- Fijo por sesión neto de IVA: Z14 Q295.36, CAES Q297.60 (techo: incluye toda la publicidad de Meta, que no se puede separar por campaña en el período; piso sin Meta: Z14 Q267.22, CAES Q277.86).
- Precio mínimo para 20% con IVA: Q250 → ~Q537-540; Q350/Q400 → Q598-601 (piso Q559-574). Terapias y evaluaciones: −Q273k en 12 meses (piso −Q214k); la formación cobró Q422.5k con IVA.
- Carro: débito ~Q4,233 = cuota G&T Q3,470.57 + seguro Q762.94. El contador no registra el interés (~Q13.5k ene-sep, ~Q3.4k de ISR) y registra el préstamo en Q316k.
- Entregables: `~/Claude/pendiente-vault/finanzas-uk/costo-real-12m/` (resumen, anexo, xlsx, PDF v3).
- Decisión JR (21-oct-2026): no se baja el detalle de Meta por campaña; se trabaja con el rango techo-piso para precios.

## Modelo financiero propio (aprobado por JR, 21-oct-2026)
- Los estados del contador tienen errores conocidos (interés del carro, préstamo en Q316k, cobrado vs facturado, anticipos de Mónica): UK lleva sus propios libros (Libro Diario en partida doble → Mayor → Balanza → Balance, Resultados, Flujo) y cuadra con el contador cada trimestre.
- Google Sheet «UK - Modelo Financiero» en el Drive de la clínica, privado para JR, todo con fórmulas y supuestos editables. Primero se arma; la automatización viene después.
- Indicadores aprobados y descartados: `~/Claude/pendiente-vault/finanzas-uk/modelo-financiero/propuesta-v1.md` (sin Estado de Cambios en el Patrimonio ni Notas; sin ROIC, AOV, ratios de deuda redundantes ni de marketplace/inmobiliario/inventario).
