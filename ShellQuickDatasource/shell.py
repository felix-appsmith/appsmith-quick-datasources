import cmd
from colorama import Fore, Style
import subprocess
import os
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

    