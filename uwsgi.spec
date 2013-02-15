%define wikiversion 43

Name:           uwsgi
Version:        1.2.6
Release:        9%{?dist}
Summary:        Fast, self-healing, application container server
Group:          System Environment/Daemons   
License:        GPLv2
URL:            http://projects.unbit.it/uwsgi
Source0:        http://projects.unbit.it/downloads/%{name}-%{version}.tar.gz
Source1:        fedora.ini
# curl -o uwsgi-wiki-doc-v${wikiversion}.txt "http://projects.unbit.it/uwsgi/wiki/Doc?version=${wikiversion}&format=txt"
Source2:        uwsgi-wiki-doc-v%{wikiversion}.txt
Source3:        uwsgi.service
Source4:        emperor.ini
Patch0:         uwsgi_trick_chroot_rpmbuild.patch
Patch1:         uwsgi_fix_rpath.patch
BuildRequires:  curl,  python2-devel, libxml2-devel, libuuid-devel, jansson-devel
BuildRequires:  libyaml-devel, perl-devel, ruby-devel, perl-ExtUtils-Embed
BuildRequires:  python3-devel, python-greenlet-devel, lua-devel, ruby, pcre-devel
BuildRequires:  php-devel, php-embedded, libedit-devel, openssl-devel
BuildRequires:  bzip2-devel, gmp-devel, systemd-units, libcap-devel

Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

%description
uWSGI is a fast (pure C), self-healing, developer/sysadmin-friendly
application container server.  Born as a WSGI-only server, over time it has
evolved in a complete stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management. 
It uses the uwsgi (all lowercase, already included by default in the Nginx
and Cherokee releases) protocol for all the networking/interprocess
communications.  Can be run in preforking mode, threaded,
asynchronous/evented and supports various form of green threads/co-routine
(like uGreen and Fiber).  Sysadmin will love it as it can be configured via
command line, environment variables, xml, .ini and yaml files and via LDAP. 
Being fully modular can use tons of different technology on top of the same
core.

%package -n %{name}-devel
Summary:  uWSGI - Development header files and libraries
Group:    Development/Libraries
Requires: %{name}

%description -n %{name}-devel
This package contains the development header files and libraries
for uWSGI extensions

%package -n %{name}-plugin-common
Summary:  uWSGI - Common plugins for uWSGI
Group:    System Environment/Daemons
Requires: %{name}

%description -n %{name}-plugin-common
This package contains the most common plugins used with uWSGI. The
plugins included in this package are: cache, CGI, RPC, uGreen

%package -n %{name}-plugin-rack
Summary:  uWSGI - Ruby rack plugin
Group:    System Environment/Daemons
Requires: rubygem-rack, %{name}-plugin-common

%description -n %{name}-plugin-rack
This package contains the rack plugin for uWSGI

%package -n %{name}-plugin-psgi
Summary:  uWSGI - Plugin for PSGI support
Group:    System Environment/Daemons
Requires: perl-PSGI, %{name}-plugin-common

%description -n %{name}-plugin-psgi
This package contains the PSGI plugin for uWSGI

%package -n %{name}-plugin-python
Summary:  uWSGI - Plugin for Python support
Group:    System Environment/Daemons
Requires: python, %{name}-plugin-common

%description -n %{name}-plugin-python
This package contains the python plugin for uWSGI

%package -n %{name}-plugin-nagios
Summary:  uWSGI - Plugin for Nagios support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-nagios
This package contains the nagios plugin for uWSGI

%package -n %{name}-plugin-fastrouter
Summary:  uWSGI - Plugin for FastRouter support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-fastrouter
This package contains the fastrouter (proxy) plugin for uWSGI

%package -n %{name}-plugin-admin
Summary:  uWSGI - Plugin for Admin support
Group:    System Environment/Daemons   
Requires: %{name}-plugin-common

%description -n %{name}-plugin-admin
This package contains the admin plugin for uWSGI

%package -n %{name}-plugin-python3
Summary:  uWSGI - Plugin for Python 3.2 support
Group:    System Environment/Daemons   
Requires: python3, %{name}-plugin-common

%description -n %{name}-plugin-python3
This package contains the Python 3.2 plugin for uWSGI

