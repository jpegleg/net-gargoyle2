Name:           net-gargoyle
Version:        1.0.0
Release:        0
Summary:        Linux honeypot/HIDS with python3 sqlite3.
BuildArch:      noarch

Group:          jpegleg
License:        MIT
URL:            https://github.com/jpegleg/net-gargoyle2
Source0:        /srv/net_gargoyle.tgz

#BuildRequires:
Requires:       bash
Requires:       python3-pip

%description
Linux honeypot/HIDS with python3 sqlite3.

%prep
%setup -q
%build
RPM_BUILD_ROOT=/srv/rpmbuild/BUILD/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
mkdir -p $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
install -m 0755 net-gargoyle $RPM_BUILD_ROOT/usr/local/sbin/
install -m 0755 reportIps $RPM_BUILD_ROOT/usr/local/sbin/
install -m 0755 kill-netg $RPM_BUILD_ROOT/usr/local/sbin/
cp net_gargoyle.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp net_set.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp net_mon.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp net_check.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp requirements.txt $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp install $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp install $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp net-gargoyle $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp reportIps $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp kill-netg $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp net_gargoyle.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp net_set.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp net_mon.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp net_check.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp requirements.txt $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/

%clean

%files
/usr/local/sbin/net-gargoyle
/usr/local/sbin/reportIps
/usr/local/sbin/kill-netg
/opt/net-gargoyle/workspace/BUILD/net_gargoyle.py
/opt/net-gargoyle/workspace/BUILD/net_mon.py
/opt/net-gargoyle/workspace/BUILD/net_set.py
/opt/net-gargoyle/workspace/BUILD/net_check.py
/opt/net-gargoyle/workspace/BUILD/install
/opt/net-gargoyle/workspace/BUILD/requirements.txt
/opt/net-gargoyle/workspace/BUILD/net-gargoyle
/opt/net-gargoyle/workspace/BUILD/reportIps
/opt/net-gargoyle/workspace/BUILD/kill-netg
/opt/net-gargoyle/workspace/net_gargoyle.py
/opt/net-gargoyle/workspace/net_mon.py
/opt/net-gargoyle/workspace/net_set.py
/opt/net-gargoyle/workspace/net_check.py
/opt/net-gargoyle/workspace/install
/opt/net-gargoyle/workspace/requirements.txt
/opt/net-gargoyle/workspace/BUILD/net_check.pyc
/opt/net-gargoyle/workspace/BUILD/net_check.pyo
/opt/net-gargoyle/workspace/BUILD/net_gargoyle.pyc
/opt/net-gargoyle/workspace/BUILD/net_gargoyle.pyo
/opt/net-gargoyle/workspace/BUILD/net_mon.pyc
/opt/net-gargoyle/workspace/BUILD/net_mon.pyo
/opt/net-gargoyle/workspace/BUILD/net_set.pyc
/opt/net-gargoyle/workspace/BUILD/net_set.pyo
/opt/net-gargoyle/workspace/net_check.pyc
/opt/net-gargoyle/workspace/net_check.pyo
/opt/net-gargoyle/workspace/net_gargoyle.pyc
/opt/net-gargoyle/workspace/net_gargoyle.pyo
/opt/net-gargoyle/workspace/net_mon.pyc
/opt/net-gargoyle/workspace/net_mon.pyo
/opt/net-gargoyle/workspace/net_set.pyc
/opt/net-gargoyle/workspace/net_set.pyo

%changelog
* Sat Jan 30 2021 Keegan Bowen  1.0.0
- Autobuilding RPMs for net-gargoyle2 packaging
