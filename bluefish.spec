#
# Conditional build:
%bcond_with opts	# use extra optimizations
#
# note: optflags used with this bcond are very strong, and partially
#	obsoleted for C (like -fno-rtti) - use at own risk!
#
Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML dla zaawansowanych
Name:		bluefish
Version:	0.12
Release:	1
License:	GPL
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://pkedu.fbt.eitn.wau.nl/~olivier/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	9b01162747c7be6e2fc46475544bf995
# but if you want ftp: try this one
# Source0:	ftp://bluefish.advancecreations.com/bluefish/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-home_etc.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.2
BuildRequires:	gtk+2-devel
BuildRequires:	libbonobo-devel >= 2.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluefish is a GTK+ based HTML editor designed for the experienced web
designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML, przeznaczonym dla
do�wiadczonych projektant�w stron WWW.

%description -l pt_BR
O bluefish � um editor HTML feito com GTK para web designers
experientes. Atualmente ele est� em est�gio alfa, mas j� est� bastante
us�vel. Algumas op��es ainda n�o est�o completamente finalizadas.
Bluefish � liberado sob a licen�a GPL.

%prep
%setup -q
%patch0 -p1
%patch1	-p1
#%patch2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{?with_opts:--enable-auto-optimization}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c inline_images/bluefish_icon1.png $RPM_BUILD_ROOT%{_pixmapsdir}/bluefish.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
