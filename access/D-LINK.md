
## Стандартна перевірка
##### Стан інтерфейсів
    show ports
##### Перевірити МАС-адреси на порту
    show fdb port 2
##### Перевірити МАС-адреси у влані
    show fdb vlanid 602
##### Перевірити оптичні показникі
    show ddm ports status 
##### Перевірити логи
    show log 
## Зміни порту
##### Вимкнути\увімкнути порт
     config ports 1:2 state disable
     config ports 1:2 state enable
##### Зміна швидкості на порту
     config ports 1:2 speed 1000
