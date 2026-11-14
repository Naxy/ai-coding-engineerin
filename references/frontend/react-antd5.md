# React + Ant Design 5 专项规范

## 项目识别
核实 React、React DOM、TypeScript、antd、图标包、构建工具、路由、请求层、状态管理和测试版本。确认 antd 5，不混用 v4 API。

## React 与 Hooks
- 默认函数组件和 Hooks，遵循项目组织方式。
- Hooks 只在组件或自定义 Hook 顶层调用，不放在条件、循环或嵌套函数中。
- useEffect 用于同步外部系统；派生数据优先直接计算或 useMemo，不用 Effect 复制状态。
- Effect 明确依赖并清理订阅、定时器和请求，避免竞态。
- useMemo、useCallback、React.memo 仅在有测量或明确引用稳定需求时使用。
- 状态尽量局部化，避免同一事实重复保存；列表使用稳定 key。
- Props、事件和 API 数据使用明确 TS 类型，避免滥用 any。

## Ant Design 5
- 使用当前项目 antd 5 版本 API；升级前核实迁移差异。
- 样式优先 Design Token、主题配置和项目样式方案，避免依赖脆弱内部 DOM。
- Form 使用 Form rules；异步校验处理加载、失败和竞态，不重复维护 Form 值的 React state。
- Table 明确 rowKey、分页、排序、筛选和 loading；服务端分页不做当前页假分页。
- Modal、Drawer、Popconfirm 明确关闭行为、异步提交状态和重复提交保护。
- 远程 Select/AutoComplete 处理 debounce、旧请求取消或过期结果和空态。
- Upload 明确 beforeUpload、类型/大小限制、进度、失败重试；服务端仍需校验。
- DatePicker 明确时区、日期格式和后端契约。
- 全局 locale/theme/component tokens 优先通过 ConfigProvider 管理。
- message/notification 遵循统一封装，避免同一错误重复提示。

## 数据与验证
- 请求层统一处理鉴权、超时、错误映射和取消。
- 区分 loading、初始空态、无结果、错误和无权限。
- 写操作防重复提交；关键写操作由服务端提供幂等保护。
- 权限按钮隐藏仅改善体验，服务端仍须鉴权。
- 大表格考虑服务端分页或虚拟滚动。
- 按项目运行 TS 检查、ESLint、单测和构建；验证 Form、Table、Modal、远程 Select、Upload 和权限状态。
