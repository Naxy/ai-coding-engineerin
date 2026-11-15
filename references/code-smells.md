# 代码坏味道清单

## 设计结构
- God Class / God Function：单个类或函数承担过多职责。
- Shotgun Surgery：简单需求迫使大量无关位置一起修改。
- Premature Abstraction：缺少稳定复用场景就引入抽象层。
- Over-engineering：为假设中的未来需求设计复杂框架。
- Feature Envy：逻辑长期依赖另一个对象的数据。
- Duplicate Logic：业务规则散落多处且可能不一致。

## 正确性健壮性
- Swallowed Exception：捕获异常后忽略。
- Empty Catch：空 catch 掩盖失败。
- Magic Values：关键状态、阈值、时间和金额散落为魔法值。
- Weak Validation：只做前端校验或缺少服务端校验。
- Hidden Side Effects：方法名与实际副作用不符。
- Unsafe Retry：重试非幂等操作造成重复写入。

## 数据性能
N+1 Query、无界查询、Chatty Calls、缺少索引意识、重复序列化、资源泄漏。

## 并发分布式
Race Condition、Deadlock、Lost Update、Duplicate Processing、无界并发、超时配置不协调。

## 测试
无有效断言、过度 Mock、测试专用生产分支、Flaky Test、只覆盖 happy path。

发现问题时区分本次必须修复项与历史遗留项；未经授权不扩大改动范围。
