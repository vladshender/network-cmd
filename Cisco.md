

## Cisco
##### Подивись статус та опис всіх портів
    show interface des | brief
##### Подивись чи приходить мак на порт
    show mac address-table interface Gi/XGi
##### Перевірити чи приходять маки у влані
    show mac address-table vlan X
##### Перевірити на яких портах є влан
    show vlan id 3301
##### Пошук логів по кокретному порту
    show log | include 1/21
##### Перевірити uptime обладнання
    show version 
##### Перегляд оптичних показників
    show interface transceiver detail
##### Перегляд статусу блоків живлення, охолодження, температури
    show env all    
##### Перевірити на яких портах є влан
    show vlan id 3301
##### Вимнкути\увімкнути порт
    configure terminal
    inteface Gi1/21
    shutdown
    no shutdown

