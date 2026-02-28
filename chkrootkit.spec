# TODO
# - move programs to sbindir?
Summary:	chkrootkit - locally checks for signs of a rootkit
Summary(pl.UTF-8):	chkrootkit - narzędzie do lokalnego szukania oznak rootkitów
Name:		chkrootkit
Version:	0.52
Release:	2
License:	AMS (BSD like; look at COPYRIGHT)
Group:		Applications/Networking
Source0:	ftp://ftp.pangeia.com.br/pub/seg/pac/%{name}-%{version}.tar.gz
# Source0-md5:	0c864b41cae9ef9381292b51104b0a04
Source1:	%{name}-check
Source2:	%{name}.sysconfig
Patch0:		%{name}-CC.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-names.patch
Patch3:		%{name}-wtmp.patch
Patch4:		%{name}-usebash.patch
Patch5:		%{name}-utmpx.patch
URL:		http://www.chkrootkit.org/
BuildRequires:	glibc-static
Requires:	bash
Requires:	binutils
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chkrootkit is a toolkit to locally check for signs of a rootkit.
- chkrootkit: a shell script that checks system binaries for rootkit
  modification. (If you can't trust rpm -Va)
- ifpromisc: checks if the network interface is in promiscuous mode.
  (If you can't trust netstat)
- chklastlog: checks for lastlog deletions.
- chkwtmp: checks for wtmp deletions.
- check_wtmpx: checks for wtmpx deletions. (Solaris only)
- chkproc: checks for signs of LKM trojans. (kernel modules)
- strings: quick and dirty strings replacement.

This package is a little outdated, please use rkhunter or similar for
better results.

%description -l pl.UTF-8
Chkrootkit to zestaw narzędzi do lokalnego sprawdzania oznak użycia
rootkitów.
- chkrootkit: skrypt powłoki sprawdzający binarne pliki systemowe na
  obecność modyfikacji typowych dla rootkitów (jeśli nie można zaufać
  rpm -Va)
- ifpromisc: sprawdza czy interfejs sieciowy jest w trybie promiscuous
  (gdy nie można zaufać netstat)
- chklastlog: sprawdza czy logi nie były kasowane
- chkwtmp: sprawdza kasowanie wtmpx
- check_wtmpx: sprawdza kasowanie w wtmpx deletions (tylko Solaris)
- chkproc: szuka oznak trojanów LKM (moduły jądra)
- strings: szybko i brzydko napisany zamiennik programu strings.

Pakiet ten jest przestarzały, lepiej używać rkhunter lub podobnego.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
CC="%{__cc}"
export CC
%{__make} sense

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/{sysconfig,cron.weekly}}

for x in check_wtmpx chkdirs chklastlog chkproc chkwtmp ifpromisc strings-static chkutmp; do
	install $x $RPM_BUILD_ROOT%{_bindir}/%{name}-$x
done

install chkrootkit $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/cron.weekly
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/chkrootkit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README README.chklastlog README.chkwtmp
%attr(750,root,root) /etc/cron.weekly/chkrootkit-check
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/chkrootkit
%attr(755,root,root) %{_bindir}/*
