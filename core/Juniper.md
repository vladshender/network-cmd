## Стандартна перевірка порту
##### Перегляд інформації про порт або інтерфейс
    show interfaces xe-a/b/c або ae8(агрегований лінк)
    show interfaces ae5.9393
##### Перeгляд розширеної інформації по інтерфейсу
	Дозволяє подивитись дропи пакетів та СРС помилки
	Якщо конкретно треба СРС, то можна додати | match CRC
    show interfaces xe-a/b/c extensive 
    show interfaces ae5.9393 extensive
##### Перегляд оптичних показників по інтерфейсу.
	Для користувача center недоступна, треба переходити в привілегійовий режим, через пам доступна
    show interfaces diagnostics optics xe-1/2/3
##### Перегляд трафіку на інтерфейсі або порту в real-time
	monitor interface xe-a/b/c
    monitor interface ae5.9393
## Перевірка абонента НЕ DHCP
	show bridge mac-table interface ae0.[знову вставляємо цифри з команди пошуку irb]
	show arp | match ip or mac
	show route ip | match irb
	show route table l3vpn-obu.ua ip client | match irb
	show configure | display set | match xxxx - ae0.xxxx
	monitor interfaceae0.xxxx
## Перевірка абонента DHCP
	show subscribers | match ip or name node or mac
	show dhcp relay binding ip client
	show configure | display set | match ae0.xxxx
## Пінг абонентів, обладнання та сайтів
	ping ip clien
	ping routing-instance l3vpn-obu.ua ip client
	ping routing-instance ZTE-control
	ping routing-instance dslam-control
	ping routing-instance Huawei-control
	ping routing-instance ZTE_NEW-control
	ping ip_site source client_gateway 
	if it is random ping without specifically client
	show interface lo0 - here we take random gateway
	modifications 
	ping ip_client rapid count 1000 size 1472 do-not-fragment
	traceroute ip_site source client_gateway 
	**Для пінгу з Бордерів(-BR-)**
	Шлюз з якого буде йти пінг потрібно взяти з будь якої bgp сесії, а саме local ip address
## Переноси вланів
	Потрібно зайти в конфіг режим
	виконати вказані команди - set ....
	сommit
	run clear dhcp relay binding interface ae0.xxxx - інтер з помилки
	і далі commit, поки не закомітить без помилок
## Перевірка стану самого обладнання
show logging messages
show bgp neigbour
show bgp summary
show chassis re
