## CSS

L2vpn, L3vpn, profi mac дивитися по vlan !

  display interface GigabitEthernet 1/1/0/22
  
  displ mac-address vlan 3902
  
  displ mac-address vlan 3903 | include  GE1/1/0/16
  
  displ mac-address vlan 3903 | include GE1/1/0/22
  
  displ mac-address vlan 3902 | include  GE1/1/0/16
  
  displ mac-address vlan 3903
  
  display transceiver interface GigabitEthernet 1/1/0/16
  
  display transceiver interface GigabitEthernet 1/1/0/16 verbose
  
  display transceiver interface GigabitEthernet 1/1/0/22 verbose
  


## JUN

#### полісери

    show configuration interfaces ae0 | match "unit| vlan-id 3903"

```
unit 7807 {
unit 7808 {
    vlan-id 3903;
unit 7809 {
unit 7810 {
unit 7811 {
```

    show configuration | display set | match 7808



