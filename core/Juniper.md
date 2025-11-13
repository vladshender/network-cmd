## Стандартна перевірка порту

- **Перегляд інформації про порт або інтерфейс**:
    - Для перегляду інформації про фізичний порт (XGigabitEthernet або агрегований лінк):
        ```bash
        show interfaces xe-a/b/c або ae8
        ```
    - Для перегляду інформації по логічному інтерфейсу:
        ```bash
        show interfaces ae5.9393
        ```

- **Перегляд розширеної інформації по інтерфейсу**:
    _Ця команда дозволяє побачити статистику пакетів, зокрема дропи та CRC помилки. Для конкретних СРС помилок можна додати фільтр `| match CRC`._
    ```bash
    show interfaces xe-a/b/c extensive
    show interfaces ae5.9393 extensive
    ```

- **Перегляд оптичних показників по інтерфейсу**:
    _Для користувачів `center` доступність обмежена. Щоб отримати доступ, потрібно увійти в привілегійовий режим._
    ```bash
    show interfaces diagnostics optics xe-1/2/3
    ```

- **Перегляд трафіку на інтерфейсі в реальному часі**:
    ```bash
    monitor interface xe-a/b/c
    monitor interface ae5.9393
    ```

## Перевірка абонента НЕ DHCP

- **Перегляд конфігурації абонента**:
    - Для `l3vpn`:
        ```bash
        show route table l3vpn-obu.ua ip client | match irb
        ```
    - Для `profi`:
        ```bash
        show route ip | match irb
        ```
    - Для загальної конфігурації:
        ```bash
        show configure | display set | match xxxx
        ```
        _Де `xxxx` береться з команд пошуку по інтерфейсу `ae0.xxxx`._

- **Перегляд MAC-адрес**:
    - Перевірка MAC-адрес на порту:
        ```bash
        show bridge mac-table interface ae0.xxxx
        ```
    - Перевірка відповідності IP та MAC в ARP таблиці:
        ```bash
        show arp | match ip or mac
        ```

## Перевірка абонента DHCP

- **Перевірка активних сесій DHCP**:
    - Перевірка сесії абонента:
        ```bash
        show subscribers | match ip or name node or mac
        ```
    - Перегляд загальної кількості активних сесій:
        ```bash
        show subscribers summary
        ```

- **Перевірка прив'язки DHCP**:
    - Перегляд прив'язки для IP клієнта:
        ```bash
        show dhcp relay binding ip-client
        ```
        _Ця команда покаже інтерфейс DHCP абонента (наприклад, `demux0.xxxxx`) та відповідний логічний інтерфейс._

- **Перегляд інтерфейсу DHCP абонента**:
    ```bash
    show interface demux0.xxxxx extensive
    ```

- **Перегляд шлюзу абонента**:
    ```bash
    show configure | display set | match xxxx
    ```
    _Де `xxxx` береться з інтерфейсу `ae0.xxxx`._

## Перевірка BGP

- **Перевірка стану BGP сесії**:
    - Перевірка загального стану BGP:
        ```bash
        show bgp summary
        ```
    - Детальна інформація по BGP сесіям:
        ```bash
        show bgp neighbour
        ```
    - Перевірка конкретної BGP сесії:
        ```bash
        show bgp neighbour ip-client
        ```

- **Перевірка переданих та отриманих IP-prefixes**:
    - Для перевірки рекламованих через BGP IP-префіксів:
        ```bash
        show route advertising-protocol bgp ip-client
        ```
    - Для перевірки отриманих через BGP IP-префіксів:
        ```bash
        show route receive-protocol bgp ip-client
        ```

## Пінг абонентів, обладнання та сайтів

- **Пінг за маршрутом**:
    - Перевірка маршруту до ресурсу:
        ```bash
        show route ip_site
        ```

- **Пінг абонентів**:
    - Пінг абонента з білою IP адресою (GPON, DSL, Profi, FTTB):
        ```bash
        ping ip-client
        ```
    - Пінг абонентів L3VPN:
        ```bash
        ping routing-instance l3vpn-obu.ua ip-client
        ```

- **Пінг обладнання**:
    - Пінг обладнання доступу (IP 10.168.x.x):
        ```bash
        ping routing-instance ZTE-control
        ```
    - Пінг обладнання доступу з IP 192.168.x.x:
        ```bash
        ping routing-instance dslam-control
        ```
    - Пінг Huawei агрегації:
        ```bash
        ping routing-instance Huawei-control
        ```
    - Пінг ZTE агрегації:
        ```bash
        ping routing-instance ZTE_NEW-control
        ```

- **Пінг з шлюзу абонента**:
    ```bash
    ping ip_site source client_gateway
    ```

### Перевірка доступу до ресурсу

- **Швидка перевірка доступу до ресурсу**:
    - Для перевірки шлюзів на маршрутизаторі:
        ```bash
        show interface lo0
        ```
    - Використовуйте знайдений шлюз для пінгу:
        ```bash
        ping <resource-ip>
        ```

### Модифікації для пінгу

- **Пінг з великим розміром пакета**:
    ```bash
    ping ip-client rapid count 1000 size 1472 do-not-fragment
    ```

- **Трасування до ресурсу через шлюз абонента**:
    ```bash
    traceroute ip_site source client_gateway
    ```

### Пінг з Border маршрутизатора

- **Пінг через BGP шлюз**:
    _Шлюз з якого буде йти пінг береться з будь-якої BGP сесії, зокрема з поля `Local: ip-address`._
    ```bash
    ping <resource-ip> source <bgp-local-ip>
    ```

## Переноси VLAN

- **Процес перенесення VLAN**:
    1. Зайти в конфігураційний режим:
        ```bash
        configure
        ```
    2. Вставити вказані команди (зазвичай через пошту):
        ```bash
        set ...
        ```
    3. Застосувати зміни:
        ```bash
        commit
        ```
    4. Якщо з'являється помилка, виконайте команду для очищення DHCP прив'язки:
        ```bash
        run clear dhcp relay binding interface ae0.xxxx
        ```
    5. Повторіть `commit` до успішного завершення.

## Перевірка стану обладнання

- **Перегляд логів**:
    - Останні логи:
        ```bash
        show log messages
        ```
    - Старіші логи (наприклад, `chassisd.0.gz`):
        ```bash
        show log chassisd.0.gz
        ```

- **Перегляд активних алармів**:
    ```bash
    show chassis alarms
    ```

- **Перевірка стану комплектуючих**:
    ```bash
    show chassis environmental
    ```

- **Перевірка стану блоків живлення**:
    ```bash
    show chassis power
    ```

- **Інші команди для перевірки обладнання**:
    ```bash
    show chassis ?
    ```

