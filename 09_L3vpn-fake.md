## on any Juniper
    show route table  l3vpn-obu.ua.inet  172.19.50.45 extensive | match origin                                 

AS path: I  (Originator)
Originator ID: `195.5.8.28`

#### on 195.5.8.28 --> 10.171.36.28
    show route table  l3vpn-obu.ua.inet  172.19.50.45 | match irb
Next hop: `via` irb.`7240`, selected

    show configuration | display set | match 
#### output
    set interfaces ae0 unit 7240 vlan-tags outer 1044
    set interfaces ae0 unit 7240 vlan-tags inner 606
    set interfaces irb unit 7240 description "Configured for customer AKCIONERNE TOVARICTVO _UKRTRANCGAZ_ SID (ukrtransgaz_opory@ethernet.atutg.ua)"


## on CSS0

<lv-HW-S9312-CSS0>
    display vlan 1044

```    
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
--------------------------------------------------------------------------------

VID  Type    Ports                                                          
--------------------------------------------------------------------------------
1044 common  TG:Eth-Trunk106(U) Eth-Trunk126(U) Eth-Trunk127(U)                 

VID  Status  Property      MAC-LRN Statistics Description      
--------------------------------------------------------------------------------
1044 enable  default       enable  disable    VLAN 1044                         
```

106 downstream
126 - upstream
127 - upstream ( see in if description )


---

## on Juniper

#### MAC абонента
    show bridge mac-table interface ae0.

#### пинг абонента
    ping routing-instance l3vpn-atutg.ua 172.19.50.45 rapid count 1000 

#### пинг обладнання в яке включений абонент
    ping routing-instance dslam-control 192.168.44.226 rapid count 1000

#### трафік на інтерфейсі
    monitor interface ae0.



