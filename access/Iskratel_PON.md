## Стандартна перевірка
Команди однакові в Iskratel MSAN SI3000(ті, що мають номер в назві 40000+)
##### Перегляд стану всіх портів та ONU
    show port all
##### Перегляд інформації по конкретному порту
    show port 0/6/2
##### Переглядаємо МАС-адрес на порту.
    show mac-addr-table interface 0/1/2
    show mac-addr-table vlan 602
##### Переглянути детальну інформацію про ОНУ
    show onu interface 0/1/2
##### Перегляд логів на обладнанні
    show logging file MsgErr
## Додаткова перевірка
##### Перегляд інформації про пристрій(mac, uptime)
    show sysinfo 
    show version
    show hardware
    show boot package
    show shelf-id 
##### Перезавантажити ONU
    configure
    interface 0/1/2
    shutdown
    no shutdown
    Паралельно треба завершити сесію в АРМУС
##### Перегляд DHCP сесії по інтерфейсу
    show dhcpsnooping interface 0/5/33
##### Очистити DHCP сесію
    clear dhcpsnooping interface 0/5/33/2
    **x/y/z/2 - 2 можна взяти переглянувти маки або сесію по інтерфейсу**
