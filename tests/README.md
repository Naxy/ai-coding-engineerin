# 技术栈冒烟测试

这些 fixture 是独立、最小化的工程样例，用来验证专项规范涉及的关键工具链能否安装、类型检查、编译和运行基础测试。它们不是完整业务系统，也不能单独证明模型行为符合 Skill。

| 技术栈 | 验证内容 |
|---|---|
| Java / Spring Boot | Maven 编译、JUnit、BigDecimal 金额与参数边界 |
| Go | go test、go vet、race detector、错误与溢出边界 |
| Python | pytest、Decimal 精度、异常边界 |
| Vue 3 | vue-tsc 类型检查、Vite 生产构建 |
| React + antd 5 | TypeScript 构建、React Hooks、Form、Table、Modal 与 antd 5 API |

CI 工作流会在每次 Skill 分支变更时运行上述检查。

除技术栈冒烟测试外，仓库还记录了脱敏真实项目验证，见[真实项目验证记录](REAL-PROJECT-VALIDATION.md)。该记录与 fixture 冒烟测试分开统计，不代表生产级验收。
