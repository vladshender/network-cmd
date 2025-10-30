### BDCOM  
##### Щоб увійти в привілегійовий режим
    enable
##### Стан всіх інтерфейсів
    show interface brief
##### Стан конкретної ONU на порту
    show interface ePON 0/4:42
##### Перегляд МАС-адреси від ONU
    show mac address-table interface epoN 0/2:32
##### Перегляд МАС-адреси по vlan
    show mac address-table vlan 604                    
##### Подивитись логи по ONU
    show logging | include EPON0/4:11
##### Подивитись оптичні показники по портам
    show epon optical-transceiver-diagnosis 
##### Подивитись оптичні показники по ONU
    show epon inteface epon 0/3:1 onu ctc optical-transceiver-diagnosis
    ----
    show epon optical-transceiver-diagnosis interface EPON0/1:4   
##### Перезавантажити ONU\OLT 
    epon reboot onu\olt interface EPON 0/1:1
##### Перевірити Uptime обладнання та current time
    show version
##### Подивитись конфігурацію
    show running-config
##### Знайти DHCP сесію абонента на обладнанні  
    show ip dhcp-relay snooping binding all | include mac абонента 
##### Очистити DHCP сесію абонента на обладнанні 
    clear dhcp-relay snooping binding mac...чи...ip ip або mac абонента
##### Додати необхідний влан на порт ONU
    configure
    interface EPON 0/1:1
    epon onu port 1 ctc vlan mode tag 1414

