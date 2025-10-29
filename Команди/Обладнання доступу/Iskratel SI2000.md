### Iskratel (mban - SI2000)
    show system info
    show shelf
    show shelf-id
    show b p
#### Отримання інформації про порт. 
     show dsl port 18 
Примітка. Піднятий чи лежить порт Operational State (Up/Down). 
#### Перегляд МАС-адрес на порті. 
     show bridge mactable interface dsl18:1_33 
     show bridge mactable interface dsl18:1_40 
Примітка. Додати коли 1_33 або 1_40 для DHCP та PPPoE (вказується в АРМУС). Може бути лише в одному з них, в разі відсутності в обох командах – МАС-адреса відсутня. 
#### Переглянути логи на обладнанні. 
     show alarm 
