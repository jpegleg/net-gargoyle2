Name:           net-gargoyle
Version:        1
Release:        0
Summary:        Linux honeypot/HIDS with python3 sqlite3.
BuildArch:      noarch

Group:          jpegleg
License:        MIT
URL:            https://github.com/jpegleg/net-gargoyle2
Source0:        /srv/net-gargoyle.tgz

#BuildRequires:  
Requires:       bash
Requires:       python3-pip
Requires:       python3-venv

%description
Linux honeypot/HIDS with python3 sqlite3.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
mkdir -p $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD
cp net-gargoyle $RPM_BUILD_ROOT/usr/local/sbin/
cp reportIps $RPM_BUILD_ROOT/usr/local/sbin/
cp kill-netg $RPM_BUILD_ROOT/usr/local/sbin/
cp net_gargoyle.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp set_set.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp net_mon.py $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp requirements.txt $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/
cp install $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/
cp -r ./* $RPM_BUILD_ROOT/opt/net-gargoyle/workspace/BUILD/

%clean
rm -rf $RPM_BUILD_ROOT

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

%changelog
* Sat January 30 2021
- Autobuilding RPMs for net-gargoyle2 packaging
