import json
import os
class RW_template_db():    
    def read_template(self):
        with open('./Go_Contact_test/Templates_config/template.json') as json_file:
            data = json.load(json_file)     
        return data
    
    def write_template(self,values):        
        with open('./Go_Contact_test/Templates_config/template.json', 'w') as file:
            json.dump(values, file, indent=4)
       
    def change(self, template):
        data =self.read_template()
        #print(data)
        data['data_name'] = (os.path.basename(template[2]))[:-4]
        data['campaign'] = template[0]
        data['template'] = template[1]
        data['db_upload_file'] = template[2]
        self.write_template(data)
        
    