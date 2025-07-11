    show route table l3vpn-atutg.ua.inet 172.19.50.45 extensive | match origin                                 

AS path: I  (Originator)
Originator ID: `195.5.8.28`

#### on 195.5.8.28 --> 10.171.36.28
    show route table l3vpn-atutg.ua.inet 172.19.50.45 extensive | match irb
Next hop: `via` irb.`7240`, selected

    show configuration | display set | match 7240

set interfaces ae0 unit 7240 vlan-tags outer 1044
set interfaces ae0 unit 7240 vlan-tags inner 606
set interfaces irb unit 7240 description "Configured for customer AKCIONERNE TOVARICTVO _UKRTRANCGAZ_ SID (ukrtransgaz_opory@ethernet.atutg.ua)"


#### on CSS0

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


{master}
center@lv-juniper-MX960-pe-l1> show bridge mac-table ae0.7240 
error: Incomplete mac address

{master}
center@lv-juniper-MX960-pe-l1> show bridge mac-table interface ae0.7240

MAC database for interface ae0.7240

MAC flags       (S -static MAC, D -dynamic MAC, L -locally learned, C -Control MAC
    O -OVSDB MAC, SE -Statistics enabled, NM -Non configured MAC, R -Remote PE MAC, P -Pinned MAC, FU - Fast Update)

Routing instance : default-switch
 Bridging domain : vlan-7240, VLAN : none
   MAC                 MAC      Logical          NH     MAC         active
   address             flags    interface        Index  property    source
   78:9a:18:b1:ab:c8   D        ae0.7240        

{master}
center@lv-juniper-MX960-pe-l1> ping routing-instance l3vpn-atutg.ua 172.19.50.45 rapid count 1000 
PING 172.19.50.45 (172.19.50.45): 56 data bytes
............^C
--- 172.19.50.45 ping statistics ---
13 packets transmitted, 0 packets received, 100% packet loss

{master}
center@lv-juniper-MX960-pe-l1> 




