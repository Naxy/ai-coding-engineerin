# Vue 专项规范

- 识别 Vue 2/3、Options/Composition API、TS、Vite/Webpack、Pinia/Vuex、路由和组件库版本。
- Vue 3 新代码按项目约定使用 Composition API；既有 Options API 项目不做无关迁移。
- 正确区分 ref、reactive、computed、watch、watchEffect；派生状态优先 computed。
- watch 应有明确副作用与清理策略，不用 watch 替代简单计算。
- 通过 props/emits 定义组件边界，不直接修改 props。
- 复杂逻辑可抽取 composable，避免过度拆分；v-for 使用稳定 key。
- 异步请求处理卸载、竞态和重复触发；监听器、定时器、订阅及时清理。
- Pinia/Vuex 按业务域组织，避免所有页面状态全局化。
- 按项目运行 vue-tsc、ESLint、单测和构建，验证路由、表单、权限和异步状态。
