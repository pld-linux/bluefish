Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML dla zaawansowanych
Summary(pt_BR):	Editor HTML Bluefish
Name:		bluefish
Version:	0.9
Release:	0.2
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
Patch4:		%{name}-pl.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1

%build
%ifarch i586
OPTIMIZATION="--enable-gcc3-optimization=pentium"
%endif
%ifarch i686 athlon
OPTIMIZATION="--enable-gcc3-optimization=pentiumpro"
%endif

%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	$OPTIMIZATION	
%{__make}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Editors/HTML,%{_pixmapsdir},%{_datadir},%{_bindir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Editors/HTML
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}/

cd po
make install DESTDIR=$RPM_BUILD_ROOT
cd ..

install src/%{name} $RPM_BUILD_ROOT%{_bindir}

install -d icons/ $RPM_BUILD_ROOT%{_datadir}/%{name}
install data/*.default $RPM_BUILD_ROOT%{_datadir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc 
%attr(755,root,root) %{_bindir}/*
%{_datadir}
%{_applnkdir}/Editors/HTML/bluefish.desktop
%{_pixmapsdir}/*
