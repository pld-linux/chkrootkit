Summary:	chkrootkit - locally checks for signs of a rootkit
Summary(pl):	chkrootkit - narz�dzie do lokalnego szukania oznak rootkit�w
Name:		chkrootkit
Version:	0.35
Release:	1
License:	Copyrighted
Group:		Applications/Networking
Group(cs):	Aplikace/S��ov�
Group(da):	Programmer/Netv�rks
Group(de):	Applikationen/Netzwerkwesen
Group(es):	Aplicaciones/Red
Group(fr):	Applications/R�seau
Group(is):	Forrit/Net
Group(it):	Applicazioni/Rete
Group(no):	Applikasjoner/Nettverk
Group(pl):	Aplikacje/Sieciowe
Group(pt):	Aplica��es/Rede
Group(pt_BR):	Aplica��es/Rede
Group(ru):	����������/�������
Group(sl):	Programi/Omre�ni
Group(sv):	Till�mpningar/N�tverk
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/security/chkrootkit/%{name}-%{version}.tar.gz
Patch0:		%{name}-CC.patch
Patch1:		%{name}-nostrip.patch
Patch2:		%{name}-names.patch.gz
URL:		http://www.chkrootkit.org/
BuildRequires:	glibc-static
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
Chkrootkit to zestaw narz�dzi do lokalnego sprawdzania oznak u�ycia
rootkit�w.
 - chkrootkit: skrypt pow�oki sprawdzaj�cy binarne pliki systemowe na
   obecno�� modyfikacji typowych dla rootkit�w (je�li nie mo�na zaufa�
   rpm -Va)
 - ifpromisc: sprawdza czy interfejs sieciowy jest w trybie promiscuous
   (gdy nie mo�na zaufa� netstat)
 - chklastlog: sprawdza czy logi nie by�y kasowane
 - chkwtmp: sprawdza kasowanie wtmpx
 - check_wtmpx: sprawdza kasowanie w wtmpx deletions (tylko Solaris)
 - chkproc: szuka oznak trojan�w LKM (modu�y j�dra)
 - strings: szybkie i brzydkie podmiany ci�g�w znak�w.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
CC=%{__cc}
export CC
%{__make} sense


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for x in check_wtmpx chklastlog chkproc chkwtmp ifpromisc strings; do
    install $x $RPM_BUILD_ROOT/%{_bindir}/%{name}-$x
done

install chkrootkit $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf COPYRIGHT README README.chklastlog README.chkwtmp


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
