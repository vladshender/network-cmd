## Стандартна перевірка
##### Переглянути стан портів на платі
    display board 0/16
##### Перегляд МАС-адреси
    enable - переглянути маки можна в привілегійованому режимі
    display mac-address port 0/11/1
    display mac-address port 0/11/1 ont 11
    display mac-address vlan 3311
##### Перегляд алармів, які є зараз на порту або ону абонента
    display alarm active all - всі актуальні логи
    display alarm active alarmparameter 0/2/4 5 - перегляв актуальних логів для 0 - фрейм, 2 - плата, 4 - порт, 5 - ону
    display alarm active alarmparameter 0/2/4 - аналогічно, але по всьому порту для всіх ону
##### Перегляд історії алармів, які були на порту або ону абонента
    display alarm history all - історія всіх логів
    display alarm history alarmparameter 0/2/4 5 
    display alarm history alarmparameter 0/2/4 
##### Вимкнути порт чи ОНУ
    Через систему управління Huawei NCE
