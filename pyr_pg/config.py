class config():
    def __init__(self, file):
        self.file = file
        self.conf = {}
        try:
            self.load()
        except FileNotFoundError:
            print("config file don't exist.\nUse var.save() to create the file.")
        
    def load(self):
        config_file = open(self.file, "r") #open the configuration file
        config_create = config_file.readlines() #read every line from the configuration file
        config_file.close() #close the configuration nfile
        config_create = [line.strip() for line in config_create]
        for configuration in config_create:
            add = configuration.split("=")
            self.conf[add[0]] = add[1]
    
    def save(self):
        export = []
        for data in self.conf:
            export.append(str(data) + "=" + str(self.conf[data]))
        config_file = open(self.file, "w") #open the configuration file
        for data in export:
            config_file.write(data + "\n")
    
    def get(self, param):
        return self.conf[param]
    
    def add(self, param, value):
        self.conf[param] = value
    
    def remove(self, param):
        pass
    
    def change(self, param, value):
        self.conf[param] = value
    
    def mknew(self, *temp):
        # make a new config 
        if temp[0] == 1:
            self.conf = {"name":" ", "lv":"0"}
        else:
            self.conf = {}
            
    def retun_all(self):
        return self.conf