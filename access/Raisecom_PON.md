## Стандартна перевірка
##### Зайти в привілегійовий режим 
    enable (далі пароль centerukrtel1) 
##### Перегляд статусу всіх ONU
    show interface gpon-onu online-information
#####  Детальніша інформація по ону
    show gpon-onu 1/1/4 information
    show gpon-onu 1/1/4 detail-information
##### Перегляд МАС-адреси по ONU 
    show mac-address-table l2-address interface gpon-onu 1/1/10 
    show mac-address-table l2-address vlan 602 
##### Перегляд логів 
    show logging history | include x/x/x 
## Додатково
##### Подивитись uptime, soft, дату
    show version
##### Перегляд оптичних показників 
    show interface gpon-olt transceiver rx-onu-power - по всім ONU на порту
    show gpon-onu 1/2/113 transceiver - по конкретній ONU
##### Перезавантажити ONU
    config
    gpon-onu 1/1/7
    reboot now

