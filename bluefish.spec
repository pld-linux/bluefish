Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML dla zaawansowanych
Name:		bluefish
Version:	0.3.2
Release:	1
Group:		X11/Applications/Editors
Group(pl):	X11/Aplikacje/Edytory
Copyright:	GPL
Source0:	http://bluefish.linuxbox.com/%{name}-%{version}.tar.gz
Source1:	bluefish.desktop
Patch:		bluefish-DESTDIR.patch
URL:            http://bluefish.linuxbox.com/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Bluefish is a GTK+ based HTML editor designed 
for the experienced web designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML, 
przeznaczonym dla doświadczonego projektanta stron WWW.

%prep
%setup -q
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--exec-prefix=%{_prefix} \
	--with-install-location=%{_datadir}/bluefish

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Editors

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Editors

gzip -9nf README ChangeLog BUGS AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,BUGS,AUTHORS,NEWS,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%{_datadir}/bluefish
/usr/X11R6/share/applnk/Editors/bluefish.desktop
