import os

def delete():
    dir = "./Go_Contact_test/Templates_config"
    list = os.listdir(dir)
    list.remove('template.json')
    initial_count = len(list)-1

    for i in list: 
        os.remove(dir+"/"+i)
    print(initial_count)
    print(list)
    return True