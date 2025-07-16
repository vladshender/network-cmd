## PON RAISECOM – в назві обладнання є -pon- 

#### Необхідно зайти в режим Enable. 
`cg-olysh-cherngv29-pon-rc5s1>enable `

#### Перегляд інформації по всім портам 
`cg-olysh-cherngv29-pon-rc5s1#show interface gpon-onu online-information `

####  link RS - ONU
    show interface gpon-onu online-information
####  ONU  -- Subsc
    show gpon-onu 1/1/4 uni eth info 
#### Перегляд МАС-адреси на порті 
    show mac-address-table l2-address interface gpon-onu 1/1/10 
####
    show mac-address-table l2-address vlan 602 
#### Перегляд логів 
    show logging history | include x/x/x 
#### Перегляд оптичних показників 
    show transceiver [ddm gigaEthernte 1/1/0] 
####
    show interface gpon-olt transceiver rx-onu-power  
####
    show gpon-onu 1/2/113 transceiver 
