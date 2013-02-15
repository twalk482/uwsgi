# revision of the uwsgi documentation corresponding to the packaged release
%global uwsgi_docs_rev 266643bffc2bee1461d3b5848a292b13b9ea998a
# exclude plugins for which we lack all necessary dependencies, which are
# unusable or just meant as examples
%global blacklist_plugins  example mono pypy stackless cheaper_backlog2 cplusplus pyuwsgi alarm_speech go systemd_logger fiber
%global embed_plugins      echo ping corerouter http

Name:           uwsgi
Version:        1.4.5
Release:        2%{?dist}
Summary:        Fast, self-healing, application container server
Group:          System Environment/Daemons   
License:        GPLv2
URL:            http://projects.unbit.it/uwsgi
Source0:        http://projects.unbit.it/downloads/%{name}-%{version}.tar.gz
Source1:        fedora.ini.in
Source2:        https://github.com/unbit/uwsgi-docs/archive/%{uwsgi_docs_rev}.zip
Source4:        emperor.ini
Source5:        uwsgi.conf
Source6:        uwsgi.logrotate
Source7:        uwsgi.init
Patch0:         uwsgi_trick_chroot_rpmbuild.patch
Patch1:         uwsgi_fix_rpath.patch
Patch2:         uwsgi_fix_jwsgi_include_lib_paths.patch
Patch3:         uwsgi_fix_boost_thread.patch
Patch4:         uwsgi_fix_older_libcurl.patch
BuildRequires:  curl,  python2-devel, libxml2-devel, libuuid-devel
BuildRequires:  libyaml-devel, perl-devel, ruby-devel, perl-ExtUtils-Embed
BuildRequires:  python-greenlet-devel, lua-devel, ruby, pcre-devel
BuildRequires:  php-devel, php-embedded, libedit-devel, openssl-devel
BuildRequires:  bzip2-devel, gmp-devel, libcap-devel, erlang
BuildRequires:  java-devel, pam-devel, postgresql-devel, zeromq-devel
BuildRequires:  sqlite-devel, openldap-devel, httpd-devel, libcurl-devel
BuildRequires:  gloox-devel, mongodb-devel, boost-devel
BuildRequires:  tcp_wrappers-devel, python-sphinx

Requires(post):   chkconfig
Requires(postun): initscripts
Requires(preun):  chkconfig
Requires(preun):  initscripts

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

%package devel
Summary:  uWSGI - Development header files and libraries
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the development header files and libraries
for uWSGI extensions

%package -n python-uwsgidecorators
Summary:  uWSGI - Python decorators
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-plugin-python = %{version}-%{release}

%description -n python-uwsgidecorators
This package contains the uwsgidecorators Python module providing higher-level
access to the uWSGI API

%package plugin-common
Summary:  uWSGI - Common plugins for uWSGI
Group:    System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%package -n %{name}-doc
Summary:  uWSGI - Documentation
Group:    Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description -n %{name}-doc
This package contains the documentation for uWSGI

%description plugin-common
This package contains the most common plugins used with uWSGI. The
plugins included in this package are: cache, CGI, RPC, uGreen

%package plugin-rack
Summary:  uWSGI - Ruby rack plugin
Group:    System Environment/Daemons
Requires: rubygem-rack, %{name}-plugin-common = %{version}-%{release}

%description plugin-rack
This package contains the rack plugin for uWSGI

%package plugin-psgi
Summary:  uWSGI - Plugin for PSGI support
Group:    System Environment/Daemons
Requires: perl-PSGI, %{name}-plugin-common = %{version}-%{release}

%description plugin-psgi
This package contains the PSGI plugin for uWSGI

%package plugin-python
Summary:  uWSGI - Plugin for Python support
Group:    System Environment/Daemons
Requires: python, %{name}-plugin-common = %{version}-%{release}

%description plugin-python
This package contains the python plugin for uWSGI

%package plugin-nagios
Summary:  uWSGI - Plugin for Nagios support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-nagios
This package contains the nagios plugin for uWSGI

%package plugin-fastrouter
Summary:  uWSGI - Plugin for FastRouter support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-fastrouter
This package contains the fastrouter (proxy) plugin for uWSGI

%package plugin-admin
Summary:  uWSGI - Plugin for Admin support
Group:    System Environment/Daemons   
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-admin
This package contains the admin plugin for uWSGI

%package plugin-ruby
Summary:  uWSGI - Plugin for Ruby support
Group:    System Environment/Daemons   
Requires: ruby, %{name}-plugin-common = %{version}-%{release}

%description plugin-ruby
This package contains the Ruby 1.9 plugin for uWSGI

