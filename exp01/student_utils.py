"""实验4 的解析工具模块。"""


def parse_student(line):
    """把一行 'name,score' 解析成字典；无效记录抛 ValueError。"""
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(fields)}")
    name, score_text = fields[0].strip(), fields[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_text)
    except ValueError as exc:
        raise ValueError(f"成绩不是整数: {score_text!r}") from exc
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
