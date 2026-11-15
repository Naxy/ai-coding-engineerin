# Python 专项规范

## 项目识别
识别 Python 版本、pyproject/requirements、虚拟环境、包管理器、框架和测试/lint 配置。优先沿用 uv、Poetry、Pipenv、pip-tools 或项目已有工具，不混用。

## 代码设计
- 遵循 PEP 8 和项目格式配置；公共接口与复杂边界添加类型注解。
- 类型检查遵循项目配置；避免滥用 Any、cast 和 ignore。
- 使用 dataclass、TypedDict、Pydantic 前确认项目依赖和边界需要。
- 避免全局可变状态和隐式副作用；异常捕获具体并保留上下文，禁止裸 except 或静默吞错。
- 使用 with / async with 管理文件、锁和连接。

## 异步并发
- 明确同步/异步边界，不在事件循环执行阻塞 I/O。
- asyncio 任务需有取消、超时和异常收集策略；避免无界创建任务。
- 共享状态需正确同步，不假定 GIL 可替代并发设计。

## Web 数据与验证
- 服务端执行输入与权限校验；关注 ORM N+1、事务、分页和连接生命周期。
- 显式定义金额、时间、时区和序列化契约；密钥通过配置注入。
- 按项目运行 pytest、ruff/black、mypy/pyright 等；覆盖异常、边界、异步取消和依赖失败。
