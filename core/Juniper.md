## Стандартна перевірка порту
##### Перегляд інформації про порт або інтерфейс
    show interfaces xe-a/b/c або ae8 - перегляд інформації по хgigaethernet(xe) порту або агрегованому лінку(ae8)
    show interfaces ae5.9393 - перегляд інформації по логічному інтерфейсу
##### Перeгляд розширеної інформації по інтерфейсу
	Дозволяє подивитись дропи пакетів та СРС помилки
	Якщо конкретно треба СРС, то можна додати | match CRC
    show interfaces xe-a/b/c extensive 
    show interfaces ae5.9393 extensive
##### Перегляд оптичних показників по інтерфейсу.
	Для користувача center недоступна, треба переходити в привілегійовий режим. Через пам логін команда доступна 
    show interfaces diagnostics optics xe-1/2/3
##### Перегляд трафіку на інтерфейсі або порту в real-time
	monitor interface xe-a/b/c
    monitor interface ae5.9393
## Перевірка абонента НЕ DHCP
##### Наступні 2 команди дозволяють переглянути конфігурацію по абоненту profi, l3vpn
	show route table l3vpn-obu.ua ip client | match irb - для l3vpn
	show route ip | match irb - для profi
	show configure | display set | match xxxx - де хххх береться з ae0.xxxx 
##### Переглянути маків
	Корисно переглянути іноді чи приходить мак від абонента на маршрутизатор
	show bridge mac-table interface ae0.[знову вставляємо цифри з команди пошуку irb] - дозволяє переглянути вивчені макі за певним інтерфейсом
	show arp | match ip or mac - дозволяє переглянути відповідність ip та маку в arp таблиці
## Перевірка абонента DHCP
	show subscribers | match ip or name node or mac - дозволяє побачити чи наявна активна сесія на маршрутизаторі
	show subscripers summary - дозволяє переглянути кількість активних сесій в загальному на маршрутизаторі
	show dhcp relay binding ip-client - вивід команди покаже інтерфейс DHCP абонента - demux0.xxxxx та в якому логічному інтерфейсі він знаходиться ae0.xxxx - цей логічний інтерфейс належить обладнанню доступу, тобто в йому належать багато інтерфейсів DHCP абонентів
	show interface demux0.xxxxx extensive - дозволить побачити які фільтри на обмеження швидкості вставнолені на інтерфейсі DHCP абонента
	show configure | display set | match xxxx - де хххх береться з ae0.xxxx дозволяє знайти шлюз абонента
## Перевірка BGP 
	В BGP сесії state має бути Established, всі інши стани означаю що вона зараз не працює.
	show bgp summary - покаже коротку інформацію по BGP сесіям
	show bgp neigbour - покаже детальну інформацію по BGP сесіям
	show bgp neigbour ip-client - покаже інформацію по конкретній BGP сесії
	show route advertising-protocol bgp ip-clien - покаже ip-prefixes, які ми передаємо через bgp сесію партнеру
	show route receive-protocol bgp ip-clien - покаже ip-prefixes, які ми отримуємо через bgp сесію з партнером
## Пінг абонентів, обладнання та сайтів
	show route ip_site - показує через який інтерфейс йде паршрут до вказаного ресурсу
	ping ip clien - пінг абонентів з білою IP адресою(gpon, dsl, profi, fttb)
	ping routing-instance l3vpn-obu.ua ip-client - пінг абонентів l3vpn
	ping routing-instance ZTE-control - пінг обладнання доступу з IP адресами 10.168.х.х
	ping routing-instance dslam-control - пінг обладнання з IP адресами 192.168.х.х(навіть cisco)
	ping routing-instance Huawei-control - пінг Huawei дистрибуції-агрегації(93xx, 53xx)
	ping routing-instance ZTE_NEW-control - пінг ZTE агрегації(8902)
	ping ip_site source client_gateway - пінг IP адреси(наприклад якогось сайту), де client_gateway - шлюз абонента
	__Якщо треба в рандомний момент перевірити доступ до ресурсу__
	show interface lo0 - виконавши команду, можна знайти деякі шлюзи на маршрутизаторі(закінчуюється ip на .1)
	**Модифікації для пінгу**
	ping ip_client rapid count 1000 size 1472 do-not-fragment - дозволяє відправити 1000 швидких пакетів з розміром 1472 байт нефрагментованими
	traceroute ip_site source client_gateway - виконати трасування до певного ресурсу з шлюза абонента
	**Щоб виконати пінг до певного ресурсу з border маршрутизатора(-BR-)**
	Шлюз з якого буде йти пінг потрібно взяти з будь якої bgp сесії, а саме Local: ip-address
	І виконати аналогічну команду, як вказана вище
## Переноси вланів
	Потрібно зайти в конфіг режим
	скопіювати з пошти та вставати вказані команди - set ....
	сommit - далі зазвичай з'явиться помилка з повідомленням, що проблеми з певним інтерфейсом ae0.xxxx
	run clear dhcp relay binding interface ae0.xxxx - інтерфейс з помилки(потрібно вставити весь інтерфейс ae0.xxxx)
	і далі знову commit, якщо знову вилазить помилка повторити дії вище, поки commit не буде успішним
## Перевірка стану самого обладнання
	show log messages - де messages це самі останні логи, chassisd.0.gz це наступний блок трохи старіших і так далі - chassisd.1.gz
	show chassis alarms - активні аларми з станом обладнання
	show chassis enviromental - стан та температура комплектуючих
	show chassis power - стан блоків живлення
	show chassis ? - можна вибрати що треба подивитись по самому обладнанню
