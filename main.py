#!/usr/bin/env python
# -*- coding: utf-8 -*-


clients = 'Pablo, Ricardo, '

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already exist in client\'s list')

def retrieve_client():
    pass

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        not_in_clients()

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
        list_clients()
    else:
        not_in_clients()


def list_clients():
    global clients

    print ('The clients list is: ')
    print (clients)

def _add_comma():
    global clients

    clients += ','

def _space_line():
    print ('*' * 50)

def not_in_clients():
    print('Client is not in clients list')

def _print_welcome():
    _space_line()
    print('Welcome to VentasLab')
    _space_line()
    print ('what would you want to do today?')
    print ('[C]reate client')
    print ('[R]etrieve client')
    print ('[U]pdate')
    print ('[D]elete client')
    print ('[E]xit')

def _get_client_name():
    return input('What is the client name?: ')

if __name__ == '__main__':

    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'R':
        pass

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('Whats is the updated client name?: ')
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)

    elif command == 'E':
        _space_line
        print('Thanks for using VentasLab services')
        exit()
    else:
        print ('Invalid command')
