# logger
一个无用的日志记录器

用法：
```
import logger,sys
log=logger.Logger(pattern="[{time}/{type}]: {log}") # 格式字符串，包含'time','type','log'三项
log.add_stream(sys.stdout) # 或者其他什么输出流
log.log("Test",level=logger.default_levels["info"]) # level应传入一个LogLevel实例，可以从logger.LogLevel创建，也可从loggert.default_levels取用："info","warning"和"error"
```
测试：
使用unittest，位于logger.test中
