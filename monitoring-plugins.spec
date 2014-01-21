%global _hardened_build 1

Name: monitoring-plugins
Version: 1.5
Release: 1%{?dist}
Summary: Host/service/network monitoring program plugins for Nagios, Icinga, Naemon, Shinken

Group: Applications/System
License: GPLv2+
URL: https://www.monitoring-plugins.org/
Source0: https://www.monitoring-plugins.org/download/%{name}-%{version}.tar.gz
Source1: monitoring-plugins.README.Fedora
# 2014-01-21 mf: verified required
Patch2: monitoring-plugins-0002-Remove-assignment-of-not-parsed-to-jitter.patch
# 2014-01-21 mf: verified required
Patch3: monitoring-plugins-0003-Fix-diff-tail-path-for-fedora-in-check_log.patch
# 2014-01-21 mf: verified required
Patch4: monitoring-plugins-0004-Fedora-specific-patch-for-not-to-fixing-fully-qualif.patch
# 2014-01-21 mf: verified required
# https://bugzilla.redhat.com/512559
Patch5: monitoring-plugins-0005-Prevent-check_swap-from-returning-OK-if-no-swap-acti.patch
# 2014-01-21 mf: verified required
Patch7: monitoring-plugins-0007-Fix-the-use-lib-statement-and-the-external-ntp-comma.patch
# 2014-01-21 mf: verified required
# https://bugzilla.redhat.com/913085
Patch10:monitoring-plugins-0010-fix-smart-attribute-comparison.patch

BuildRequires: openldap-devel
BuildRequires: mysql-devel
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
BuildRequires: samba-client
BuildRequires: postgresql-devel
BuildRequires: gettext
BuildRequires: %{_bindir}/ssh
BuildRequires: bind-utils
BuildRequires: ntp
BuildRequires: %{_bindir}/mailq
BuildRequires: %{_sbindir}/fping
BuildRequires: perl(Net::SNMP)
BuildRequires: radiusclient-ng-devel
BuildRequires: qstat
BuildRequires: libdbi-devel

Requires: monitoring-plugins-common = %{version}-%{release}

# monitoring-plugins-1.4.16: the included gnulib files were last updated
# in June/July 2010
# Bundled gnulib exception (https://fedorahosted.org/fpc/ticket/174)
Provides: bundled(gnulib)

%global reqfilt sh -c "%{__perl_requires} | sed -e 's!perl(utils)!monitoring-plugins-perl!'"
%global __perl_requires %{reqfilt}


%description
Nagios, Icinga, Naemon, Shinken are programs that will monitor hosts
and services on your network, and to email or page you when a problem
arises or is resolved. They run on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to the application.
This package contains those plugins.

%package all
Summary: Monitoring Plugins - All plugins
Group: Applications/System
Requires: monitoring-plugins-breeze, monitoring-plugins-by_ssh, monitoring-plugins-dhcp, monitoring-plugins-dig, monitoring-plugins-disk, monitoring-plugins-disk_smb, monitoring-plugins-dns, monitoring-plugins-dummy, monitoring-plugins-file_age, monitoring-plugins-flexlm, monitoring-plugins-fping, monitoring-plugins-hpjd, monitoring-plugins-http, monitoring-plugins-icmp, monitoring-plugins-ide_smart, monitoring-plugins-ircd, monitoring-plugins-ldap, monitoring-plugins-load, monitoring-plugins-log, monitoring-plugins-mailq, monitoring-plugins-mrtg, monitoring-plugins-mrtgtraf, monitoring-plugins-mysql, monitoring-plugins-core, monitoring-plugins-nt, monitoring-plugins-ntp, monitoring-plugins-ntp-perl, monitoring-plugins-nwstat, monitoring-plugins-oracle, monitoring-plugins-overcr, monitoring-plugins-pgsql, monitoring-plugins-ping, monitoring-plugins-procs, monitoring-plugins-game, monitoring-plugins-real, monitoring-plugins-rpc, monitoring-plugins-smtp, monitoring-plugins-snmp, monitoring-plugins-ssh, monitoring-plugins-swap, monitoring-plugins-tcp, monitoring-plugins-time, monitoring-plugins-ups, monitoring-plugins-users, monitoring-plugins-wave, monitoring-plugins-cluster
%ifnarch ppc ppc64 ppc64p7 sparc sparc64
Requires: monitoring-plugins-sensors
%endif

