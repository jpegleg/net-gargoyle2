Name:           net-gargoyle
Version:        1.0.0
Release:        1
Summary:        Linux honeypot/HIDS with python3 sqlite3.

Group:          jpegleg
License:        MIT
URL:            https://github.com/jpegleg/net-gargoyle2
Source0:        /srv/net-gargoyle.tgz

%description
Linux honeypot/HIDS with python3 sqlite3.

%prep
yum install -y python3-pip
%build
%install
bash ./install

%files
/usr/local/sbin/net-gargoyle
/usr/local/sbin/reportIps
/usr/local/sbin/kill-netg
/opt/net-gargoyle/workspace/net_gargoyle.py
/opt/net-gargoyle/workspace/net_check.py
/opt/net-gargoyle/workspace/net_mon.py
/opt/net-gargoyle/workspace/net_set.py
/opt/net-gargoyle/workspace/requirements.txt
/etc/systemd/system/multi-user.target.wants/net-gargoyle.service

%changelog
* Sat Jan 30 2021 Keegan Bowen  1.0.0
  - starting packaging for rpm
