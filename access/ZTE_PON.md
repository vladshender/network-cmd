## Стандартна перевірка
##### Перегляд всіх ONU на порту
    1/3 - пишеться завжди, далі номер порту(іноді може бути 1/1 і тоді буде 1/1/1, де остання 1 це номер порту)
    DyingGasp - статус ОНУ означає, що вона на "на останньому подиху, щоб упасти" - перевіряти далі
    show pon onu information gpon_olt-1/3/15
##### Перегляд інформації по ONU 
    show gpon onu detail-info gpon_onu 1/3/1:1
    show pon onu information gpon_onu-1/3/1:1
##### Якщо необхідно переглянути МАС-адресу на порті. (переглядаємо на всіх портах)
    show mac - перегляд всіх маків
    show mac interface gpon_onu 1/3/1:2 -перегляд маку по конкретній ОНУ
    show mac vlan 602 - перегляд маку у влані
##### Перегляд логів. 
    show logging alarm 
## Додатково
##### Перегляд uptime, soft
    show software 
##### Перегляд оптичних показників
    show pon power olt-rx gpon_olt-1/3/7 - перегляд оптики по всьому порту 7
    show pon power attenuation gpon_onu-1/3/1:6 - перегляд оптики по ОНУ
###### Перегляд активної DHCP сесії
    show ip dhcp snooping dynamic database - перегляд всіх сесій
    show ip dhcp snooping dynamic ip - перегляд чи існує сесії по IP
    show ip dhcp snooping dynamic port vport-1/3/7.3:1 - ":1" додається просто до номеру ОНУ
###### Видалити мак на ОНУ та IP(DHCP сесію)
    configure terminal
    mac delete dynamic interface vport-1/3/7.3:1
    ip dhcp snooping clear interface vport-1/3/7.3:1 CA21.72EB.58BC vlan 1300
##### Перезавантажити ОНУ
    configure terminal
    interface gpon_onu-1/3/1:39 
    reset
