#!/usr/bin/env python3
"""Modelo de costo del menú semanal contra el presupuesto mensual de JR.

Presupuesto: Q3,500/mes de súper, **incluyendo** limpieza e higiene.
Eso deja el techo real de comida en Q3,500 − gastos de casa.

Uso:
    presupuesto.py                      # menú vigente
    presupuesto.py --res 3 --pollo 8    # simular otra mezcla de proteínas
"""

import argparse

PRESUPUESTO_MES = 3500
SEMANAS_MES = 4.345

# Precios verificados 2026-08-10. PS = PriceSmart, LT = La Torre, PZ = Paiz.
PRECIOS = {
    "pollo_lb":     (31.33, "PS filete pechuga 15 lb (Q469.95)"),
    "res_lb":       (38.73, "LT carne para asar económica"),
    "res_caro_lb":  (45.50, "PZ churrasco Don Cristóbal"),
    "molida_lb":    (38.45, "PS molida fresca 9.27 lb (Q368.74)"),
    "tilapia_lb":   (39.99, "PZ filete Costa Mar 1 lb — fresca"),
    "huevo_docena": (16.59, "PS Mister Huevo 60 u (Q82.95)"),
    "claras_l":     (58.00, "LT/PZ Granjazul líquida"),
    "frijol_lb":    (10.00, "estimado"),
    "arroz_lb":     (6.00,  "estimado"),
    "gama_paq":     (7.50,  "PZ Gama Salada Soda 192 g"),
    "sanissimo_paq": (15.00, "estimado"),
}

# Gramos por comida (crudo), suma de las dos porciones
G_POR_COMIDA = {"pollo": 453, "res": 420, "tilapia": 450}
LB = 453.59


def costo(res_comidas, pollo_comidas, ceviche_comidas, verdura_sem, fruta_sem, casa_mes,
          precio_res=None):
    p_res = precio_res if precio_res else PRECIOS["res_lb"][0]

    lb_res = res_comidas * G_POR_COMIDA["res"] / LB
    lb_pollo = pollo_comidas * G_POR_COMIDA["pollo"] / LB
    lb_tila = ceviche_comidas * G_POR_COMIDA["tilapia"] / LB

    lineas = [
        ("Res", lb_res, p_res, lb_res * p_res),
        ("Pollo", lb_pollo, PRECIOS["pollo_lb"][0], lb_pollo * PRECIOS["pollo_lb"][0]),
        ("Tilapia", lb_tila, PRECIOS["tilapia_lb"][0], lb_tila * PRECIOS["tilapia_lb"][0]),
        ("Huevos (3 doc)", 3, PRECIOS["huevo_docena"][0], 3 * PRECIOS["huevo_docena"][0]),
        ("Claras (0.7 L)", 0.7, PRECIOS["claras_l"][0], 0.7 * PRECIOS["claras_l"][0]),
        ("Frijol (2 lb)", 2, PRECIOS["frijol_lb"][0], 2 * PRECIOS["frijol_lb"][0]),
        ("Arroz (3 lb)", 3, PRECIOS["arroz_lb"][0], 3 * PRECIOS["arroz_lb"][0]),
        ("Galletas", 4, 11.25, 45.0),
    ]
    subtotal = sum(x[3] for x in lineas)
    semana = subtotal + verdura_sem + fruta_sem
    mes_comida = semana * SEMANAS_MES
    total_mes = mes_comida + casa_mes

    return lineas, subtotal, semana, mes_comida, total_mes


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--res", type=int, default=7, help="comidas de res por semana")
    ap.add_argument("--pollo", type=int, default=4)
    ap.add_argument("--ceviche", type=int, default=2)
    ap.add_argument("--verdura", type=float, default=200, help="Q/semana del verdulero")
    ap.add_argument("--fruta", type=float, default=130)
    ap.add_argument("--casa", type=float, default=800, help="Q/mes en limpieza e higiene")
    ap.add_argument("--precio-res", type=float, default=None)
    a = ap.parse_args()

    total_comidas = a.res + a.pollo + a.ceviche
    lineas, sub, sem, mes_com, total = costo(
        a.res, a.pollo, a.ceviche, a.verdura, a.fruta, a.casa, a.precio_res)

    print(f"Mezcla: {a.res} res · {a.pollo} pollo · {a.ceviche} ceviche = {total_comidas} comidas/semana")
    if total_comidas != 13:
        print(f"  ⚠ El plan necesita 13 comidas (14 menos la cena del martes). Faltan/sobran {13-total_comidas}.")
    print()
    print(f"{'Línea':<18} {'Cant':>7} {'Q/u':>8} {'Total':>9}")
    print("-" * 46)
    for n, c, p, t in lineas:
        print(f"{n:<18} {c:>7.2f} {p:>8.2f} {t:>9.2f}")
    print("-" * 46)
    print(f"{'Proteína+abarrotes':<18} {'':>7} {'':>8} {sub:>9.2f}")
    print(f"{'Verduras':<18} {'':>7} {'':>8} {a.verdura:>9.2f}")
    print(f"{'Frutas':<18} {'':>7} {'':>8} {a.fruta:>9.2f}")
    print(f"{'SEMANA':<18} {'':>7} {'':>8} {sem:>9.2f}")
    print()
    print(f"Comida al mes  ({SEMANAS_MES} sem)  Q{mes_com:>9,.2f}")
    print(f"Casa al mes                    Q{a.casa:>9,.2f}")
    print(f"TOTAL MES                      Q{total:>9,.2f}")
    print(f"PRESUPUESTO                    Q{PRESUPUESTO_MES:>9,.2f}")
    d = PRESUPUESTO_MES - total
    estado = "DENTRO" if d >= 0 else "EXCEDIDO"
    print(f"{estado:<18}             Q{abs(d):>9,.2f}  ({abs(d)/PRESUPUESTO_MES*100:.0f}%)")


if __name__ == "__main__":
    main()
