# Criador do Gerador *Cl4y*
#!/bin/bash
#!/usr/bin/env python3
from os import system
from time import sleep
from subprocess import run
import requests
import re
from banner import Banner
import random 
# Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

system('clear')

print(f'{C}Ferramenta {G}Cl4y=ON... {C}')

Banner()

sleep(3)

system('clear')

print(f'''{G}*By Cl4y 
{B}████████╗ ██████╗  ██████╗ ██╗     ███████╗
{B}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{B}   ██║   ██║   ██║██║   ██║██║     ███████╗
{B}   ██║   ██║   ██║██║   ██║██║     ╚════██║
{B}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{R}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {G}v0.1
{G}Trending {C} obrigado a todos!
{G}Criador: https://github.com/Hack-Cl4y/        ''')


def gerarcpf():
	print(f'{C}[{G}*{C}] Gerando CPF...')
	sleep(1)
	cpf = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
	cpf2 = cpf['data']['number_formatted']
	cpf = cpf['data']['number']
	print(f'{C}[{Y}+{C}] O CPF gerado foi: {B} {cpf2}')
	print(f'{C}[{G}V{C}]CPF Valido')
	sleep(1)


def gerarcnpj():
	print(f'{C}[{G}*{C}] Gerando CNPJ...')
	sleep(1)
	cnpj = requests.get('http://geradorapp.com/api/v1/cnpj/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
	cnpj2 = cnpj['data']['number_formatted']
	cnpj = cnpj['data']['number']
	print(f'{C}[{Y}+{C}] O CNPJ gerado foi: {B} {cnpj2}')
	print(f'{C}[{G}V{C}]CNPJ Valido')
	sleep(1)

def gerarcns():
	print(f'{C}[{G}*{C}] Gerando CNS...')
	sleep(1)
	cns = requests.get('http://geradorapp.com/api/v1/cns/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
	cns2 = cns['data']['number_formatted']
	cns = cns['data']['number']
	print(f'{C}[{Y}+{C}] O CNS gerado foi: {B} {cns2}')
	print(f'{C}[{G}V{C}]CNS Valido')
	sleep(1)

def menu():
        
        print(f'''
                {C}[{G}+{C}] Formas de operação: 

                [{G}1{C}] Gerar CPF

                [{G}2{C}] Gerar CNPJ

                [{G}3{C}] Gerar CNS

                [{G}Q{C}] Sair 
''')
mnu = input(f''' {C}[{G}+{C}]Formas de operação: 

                [{G}1{C}] Gerar CPF

                [{G}2{C}] Gerar CNPJ

                [{G}3{C}] Gerar CNS

                [{G}Q{C}] Sair

Digite sua opcao:             
''')
	
if mnu == '1':
	gerarcpf()

elif mnu == '2':
       
       gerarcnpj()

elif mnu == '3':
        
        gerarcns() 

if mnu == "Q" or 'q':
       print("obg") 
