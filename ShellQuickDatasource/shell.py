import cmd
from colorama import Fore, Style
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
      
    def do_mongo(self,arg):
        print(F'{Fore.GREEN}Mongo Server is starting...')
    
    def do_arango(self,arg):
        print(F'{Fore.GREEN}Arango Server is starting...')
    
    def do_elasticsearch(self,arg):
        print(F'{Fore.GREEN}ElasticSearch Server is starting...')

    def do_mysql(self,arg):
        print(F'{Fore.GREEN}MySQL Server is starting...')
    
    def do_postgres(self,arg):
        print(F'{Fore.GREEN}Postgres Server is starting...')
    
    def do_smtp(self,arg):
        print(F'{Fore.GREEN}SMTP Server is starting...')
        
    def do_mssql(self,arg):
        print(F'{Fore.GREEN}MsSql Server is starting...')
    def do_clear(self, arg):
        os.system('cls' if os.name == 'nt' else 'clear')

    