%description all
This package provides all Monitoring plugins.

%package common
Group: Applications/System
Summary: Provides common directories, uid and gid among monitoring-plugin-related packages
Requires(pre): shadow-utils
Requires(post): shadow-utils
Provides: user(monplug)
Provides: group(monplug)

%description common
Provides common directories, uid and gid among monitoring-plugin-related packages.

%package apt
Summary: Monitoring Plugin - check_apt
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description apt
Provides check_apt support for Nagios, Icinga, Naemon, Shinken.

%package breeze
Summary: Monitoring Plugin - check_breeze
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description breeze
Provides check_breeze support for Nagios, Icinga, Naemon, Shinken.

%package by_ssh
Summary: Monitoring Plugin - check_by_ssh
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/ssh

%description by_ssh
Provides check_by_ssh support for Nagios, Icinga, Naemon, Shinken.

%package cluster
Summary: Monitoring Plugin - check_cluster
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description cluster
Provides check_cluster support for Nagios, Icinga, Naemon, Shinken.

%package dbi
Summary: Monitoring Plugin - check_dbi
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description dbi
Provides check_dbi support for Nagios, Icinga, Naemon, Shinken.

%package dbi-mysql
Summary: Monitoring Plugin - check_dbi
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: libdbi-dbd-mysql

%description dbi-mysql
Provides check_dbi MySQL support for Nagios, Icinga, Naemon, Shinken.

%package dbi-pgsql
Summary: Monitoring Plugin - check_dbi
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: libdbi-dbd-pgsql

%description dbi-pgsql
Provides check_dbi PostgreSQL support for Nagios, Icinga, Naemon, Shinken.

%package dbi-sqlite
Summary: Monitoring Plugin - check_dbi
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: libdbi-dbd-sqlite

%description dbi-sqlite
Provides check_dbi SQLite support for Nagios, Icinga, Naemon, Shinken.

%package dhcp
Summary: Monitoring Plugin - check_dhcp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: group(monplug)
Requires(pre): group(monplug)

%description dhcp
Provides check_dhcp support for Nagios, Icinga, Naemon, Shinken.

%package dig
Summary: Monitoring Plugin - check_dig
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/dig

%description dig
Provides check_dig support for Nagios, Icinga, Naemon, Shinken.

%package disk
Summary: Monitoring Plugin - check_disk
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description disk
Provides check_disk support for Nagios, Icinga, Naemon, Shinken.

%package disk_smb
Summary: Monitoring Plugin - check_disk_smb
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/smbclient

%description disk_smb
Provides check_disk_smb support for Nagios, Icinga, Naemon, Shinken.

%package dns
Summary: Monitoring Plugin - check_dns
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/nslookup

%description dns
Provides check_dns support for Nagios, Icinga, Naemon, Shinken.

%package dummy
Summary: Monitoring Plugin - check_dummy
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description dummy
Provides check_dummy support for Nagios, Icinga, Naemon, Shinken.
This plugin does not actually check anything, simply provide it with a flag
0-4 and it will return the corresponding status code to Nagios.

%package file_age
Summary: Monitoring Plugin - check_file_age
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description file_age
Provides check_file_age support for Nagios, Icinga, Naemon, Shinken.

%package flexlm
Summary: Monitoring Plugin - check_flexlm
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description flexlm
Provides check_flexlm support for Nagios, Icinga, Naemon, Shinken.

%package fping
Summary: Monitoring Plugin - check_fping
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_sbindir}/fping
Requires: group(monplug)
Requires(pre): group(monplug)

%description fping
Provides check_fping support for Nagios, Icinga, Naemon, Shinken.

%package game
Summary: Monitoring Plugin - check_game
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: qstat

