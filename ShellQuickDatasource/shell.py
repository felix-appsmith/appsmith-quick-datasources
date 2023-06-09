import cmd
from colorama import Fore, Style
import subprocess
import os
from ShellServices.ngrokServer import open_server_ngrok
from colorama import Fore
class MyShell(cmd.Cmd):
    prompt = f'{Fore.GREEN}>>{Style.RESET_ALL} '

    def do_hello(self, arg):
        welcome_message = f"""
╔═══╦╗░╔╦══╦═══╦╗╔═╗╔═══╦═══╦════╦═══╦═══╦═══╦╗░╔╦═══╦═══╦═══╗╔══╦═══╗╔═══╦╗░╔╦═╗░╔╗
║╔═╗║║░║╠╣╠╣╔═╗║║║╔╝╚╗╔╗║╔═╗║╔╗╔╗║╔═╗║╔═╗║╔═╗║║░║║╔═╗║╔═╗║╔══╝╚╣╠╣╔═╗║║╔═╗║║░║║║╚╗║║
║║░║║║░║║║║║║░╚╣╚╝╝░░║║║║║░║╠╝║║╚╣║░║║╚══╣║░║║║░║║╚═╝║║░╚╣╚══╗░║║║╚══╗║╚═╝║║░║║╔╗╚╝║
║║░║║║░║║║║║║░╔╣╔╗║░░║║║║╚═╝║░║║░║╚═╝╠══╗║║░║║║░║║╔╗╔╣║░╔╣╔══╝░║║╚══╗║║╔╗╔╣║░║║║╚╗║║
║╚═╝║╚═╝╠╣╠╣╚═╝║║║╚╗╔╝╚╝║╔═╗║░║║░║╔═╗║╚═╝║╚═╝║╚═╝║║║╚╣╚═╝║╚══╗╔╣╠╣╚═╝║║║║╚╣╚═╝║║░║║║
╚══╗╠═══╩══╩═══╩╝╚═╝╚═══╩╝░╚╝░╚╝░╚╝░╚╩═══╩═══╩═══╩╝╚═╩═══╩═══╝╚══╩═══╝╚╝╚═╩═══╩╝░╚═╝
░░░╚╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


                            
Hello, welcome to Appsmith Quick Datasource. The best option for deploying and testing Datasources in Appsmith.
        """
        print(Fore.MAGENTA + welcome_message + Style.RESET_ALL + arg)
    def do_exit(self, arg):
        return True
      
    stop_commands = {
        'arangodb': 'cd arangodb && sudo docker-compose down',
        'elasticsearch': 'cd elasticsearch && sudo docker-compose down',
        'mongodb': 'cd mongodb && sudo docker-compose down',
        'mysql': 'cd mysql && sudo docker-compose down',
        'postgres': 'cd postgress && sudo docker-compose down',
        'redis': 'cd redis && sudo docker-compose down',
        'smtp': 'cd smtp && sudo docker-compose down',
        'mssql': 'cd sqlserver && sudo docker-compose down',
        
    }

    start_commands = {
        'arangodb': 'cd arangodb && sudo docker-compose up -d ',
        'elasticsearch': 'cd elasticsearch && sudo docker-compose up -d ',
        'mongodb': 'cd mongodb && sudo docker-compose up -d ',
        'mysql': 'cd mysql && sudo docker-compose up -d ',
        'postgres': 'cd postgress && sudo docker-compose up -d ',
        'redis': 'cd redis && sudo docker-compose up -d ',
        'smtp': 'cd smtp && sudo docker-compose up -d ',
        'mssql': 'cd sqlserver && sudo docker-compose up -d ',
    }

    expose_commands = {
        'arangodb': {'port': 8529, 'protocol': 'tcp',  'db_name': '_system', 'username': 'root', 'password': 'arangoappsmith'},
        'elasticsearch': {'port': 9200, 'protocol': 'http',  'db_name': 'db', '443': 'root', '443': '443'},
        'mongodb': {'port': 27017, 'protocol': 'tcp', 'db_name': 'admin', 'username': 'appsmith', 'password': 'appsmith'},
        'mysql': {'port': 3306, 'protocol': 'tcp', 'db_name': 'db', 'username': 'root', 'password': 'password'},  
        'postgres': {'port': 5432, 'protocol': 'tcp',  'db_name': 'postgres', 'username': 'postgres', 'password': 'appsmith'},
        'redis': {'port': 6379, 'protocol': 'tcp',  'db_name': '0', 'username': '', 'password': ''},
        'smtp': {'port': 25, 'protocol': 'tcp',  'db_name': 'db', 'username': 'appsmith', 'password': 'appsmith'},
        'mssql': {'port': 1433, 'protocol': 'tcp',  'db_name': 'master', 'username': 'sa', 'password': 'Appsmith1!'},
    }



    def do_expose(self, arg):
        if arg in self.expose_commands:
            print(F'{Fore.GREEN} Starting ngrok tunnel {arg.capitalize()}')
            url, puerto = open_server_ngrok(self.expose_commands[arg]['port'], self.expose_commands[arg]['protocol'])
            db_name = self.expose_commands[arg].get('db_name', '')
            username = self.expose_commands[arg].get('username', '')
            password = self.expose_commands[arg].get('password', '')
            host = url.split(':')[0]
            print(f"Host: {host}")
            print(f"Port: {puerto}")
            print(f"Database Name: {db_name}")
            print(f"Username: {username}")
            print(f"Password: {password}")
         


    def do_dblists(self, arg):
        subprocess.run('sudo docker ps', shell=True)



    def do_start(self,arg):
        if arg in self.start_commands:
            print(F'{Fore.GREEN} {arg.capitalize()} Server is starting...')
            subprocess.run(self.start_commands[arg], shell=True)

    def do_stop(self,arg):
        if arg in self.stop_commands:
            print(F'{Fore.GREEN}Stopping {arg.capitalize()} Server...')
            subprocess.run(self.stop_commands[arg], shell=True)

    def do_clear(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')

    

    