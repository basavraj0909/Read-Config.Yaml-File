import yaml


def read_config(file_path):

    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    return config



if __name__ == '__main__':
    config = read_config('config.yaml')
    print("Database Configuration:")
    print(f"Host: {config['DATABASE']['HOST']}")
    print(f"Port: {config['DATABASE']['PORT']}")
    print(f"Username: {config['DATABASE']['USERNAME']}")
    print(f"Password: {config['DATABASE']['PASSWORD']}")

    print("\nDjango Configuration:")
    print(f"Debug: {config['DJANGO']['DEBUG']}")
    print(f"Allowed Hosts: {', '.join(config['DJANGO']['ALLOWED_HOSTS'])}")