%description game
Provides check_game support for Nagios, Icinga, Naemon, Shinken.

%package hpjd
Summary: Monitoring Plugin - check_hpjd
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description hpjd
Provides check_hpjd support for Nagios, Icinga, Naemon, Shinken.

%package http
Summary: Monitoring Plugin - check_http
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description http
Provides check_http support for Nagios, Icinga, Naemon, Shinken.

%package icmp
Summary: Monitoring Plugin - check_icmp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: group(monplug)
Requires(pre): group(monplug)

%description icmp
Provides check_icmp support for Nagios, Icinga, Naemon, Shinken.

%package ide_smart
Summary: Monitoring Plugin - check_ide_smart
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: group(monplug)
Requires(pre): group(monplug)

%description ide_smart
Provides check_ide_smart support for Nagios, Icinga, Naemon, Shinken.

%package ifoperstatus
Summary: Monitoring Plugin - check_ifoperstatus
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ifoperstatus
Provides check_ifoperstatus support for Nagios, Icinga, Naemon, Shinken to monitor network interfaces.

%package ifstatus
Summary: Monitoring Plugin - check_ifstatus
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ifstatus
Provides check_ifstatus support for Nagios, Icinga, Naemon, Shinken to monitor network interfaces.

%package ircd
Summary: Monitoring Plugin - check_ircd
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ircd
Provides check_ircd support for Nagios, Icinga, Naemon, Shinken.

%package ldap
Summary: Monitoring Plugin - check_ldap
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ldap
Provides check_ldap support for Nagios, Icinga, Naemon, Shinken.

%package load
Summary: Monitoring Plugin - check_load
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description load
Provides check_load support for Nagios, Icinga, Naemon, Shinken.

%package log
Summary: Monitoring Plugin - check_log
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: /bin/egrep
Requires: /bin/mktemp

%description log
Provides check_log support for Nagios, Icinga, Naemon, Shinken.

%package mailq
Summary: Monitoring Plugin - check_mailq
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/mailq

%description mailq
Provides check_mailq support for Nagios, Icinga, Naemon, Shinken.

%package mrtg
Summary: Monitoring Plugin - check_mrtg
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description mrtg
Provides check_mrtg support for Nagios, Icinga, Naemon, Shinken.

%package mrtgtraf
Summary: Monitoring Plugin - check_mrtgtraf
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description mrtgtraf
Provides check_mrtgtraf support for Nagios, Icinga, Naemon, Shinken.

%package mysql
Summary: Monitoring Plugin - check_mysql
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description mysql
Provides check_mysql and check_mysql_query support for Nagios, Icinga, Naemon, Shinken.

%package core
Summary: Monitoring Plugin - check_monitoring_core
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description core
Provides check_monitoring_core support for Nagios, Icinga, Naemon, Shinken.

%package nt
Summary: Monitoring Plugin - check_nt
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description nt
Provides check_nt support for Nagios, Icinga, Naemon, Shinken.

%package ntp
Summary: Monitoring Plugin - check_ntp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ntp
Provides check_ntp support for Nagios, Icinga, Naemon, Shinken.

%package ntp-perl
Summary: Monitoring Plugin - check_ntp.pl
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_sbindir}/ntpdate
Requires: %{_sbindir}/ntpq

%description ntp-perl
Provides check_ntp.pl support for Nagios, Icinga, Naemon, Shinken.

%package nwstat
Summary: Monitoring Plugin - check_nwstat
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description nwstat
Provides check_nwstat support for Nagios, Icinga, Naemon, Shinken.

%package oracle
Summary: Monitoring Plugin - check_oracle
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description oracle
Provides check_oracle support for Nagios, Icinga, Naemon, Shinken.

%package overcr
Summary: Monitoring Plugin - check_overcr
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description overcr
Provides check_overcr support for Nagios, Icinga, Naemon, Shinken.

%package perl
Summary: Nagios plugins perl dep.
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description perl
Perl dep for monitoring plugins.  This is *NOT* an actual plugin it simply provides
utils.pm

