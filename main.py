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


def list_clients():
    global clients

    print ('The clients list is: ')
    print (clients)


def _add_comma():
    global clients

    clients += ','

def _space_line():
    print ('*' * 50)

def _print_welcome():
    _space_line()
    print('Welcome to VentasLab')
    _space_line()
    print ('what would you want to do today?')
    print ('[C]reate client')
    print ('[D]elete client')
    print ('[E]xit')

if __name__ == '__main__':

    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name?: ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'E':
        _space_line
        print('Thanks for using VentasLab services')
        exit()
    else:
        print ('Invalid command')
