### Стандартна перевірка
##### Перегляд інформації по інтерфейсам
    show interface brief
    show interface description
    show interface gigaethernet 1/1/23
##### Перегляд МАС-адреси по порту
    show mac-address dynamic gigaethernet 1/1/23
    show mac-address dynamic vlan 602
##### Перегляд логів
    В залежності від моделі можуть буть різні команди для перегляду логів, logging history зазвичай зависає на певний час і з цим нічого не поробиш і якщо в цей час пінгувати обладнання, то будуть втрати, але це така фіча.
    show logging history 
    show logging history | include 1/1/23
    show logging buffer 
    show logging buffer | include 1/1/23 
    show alarm log | include 1/18 
    show alarm active | include 1/18
## Додатково
##### Перевірка uptime, софту, дати
    show version
##### Перегляд оптичних показників порту
    show transceiver ddm gigaethernet 1/1/28 detail
##### Перегляд історії помилок оптичних показників
    show transceiver ddm alarm history 

