# 技术栈实测报告

- 测试分支：`feat/ai-coding-engineering-v1`
- 测试提交：`cb58c4464b0fdc77f79662ed90ae18b769134137`
- 执行环境：GitHub Actions / Ubuntu latest
- 总体结果：5 个技术栈冒烟任务全部通过；Skill 结构校验通过。

## 结果

| 技术栈 | 实际执行 | 结果 |
|---|---|---|
| Java 17 / Spring Boot 3.3.5 | `mvn verify`；JUnit 覆盖金额精度、负数参数、空值 | 通过 |
| Go 1.22 | `go test ./...`、`go vet ./...`、`go test -race ./...`；覆盖正常、负数和溢出 | 通过 |
| Python 3.12 | `pytest`；覆盖 Decimal 金额舍入和非法输入 | 通过 |
| Vue 3.5 / TypeScript | `vue-tsc -b`、`vite build` | 通过 |
| React 18 / TypeScript / antd 5.22 | `tsc -b`、`vite build`；编译检查 Hooks、Form、Table、Modal 的组合用法 | 通过 |

## 测试过程中修复的问题

1. Vue 示例的 Vite 与 `@vitejs/plugin-vue` peer dependency 不兼容，已统一到兼容版本。
2. React 示例缺少 `tsconfig.app.json`，已补齐。
3. React/Vue 示例调整了 Vite 版本，避免使用不匹配的插件组合。

修复后，最新提交对应的 Stack Smoke Tests 和 Validate Skill 两个 GitHub Actions 均为 success。

## 测试边界与待办

- 这是可复现的工具链/编译/基础测试冒烟验证，不是五套完整业务系统的端到端验收。
- React + antd 5 当前做了 TypeScript 和生产构建验证，尚未运行浏览器级交互测试（如 Playwright）。
- Vue 当前做了类型检查和生产构建，尚未做组件交互测试。
- npm 安装日志报告依赖树存在 1 个 moderate 和 1 个 high 漏洞提示；本轮尚未完成 `npm audit` 逐项归因与升级验证，因此不应将依赖安全状态标记为完全通过。
- Skill 是否能稳定引导不同 AI Agent 遵循规范，还需要在真实业务仓库中做任务对照测试。

## 结论

五种技术栈的最小工程样例均已通过自动化冒烟测试，可以用于真实项目试用和持续迭代。当前验证不等同于完整业务系统的端到端验收；在完成 npm 漏洞归因、前端浏览器交互测试及真实项目对照测试前，不应宣称已完成全面的生产级验证。
