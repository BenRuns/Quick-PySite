import yaml
import json
from models.movie import *


class Website:
    """This is the main object for the website  """
    def __init__(self, models='', structure='') :
        self.data = {}
        self.model_reference = models
        self.structure = structure

        self.process_models()  

        #goes through the data and loads it 
    def load_db(self, model_with_s):
        """ this goes through the data folder and instantiates the yaml files into their 
        respective model classes and builds a temporary db attached to the self.data field """
        path_to_data = 'data/' + model_with_s + '/data.yml'
        self.data[model_with_s ] = {}
        f = open(path_to_data)
        model_data = yaml.safe_load(f)
        f.close()
        #TODO get rid of eval below... it is bad ... the Internet says so
        #try and find source code that has a similar problem
        model_class = eval(model_with_s[:-1].capitalize())
        if model_data:
            for data in model_data:
                self.add_model_to_site_table(model_class(**data)) 

    def process_models(self):
        models =  [  [ key, self.model_reference[key]['template'],
         self.model_reference[key]['index_on'] ] for key,value in self.model_reference.iteritems() ]
        for model in models:
            self.load_db(model[0])

    def add_model_to_site_table(self,model_instance):
        table = model_instance.table()
        self.data[table][model_instance.index] = model_instance

    def add_model(self, model_instance ):
        self.add_model_to_site_table( model_instance )
        self.save_model(model_instance)

    def save_model(self, model_instance):
        table = model_instance.table()
        path_to_data = 'data/' + table + '/data.yml'
        model_yaml = yaml.dump([model_instance.nice_yaml()], encoding=None, default_flow_style=False )
        with open(path_to_data, 'a') as output_file:
            output_file.write( model_yaml )
            output_file.close() 
    


    def save_db(self,table):    
        updated = [ model.nice_yaml() for key,model in self.data[table].iteritems()]
        path_to_data = 'data/' + table + '/data.yml'
        updated_yaml = yaml.dump(updated, encoding=None, default_flow_style=False )
        with open(path_to_data, 'w') as output_file:
            output_file.write(updated_yaml)
            output_file.close() 
        

    def build_site(self):
        """ builds the site to public according to the manifest """

        #goes through the assets and makes them public

        #builds each model via template
            #builds the head according to the head
            #adds assets according to the assets
            #format the body

        pass



        