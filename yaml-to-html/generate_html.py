import yaml

def generate_html_from_yaml(yaml_file, output_file):

    # Load the YAML configuration file
    with open('menu.yaml', 'r') as yaml_file:
        menu_config = yaml.safe_load(yaml_file)

    # Initialize the HTML content
    html_content = '''<ul class="nav navbar-nav navbar-right">     
    <li><a href="/">Home</a></li>'''

    # Iterate through the YAML configuration to generate HTML
    for item in menu_config['doc']:
        if isinstance(item, dict):
            for key, val in item.items():
                if isinstance(val, str):  # Direct link
                    html_content += f'    <li><a href="/{val}" target="_blank">{key}</a></li>\n'
                elif isinstance(val, list):  # Nested menu
                    html_content += f'''    <li class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">{key} <span class="caret"></span></a>
            <ul class="dropdown-menu">\n'''
                    for subitem in val:
                        for sub_key, sub_val in subitem.items():
                            html_content += f'                <li><a href="/{sub_val}">{sub_key}</a></li>\n'
                    html_content += '            </ul>\n    </li>\n'

        else:
            for key, value in item.items():
                html_content += f'    <li><a href="/{value}" target="_blank">{key}</a></li>\n'

    html_content += '</ul>'


    # Write the generated HTML to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)
    # print("HTML file generated successfully.")

generate_html_from_yaml('menu.yaml', 'menu_generated.html')



