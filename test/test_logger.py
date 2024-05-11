
import logging

# 创建一个全局 logger
logger = logging.getLogger(__name__)

# 设置日志级别
logger.setLevel(logging.INFO)

# 创建一个日志格式器
formatter = logging.Formatter('%(asctime)s    %(levelname)s:    %(message)s')

# 创建一个输出到控制台的处理器，并应用格式器
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(console_handler)

# 示例日志信息
logger.debug('这是一个调试信息')
logger.info('这是一个信息')
logger.warning('这是一个警告')
logger.error('这是一个错误')
logger.critical('这是一个严重错误')
