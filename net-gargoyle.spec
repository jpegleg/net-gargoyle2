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
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m 0755 SOURCES/net-gargoyle $RPM_BUILD_ROOT/usr/local/bin/
install -m 0755 SOURCES/reportIps $RPM_BUILD_ROOT/usr/local/bin/
install -m 0755 SOURCES/kill-netg $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
install -m 0755 SOURCES/net_gargoyle.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
install -m 0755 SOURCES/net_set.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
install -m 0755 SOURCES/net_check.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
install -m 0755 SOURCES/net_mon.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
install -m 0755 SOURCES/requirements.txt $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
mkdir -p $RPM_BUILD_ROOT/etc/systemd/system/multi-user.target.wants/
install -m 0777 SOURCES/net-gargoyle.service $RPM_BUILD_ROOT/etc/systemd/system/multi-user.target.wants/

%files
/usr/local/sbin/net-gargoyle
/usr/local/sbin/reportIps
/usr/local/sbin/kill-netg
/opt/net-gargoyle/workspace/net_gargoyle.py
/opt/net-gargoyle/workspace/net_check.py
/opt/net-gargoyle/workspace/net_mon.py
/opt/net-gargoyle/workspace/net_set.py
/opt/net-gargoyle/workspace/requirements.txt
/etc/systemd/system/multi-user.target.wants/net-gargoyle.servic

$post
cd /opt/net-gargoyle/workspace
python3 -m venv ngvenv
source ngvenv/bin/activate
pip3 install -r requirements.txt
ls gargoyle.db || python3 net_set.py
cp net-gargoyle.service /usr/lib/systemd/system/net-gargoyle.service
systemctl enable net-gargoyle

%changelog
* Sat Jan 30 2021 Keegan Bowen  1.0.0
  - starting packaging for rpm
