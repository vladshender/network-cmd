    show route table l3vpn-atutg.ua.inet 172.19.50.45 extensive | match origin                                 

AS path: I  (Originator)
Originator ID: `195.5.8.28`

#### on 195.5.8.28 --> 10.171.36.28
    show route table l3vpn-atutg.ua.inet 172.19.50.45 extensive | match irb
Next hop: `via` irb.`7240`, selected

    show configuration | display set | match 7240
