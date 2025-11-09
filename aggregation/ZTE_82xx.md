## Стандартна перевірка  
##### Перегляд стану портів
  show interface description
##### Перегляд маків
  show mac table 
  show mac table interface gei-0/1/0/40
  show mac table vlan 1110
##### Перегляд логів
  show logging alarm | include 0/1/0/40
## Додатково
##### Перегляд оптичних показників
  show optical-inform detail info interface gei-0/1/0/40
##### Переглянути конфігурацію
  show running-config
  show running-config-interface gei-0/1/0/40
##### Перегляд uptime, soft
  show version