%package pgsql
Summary: Monitoring Plugin - check_pgsql
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description pgsql
Provides check_pgsql (PostgreSQL)  support for Nagios, Icinga, Naemon, Shinken.

%package ping
Summary: Monitoring Plugin - check_ping
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: /bin/ping
Requires: /bin/ping6

%description ping
Provides check_ping support for Nagios, Icinga, Naemon, Shinken.

%package procs
Summary: Monitoring Plugin - check_procs
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description procs
Provides check_procs support for Nagios, Icinga, Naemon, Shinken.

%package radius
Summary: Monitoring Plugin - check_radius
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description radius
Provides check_radius support for Nagios, Icinga, Naemon, Shinken.

%package real
Summary: Monitoring Plugin - check_real
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description real
Provides check_real (rtsp) support for Nagios, Icinga, Naemon, Shinken.

%package rpc
Summary: Monitoring Plugin - check_rpc
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_sbindir}/rpcinfo

%description rpc
Provides check_rpc support for Nagios, Icinga, Naemon, Shinken.

%ifnarch ppc ppc64 sparc sparc64
%package sensors
Summary: Monitoring Plugin - check_sensors
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: /bin/egrep
Requires: %{_bindir}/sensors

%description sensors
Provides check_sensors support for Nagios, Icinga, Naemon, Shinken.
%endif

%package smtp
Summary: Monitoring Plugin - check_smtp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description smtp
Provides check_smtp support for Nagios, Icinga, Naemon, Shinken.

%package snmp
Summary: Monitoring Plugin - check_snmp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Requires: %{_bindir}/snmpgetnext
Requires: %{_bindir}/snmpget

%description snmp
Provides check_snmp support for Nagios, Icinga, Naemon, Shinken.

%package ssh
Summary: Monitoring Plugin - check_ssh
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ssh
Provides check_ssh support for Nagios, Icinga, Naemon, Shinken.

%package swap
Summary: Monitoring Plugin - check_swap
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description swap
Provides check_swap support for Nagios, Icinga, Naemon, Shinken.

%package tcp
Summary: Monitoring Plugin - check_tcp
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}
Provides: monitoring-plugins-ftp = %{version}-%{release}
Provides: monitoring-plugins-imap = %{version}-%{release}
Provides: monitoring-plugins-jabber = %{version}-%{release}
Provides: monitoring-plugins-nntp = %{version}-%{release}
Provides: monitoring-plugins-nntps = %{version}-%{release}
Provides: monitoring-plugins-pop = %{version}-%{release}
Provides: monitoring-plugins-simap = %{version}-%{release}
Provides: monitoring-plugins-spop = %{version}-%{release}
Provides: monitoring-plugins-ssmtp = %{version}-%{release}
Provides: monitoring-plugins-udp = %{version}-%{release}
Provides: monitoring-plugins-udp2 = %{version}-%{release}
Obsoletes: monitoring-plugins-udp < 1.4.15-2

%description tcp
Provides check_tcp, check_ftp, check_imap, check_jabber, check_nntp,
check_nntps, check_pop, check_simap, check_spop, check_ssmtp, check_udp
and check_clamd support for Nagios, Icinga, Naemon, Shinken.

%package time
Summary: Monitoring Plugin - check_time
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description time
Provides check_time support for Nagios, Icinga, Naemon, Shinken.

%package ups
Summary: Monitoring Plugin - check_ups
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description ups
Provides check_ups support for Nagios, Icinga, Naemon, Shinken.

%package users
Summary: Monitoring Plugin - check_users
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description users
Provides check_users support for Nagios, Icinga, Naemon, Shinken.

%package wave
Summary: Monitoring Plugin - check_wave
Group: Applications/System
Requires: monitoring-plugins = %{version}-%{release}

%description wave
Provides check_wave support for Nagios, Icinga, Naemon, Shinken.

%prep
%setup -q

%patch2 -p1 -b .not_parsed
%patch3 -p1 -b .proper_paths
%patch4 -p1 -b .no_need_fo_fix_paths
%patch5 -p1 -b .fix_missing_swap
%patch7 -p1 -b .ext_ntp_cmds
%patch10 -p1 -b .ssd_smart_params

