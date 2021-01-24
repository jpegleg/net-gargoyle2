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

