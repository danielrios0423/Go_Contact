import json

class Templates_db():
    
    def read_template(self):
        with open("./Templates_db/template.json", "r") as json_file:
            data = json.load(json_file)
        return data
    
