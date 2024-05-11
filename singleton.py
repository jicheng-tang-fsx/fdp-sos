import tomllib
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s    %(levelname)s:     %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def load_config_file(path: str):
    """
    读取并返回指定路径的TOML配置文件内容。
    如果文件不存在或读取出错，将抛出异常。
    """
    try:
        with open(path, 'rb') as config_file:
            return tomllib.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found")
    except Exception as e:
        raise Exception(f"An error occurred while reading the config file: {str(e)}")

config = load_config_file("/app/config.toml")