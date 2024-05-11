import tomllib

def read_config(path):
    with open(path, 'rb') as config_file:
        config = tomllib.load(config_file)
    return config

# 使用函数读取配置
config = read_config('./config.toml')
print(config)
