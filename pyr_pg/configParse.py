"""
    Config parser for pyr_pg
    (c) 2025 Spyro24
"""

def parse_config(config_file: str):
    config = {"":{}}
    configFile = open(config_file, "r")
    configFileLines = configFile.readlines()
    configFile.close()
    curConfigEntry = ""
    lines = []
    for line in configFileLines:
        line = line.strip()
        if line != "":
            if line[0] == "[" and line.endswith("]") and len(line) > 2:
                entry = line.strip("[]")
                curConfigEntry = entry
                config[curConfigEntry] = {}
            elif line[0] != "#":
                element = line.split("=")
                config[curConfigEntry][element[0].strip()] = element[1].strip()
    return(config)
