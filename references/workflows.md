# 常见研发工作流

- 新功能：需求与验收 → 项目调查 → 方案 → 拆解 → 实现测试 → diff 审查 → 交付。
- Bug：复现 → 根因定位 → 失败测试 → 最小修复 → 回归 → 副作用检查。
- 重构：明确行为不变边界 → 特征测试 → 小步重构 → 每步验证；避免与新功能混在大 diff。
- 代码审查：只读检查 → 按严重度排序 → 位置、条件、影响、建议；用户要求只审查时不修改。
- 数据库变更：High-Risk；评估数据量、锁、兼容窗口、备份、迁移和回滚；执行前确认环境和授权。
- Java：读取 backend/java-spring.md，识别 JDK、Spring、ORM 和构建工具版本。
- Go：读取 backend/go.md，识别 Go 版本、模块、并发和错误处理约定。
- Python：读取 backend/python.md，识别 Python 版本、虚拟环境、依赖管理和框架。
- Vue：读取 frontend/vue.md 与 frontend/frontend-common.md，识别主版本、状态管理和组件库。
- React + antd：读取 frontend/react-antd5.md 与 frontend/frontend-common.md，核实 React、TS、antd 版本及状态管理。
