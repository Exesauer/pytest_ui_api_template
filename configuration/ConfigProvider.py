import configparser

config = configparser.ConfigParser()
print("Обратились к файловой системе")
config.read("./test_config.ini")

class ConfigProvider:

    def __init__(self) -> None:
        self.config = config

    def get(self, section, prop):
        return self.config[section].get(prop)

    def get_int(self, section, prop):
        return self.config[section].getint(prop)