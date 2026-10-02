# Промпты для иконок HUSH HOLLOW

## Как пользоваться

1. Каждый промпт = **общий стиль** + **описание иконки**. Склейте их: сначала стиль, потом объект.
2. Сначала сгенерируйте **одну** иконку (например, лупу), пока она не понравится.
   Потом используйте её как образец стиля для всех остальных, чтобы набор был единым:
   - **Midjourney:** добавьте `--sref <ссылка на картинку>` и `--ar 1:1`
   - **ChatGPT / другие:** прикрепите картинку и напишите «in the exact same style as the attached icon»
3. **Фон.** ChatGPT умеет прозрачный фон: допишите `transparent background`.
   Другие генераторы рисуют на белом фоне: уберите его через remove.bg или Photopea.
4. Сохраните PNG **512×512** под именем из таблицы и загрузите в папку `assets/icons/` репозитория.

---

## Общий стиль (вставлять в начало каждого промпта)

```
Glossy 3D cartoon game icon in the style of popular Roblox simulator games, chunky rounded exaggerated shapes, thick dark navy outline around the whole object, bright saturated colors, soft cel shading with strong white highlights and rim light, subtle bevel, toy-like plastic feel, single object centered with padding, slight three-quarter view, isolated on a plain white background, no text, no letters, no logo, no background scene, crisp clean edges, high quality game asset, 1:1
```

---

## Роли

| Файл | Объект (дописать после стиля) |
|---|---|
| `role_detective.png` | `a big magnifying glass with a golden rim, light blue glass with a shiny reflection, short brown wooden handle` |
| `role_guardian.png` | `a heroic blue shield with a golden border and a small white star in the center` |
| `role_observer.png` | `a large cartoon eye with a purple iris, surrounded by a soft glowing aura, slightly mysterious` |
| `role_deceiver.png` | `a sneaky dark red theater mask with narrow eyes and a sly grin, small purple smoke wisps` |
| `role_neutral.png` | `a playful jester hat in yellow and purple with golden bells` |
| `role_citizen.png` | `a cozy small cartoon house with a red roof, warm glowing window and a chimney` |

## Стороны (значки фракций)

| Файл | Объект |
|---|---|
| `faction_innocent.png` | `a round green badge emblem with a white heart in the center, golden rim` |
| `faction_deceiver.png` | `a round red badge emblem with a black dagger silhouette in the center, dark rim` |
| `faction_neutral.png` | `a round yellow badge emblem with a purple question mark in the center, golden rim` |

## Фазы игры

| Файл | Объект |
|---|---|
| `phase_night.png` | `a golden crescent moon with small craters and two tiny sparkling stars` |
| `phase_day.png` | `a bright smiling cartoon sun with thick rounded rays` |
| `phase_discussion.png` | `two overlapping speech bubbles, one white and one light blue, with three dots inside` |
| `phase_vote.png` | `a blue ballot box with a white paper ballot with a green checkmark sliding into the slot` |
| `timer.png` | `a wooden hourglass with glowing golden sand` |

## Статусы

| Файл | Объект |
|---|---|
| `status_eliminated.png` | `a cute cartoon skull, ivory white, big black eye holes, not scary, friendly game style` |
| `status_alive.png` | `a glossy red heart with a white shine` |
| `status_protected.png` | `a glowing translucent blue bubble shield with sparkles` |
| `check.png` | `a fat green checkmark inside a round green button` |
| `close.png` | `a fat white X inside a square red button with rounded corners` |
| `lock.png` | `a golden padlock, closed, with a dark keyhole` |

## Итоги матча

| Файл | Объект |
|---|---|
| `victory_trophy.png` | `a shiny golden trophy cup with two handles on a dark wooden base, sparkles around it` |
| `victory_star.png` | `a fat glossy golden star with a shine` |
| `defeat.png` | `a cracked grey broken heart with a small rain cloud above it` |
| `crown.png` | `a golden royal crown with red and blue gems` |

## Валюта и меню

| Файл | Объект |
|---|---|
| `coin.png` | `a single thick golden coin with a star embossed in the center, seen at a slight angle` |
| `coins_pile.png` | `a small pile of shiny golden coins` |
| `shop.png` | `a red gift box with a big yellow ribbon bow` |
| `outfit.png` | `a yellow cartoon t-shirt on a small hanger` |
| `emotes.png` | `a big round yellow smiley face laughing with closed eyes` |
| `guide.png` | `an open purple book with glowing pages and a small bookmark` |
| `settings.png` | `a chunky grey metal gear with a blue center` |
| `players.png` | `two simple blocky cartoon character heads side by side, one blue one orange` |

---

## Логотип игры (отдельно)

Лучше генерировать в ChatGPT или Ideogram: они нормально пишут текст.

```
Game logo for a Roblox game called "HUSH HOLLOW", big chunky bubbly 3D letters, yellow to orange gradient fill, thick dark navy outline, glossy highlights on top of each letter, slightly tilted playful layout, a small crescent moon and a cute cartoon house integrated into the letters, mysterious but friendly, isolated on a plain white background, high quality mobile game logo
```

## Фоны для экранов (по желанию)

```
Stylized cartoon Roblox-style small cozy town at night, colorful rounded houses with glowing windows, central plaza with a fountain, street lamps, big crescent moon, soft purple and blue lighting, simple clean shapes, game background, no characters, no text, 16:9
```

То же самое для дня: замените `at night` → `on a sunny morning`, `glowing windows` → `bright windows`, `purple and blue lighting` → `warm golden lighting`, `big crescent moon` → `blue sky with fluffy clouds`.
