# Go 专项规范

## 项目识别
检查 go.mod、Go 版本、目录布局、Makefile/Taskfile、CI 和测试约定；不擅自升级 Go 版本。

## 设计与错误
- 遵循 gofmt；保持小接口、简单组合和清晰包边界。
- 避免循环依赖、宽泛 utils 包和过早抽象。
- 使用 errors.Is / errors.As；错误增加上下文，不重复堆栈包装。
- 不忽略返回错误；不使用 panic 处理常规业务错误。

## 并发与资源
- goroutine 必须有退出条件和生命周期管理。
- context.Context 用于取消、截止时间和请求级元数据，不作为普通结构体状态长期保存。
- 明确 channel 关闭责任，避免向已关闭 channel 发送。
- 检查数据竞争、死锁、泄漏和无界并发；按需使用 worker pool/errgroup。
- 文件、连接、响应体及时 Close；HTTP Client/Transport 合理复用。
- 锁范围尽量小，不持锁执行不可控 I/O。

## API 与验证
- Handler 负责协议转换和输入校验，业务逻辑可独立测试。
- 明确 JSON、状态码、超时和错误响应契约。
- 覆盖表驱动、边界和并发场景；测试不依赖执行顺序。
- 按项目运行 go test ./...、go vet ./...；并发改动可运行 go test -race ./...；遵循已有 golangci-lint 配置。