%package plugin-greenlet
Summary:  uWSGI - Plugin for Python Greenlet support
Group:    System Environment/Daemons   
Requires: python-greenlet, %{name}-plugin-common = %{version}-%{release}

%description plugin-greenlet
This package contains the python greenlet plugin for uWSGI

%package plugin-lua
Summary:  uWSGI - Plugin for LUA support
Group:    System Environment/Daemons   
Requires: lua, %{name}-plugin-common = %{version}-%{release}

%description plugin-lua
This package contains the lua plugin for uWSGI

%package plugin-php
Summary:  uWSGI - Plugin for PHP support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-php
This package contains the PHP plugin for uWSGI

%package plugin-carbon
Summary:  uWSGI - Plugin for Carbon/Graphite support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-carbon
This package contains the Carbon plugin for uWSGI (to use in graphite)

%package plugin-rrdtool
Summary:  uWSGI - Plugin for RRDTool support
Group:    System Environment/Daemons
Requires: rrdtool, %{name}-plugin-common = %{version}-%{release}

%description plugin-rrdtool
This package contains the RRD Tool plugin for uWSGI

%package plugin-rsyslog
Summary:  uWSGI - Plugin for rsyslog support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-rsyslog
This package contains the rsyslog plugin for uWSGI

%package plugin-syslog
Summary:  uWSGI - Plugin for syslog support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-syslog
This package contains the syslog plugin for uWSGI

%package plugin-erlang
Summary:  uWSGI - Plugin for Erlang support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-erlang
This package contains the Erlang plugin for uWSGI

%package plugin-gevent
Summary:  uWSGI - Plugin for Python Gevent support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-gevent
This package contains the Python Gevent plugin for uWSGI

%package plugin-graylog2
Summary:  uWSGI - Plugin for logging to Gralylog2 servers
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-graylog2
This package contains the Graylog2 plugin for uWSGI

%package plugin-jvm
Summary:  uWSGI - Plugin for JVM support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-jvm
This package contains the JVM plugin for uWSGI

%package plugin-jwsgi
Summary:  uWSGI - Plugin for Java WSGI support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-jwsgi
This package contains the Java WSGI plugin for uWSGI

%package plugin-logsocket
Summary:  uWSGI - Plugin for logging to UNIX and UDP sockets
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-logsocket
This package contains the logsocket plugin for uWSGI

%package plugin-pam
Summary:  uWSGI - Plugin for PAM authentication support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-pam
This package contains the PAM plugin for uWSGI

%package plugin-probepg
Summary:  uWSGI - Plugin for probing PostgreSQL servers
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-probepg
This package contains the PostgreSQL probing plugin for uWSGI

%package plugin-pyerl
Summary:  uWSGI - Plugin for Python-Erlang support
Group:    System Environment/Daemons
Requires: %{name}-plugin-erlang = %{version}-%{release}
Requires: %{name}-plugin-python = %{version}-%{release}
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-pyerl
This package contains the Python-Erlang plugin for uWSGI

%package plugin-redislog
Summary:  uWSGI - Plugin for logging to Redis servers
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description plugin-redislog
This package contains the Redis plugin for uWSGI

%package -n %{name}-plugin-alarm-curl
Summary:  uWSGI - Plugin for passing alarm messages via curl URLs
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-alarm-curl
This package contains the alarm_curl plugin for uWSGI

%package -n %{name}-plugin-alarm-xmpp
Summary:  uWSGI - Plugin for passing alarm messages via XMPP
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-alarm-xmpp
This package contains the alarm_xmpp plugin for uWSGI

%package -n %{name}-plugin-emperor-mongodb
Summary:  uWSGI - Plugin for reading emperor configurations from MongoDB
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-emperor-mongodb
This package contains the emperor_mongodb plugin

%package -n %{name}-plugin-emperor-pg
Summary:  uWSGI - Plugin for reading emperor configurations from PostgreSQL
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-emperor-pg
This package contains the emperor_pg plugin

%package -n %{name}-plugin-emperor-amqp
Summary:  uWSGI - Plugin for reading emperor configuration locations from AMQP
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-emperor-amqp
This package contains the emperor_amqp plugin

%package -n %{name}-plugin-mongodblog
Summary:  uWSGI - Plugin for logging to MongoDB
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-mongodblog
This package contains the mongodblog plugin

%package -n %{name}-plugin-stats-pusher-mongodb
Summary:  uWSGI - Plugin for push statistics to MongoDB
Group:    System Environment/Daemons
Requires: %{name}-plugin-common = %{version}-%{release}

%description -n %{name}-plugin-stats-pusher-mongodb
This package contains the stats_pusher_mongodb plugin

