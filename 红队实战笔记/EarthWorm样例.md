# EarthWorm样例

[原文链接](http://rootkiter.com/EarthWorm/)

共有六种转发方式：ssocksd、rcsocks、rssocks、lcx_slave、lcx_listen、lcx_tran

# 正向SOCKSv5服务器

`./ew -s ssocksd -l 1080`

# 反弹SOCKSv5服务器

0. 1.1.1.1主机监听：`./ew -s rcsocks -l 1080 -e 8888`

1. 跳板机反弹：`./ew -s rssocks -d 1.1.1.1 -e 8888`

# 二级级联

## lcx_tran

0. `./ew -s ssocksd  -l 9999`

1. `./ew -s lcx_tran -l 1080 -f 127.0.0.1 -g 9999`

## lcx_listen、lcx_slave

0. `./ew -s lcx_listen -l 1080 -e 8888`

1. `./ew -s ssocksd -l 9999`

2. `./ew -s lcx_slave -d 127.0.0.1 -e 8888 -f 127.0.0.1 -g 9999`

# 三级级联

SOCKS v5 -> 1080 -> 8888 -> 9999 -> 7777 -> rssocks

0. `./ew -s rcsocks -l 1080 -e 8888`

1. `./ew -s lcx_slave -d 127.0.0.1 -e 8888 -f 127.0.0.1 -g 9999`

2. `./ew -s lcx_listen -l 9999 -e 7777`

3. `./ew -s rssocks -d 127.0.0.1 -e 7777`