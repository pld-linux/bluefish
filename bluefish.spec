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
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	imlib-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libungif-devel
BuildPrereq:	zlib-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Bluefish is a GTK+ based HTML editor designed 
for the experienced web designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML, 
przeznaczonym dla do¶wiadczonego projektanta stron WWW.

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
install -d $RPM_BUILD_ROOT/etc/X11/applnk/Editors

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Editors

gzip -9nf README ChangeLog BUGS AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,BUGS,AUTHORS,NEWS,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%{_datadir}/bluefish
/etc/X11/applnk/Editors/bluefish.desktop

%changelog
* Mon Jun 28 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.3.1-1]
- initial rpm release.
