## PON ZTE

##### Перегляд портів. 

`rv-mickevycha2-ats26-pon-zt7s1# show pon onu information gpon_olt-1/1/15`

    show pon onu information gpon_olt-

> [!NOTE]  
> Примітка. 1/1 або 1/3 прописуємо та 15 або 3 підставляємо згідно інформації в АРМ УС. \
> Якщо в графі State working – порт піднятий, Los – впав по фізиці, DyingGasp – «Доживає останнє», працює, але йому погано. 

##### Якщо необхідно переглянути МАС-адресу на порті. (переглядаємо на всіх портах)

`rv-mickevycha2-ats26-pon-zt7s1# show mac dynamic`

    show mac dynamic
##### Перегляд маків по влану
    show mac vlan 
##### Перегляд логів. 
    show logging alarm 
##### Перегляд аптайм обладнання
    show software 
##### Перегляд оптичних показників
    show pon power olt-rx gpon_olt-1/3/7
#####
    show pon power attenuation gpon_onu-1/3/1:6 

##### логи по інтерфейсу
    show pon onu information gpon_onu-1/3/1:1


#####
     show ip dhcp snooping dynamic database
#####
     show ip dhcp snooping dynamic ip
#####
     show ip dhcp snooping dynamic port
#####

     
