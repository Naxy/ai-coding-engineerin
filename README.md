# AI Coding Engineering

中文优先、风险驱动、面向日常软件研发的 AI Coding 工程规范。

## 能力
- 自动选择 Quick / Standard / High-Risk，并在风险升高时升级。
- 覆盖需求理解、项目认知、设计、拆解、实现、审查、测试和交付。
- 按需加载 Java / Spring Boot、Go、Python、Vue、React + Ant Design 5 专项规范。
- 强调最小必要修改、真实验证、保护用户改动和高风险操作授权。

## 安装
将本仓库作为 Skill 来源，按目标 AI Coding Agent 的 Skill 安装机制放入其 skills 目录。确保目录名为 `ai-coding-engineering`，并保留 `SKILL.md` 与 `references/` 的相对路径。不同 Agent 的发现路径和元数据要求可能不同，请以其当前版本文档为准。安装后可让 Agent 说明已识别的 Skill 名称与触发范围。

## 使用示例
- “自动判断模式，帮我修复这个 Bug。”
- “按 Standard 模式开发订单查询接口。”
- “按 High-Risk 模式评估数据库迁移，先给方案，不执行。”
- “只做代码审查，不修改代码。”

## 目录
- `SKILL.md`：核心规则与模式调度。
- `references/quality-gates.md`：阶段质量门禁。
- `references/code-smells.md`：常见代码坏味道。
- `references/prompt-patterns.md`：协作提示词模板。
- `references/workflows.md`：常见研发工作流。
- `references/backend/`：Java、Go、Python 专项规范。
- `references/frontend/`：前端通用、Vue、React + Ant Design 5 专项规范。
- `scripts/validate_skill.py`：结构与引用检查。
- `.github/workflows/validate-skill.yml`：自动校验。

## 版本与状态
当前版本为 V1.0.0。结构校验与技术栈冒烟测试已纳入 GitHub Actions；测试范围和已知限制见 [技术栈实测报告](tests/TEST-REPORT.md)。实际使用时仍需以目标项目的技术版本、工程约定和验证结果为准。