%package -n mod_uwsgi
Summary:  uWSGI - Apache module
Group:    System Environment/Libraries
Requires: httpd >= 2.4, %{name} = %{version}-%{release}

%description -n mod_uwsgi
This package contains the uWSGI Apache module

# prevent auto-generated requires and provides for Apache modules, see
# https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
%{?filter_setup:
%filter_provides_in %{_libdir}/httpd/modules/.*\.so$
%filter_setup
}

%prep
%setup -q -a2
cp -p %{SOURCE1} buildconf/fedora.ini
ls -1 plugins | \
    awk '
BEGIN {
    n = split("%{blacklist_plugins}", tmp)
    for (i = 1; i <= n; i++) { blacklist_plugins[tmp[i]] = 1 }
    n = split("%{embed_plugins}", tmp)
    for (i = 1; i <= n; i++) { embed_plugins[tmp[i]] = 1 }
}
$0 in blacklist_plugins { next }
$0 in embed_plugins {
    embed_str = (embed_str) ? embed_str ", " $0 : $0
    next
}
{ 
    plugins_str = (plugins_str) ? plugins_str ", " $0 : $0
}
END {
    print "embedded_plugins = " embed_str
    print "plugins = " plugins_str
    print "plugin_dir = %{_libdir}/%{name}"
}
' >> buildconf/fedora.ini
cp -p %{SOURCE4} %{name}.ini
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd uwsgi-docs-%{uwsgi_docs_rev}
# remove empty files
find . -name '*.rst' -and -size 0 -exec rm {} \+
# remove languages unknown to sphinx which otherwise cause build failures
find . -name '*.rst' -exec sed -i 's|code-block:: .*$|code-block:: none|' {} \+
popd