%build
%configure \
	--libexecdir=%{_libdir}/monitoring/plugins \
	--with-dbi \
	--with-mysql \
	PATH_TO_QSTAT=%{_bindir}/quakestat \
	PATH_TO_FPING=%{_sbindir}/fping \
	PATH_TO_NTPQ=%{_sbindir}/ntpq \
	PATH_TO_NTPDC=%{_sbindir}/ntpdc \
	PATH_TO_NTPDATE=%{_sbindir}/ntpdate \
	PATH_TO_RPCINFO=%{_sbindir}/rpcinfo \
	--with-ps-command="`which ps` -eo 's uid pid ppid vsz rss pcpu etime comm args'" \
	--with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
	--with-ps-cols=10 \
	--enable-extra-opts \
	--with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos'

make %{?_smp_mflags}
cd plugins
make check_ide_smart
make check_ldap
make check_radius
make check_pgsql

cd ..

mv plugins-scripts/check_ntp.pl plugins-scripts/check_ntp.pl.in
gawk -f plugins-scripts/subst plugins-scripts/check_ntp.pl.in > plugins-scripts/check_ntp.pl

cp %{SOURCE1} ./README.Fedora

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install
install -m 0755 plugins-root/check_icmp %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins-root/check_dhcp %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins/check_ide_smart %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins/check_ldap %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins-scripts/check_ntp.pl %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins/check_radius %{buildroot}/%{_libdir}/monitoring/plugins
install -m 0755 plugins/check_pgsql %{buildroot}/%{_libdir}/monitoring/plugins

%ifarch ppc ppc64 ppc64p7 sparc sparc64
rm -f %{buildroot}/%{_libdir}/monitoring/plugins/check_sensors
%endif

#until fixed upstream
mv %{buildroot}/%{_libdir}/monitoring/plugins/check_nagios %{buildroot}/%{_libdir}/monitoring/plugins/check_monitoring_core

chmod 644 %{buildroot}/%{_libdir}/monitoring/plugins/utils.pm

%find_lang %{name}

%pre common
getent group monplug >/dev/null || groupadd -r monplug
getent passwd monplug >/dev/null || useradd -r -g monplug -d %{buildroot}/%{_libdir}/monitoring/plugins -s /sbin/nologin monplug
exit 0

%files -f %{name}.lang
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog CODING COPYING FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS README.Fedora
%{_libdir}/monitoring/plugins/negate
%{_libdir}/monitoring/plugins/urlize
%{_libdir}/monitoring/plugins/utils.sh

%files all

%files common
%dir %{_libdir}/monitoring
%dir %{_libdir}/monitoring/plugins

%files apt
%{_libdir}/monitoring/plugins/check_apt

%files breeze
%{_libdir}/monitoring/plugins/check_breeze

%files by_ssh
%{_libdir}/monitoring/plugins/check_by_ssh

%files cluster
%{_libdir}/monitoring/plugins/check_cluster

%files dbi
%{_libdir}/monitoring/plugins/check_dbi

%files dbi-mysql

%files dbi-pgsql

%files dbi-sqlite

%files dhcp
%defattr(4750,root,monplug,-)
%{_libdir}/monitoring/plugins/check_dhcp

%files dig
%{_libdir}/monitoring/plugins/check_dig

%files disk
%{_libdir}/monitoring/plugins/check_disk

%files disk_smb
%{_libdir}/monitoring/plugins/check_disk_smb

%files dns
%{_libdir}/monitoring/plugins/check_dns

%files dummy
%{_libdir}/monitoring/plugins/check_dummy

%files file_age
%{_libdir}/monitoring/plugins/check_file_age

%files flexlm
%{_libdir}/monitoring/plugins/check_flexlm

%files fping
%defattr(4750,root,monplug,-)
%{_libdir}/monitoring/plugins/check_fping

%files game
%{_libdir}/monitoring/plugins/check_game

%files hpjd
%{_libdir}/monitoring/plugins/check_hpjd

