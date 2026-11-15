#!/usr/bin/env python3
"""Validate the repository structure and local Markdown references for the Skill."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "references/quality-gates.md",
    "references/code-smells.md",
    "references/prompt-patterns.md",
    "references/workflows.md",
    "references/backend/java-spring.md",
    "references/backend/go.md",
    "references/backend/python.md",
    "references/frontend/frontend-common.md",
    "references/frontend/vue.md",
    "references/frontend/react-antd5.md",
]
errors = []

for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"缺少必需文件：{relative}")
    elif not path.read_text(encoding="utf-8").strip():
        errors.append(f"文件为空：{relative}")

skill_path = ROOT / "SKILL.md"
if skill_path.is_file():
    skill = skill_path.read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        errors.append("SKILL.md 缺少 YAML frontmatter")
    else:
        frontmatter = skill.split("---", 2)[1]
        for key in ("name:", "description:"):
            if key not in frontmatter:
                errors.append(f"SKILL.md frontmatter 缺少 {key}")
    if "Quick" not in skill or "Standard" not in skill or "High-Risk" not in skill:
        errors.append("SKILL.md 未完整定义三种执行模式")

# Validate relative Markdown links, ignoring external URLs and anchors.
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target):
            continue
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{md.relative_to(ROOT)} 引用了不存在的路径：{target}")

if errors:
    print("Skill 校验失败：")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Skill 校验通过：{len(REQUIRED)} 个必需文件存在，Markdown 本地链接有效。")