%build
export UWSGICONFIG_JVM_INCPATH="%{_jvmdir}/java/include -I/usr/lib/jvm/java/include/linux"
export UWSGICONFIG_JVM_LIBPATH="$(dirname %{_jvmdir}/java/jre/lib/*/server/libjvm.so | head -1)"
export UWSGICONFIG_LUALIB="lua"
export UWSGICONFIG_LUAINC="%{_includedir}"
export UWSGICONFIG_LUALIBPATH="%{_libdir}"
export CFLAGS="%{optflags} -Wno-unused-but-set-variable"
python uwsgiconfig.py --build fedora.ini
pushd apache2
apxs -c mod_uwsgi.c
popd
mkdir html
sphinx-build -b html uwsgi-docs-%{uwsgi_docs_rev} html
rm -rf html/.doctrees html/.buildinfo

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%{__install} -p -m 0755 %{name} %{buildroot}%{_sbindir}
%{__install} -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python_sitelib}/uwsgidecorators.py
%{__install} -p -m 0644 *.h %{buildroot}%{_includedir}/%{name}
%{__install} -p -m 0755 *_plugin.so %{buildroot}%{_libdir}/%{name}
%{__install} -D -p -m 0755 apache2/.libs/mod_uwsgi.so %{buildroot}%{_libdir}/httpd/modules/mod_uwsgi.so
%{__install} -D -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/httpd/conf.d/10-uwsgi.conf
%{__install} -p -m 0644 %{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
%{__install} -D -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -D -p -m 0755 %{SOURCE7} %{buildroot}%{_initddir}/%{name}


%pre
getent group uwsgi >/dev/null || groupadd -r uwsgi
getent passwd uwsgi >/dev/null || \
    useradd -r -g uwsgi -d %{_localstatedir}/run/uwsgi -s /sbin/nologin \
    -c "uWSGI daemon user" uwsgi
exit 0

%post
/sbin/chkconfig --add %{name}

%preun
if [ "$1" -eq 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" -ge 1 ]; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi


%files 
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.ini
%dir %{_sysconfdir}/%{name}.d
%{_initddir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_localstatedir}/run/%{name}
%doc ChangeLog LICENSE README

%files devel
%{_includedir}/%{name}

%files -n python-uwsgidecorators
%{python_sitelib}/uwsgidecorators.py*

%files -n %{name}-doc
%doc html/

%files plugin-common
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/cache_plugin.so
%{_libdir}/%{name}/cgi_plugin.so
%{_libdir}/%{name}/cheaper_busyness_plugin.so
%{_libdir}/%{name}/clock_monotonic_plugin.so
%{_libdir}/%{name}/clock_realtime_plugin.so
%{_libdir}/%{name}/dumbloop_plugin.so
%{_libdir}/%{name}/dummy_plugin.so
%{_libdir}/%{name}/logfile_plugin.so
%{_libdir}/%{name}/notfound_plugin.so
%{_libdir}/%{name}/probeconnect_plugin.so
%{_libdir}/%{name}/rawrouter_plugin.so
%{_libdir}/%{name}/router_access_plugin.so
%{_libdir}/%{name}/router_basicauth_plugin.so
%{_libdir}/%{name}/router_cache_plugin.so
%{_libdir}/%{name}/router_http_plugin.so
%{_libdir}/%{name}/router_redirect_plugin.so
%{_libdir}/%{name}/router_rewrite_plugin.so
%{_libdir}/%{name}/router_uwsgi_plugin.so
%{_libdir}/%{name}/rpc_plugin.so
%{_libdir}/%{name}/signal_plugin.so
%{_libdir}/%{name}/spooler_plugin.so
%{_libdir}/%{name}/symcall_plugin.so
%{_libdir}/%{name}/ugreen_plugin.so
%{_libdir}/%{name}/zergpool_plugin.so

%files plugin-rack
%{_libdir}/%{name}/rack_plugin.so

%files plugin-psgi
%{_libdir}/%{name}/psgi_plugin.so

%files plugin-python
%{_libdir}/%{name}/python_plugin.so

%files plugin-nagios
%{_libdir}/%{name}/nagios_plugin.so

%files plugin-fastrouter
%{_libdir}/%{name}/fastrouter_plugin.so

%files plugin-admin
%{_libdir}/%{name}/admin_plugin.so

%files plugin-ruby
%{_libdir}/%{name}/ruby19_plugin.so

%files plugin-greenlet
%{_libdir}/%{name}/greenlet_plugin.so

%files plugin-lua
%{_libdir}/%{name}/lua_plugin.so

%files plugin-php
%{_libdir}/%{name}/php_plugin.so

%files plugin-carbon
%{_libdir}/%{name}/carbon_plugin.so

%files plugin-rrdtool
%{_libdir}/%{name}/rrdtool_plugin.so

%files plugin-rsyslog
%{_libdir}/%{name}/rsyslog_plugin.so

%files plugin-syslog
%{_libdir}/%{name}/syslog_plugin.so

%files plugin-erlang
%{_libdir}/%{name}/erlang_plugin.so

%files plugin-gevent
%{_libdir}/%{name}/gevent_plugin.so

%files plugin-graylog2
%{_libdir}/%{name}/graylog2_plugin.so

%files plugin-jvm
%{_libdir}/%{name}/jvm_plugin.so

%files plugin-jwsgi
%{_libdir}/%{name}/jwsgi_plugin.so

%files plugin-logsocket
%{_libdir}/%{name}/logsocket_plugin.so

%files plugin-pam
%{_libdir}/%{name}/pam_plugin.so

%files plugin-probepg
%{_libdir}/%{name}/probepg_plugin.so

%files plugin-pyerl
%{_libdir}/%{name}/pyerl_plugin.so

%files plugin-redislog
%{_libdir}/%{name}/redislog_plugin.so
 
%files -n %{name}-plugin-alarm-curl
%{_libdir}/%{name}/alarm_curl_plugin.so

%files -n %{name}-plugin-alarm-xmpp
%{_libdir}/%{name}/alarm_xmpp_plugin.so

%files -n %{name}-plugin-emperor-mongodb
%{_libdir}/%{name}/emperor_mongodb_plugin.so

%files -n %{name}-plugin-emperor-pg
%{_libdir}/%{name}/emperor_pg_plugin.so

%files -n %{name}-plugin-emperor-amqp
%{_libdir}/%{name}/emperor_amqp_plugin.so

%files -n %{name}-plugin-mongodblog
%{_libdir}/%{name}/mongodblog_plugin.so

%files -n %{name}-plugin-stats-pusher-mongodb
%{_libdir}/%{name}/stats_pusher_mongodb_plugin.so

%files -n mod_uwsgi
%{_sysconfdir}/httpd/conf.d/10-uwsgi.conf
%{_libdir}/httpd/modules/mod_uwsgi.so

%changelog
* Tue Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.4.5-2
- Adapted for EPEL-6

* Tue Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.4.5-1
- Update to latest stable release from upstream
- Add doc subpackage with the complete documentation

* Mon Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.2.6-13
- Build mod_uwsgi

* Mon Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.2.6-12
- Build all plugins all available plugins except those for which we lack all
  necessary dependencies or which are unusable or examples
- Enable configuration from LDAP and SQlite, enable ZeroMQ transport
- Some stylistic fixes

* Mon Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.2.6-11
- Use versioned dependencies from the devel subpackage on the main package and
  from plugins on the plugins-common subpackage

* Mon Feb 15 2013 Guido Berhoerster <guido+fedora@berhoerster.name> - 1.2.6-10
- Mark uwsgi.ini as a config file

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
