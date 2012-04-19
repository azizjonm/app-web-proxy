
Name: app-web-proxy
Epoch: 1
Version: 1.1.0
Release: 1%{dist}
Summary: Web Proxy
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-network

%description
The Web Proxy app acts as an intermediary for web requests originating from your network.  Implementing the proxy server improves page access times, decreases bandwidth use, and provides site visit audits by user and IP address.

%package core
Summary: Web Proxy - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-network-core
Requires: app-firewall-core
Requires: app-samba-core >= 1:1.0.6
Requires: app-web-proxy-plugin-core
Requires: csplugin-filewatch
Requires: squid >= 3.1.10

%description core
The Web Proxy app acts as an intermediary for web requests originating from your network.  Implementing the proxy server improves page access times, decreases bandwidth use, and provides site visit audits by user and IP address.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/web_proxy
cp -r * %{buildroot}/usr/clearos/apps/web_proxy/

install -d -m 0755 %{buildroot}/etc/clearos/web_proxy.d
install -d -m 0755 %{buildroot}/var/clearos/web_proxy
install -d -m 0755 %{buildroot}/var/clearos/web_proxy/backup
install -d -m 0755 %{buildroot}/var/clearos/web_proxy/errors
install -D -m 0644 packaging/authorize %{buildroot}/etc/clearos/web_proxy.d/authorize
install -D -m 0644 packaging/filewatch-web-proxy-configuration.conf %{buildroot}/etc/clearsync.d/filewatch-web-proxy-configuration.conf
install -D -m 0644 packaging/filewatch-web-proxy-network.conf %{buildroot}/etc/clearsync.d/filewatch-web-proxy-network.conf
install -D -m 0644 packaging/squid.php %{buildroot}/var/clearos/base/daemon/squid.php
install -D -m 0644 packaging/squid_acls.conf %{buildroot}/etc/squid/squid_acls.conf
install -D -m 0644 packaging/squid_auth.conf %{buildroot}/etc/squid/squid_auth.conf
install -D -m 0644 packaging/squid_http_access.conf %{buildroot}/etc/squid/squid_http_access.conf
install -D -m 0644 packaging/squid_http_port.conf %{buildroot}/etc/squid/squid_http_port.conf
install -D -m 0644 packaging/squid_lans.conf %{buildroot}/etc/squid/squid_lans.conf
install -D -m 0644 packaging/web_proxy.acl %{buildroot}/var/clearos/base/access_control/public/web_proxy

%post
logger -p local6.notice -t installer 'app-web-proxy - installing'

%post core
logger -p local6.notice -t installer 'app-web-proxy-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/web_proxy/deploy/install ] && /usr/clearos/apps/web_proxy/deploy/install
fi

[ -x /usr/clearos/apps/web_proxy/deploy/upgrade ] && /usr/clearos/apps/web_proxy/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-web-proxy - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-web-proxy-core - uninstalling'
    [ -x /usr/clearos/apps/web_proxy/deploy/uninstall ] && /usr/clearos/apps/web_proxy/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/web_proxy/controllers
/usr/clearos/apps/web_proxy/htdocs
/usr/clearos/apps/web_proxy/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/web_proxy/packaging
%exclude /usr/clearos/apps/web_proxy/tests
%dir /usr/clearos/apps/web_proxy
%dir /etc/clearos/web_proxy.d
%dir /var/clearos/web_proxy
%dir /var/clearos/web_proxy/backup
%dir /var/clearos/web_proxy/errors
/usr/clearos/apps/web_proxy/deploy
/usr/clearos/apps/web_proxy/language
/usr/clearos/apps/web_proxy/libraries
%config(noreplace) /etc/clearos/web_proxy.d/authorize
/etc/clearsync.d/filewatch-web-proxy-configuration.conf
/etc/clearsync.d/filewatch-web-proxy-network.conf
/var/clearos/base/daemon/squid.php
%config(noreplace) /etc/squid/squid_acls.conf
%config(noreplace) /etc/squid/squid_auth.conf
%config(noreplace) /etc/squid/squid_http_access.conf
%config(noreplace) /etc/squid/squid_http_port.conf
%config(noreplace) /etc/squid/squid_lans.conf
/var/clearos/base/access_control/public/web_proxy
