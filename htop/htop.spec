Name:           htop
Version:        1.0.2
Release:        1%{?dist}
Summary:        Interactive process viewer

Group:          Applications/System
License:        GPL+
URL:            http://htop.sourceforge.net/
Source0:        http://download.sourceforge.net/htop/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses-devel

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
%setup -q

%build
%configure --enable-openvz --enable-vserver --enable-taskstats \
           --enable-unicode --enable-native-affinity --enable-cgroup
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#remove empty direcories
rm -rf $RPM_BUILD_ROOT%{libdir}
rm -rf $RPM_BUILD_ROOT%{includedir}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/htop
%{_mandir}/man1/htop.1*

%changelog
