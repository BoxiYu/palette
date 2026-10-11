# 数学讲解视频调色板（三套配色，语义角色保持一致）
# 用法（mk3b.py 中）：
#   from palettes import JADE as P
#   config.background_color = P["BG"]
#   FG, C_A, C_B, C_C, C_HL, C_NO, C_DIM = (P[k] for k in ("FG","C_A","C_B","C_C","C_HL","C_NO","C_DIM"))

# 1. 草稿纸 Paper（浅色）：像彩色铅笔画在米色草稿纸上
PAPER = {
    "BG":    "#F7F3EA",  # 背景：米白草稿纸
    "FG":    "#1E2430",  # 主文字：墨黑
    "C_A":   "#2563A8",  # 第一个集合/对象：墨水蓝
    "C_B":   "#2F7D5B",  # 第二个集合：森林绿
    "C_C":   "#C2561F",  # 第三个集合：铁锈橙
    "C_HL":  "#FFD84D",  # 结论/交集：荧光笔黄，作为半透明底色(opacity≈0.55)放在文字/区域后面
    "C_HL_INK": "#B7860B",  # 荧光黄在浅底上太淡，描边/文字改用这个深金色
    "C_NO":  "#C0392B",  # 错误/排除：砖红
    "C_DIM": "#9AA0A8",  # 次要元素/网格/全集框：浅灰
}
PAPER_FILL_OPACITY = 0.30  # 韦恩图区域填充透明度（铅笔感）

# 2. 黑板 Chalkboard：墨绿黑板 + 粉笔色
CHALK = {
    "BG":    "#1E2B27",  # 背景：墨绿黑板
    "FG":    "#F1EEE4",  # 主文字：粉笔白
    "C_A":   "#F4A6B7",  # 第一个集合/对象：粉笔粉
    "C_B":   "#9AD9C8",  # 第二个集合：薄荷绿
    "C_C":   "#AFC3F2",  # 第三个集合：长春花蓝
    "C_HL":  "#FFE28A",  # 结论/交集/强调：粉笔黄
    "C_NO":  "#FF8C7A",  # 错误/排除：粉笔珊瑚红
    "C_DIM": "#6F7F79",  # 次要元素/网格/全集框：灰绿
}
CHALK_FILL_OPACITY = 0.38

# 3. 玉夜 Jade Night：深青夜色 + 玉石/杏/薰衣草
JADE = {
    "BG":    "#0E1A1C",  # 背景：深青夜色
    "FG":    "#E7F0EC",  # 主文字：月白
    "C_A":   "#35C3AE",  # 第一个集合/对象：玉绿
    "C_B":   "#F2A35E",  # 第二个集合：杏橙
    "C_C":   "#9C8CFF",  # 第三个集合：薰衣草紫
    "C_HL":  "#F6C945",  # 结论/交集/强调：暖金
    "C_NO":  "#EF5B5B",  # 错误/排除：朱红
    "C_DIM": "#5E6E6D",  # 次要元素/网格/全集框：青灰
}
JADE_FILL_OPACITY = 0.38

# 交集区域 HL 填充透明度：浅色 0.55；深色 0.80（0.6 左右在深底上会发灰发橄榄色）
HL_FILL_OPACITY = {"PAPER": 0.55, "CHALK": 0.80, "JADE": 0.80}

PALETTES = {"paper": PAPER, "chalk": CHALK, "jade": JADE}
