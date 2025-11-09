##### Перегляд інформації по інтерфейсам (фізичні та логічні)
    display interface description
    display interface GigabitEthernet 1/6/1/0
    display interface XGigabitEthernet 1/2/0/0
    display interface Eth-Trunk0
##### Перегляд мак-адрес на обладнанні
    display mac-address - вивід всіх маків
    display mac-address dynamic vlan 4092 – вивід всіх мас-адрес в vlan-і
    display mac-address dynamic GigabitEthernet 1/1/0/0 – вивід всіх мас-адрес з
    display mac-address 0013-d3c5-d3de – перевірка наявності мас-адреси 
##### Перегляд логів на обладнанні
    display logbuffer
    display trapbuffer - тут можна перевірити наявність СРС на інтерфейсі
##### Перевірка uptime, soft
    display version
##### Перегляд оптичних показників на інтерфейсі
    display transceiver interface XGi1/1/1 verbose
##### Перевірка актуального часу на пристрої
    display clock 
##### Перегляд стану лінійних та керуючих карт
    display device 
#####  Перезавантажити порт
    system-view
    interface Gi1/1/1
    shutdown
    undo shutdown
    quit
