import json

class Templates_db():
    
    def read_template(self):
        with open('./Go_Contact_test/Templates_config/template.json', "r") as json_file:
            data = json.load(json_file)
        return data
    