%package -n %{name}-plugin-ruby
Summary:  uWSGI - Plugin for Ruby support
Group:    System Environment/Daemons   
Requires: ruby, %{name}-plugin-common

%description -n %{name}-plugin-ruby
This package contains the Ruby 1.9 plugin for uWSGI

%package -n %{name}-plugin-greenlet
Summary:  uWSGI - Plugin for Python Greenlet support
Group:    System Environment/Daemons   
Requires: python-greenlet, %{name}-plugin-common

%description -n %{name}-plugin-greenlet
This package contains the python greenlet plugin for uWSGI

%package -n %{name}-plugin-lua
Summary:  uWSGI - Plugin for LUA support
Group:    System Environment/Daemons   
Requires: lua, %{name}-plugin-common

%description -n %{name}-plugin-lua
This package contains the lua plugin for uWSGI

%package -n %{name}-plugin-php
Summary:  uWSGI - Plugin for PHP support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-php
This package contains the PHP plugin for uWSGI

%package -n %{name}-plugin-carbon
Summary:  uWSGI - Plugin for Carbon/Graphite support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-carbon
This package contains the Carbon plugin for uWSGI (to use in graphite)

%package -n %{name}-plugin-rrdtool
Summary:  uWSGI - Plugin for RRDTool support
Group:    System Environment/Daemons
Requires: rrdtool, %{name}-plugin-common

%description -n %{name}-plugin-rrdtool
This package contains the RRD Tool plugin for uWSGI

%package -n %{name}-plugin-rsyslog
Summary:  uWSGI - Plugin for rsyslog support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-rsyslog
This package contains the rsyslog plugin for uWSGI

%package -n %{name}-plugin-syslog
Summary:  uWSGI - Plugin for syslog support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-syslog
This package contains the syslog plugin for uWSGI

%prep
%setup -q
cp -p %{SOURCE1} buildconf/
cp -p %{SOURCE2} uwsgi-wiki-doc-v%{wikiversion}.txt
cp -p %{SOURCE3} %{name}.service
cp -p %{SOURCE4} %{name}.ini
sed -i 's/\r//' uwsgi-wiki-doc-v%{wikiversion}.txt
echo "plugin_dir = %{_libdir}/%{name}" >> buildconf/$(basename %{SOURCE1})
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{optflags} -Wno-unused-but-set-variable" python uwsgiconfig.py --build fedora.ini
CFLAGS="%{optflags} -Wno-unused-but-set-variable" python3 uwsgiconfig.py --plugin plugins/python fedora python32

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}/run/%{name}
%{__install} -p -m 0755 %{name} %{buildroot}%{_sbindir}
%{__install} -p -m 0644 *.h %{buildroot}%{_includedir}/%{name}
%{__install} -p -m 0755 *_plugin.so %{buildroot}%{_libdir}/%{name}
%{__install} -p -m 0644 %{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
%{__install} -p -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service


%pre
getent group uwsgi >/dev/null || groupadd -r uwsgi
getent passwd uwsgi >/dev/null || \
    useradd -r -g uwsgi -d /run/uwsgi -s /sbin/nologin \
    -c "uWSGI daemon user" uwsgi
exit 0

%post
%if 0%{?systemd_post:1}
    %systemd_post uwsgi.service
%else
    if [ $1 -eq 1 ] ; then 
        # Initial installation 
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    fi
%endif

%preun
%if 0%{?systemd_preun:1}
    %systemd_preun uwsgi.service
%else
    if [ $1 -eq 0 ] ; then
        # Package removal, not upgrade
        /bin/systemctl --no-reload disable uwsgi.service > /dev/null 2>&1 || :
        /bin/systemctl stop uwsgi.service > /dev/null 2>&1 || :
    fi
%endif

%postun
%if 0%{?systemd_postun:1}
    %systemd_postun uwsgi.service
%else
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    if [ $1 -ge 1 ] ; then
        # Package upgrade, not uninstall
        /bin/systemctl try-restart uwsgi.service >/dev/null 2>&1 || :
    fi
%endif


%files 
%{_sbindir}/%{name}
%{_sysconfdir}/%{name}.ini
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}.d
%dir /run/%{name}
%doc ChangeLog LICENSE README
%doc uwsgi-wiki-doc-v%{wikiversion}.txt

