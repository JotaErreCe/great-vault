---
type: resource
date: 2026-10-19
tags: [resource, tema/hogar, interiores]
fuente: agente interiores de Claude, 2026-10-18
estado: propuesta v1 (sin verificar si JR la aprobó)
---

# Sala principal: propuesta de interiores v1

Propuesta del agente `interiores` ([[agentes/claude/subagentes]]) para amueblar la sala de la [[casa-canada-de-elgin|casa nueva]]: estilo **colonial guatemalteco actualizado** (madera, textiles típicos, tonos tierra, líneas simples), **sin TV**, esquinas redondeadas y reja frente a la chimenea por [[nicolas|Nico]], un solo conjunto contra la pared blanca y el paso junto a la piedra libre. Está escrita como prompt para generar la imagen con ChatGPT (gpt-image) sobre la foto real.

> Copiada de `~/Claude/pendiente-vault/interiores/sala/prompt-chatgpt-sala-v1.md` (rutas completadas). Los planos (PNG) y la foto quedan fuera del Vault: [[mapa-de-archivos]] § Casa nueva. **(sin verificar):** si JR aprobó el estilo y la distribución; las medidas de los muebles son de la propuesta, no de JR.

**Foto que hay que adjuntar:** `~/Claude/pendiente-vault/fotos-casa-nueva/sala-01.jpg` (una sola, la original y no una captura).
Está tomada desde los arcos y mira hacia la chimenea. En ella se ven la chimenea de esquina, la pared
blanca larga donde va el conjunto, la entrada del vestíbulo, el pasillo junto a la piedra y el pilar
de piedra del escalón. Es justo la zona que se amuebla.

**Distribución base:** `~/Claude/pendiente-vault/interiores/sala/plano-sala-amueblado-v1.png`.

---

## Prompt principal (copiar y pegar tal cual)

```
Edit this exact photo of an empty living room. Keep the architecture 100% identical: the rough stone wall with red brick accents and the stone and brick pillar in the left foreground, the dark wood parquet floor, the white corner fireplace with its brick chimney and brick hearth, the white walls, the ceiling, the crown moldings, the dark baseboards, the ceiling light fixtures, every wall outlet, the doorway and hallway in the back left that leads to the entrance, the brick arch edge on the right, and the tiled floor visible on the far right. Do not add or remove windows, doors or arches. Do not change the camera position, perspective, lens or framing. Keep the same aspect ratio. Remove the measuring tape from the floor.

Furnish the room in an updated Guatemalan colonial style: warm natural wood, hand-woven Guatemalan textiles, earth tones (terracotta, ochre, cream, deep red, indigo accents), simple clean-lined furniture. No TV. A toddler lives here, so all furniture has rounded corners and nothing looks tippy.

Place the furniture as one seating group in the right half of the room, along the long white wall on the right:
1. Sofa: a three-seat sofa about 2 m long and 90 cm deep, with straight lines, low rounded arms and solid wood legs, upholstered in a cream or oatmeal woven fabric. It sits closest to the camera on the right side, standing free in the room with its BACK toward the camera, running from the white wall toward the middle of the room, facing the fireplace.
2. Two armchairs: a matching pair of wooden armchairs with cushioned seats in a terracotta or rust handwoven Guatemalan fabric, each about 70 cm wide. They stand farther back along the white wall, about 2 m in front of the fireplace wall, side by side, facing the sofa and the camera, with their backs toward the fireplace.
3. Between the two armchairs: a small round solid wood side table, about 40 cm across.
4. Coffee table: an oval solid wood coffee table, about 1 m by 55 cm, low, centered between the armchairs and the sofa, with a woven basket and a small stack of books on it.
5. Another small round wood side table, about 45 cm across, at the left end of the sofa (the end that points toward the middle of the room).
6. Rug: a flat handwoven wool rug in natural cream, brown and terracotta stripes, about 1.8 m by 2.7 m, under the whole seating group, ending well before the area in front of the fireplace.
7. Throw pillows on the sofa in colorful Guatemalan woven textile (jaspe style), and a folded woven throw on one armchair.
8. On the white wall above the armchairs and coffee table: one large framed Guatemalan textile (huipil style), about 1.4 m wide, flanked by two wrought iron wall sconces.
9. A decorative carved wooden column covered in gold leaf, in the Antigua Guatemala colonial style, about the height of a person, standing on the floor against the face of the stone pillar in the left foreground, close to the left edge of the image.
10. In front of the fireplace: a black metal child safety gate that encloses the hearth at about 60 cm from the firebox opening. Leave at least 90 cm of empty floor in front of the fireplace, with no rug and no furniture there. A few simple items on the mantel: two iron candleholders and a clay pot.

Keep the circulation clear: the floor along the stone wall on the left, from the back hallway to the camera, stays completely empty, and the floor in the foreground stays open so there is a clear path toward the camera. Nothing blocks the hallway or the arch.

Photorealistic interior photography, soft natural daylight, realistic shadows and reflections on the parquet, realistic scale. No people, no animals, no text, no watermark.
```

---

## Traducción breve para JR

Edita esta foto de la sala vacía sin tocar la arquitectura: pared de piedra con ladrillo, pilar de
piedra, parquet, chimenea de esquina, paredes blancas, techo, molduras, enchufes, el pasillo del fondo
y el arco. Sin agregar ni quitar ventanas, puertas ni arcos, y sin cambiar el encuadre. Quita la cinta
métrica.

Estilo colonial guatemalteco actualizado, madera, textiles típicos, tonos tierra, líneas simples, sin
TV y con esquinas redondeadas por Nico. Un solo conjunto contra la pared blanca de la derecha: el sofá
de 2 m más cerca de la cámara, de espaldas a ella y mirando a la chimenea; dos butacas de madera con
tela terracota junto a la chimenea, mirando al sofá, con una mesita redonda entre ellas; una mesa de
centro ovalada de madera; otra mesita junto al sofá; una alfombra de lana tejida de 1.80 × 2.70 m
debajo del conjunto; cojines típicos; un textil enmarcado con dos apliques de hierro en la pared
blanca; la columna antigüeña dorada junto al pilar de piedra de la izquierda; una reja de seguridad
frente a la chimenea y 90 cm libres delante de ella. El paso junto a la piedra, libre. Foto realista,
luz natural, sin personas.

---

## Prompts cortos de corrección (si algo sale mal)

Pegar en el mismo chat, después de la imagen que salió mal.

1. Si cambió la arquitectura:
```
Keep this furniture, but restore the architecture exactly as in the original photo: the same rough stone wall with brick accents, the same stone pillar, the same corner fireplace and brick chimney, the same parquet, ceiling, moldings and outlets. Do not add windows or doors. Same camera angle and framing as the original.
```

2. Si tapó el paso o metió muebles junto a la piedra:
```
Move all furniture to the right half of the room, along the white wall. The floor along the stone wall on the left and the path from the back hallway toward the camera must be completely empty. Keep 90 cm of empty floor in front of the fireplace.
```

3. Si la escala o el estilo se fueron (muebles enormes, demasiado modernos o recargados):
```
Make the furniture smaller and true to scale: the sofa is 2 m long, the armchairs 70 cm wide, the oval coffee table 1 m long. Simple clean-lined solid wood pieces in an updated Guatemalan colonial style, warm earth tones, handwoven Guatemalan textiles. Rounded corners, no glass, no metal legs.
```

## Relacionado

- [[casa-canada-de-elgin]] · [[casa-canada-de-elgin/electrodomesticos]] · [[agentes/claude/subagentes]] · [[mapa-de-archivos]]
