### BDCOM  
##### Щоб увійти в конфігурацій режим
    enable
##### Стан всіх інтерфейсів
    show interface brief
##### Стан конкретної ONU на порту
    show interface ePON 0/4:42
##### Перегляд МАС-адреси від ONU
    show mac address-table interface epoN 0/2:32
##### Перегляд МАС-адреси по vlan
    show mac address-table vlan 604                    
##### логи
    show logging | include EPON0/4:11
##### оптичні показникі
    show epon optical-transceiver-diagnosis interface EPON0/1:4
##### Uptime обладнання та current time
    show version
##### Подивитись конфігурацію
    show running-config
