## Juniper

#### Перегляд інформації по інтерфейсам (фізичні та логічні)
    show interfaces xe-a/b/c
####
    show interfaces ae(1,2,3)



#### Перeгляд розширеної інформації по інтерфейсу
    show interfaces xe-a/b/c extensive
####
    show interfaces ae(1,2,3) extensive

#### Перегляд оптичних показників по інтерфейсу.
    show interfaces diagnostics optics xe-1/2/3

#### Перегляд лічильників інтерфейсу.
    monitor interface 

#### Перегляд ARP табл по IRB аб-та L3vpn, Prof
    show arp | match 7182 

```
00:09:0f:09:00:12 94.179.118.82   94.179.118.82             irb.7182 [ae0.7182]     none
00:09:0f:09:00:12 94.179.118.83   94.179.118.83             irb.7182 [ae0.7182]     none
bc:24:11:01:72:df 94.179.118.84   94.179.118.84             irb.7182 [ae0.7182]     none
```
