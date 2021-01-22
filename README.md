# net-gargoyle2

Designed for linux, but will work on FreeBSD etc via linking ss to netstat. The install script does that if ss is not found.

Track IP addresses and connection state changes along with running processes.

A basic HIDS component and/or honeypot that stores data in the working directory of the exeution to gargoyle.db, an sqlite3 database file.

The intent is to be a minimal set of functions and structures for a transactional-at-change local blockchain, bassed on active network connections and running processes, and hashes of those outputs.


#### Install:

sudo bash ./install


#### Start it up:

net-gargoyle


#### Generate a report of unique IPs in the gargoyle.db file:

reportIps



## Review db contents example:

cd /opt/net-gargoyle/workspace

source ngvenv/bin/activate

python3 netCheck.py | less -S


