# palette

数学讲解视频的三套配色，每套的颜色角色一致，可以直接换用。

- **草稿纸**：浅色，适合题目讲解。
- **黑板**：深墨绿，课堂感。
- **玉夜**：深青色，适合代码和技术类内容。

## 草稿纸 Paper

| 角色 | 变量 | 色值 |
|---|---|---|
| 背景 | `BG` | ![](https://placehold.co/14x14/F7F3EA/F7F3EA.png) `#F7F3EA` |
| 主文字 | `FG` | ![](https://placehold.co/14x14/1E2430/1E2430.png) `#1E2430` |
| 对象 A | `C_A` | ![](https://placehold.co/14x14/2563A8/2563A8.png) `#2563A8` |
| 对象 B | `C_B` | ![](https://placehold.co/14x14/2F7D5B/2F7D5B.png) `#2F7D5B` |
| 对象 C | `C_C` | ![](https://placehold.co/14x14/C2561F/C2561F.png) `#C2561F` |
| 结论 / 强调 | `C_HL` | ![](https://placehold.co/14x14/FFD84D/FFD84D.png) `#FFD84D` |
| 强调描边（浅底用） | `C_HL_INK` | ![](https://placehold.co/14x14/B7860B/B7860B.png) `#B7860B` |
| 错误 / 排除 | `C_NO` | ![](https://placehold.co/14x14/C0392B/C0392B.png) `#C0392B` |
| 次要 / 网格 | `C_DIM` | ![](https://placehold.co/14x14/9AA0A8/9AA0A8.png) `#9AA0A8` |

## 黑板 Chalkboard

| 角色 | 变量 | 色值 |
|---|---|---|
| 背景 | `BG` | ![](https://placehold.co/14x14/1E2B27/1E2B27.png) `#1E2B27` |
| 主文字 | `FG` | ![](https://placehold.co/14x14/F1EEE4/F1EEE4.png) `#F1EEE4` |
| 对象 A | `C_A` | ![](https://placehold.co/14x14/F4A6B7/F4A6B7.png) `#F4A6B7` |
| 对象 B | `C_B` | ![](https://placehold.co/14x14/9AD9C8/9AD9C8.png) `#9AD9C8` |
| 对象 C | `C_C` | ![](https://placehold.co/14x14/AFC3F2/AFC3F2.png) `#AFC3F2` |
| 结论 / 强调 | `C_HL` | ![](https://placehold.co/14x14/FFE28A/FFE28A.png) `#FFE28A` |
| 错误 / 排除 | `C_NO` | ![](https://placehold.co/14x14/FF8C7A/FF8C7A.png) `#FF8C7A` |
| 次要 / 网格 | `C_DIM` | ![](https://placehold.co/14x14/6F7F79/6F7F79.png) `#6F7F79` |

## 玉夜 Jade Night

| 角色 | 变量 | 色值 |
|---|---|---|
| 背景 | `BG` | ![](https://placehold.co/14x14/0E1A1C/0E1A1C.png) `#0E1A1C` |
| 主文字 | `FG` | ![](https://placehold.co/14x14/E7F0EC/E7F0EC.png) `#E7F0EC` |
| 对象 A | `C_A` | ![](https://placehold.co/14x14/35C3AE/35C3AE.png) `#35C3AE` |
| 对象 B | `C_B` | ![](https://placehold.co/14x14/F2A35E/F2A35E.png) `#F2A35E` |
| 对象 C | `C_C` | ![](https://placehold.co/14x14/9C8CFF/9C8CFF.png) `#9C8CFF` |
| 结论 / 强调 | `C_HL` | ![](https://placehold.co/14x14/F6C945/F6C945.png) `#F6C945` |
| 错误 / 排除 | `C_NO` | ![](https://placehold.co/14x14/EF5B5B/EF5B5B.png) `#EF5B5B` |
| 次要 / 网格 | `C_DIM` | ![](https://placehold.co/14x14/5E6E6D/5E6E6D.png) `#5E6E6D` |

## 用法（Manim）

```python
from palettes import PAPER as P
config.background_color = P["BG"]
C_A, C_B, C_C = P["C_A"], P["C_B"], P["C_C"]
```

也可以读 `palette.json`。
