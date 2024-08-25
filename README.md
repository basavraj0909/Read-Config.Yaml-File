# YAML Config Reader

This project demonstrates how to read configuration data from a YAML file using Python.

## Project Structure

- `config.yaml`: The YAML configuration file containing settings for database and Django.
- `read_config.py`: The Python script that reads the configuration from the `config.yaml` file and prints it to the console.

## How to Use

1. Clone the repository to your local machine.
2. Ensure that you have Python installed.
3. Install the required Python packages using `pip`:
    ```bash
    pip install pyyaml
    ```
4. Run the Python script:
    ```bash
    python read_config.py
    ```

The script will output the configuration settings defined in the `config.yaml` file.

## Example Output

```bash
Database Configuration:
Host: localhost
Port: 5432
Username: admin
Password: password

Django Configuration:
Debug: True
Allowed Hosts: localhost, 127.0.0.1
