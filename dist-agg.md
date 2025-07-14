Huawei
Перегляд інформації по інтерфейсам (фізичні та логічні)
display interface GigabitEthernet 1/6/1/0
display interface XGigabitEthernet 1/2/0/0
display interface Eth-Trunk0

Перегляд мак-адрес на обладнанні
display mac-address  
Перегляд мак-адрес на інтерфейсі
display mac-address XGigabitEthernet 1/0/8 (Eth-Trunk, GigabitEthernet)

Перегляд логів на обладнанні
display logbuffer
display trapbuffer

Перегляд оптичних показників на інтерфейсі
display transceiver interface [g/xg] verbose

Cisco
Перегляд інформації по інтерфейсам (фізичні та логічні)
show interfaces gigabitEthernet 1/1 (0/1)
show interfaces tenGigabitEthernet 1/29
show interfaces Po1

Перегляд всіх мак-адрес на обладнанні
show mac address-table 

Перегляд мак-адрес на інтерфейсі
show mac address-table interface gigabitEthernet 1/1 (tenGigabitEthernet, Po1)

show mac address-table vlan []

Перегляд логів на обладнанні
show logging 

Перегляд оптичних показників
show interface transceiver

ZTE
show interface | include ifindex: 27
show interface gei-0/1/0/24 (xgei-, smartgroup1)
show interface smartgroup1

Перегляд всіх мак-адрес на обладнанні
show mac table
show mac table interface gei-0/1/0/24 (xgei-, smartgroup1)
show mac table vlan []

Перегляд оптичних показників
show optical-inform details rx-power interface []
show optical-inform details tx-power interface []
