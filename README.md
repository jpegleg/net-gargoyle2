![net-gargoyle2](https://carefuldata.com/images/cdlogo.png)

# net-gargoyle2

Track IP addresses and connection state changes along with running processes.

A basic HIDS component and/or honeypot that stores data in the working directory of the exeution to gargoyle.db, an sqlite3 database file.

The intent is to be a minimal set of functions and structures for a transactional-at-change local blockchain, bassed on active network connections and running processes, and hashes of those outputs.


#### Install:

```
sudo bash ./install
```

#### Start it up:

```
net-gargoyle
```

#### Or with systemd:

```
systemctl start net-gargoyle
```

#### And stop it with systemd:

```
systemctl stop net-gargoyle
```

#### If you ar enot using systemd, you can stop it will kill-netg:

```
kill-netg
```

#### Generate a report of unique IPs in the gargoyle.db file:

```
reportIps
```

#### If you have or estblish a hash that is an expected state you want to remember it can go in /etc/normstate.cfg

#### To run with STDOUT log, rather than use net-gargoyle, call net_mon.py directly with arguments like so:

```
cd /opt/net-gargoyle/workspace

source ngvenv/bin/activate

python3 net_mon.py 1 $(cat /etc/normstate.cfg || echo -n NOTSET)
```

## Review db contents example:

```
cd /opt/net-gargoyle/workspace

source ngvenv/bin/activate

python3 net_check.py | less -S
```

## New features and updates

4/13/21 - Added in handling for empty gargoyle.db into net_mon.py and removed the check in the wrapper net-gargoyle. Additionally if the gargoyle.db is larger than 500 MB during start up, the database will be deleted. This max size detecting during start up can be adjusted in net_mon.py on line 38. I may move control over that to a config setting.

I have prototype scripts that are doing gargoyle.db backups as well as capturing pcap data. Those prototypes are not yet in this repo, but shall be added in the future!
