Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML dla zaawansowanych
Name:		bluefish
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Source0:	http://bluefish.openoffice.nl/download/%{name}-%{version}.tar.bz2
Source1:	bluefish.desktop
Patch0:		bluefish-DESTDIR.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Bluefish is a GTK+ based HTML editor designed for the experienced web
designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML, przeznaczonym dla
do¶wiadczonych projektantów stron WWW.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-install-location=%{_datadir}/bluefish
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors

make install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Editors

gzip -9nf README ChangeLog BUGS AUTHORS NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,BUGS,AUTHORS,NEWS,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%{_datadir}/bluefish
%{_applnkdir}/Office/Editors/bluefish.desktop
