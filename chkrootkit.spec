Summary:	chkrootkit - locally checks for signs of a rootkit
Summary(pl):	chkrootkit - narzêdzie do lokalnego szukania oznak rootkitów
Name:		chkrootkit
Version:	0.42b
Release:	1
License:	AMS (BSD like; look at COPYRIGHT)
Group:		Applications/Networking
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/security/chkrootkit/%{name}-%{version}.tar.gz
# Source0-md5:	b708c13663b784db1b1e675279707f7e
Source1:	%{name}-check
Source2:	%{name}.sysconfig
Patch0:		%{name}-CC.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-names.patch
Patch3:		%{name}-wtmp.patch
Patch4:		%{name}-usebash.patch
Patch5:   http://www.rootshell.be/~unspawn/packaging/chkrootkit-0.42-ip.patch
# Patch5-md5: 0dfeda71b081eaa8c316eca1f81b21f0
URL:		http://www.chkrootkit.org/
BuildRequires:	glibc-static
Requires:	binutils
Requires:	bash
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

%description -l pl
Chkrootkit to zestaw narzêdzi do lokalnego sprawdzania oznak u¿ycia
rootkitów.
 - chkrootkit: skrypt pow³oki sprawdzaj±cy binarne pliki systemowe na
   obecno¶æ modyfikacji typowych dla rootkitów (je¶li nie mo¿na zaufaæ
   rpm -Va)
 - ifpromisc: sprawdza czy interfejs sieciowy jest w trybie promiscuous
   (gdy nie mo¿na zaufaæ netstat)
 - chklastlog: sprawdza czy logi nie by³y kasowane
 - chkwtmp: sprawdza kasowanie wtmpx
 - check_wtmpx: sprawdza kasowanie w wtmpx deletions (tylko Solaris)
 - chkproc: szuka oznak trojanów LKM (modu³y j±dra)
 - strings: szybko i brzydko napisany zamiennik programu strings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
CC=%{__cc}
export CC
%{__make} sense

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/{sysconfig,cron.weekly}}

for x in check_wtmpx chkdirs chklastlog chkproc chkwtmp ifpromisc strings; do
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
%attr(640,root,root) %config(noreplace) %verify(not mtime size md5) /etc/sysconfig/chkrootkit
%attr(755,root,root) %{_bindir}/*
