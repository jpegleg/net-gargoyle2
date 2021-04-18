![net-gargoyle2](https://carefuldata.com/images/cdlogo.png)

# honey-cycle for net-gargoyle2

Also see https://github.com/jpegleg/honey-cycle
The honey-cycle daemon cleans up after net-gargoyle2 and also collects pcaps.

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

The file $PWD/gargoyle.json for net_mon.py contains byte size integers for configuring the maximum size of the gargoyle.db during runtime
and during startup.

Example default gargoyle.json set to 500 MB for both values:

```
{
  "MAXSTARTSIZE": "500000000",
  "MAXRUNSIZE": "500000000"
}
```

When the gargoyle.db is rotated at start up or run time because it hit a limit, a copy is made in /opt/net-gargoyle/
The files start with g_ and contain a timestamp.
