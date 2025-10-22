## PON ISkratel 

#### rv-zdolbun-grush15-pon-ik1s2# show port all 
    show port all

Якщо нам потрібно перевірити х/y/z, то спочатку перевіряємо x/y аби були в Up.
Якщо Down – нема сенсу далі перевіряти.

#### rv-zdolbun-grush15-pon-ik1s2# show port 0/6/2

    show port 0/6/2 
Переглядаємо МАС-адрес на порту. 
#### rv-zdolbun-grush15-pon-ik1s2# show mac-addr-table interface 0/6/35

    show mac-addr-table interface 0/6/35 
Переглядаємо інформацію по пристрою(час роботи). 
#### rv-zdolbun-grush15-pon-ik1s2# show sysinfo

    show sysinfo 
Перегляд логів
#### dc-svyatogirsk-maz54-pon-ik1s1# show logging file MsgErr

    show logging file MsgErr 

#### reset port
    clear ipsg interface 0/5/33/2
    
    show dhcpsnooping interface 0/5/33
