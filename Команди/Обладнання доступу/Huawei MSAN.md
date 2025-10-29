## Huawei-56

##### Переглянути стан інтерфейсу
    display board 0/16
##### перегляд МАС-адреси
    enable
#####    
    display mac-address port 0/11/1
##### Відібрати по ONT
    mac-address port 0/11/1 ont 11
##### Відібрати по vlan
    display mac-address vlan 602 
##### Перегляд алармів, які є зараз на порту або ону абонента
    display alarm active all - всі актуальні логи
    -----
    display alarm active alarmparameter 0/2/4 5 - де 6 це ону абонента на порту 4 слота 2 фрейма 0
    display alarm active alarmparameter 0/2/4 - аналогічно перегляд актуальних алармів по порту
##### Перегляд історії алармів, які були на порту або ону абонента
    display alarm history all - всі актуальні логи
    -----
    display alarm history alarmparameter 0/2/4 5 - де 6 це ону абонента на порту 4 слота 2 фрейма 0
    display alarm history alarmparameter 0/2/4 - аналогічно перегляд актуальних алармів по порту
#### reboot port
через систему управління
