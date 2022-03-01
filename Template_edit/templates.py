import json
import os
class RW_template_db():    
    def read_template(self):
        with open(f'./Templates_db/template.json') as json_file:
            data = json.load(json_file)
            data['data_name'] = (os.path.basename(data["db_upload_file"]))[:-4]
            
        return data
    
    def write_template(self,values):        
        with open(f'./Templates_db/template.json', 'w') as file:
            json.dump(values, file, indent=4)
        
        with open(f'./Templates_db/template.json') as json_file:
            data = json.load(json_file)
        return data
    
    def change(self, template):
        data =self.read_template()
        print(data)
        data['campaign'] = template[0]
        data['template'] = template[1]
        data['db_upload_file'] = template[2]
        print(data)
        self.write_template(data)