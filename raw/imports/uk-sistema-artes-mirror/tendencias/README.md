# Ledger de tendencias

Estado que el agente `uk-tendencias-virales` guarda **entre corridas**. Sin esto, cada corrida arranca ciega y solo puede ver una foto de 7 días; con esto puede ver la **pendiente** (un ángulo que estaba en 1 cuenta y ahora está en 4), que es lo que permite llegar temprano.

## Archivos

- **`posts.csv`** — historial de posts vistos. Una fila por post: `cuenta, shortcode, fecha, tipo, likes, comentarios`. Tipo: `V` reel, `S` carrusel, `I` estático. `likes = -1` significa que la cuenta oculta los likes.
- **`angles.jsonl`** — un ángulo o formato por línea, con las cuentas donde se fue viendo y la fecha del primer avistamiento. Es el detector de convergencia.
- **`ledger.py`** — consultas sobre lo anterior.

## Comandos

```bash
python3 ledger.py stats
```
Baseline por cuenta: mediana de likes y comentarios, % de contenido estático, días desde el último post. Marca cuentas **INACTIVAS** (>60 días) y clasifica cada una como fuente de **ÁNGULOS** o de **FORMATOS**.

```bash
python3 ledger.py outliers 10
```
Posts de los últimos N días que superan **2× la mediana de su propia cuenta**. Comparar likes crudos entre cuentas no sirve: 1,200 likes es flojo para paupautista y enorme para alimento.red. Si la cuenta oculta los likes, usa comentarios.

```bash
python3 ledger.py angles
```
Estado de cada ángulo: `CONVERGE` (3+ cuentas), `emergente` (2), `aislado` (1). Los aislados son los que hay que vigilar — si pasan a 2 o 3, ahí está la señal temprana.

```bash
python3 ledger.py nuevos <archivo.csv>
```
Qué shortcodes de un barrido nuevo no estaban en el ledger.

## Mantenimiento

Cada corrida: agregar las filas nuevas a `posts.csv` y actualizar `angles.jsonl` (sumar cuentas a un ángulo existente, o abrir uno nuevo). El campo `sugerido_en_notion` evita volver a sugerir lo mismo con otro nombre.
