# -*- coding: utf-8 -*-
'''
Задание 7.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Аргумент access - это словарь access-портов, вида:
    { 'FastEthernet0/12':'10','FastEthernet0/14':'11','FastEthernet0/16':'17','FastEthernet0/17':'150' }

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря access_dict.
'''

def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':'10','FastEthernet0/14':'11','FastEthernet0/16':'17'}
    
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']


access_dict = { 'FastEthernet0/12':'10',
                'FastEthernet0/14':'11',
                'FastEthernet0/16':'17',
                'FastEthernet0/17':'150' }
