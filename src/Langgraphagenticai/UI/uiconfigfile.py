from configparser import ConfigParser
class config:
    def __init__(self,config_file="./src/langgraphagenticai/UI/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)
    def get_llm_option(self):
        retrun self.config["DEFAULT"].get(LLM_OPTIONS).split(", ")

    def get_usecase_option(self):
        retrun self.config["DEFAULT"].get(USE_CASE_OPTIONS).split(", ")

    def get_usecase_option(self):
        retrun self.config["DEFAULT"].get(GROQ_MODEL_OPTIONS).split(", ")
    
    