%files -n %{name}-devel
%{_includedir}/%{name}

%files -n %{name}-plugin-common
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/cache_plugin.so
%{_libdir}/%{name}/cgi_plugin.so
%{_libdir}/%{name}/rpc_plugin.so
%{_libdir}/%{name}/ugreen_plugin.so

%files -n %{name}-plugin-rack
%{_libdir}/%{name}/rack_plugin.so

%files -n %{name}-plugin-psgi
%{_libdir}/%{name}/psgi_plugin.so

%files -n %{name}-plugin-python
%{_libdir}/%{name}/python_plugin.so

%files -n %{name}-plugin-nagios
%{_libdir}/%{name}/nagios_plugin.so

%files -n %{name}-plugin-fastrouter
%{_libdir}/%{name}/fastrouter_plugin.so

%files -n %{name}-plugin-admin
%{_libdir}/%{name}/admin_plugin.so

%files -n %{name}-plugin-python3
%{_libdir}/%{name}/python32_plugin.so

%files -n %{name}-plugin-ruby
%{_libdir}/%{name}/ruby19_plugin.so

%files -n %{name}-plugin-greenlet
%{_libdir}/%{name}/greenlet_plugin.so

%files -n %{name}-plugin-lua
%{_libdir}/%{name}/lua_plugin.so

%files -n %{name}-plugin-php
%{_libdir}/%{name}/php_plugin.so

%files -n %{name}-plugin-carbon
%{_libdir}/%{name}/carbon_plugin.so

%files -n %{name}-plugin-rrdtool
%{_libdir}/%{name}/rrdtool_plugin.so

%files -n %{name}-plugin-rsyslog
%{_libdir}/%{name}/rsyslog_plugin.so

%files -n %{name}-plugin-syslog
%{_libdir}/%{name}/syslog_plugin.so


%changelog
* Fri Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.2.6-9
- Build with support for POSIX capabilities

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Jorge A Gallegos <kad@blegh.net> - 1.2.6-7
- Tyrant mode shouldn't be used here, tyrant mode is root-only

* Thu Dec 27 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-6
- Systemd now supports an exit status directive, fixing bugz 873382

* Fri Nov  9 2012 Remi Collet <rcollet@redhat.com> - 1.2.6-5
- rebuild against new php embedded library soname (5.4)

* Thu Oct 18 2012 Remi Collet <remi@fedoraproject.org> - 1.2.6-4
- rebuild for new PHP 5.4.8

* Wed Sep 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-3
- Dropped requirement on PHP for the PHP plugin

* Sat Sep 15 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-2
- Rebuilt with new systemd macros

* Sun Sep 09 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-1
- Updated to latest stable from upstream

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.4-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.4-1
- Updated to latest stable from upstream

* Tue Jun 26 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.3-1
- Updated to latest stable upstream
- Building the pytho3 plugin is a bit trickier now, but still possible
- Added PHP plugin
- Added Carbon plugin
- Added RRDTool plugin
- Added rsyslog plugin
- Added syslog plugin

* Sun Feb 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.4-1
- Addressing issues from package review feedback
- s/python-devel/python2-devel
- Make the libdir subdir owned by -plugins-common
- Upgraded to latest stable upstream version

* Mon Feb 06 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-2
- Fixing 'unstripped-binary-or-object'

* Thu Jan 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-1
- New upstream version

* Thu Dec 08 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.3-1
- New upstream version

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-2
- Don't download the wiki page at build time

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-1
- Updated to latest stable version
- Correctly linking plugin_dir
- Patches 1 and 2 were addressed upstream

* Sun Aug 21 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.8.3-3
- Got rid of BuildRoot
- Got rid of defattr()

* Sun Aug 14 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-2
- Added uwsgi_fix_rpath.patch
- Backported json_loads patch to work with jansson 1.x and 2.x
- Deleted clean steps since they are not needed in fedora

* Sun Jul 24 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-1
- rebuilt
- Upgraded to latest stable version 0.9.8.3
- Split packages

* Sun Jul 17 2011 Jorge Gallegos <kad@blegh.net> - 0.9.6.8-2
- Heavily modified based on Oskari's work

* Mon Feb 28 2011 Oskari Saarenmaa <os@taisia.fi> - 0.9.6.8-1
- Initial.
