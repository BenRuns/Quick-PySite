import yaml


def get_template(path_to_template):
    """ takes a yaml file as a template """
    with open(path_to_template) as template_file:
        template = yaml.load(template_file.read())
        template_file.close() 
    return template


def title(template):
    return "<title>{title}</title>".format( title=template['title'])

def assets(template):
    instructions = {'stylesheet': {'link':'        <link rel="stylesheet" href="{location}">\n',
                                   'local':'        <link rel="stylesheet" href="css/{location}">\n' } ,
                        'script': {'link':'        <script src="{location}"></script>\n',
                                   'local':'        <script src="js/{location}"></script>\n' } 
                    }
    content = '\n'               
    for asset in template['assets']:
        content += instructions[asset[0]][asset[1]].format(location=asset[2])

    return content

def build_header(template):
    outline = """
    <head>
        <meta charset="utf-8">
        {data}
    </head>
    """
    data = title(template)
    data += assets(template)
    return outline.format(data=data)





print build_header(get_template('./templates/application/header.yml'))