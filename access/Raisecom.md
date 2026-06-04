## Стандартна перевірка

### **Перегляд інформації по інтерфейсах**  
_Щоб отримати загальну інформацію про інтерфейси на обладнанні:_  
- **Перегляд всіх інтерфейсів**:
    ```bash
    show interface brief
    ```

- **Перегляд опису всіх інтерфейсів**:
    ```bash
    show interface description
    ```

- **Перегляд конкретного інтерфейсу (наприклад, GigaEthernet 1/1/23)**:
    ```bash
    show interface gigaethernet 1/1/23
    ```

### **Перегляд MAC-адрес на порту**  
_Команди для перегляду MAC-адрес на певному порту або в VLAN:_  
- **Перегляд динамічних MAC-адрес на порту (наприклад, GigaEthernet 1/1/23)**:
    ```bash
    show mac-address dynamic gigaethernet 1/1/23
    ```

- **Перегляд динамічних MAC-адрес в певному VLAN (наприклад, VLAN 602)**:
    ```bash
    show mac-address dynamic vlan 602
    ```

### **Перегляд логів**  
_Команди для перегляду логів на обладнанні._  
_В залежності від моделі, можуть бути різні команди для перегляду логів. Логування зазвичай може "зависати" на певний час, і це може призвести до втрат пінгів під час роботи з логами. Це особливість деяких моделей._

- **Перегляд історії логів**:
    ```bash
    show logging history
    ```

- **Перегляд історії логів з фільтром (наприклад, для порту 1/1/23)**:
    ```bash
    show logging history | include 1/1/23
    ```

- **Перегляд поточного буфера логів**:
    ```bash
    show logging buffer
    ```

- **Перегляд буфера логів з фільтром (для порту 1/1/23)**:
    ```bash
    show logging buffer | include 1/1/23
    ```

- **Перегляд активних алармів з фільтром (для порту 1/18)**:
    ```bash
    show alarm log | include 1/18
    ```

- **Перегляд активних алармів**:
    ```bash
    show alarm active | include 1/18
    ```

## Додатково

### **Перевірка uptime, софту, дати**  
_Команди для перегляду часу роботи пристрою, версії програмного забезпечення та поточної дати:_  
- **Перегляд інформації про систему (uptime, версія ПО, поточна дата)**:
    ```bash
    show version
    ```

### **Перегляд оптичних показників порту**  
_Перегляд детальних оптичних показників для конкретного порту:_  
- **Перегляд оптичних показників для порту GigaEthernet 1/1/28**:
    ```bash
    show transceiver ddm gigaethernet 1/1/28 detail
    ```

### **Перегляд історії помилок оптичних показників**  
_Перегляд історії алармів та помилок для оптичних показників:_  
- **Перегляд історії помилок оптичних показників**:
    ```bash
    show transceiver ddm alarm history
    ```

## Оновлення ПЗ -- оформити
Оновлення ПЗ 2624G
 
1) download bootstrap tftp 10.36.202.33 ISCOM2600G_BOOT_1.20.7
 
 
2 ) download system-boot tftp 10.36.202.33 ISCOM2600_3.50.365_10052018
 
Після завантаження 2-х файлів перегружаємо
 
 
1) download bootstrap tftp 10.36.202.33 ISCOM2600G_BOOT_2.0.11
2)download system-boot tftp 10.36.202.222 ISCOM2600G_SYSTEM_3.62.217_20220414
 
ip dhcp information option circuit-id format "%h eth %s/%pn:"
 
 
 
 
 
Злити з комутатора на сервер..!!!
 
upload bootstrap tftp 10.36.202.33 <ISCOM2600G_BOOT_1.20.7>
 

upload system-boot tftp 10.36.202.33 <ISCOM2600_3.50.365_10052018>
 
 
__________________2624GF_____________
 
 
upload bootstrap tftp 10.36... ISCOM2600G_BOOT_2.0.11
 

upload system-boot tftp 10.36... ISCOM2600G-HI_SYSTEM_3.50.336_20180611
 
 
Оновлення ПЗ 2624GF
 
1) download bootstrap tftp 10.36.202.33 ISCOM2600G_BOOT_2.0.11
 
2 ) download system-boot tftp <FTP-IP> ISCOM2600G-HI_SYSTEM_3.73.115_20240116
 
<FTP-IP>В вас це мабуть 10.36.202.222
 
 
_______________________2924_3024___________________________________________-
 
download system-boot tftp 10.36.202.33 ISCOM3000G_B_SYSTEM_3.611495706407.189_20200804
 
 
_______________________5600_______actual_soft__________________
 
Product Name: ISCOM S5600-28C-EI-24F
Hardware Version: A.01
Software Version: 3.60.309(Compiled Feb 24 2020 18:39:04)
ROS Version: ROS_5.2.1_20200224
REAP Version:3.0
Bootrom Version: 1.4.9
 
download system-boot tftp 10.36.202.33 ISCOM_S5600-28C-EI-24F_SYSTEM_3.60.309_2_24_2020
ISCOMS5600-EI_SYSTEM_3.61.57_20201118