%files http
%{_libdir}/monitoring/plugins/check_http

%files icmp
%defattr(4750,root,monplug,-)
%{_libdir}/monitoring/plugins/check_icmp

%files ifoperstatus
%{_libdir}/monitoring/plugins/check_ifoperstatus

%files ifstatus
%{_libdir}/monitoring/plugins/check_ifstatus

%files ide_smart
%defattr(4750,root,monplug,-)
%{_libdir}/monitoring/plugins/check_ide_smart

%files ircd
%{_libdir}/monitoring/plugins/check_ircd

%files ldap
%{_libdir}/monitoring/plugins/check_ldap
%{_libdir}/monitoring/plugins/check_ldaps

%files load
%{_libdir}/monitoring/plugins/check_load

%files log
%{_libdir}/monitoring/plugins/check_log

%files mailq
%{_libdir}/monitoring/plugins/check_mailq

%files mrtg
%{_libdir}/monitoring/plugins/check_mrtg

%files mrtgtraf
%{_libdir}/monitoring/plugins/check_mrtgtraf

%files mysql
%{_libdir}/monitoring/plugins/check_mysql
%{_libdir}/monitoring/plugins/check_mysql_query

%files core
%{_libdir}/monitoring/plugins/check_monitoring_core

%files nt
%{_libdir}/monitoring/plugins/check_nt

%files ntp
%{_libdir}/monitoring/plugins/check_ntp
%{_libdir}/monitoring/plugins/check_ntp_peer
%{_libdir}/monitoring/plugins/check_ntp_time

%files ntp-perl
%{_libdir}/monitoring/plugins/check_ntp.pl

%files nwstat
%{_libdir}/monitoring/plugins/check_nwstat

%files oracle
%{_libdir}/monitoring/plugins/check_oracle

%files overcr
%{_libdir}/monitoring/plugins/check_overcr

%files perl
%{_libdir}/monitoring/plugins/utils.pm

%files pgsql
%{_libdir}/monitoring/plugins/check_pgsql

%files ping
%{_libdir}/monitoring/plugins/check_ping

%files procs
%{_libdir}/monitoring/plugins/check_procs

%files radius
%{_libdir}/monitoring/plugins/check_radius

%files real
%{_libdir}/monitoring/plugins/check_real

%files rpc
%{_libdir}/monitoring/plugins/check_rpc

%ifnarch ppc ppc64 ppc64p7 sparc sparc64
%files sensors
%{_libdir}/monitoring/plugins/check_sensors
%endif

%files smtp
%{_libdir}/monitoring/plugins/check_smtp

%files snmp
%{_libdir}/monitoring/plugins/check_snmp

%files ssh
%{_libdir}/monitoring/plugins/check_ssh

%files swap
%{_libdir}/monitoring/plugins/check_swap

%files tcp
%{_libdir}/monitoring/plugins/check_clamd
%{_libdir}/monitoring/plugins/check_ftp
%{_libdir}/monitoring/plugins/check_imap
%{_libdir}/monitoring/plugins/check_jabber
%{_libdir}/monitoring/plugins/check_nntp
%{_libdir}/monitoring/plugins/check_nntps
%{_libdir}/monitoring/plugins/check_pop
%{_libdir}/monitoring/plugins/check_simap
%{_libdir}/monitoring/plugins/check_spop
%{_libdir}/monitoring/plugins/check_ssmtp
%{_libdir}/monitoring/plugins/check_tcp
%{_libdir}/monitoring/plugins/check_udp

%files time
%{_libdir}/monitoring/plugins/check_time

%files ups
%{_libdir}/monitoring/plugins/check_ups

%files users
%{_libdir}/monitoring/plugins/check_users

%files wave
%{_libdir}/monitoring/plugins/check_wave

%changelog
* Tue Jan 21 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.5-1
- import & refactoring from nagios plugins package
- use generic user 'monplug'
- mv check_nagios check_monitoring_core
- introduce check-dbi-{mysql,pgsql,sqlite} with dependencies on db drivers


