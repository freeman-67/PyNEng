## Модуль telnetlib

Модуль telnetlib входит в стандартную библиотеку Python. Это реализация клиента telnet.

> Подключиться по telnet можно и используя pexpect. Плюс telnetlib в том, что этот модуль входит в стандартную библиотеку Python.

Принцип работы telnetlib напоминает pexpect, поэтому пример ниже должен быть понятен.

Файл 2_telnetlib.py:
```python
import telnetlib
import time
import getpass
import sys

COMMAND = sys.argv[1]
USER = raw_input("Username: ")
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')

DEVICES_IP = ['192.168.100.1','192.168.100.2','192.168.100.3']

for IP in DEVICES_IP:
    print "Connection to device %s" % IP
    t = telnetlib.Telnet(IP)

    t.read_until("Username:")
    t.write(USER + '\n')

    t.read_until("Password:")
    t.write(PASSWORD + '\n')
    t.write("enable\n")

    t.read_until("Password:")
    t.write(ENABLE_PASS + '\n')
    t.write("terminal length 0\n")
    t.write(COMMAND + '\n')

    time.sleep(5)

    output = t.read_very_eager()
    print output

```

Первая особенность, которая бросается в глаза - в конце отправляемых команд, надо добавлять символ перевода строки.

В остальном, telnetlib очень похож на pexpect:
* ```t = telnetlib.Telnet(ip)``` - класс Telnet представляет соединение к серверу.
 * в данном случае, ему передается только IP-адрес, но можно передать и порт, к которому нужно подключаться
* ```read_until``` - похож на метод ```expect``` в модуле pexpect. Указывает до какой строки следует считывать вывод
* ```write``` - передать строку
* ```read_very_eager``` - считать всё, что получается


Выполнение скрипт:
```
$ python 2_telnetlib.py "sh ip int br"
Username: nata
Password:
Enter enable secret:
Connection to device 192.168.100.1

R1#terminal length 0
R1#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.1   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.1.10.1       YES manual up                    up
FastEthernet0/1.20     10.1.20.1       YES manual up                    up
FastEthernet0/1.30     10.1.30.1       YES manual up                    up
FastEthernet0/1.40     10.1.40.1       YES manual up                    up
FastEthernet0/1.50     10.1.50.1       YES manual up                    up
FastEthernet0/1.60     10.1.60.1       YES manual up                    up
FastEthernet0/1.70     10.1.70.1       YES manual up                    up
R1#
Connection to device 192.168.100.2

R2#terminal length 0
R2#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.2   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.2.10.1       YES manual up                    up
FastEthernet0/1.20     10.2.20.1       YES manual up                    up
FastEthernet0/1.30     10.2.30.1       YES manual up                    up
FastEthernet0/1.40     10.2.40.1       YES manual up                    up
FastEthernet0/1.50     10.2.50.1       YES manual up                    up
FastEthernet0/1.60     10.2.60.1       YES manual up                    up
FastEthernet0/1.70     10.2.70.1       YES manual up                    up
R2#
Connection to device 192.168.100.3

R3#terminal length 0
R3#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.100.3   YES NVRAM  up                    up
FastEthernet0/1        unassigned      YES NVRAM  up                    up
FastEthernet0/1.10     10.3.10.1       YES manual up                    up
FastEthernet0/1.20     10.3.20.1       YES manual up                    up
FastEthernet0/1.30     10.3.30.1       YES manual up                    up
FastEthernet0/1.40     10.3.40.1       YES manual up                    up
FastEthernet0/1.50     10.3.50.1       YES manual up                    up
FastEthernet0/1.60     10.3.60.1       YES manual up                    up
FastEthernet0/1.70     10.3.70.1       YES manual up                    up
R3#
```

Мы не будем подробнее останавливаться на telnetlib. Остальные методы, которые поддерживает модуль, можно посмотреть в документации.

Документация модуля telnetlib: [telnetlib](https://docs.python.org/2/library/telnetlib.html)

