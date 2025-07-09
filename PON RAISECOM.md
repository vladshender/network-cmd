PON RAISECOM – в назві обладнання є -pon- 
Необхідно зайти в режим Enable. 
cg-olysh-cherngv29-pon-rc5s1>enable 
Перегляд інформації по всім портам 
cg-olysh-cherngv29-pon-rc5s1#show interface gpon-onu online-information 
hr-zolochiv-centr27a-pon-rc5s1#show gpon-onu 1/1/4 uni eth info 
Перегляд МАС-адреси на порті 
cg-olysh-cherngv29-pon-rc5s1#show mac-address-table l2-address interface gpon-onu 1/1/10 
cg-olysh-cherngv29-pon-rc5s1#show mac-address-table l2-address vlan 602 
Перегляд логів 
cg-olysh-cherngv29-pon-rc5s1#show logging history | include x/x/x 
Перегляд оптичних показників 
cg-olysh-cherngv29-pon-rc5s1#show transceiver [ddm gigaEthernte 1/1/0] 
show interface gpon-olt transceiver rx-onu-power  
show gpon-onu 1/2/113 transceiver 