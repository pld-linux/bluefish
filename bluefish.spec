Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML dla zaawansowanych
Summary(pt_BR):	Editor HTML Bluefish
Name:		bluefish
Version:	0.7
Release:	4
License:	GPL
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://pkedu.fbt.eitn.wau.nl/~olivier/downloads/%{name}-%{version}.tar.bz2
# but if you want ftp: try this one
# Source0:	ftp://bluefish.advancecreations.com/bluefish/downloads/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_lt.patch
Patch2:		%{name}-locale.patch
Patch3:		%{name}-netscape-now-mozilla.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Bluefish is a GTK+ based HTML editor designed for the experienced web
designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML, przeznaczonym dla
do¶wiadczonych projektantów stron WWW.

%description -l pt_BR
O bluefish é um editor HTML feito com GTK para web designers
experientes. Atualmente ele está em estágio alfa, mas já está bastante
usável. Algumas opções ainda não estão completamente finalizadas.
Bluefish é liberado sob a licença GPL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%ifarch i586
OPTIMIZATION="--with-pentium"
%endif
%ifarch i686 athlon
OPTIMIZATION="--with-pentiumpro"
%endif

%{__gettextize}
%{__libtoolize}
aclocal
%{__autoconf}
%configure \
	--with-install-location=%{_datadir}/bluefish \
	--with-autocomplet \
	$OPTIMIZATION
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Office/Editors,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog BUGS AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*

%{_datadir}/bluefish
%{_applnkdir}/Office/Editors/bluefish.desktop
%{_pixmapsdir}/*
