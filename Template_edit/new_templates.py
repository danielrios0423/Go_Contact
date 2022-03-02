import json
import os
class NewJason():
    
    def read_template(self):
        with open(f'./Go_Contact_test/Templates_config/template.json') as json_file:
            data = json.load(json_file)  
            print(data)
        return data  
        

    def new_template(self,template): 
        data = self. read_template()
        
        data['data_name'] = (os.path.basename(template[2]))[:-4]
        data['campaign'] = template[0]
        data['template'] = template[1]
        data['db_upload_file'] = template[2]
        self.write_template(data)
        
    def write_template(self,values):
        dir = "./Go_Contact_test/Templates_config"
        list = os.listdir(dir)
        initial_count = len(list)-1
        print(initial_count)
        with open(f'./Go_Contact_test/Templates_config/template_{initial_count}.json', 'w') as file:
            json.dump(values, file, indent=4)
            
        with open(f'./Go_Contact_test/Templates_config/template_{initial_count}.json') as json_file:
            data = json.load(json_file)  
            print(data)   
                
        