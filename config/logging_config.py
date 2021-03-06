import logging
import logging.handlers


def set_log_config():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(level=logging.INFO)
    # 创建处理器
    ls = logging.StreamHandler()
    lf = logging.handlers.TimedRotatingFileHandler(filename='./log/tpshop.log', when='d', backupCount=3)
    # 创建格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 将格式器添加到处理器
    ls.setFormatter(formatter)
    lf.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lf)




