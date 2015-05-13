import yaml
import json
from models.movie import *
import shutil
import os


class Website:

    """This is the main object for the website when the it is responsible
    the database is loaded as self.data it is also responsible for building out assets
    and individual pages  """

    def __init__(self, models='', structure=''):
        self.data = {}
        self.model_reference = models
        self.structure = structure

        self.process_models()

        # goes through the data and loads it
    def load_db(self, model_table):
        """ this goes through the data folder and instantiates the yaml files into their
        respective model classes and builds a temporary db attached to the self.data field """
        path_to_data = 'data/' + model_table + '/data.yml'
        self.data[model_table] = {}
        f = open(path_to_data)
        model_data = yaml.safe_load(f)
        f.close()
        # TODO get rid of eval below... it is bad ... the Internet says so
        # try and find source code that has a similar problem
        model_class = eval(model_table[:-1].capitalize())
        if model_data:
            for data in model_data:
                self.add_model_to_site_table(model_class(**data))

    def process_models(self):
        models = [key for key, value in self.model_reference.iteritems()]
        for model in models:
            self.load_db(model)

    def add_model_to_site_table(self, model_instance):
        table = model_instance.table()
        self.data[table][model_instance.index] = model_instance

    def add_model(self, model_instance):
        self.add_model_to_site_table(model_instance)
        self.save_model(model_instance)

    def save_model(self, model_instance):
        table = model_instance.table()
        path_to_data = 'data/' + table + '/data.yml'
        model_yaml = yaml.dump(
            [model_instance.nice_yaml()], encoding=None, default_flow_style=False)
        with open(path_to_data, 'a') as output_file:
            output_file.write(model_yaml)
            output_file.close()

    def save_db(self, table):
        updated = [
            model.nice_yaml() for key,
            model in self.data[table].iteritems()]
        path_to_data = 'data/' + table + '/data.yml'
        updated_yaml = yaml.dump(
            updated,
            encoding=None,
            default_flow_style=False)
        with open(path_to_data, 'w') as output_file:
            output_file.write(updated_yaml)
            output_file.close()

    def get_template(self, path_to_template):
        """ takes a yaml file as a template """
        with open(path_to_template) as template_file:
            template = yaml.load(template_file.read())
            template_file.close()
        return template

    def clean_public_folder(self):
        """THIS DELETES ALL THE ASSETS IN THE PUBLIC FOLDER

        """
        # TODO find a more elegant solution
        shutil.rmtree('./public/')
        os.mkdir('./public/')

    def make_assets_public(self):
        self.clean_public_folder()
        # TODO add some minifying here
        shutil.copytree('./assets/css', './public/css')
        shutil.copytree('./assets/script', './public/script')

    def title(self, template):
        return "<title>{title}</title>".format(title=template['title'])

    def assets(self, template):
        """
        processes the assets listed in the template
        each asset is in the below format
         asset[0] is either a stylesheet or a script
         asset[1] signifies an internal assset or external link
         asset[2] is the external file or local file name
        ['stylesheet', 'link', "https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css"]
        """
        instructions = {
            'stylesheet': {
                'link': '        <link rel="stylesheet" href="{location}">\n',
                'local': '        <link rel="stylesheet" href="/css/{location}">\n'},
            'script': {
                'link': '        <script src="{location}"></script>\n',
                'local': '        <script src="/script/{location}"></script>\n'}}
        content = '\n'
        for asset in template['assets']:
            content += instructions[asset[0]
                                    ][asset[1]].format(location=asset[2])

        return content

    def build_head(self, template):
        outline = """
        <head>
            <base href="~/">
            <meta charset="utf-8">
            {data}

        </head>
        """
        data = self.title(template)
        data += self.assets(template)
        return outline.format(data=data)

    def build_page(self, path_to_template, model):
        """ builds a single page from a yaml template  """
        template = self.get_template(path_to_template)
        path_to_header_template = "./templates/" + template['header'] + '.yml'
        header_template = self.get_template(path_to_header_template)
        if template['type'] == 'all':
            page = self.build_head(header_template)
            content = model.get_index_content(self.data[model.table()])
            page += template['body'].format(content=content)
            destination = "./public" + \
                template['destination'] + template['file_name']
            self.write_file(destination, page)
        elif template['type'] == 'each':
            os.mkdir('./public/' + model.table())
            for key, value in self.data[model.table()].iteritems():
                page = self.build_head(header_template)
                content = value.content_to_html()
                details = value.get_html_omdb_data()
                page += template['body'].format(
                    content=content,
                    details=details)
                destination = "./public" + \
                    template['destination'] + value.index + '.html'
                self.write_file(destination, page)

        else:
            print "build failed template type not specified"

    def write_file(self, destination, page):
        with open(destination, 'w') as new_file:
            new_file.write(page)
            new_file.close()

    def build_all(self):
        self.make_assets_public()
        for key, models in self.model_reference.iteritems():
            model = eval(models['classname'])
            self.process_templates(models['templates'], model)

    def process_templates(self, templates, model):
        for template in templates:
            path_to_template = 'templates/' + \
                model.table() + '/' + template + '.yml'
            self.build_page(path_to_template, model)
