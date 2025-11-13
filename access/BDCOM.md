## Стандартна перевірка ONU

- **Увійти в привілегійовий режим**:
    ```bash
    enable
    ```

- **Перегляд стану всіх інтерфейсів**:
    ```bash
    show interface brief
    ```

- **Перегляд стану конкретної ONU на порту**:
    _Для перевірки стану ONU на конкретному порту, вказати номер порту (наприклад, `0/4:42`):_
    ```bash
    show interface ePON 0/4:42
    ```

- **Перегляд MAC-адреси від ONU**:
    _Для перегляду MAC-адреси ONU на вказаному порту:_
    ```bash
    show mac address-table interface ePON 0/2:32
    ```

- **Перегляд MAC-адреси по VLAN**:
    _Для перевірки MAC-адрес в певному VLAN:_
    ```bash
    show mac address-table vlan 604
    ```

- **Перегляд логів по ONU**:
    _Для перегляду логів, пов'язаних з конкретною ONU:_
    ```bash
    show logging | include EPON0/4:11
    ```

- **Перегляд оптичних показників по всіх портах**:
    _Для загального перегляду оптичних показників по портах ePON:_
    ```bash
    show epon optical-transceiver-diagnosis
    ```

- **Перегляд оптичних показників для конкретної ONU**:
    - Для конкретного порту та ONU:
        ```bash
        show epon interface epon 0/3:1 onu ctc optical-transceiver-diagnosis
        ```
    - Або:
        ```bash
        show epon optical-transceiver-diagnosis interface EPON0/1:4
        ```

- **Перезавантаження ONU або OLT**:
    _Для перезавантаження ONU або OLT на конкретному порту:_
    ```bash
    epon reboot onu\olt interface EPON 0/1:1
    ```

## Інше

- **Перевірка Uptime обладнання та поточного часу**:
    _Для перевірки часу роботи та поточного часу на пристрої:_
    ```bash
    show version
    ```

- **Перегляд поточної конфігурації**:
    ```bash
    show running-config
    ```

- **Знайти DHCP сесію абонента на обладнанні**:
    _Для пошуку сесії DHCP абонента по його MAC-адресі:_
    ```bash
    show ip dhcp-relay snooping binding all | include mac абонента
    ```

- **Очистити DHCP сесію абонента на обладнанні**:
    _Для очищення DHCP сесії за MAC-адресою або IP-адресою абонента:_
    ```bash
    clear dhcp-relay snooping binding mac <MAC> або ip <IP>
    ```

- **Додавання VLAN на порт ONU**:
    _Для додавання необхідного VLAN на порт ONU:_
    ```bash
    configure
    interface EPON 0/1:1
    epon onu port 1 ctc vlan mode tag 1414
    ```

