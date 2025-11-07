## Стандартна перевірка
##### Перевірити стан порту
    display interface description
    display intergace brief
    display interface Ethernet 0/0/5
##### Перевірити мак адреси
    display mac-address Ethernet 0/0/5
    display mac-address vlan 602
##### Переглянути логи
    display logbuffer | include Ethernet0/0/5
##### Переглянути логи(СРС помилки)
    display trapbuffer | include Ethernet0/0/5
##### Перевірити оптичні показники на інтерфейсі
    display transceiver interface Ethernet 0/0/3 verbose
##### Переглянути конфігурацію
    display current-configuration
##### Вимкнути інтерфейс 
    system-view - зайти в конфіг режим
    interface Eth0/0/5 - зайти в конфігурування конкретного інтерфейсу
    shutdown - вимкнути порт адміністративно
    undo shutdown - увімкнути порт
    quit - вийти з конфіг режиму
