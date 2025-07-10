## HW_FTTB
####
    display interface Ethernet 0/0/5
####  
    display mac-address Ethernet 0/0/5
####  
    display logbuffer
####  
    display logbuffer | include Ethernet0/0/5
####  
    display history-command


## PE з сессії (F11 - subscriber F8 session ) в УС

####
     show dhcp relay binding 82.207.105.88

####
    ping 82.207.105.88 rapid count 1000
####
    show subscribers | match 82.207.105.88 

demux0.3221533785               82.207.105.88                           cg-ivanafranka4a-f-hw1s1 eth 0/0/5:.BC620E4CB797       default:default      

    monitor interface demux0.3221533785
