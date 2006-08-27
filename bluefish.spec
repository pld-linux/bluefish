#
# Conditional build:
%bcond_with	opts	# use extra optimizations
#
# note: optflags used with this bcond are very strong, and partially
#	obsoleted for C (like -fno-rtti) - use at own risk!
#
Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl):	Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	1.0.4
Release:	2
License:	GPL
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://pkedu.fbt.eitn.wau.nl/~olivier/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	8d5c1b7315cdc935aa024954093d2b32
# but if you want ftp: try this one
# Source0:	ftp://bluefish.advancecreations.com/bluefish/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-locales.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gnome-vfs2-devel >= 2.2
BuildRequires:	gtk+2-devel
BuildRequires:	libbonobo-devel >= 2.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluefish is a GTK+ based HTML editor designed for the experienced web
designer.

%description -l pl
Bluefish jest opartym na GTK+ edytorem HTML-a, przeznaczonym dla
do¶wiadczonych projektantów stron WWW.

%description -l pt_BR
O bluefish é um editor HTML feito com GTK+ para web designers
experientes. Atualmente ele está em estágio alfa, mas já está bastante
usável. Algumas opções ainda não estão completamente finalizadas.
Bluefish é liberado sob a licença GPL.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po
mv -f po/sr{,@Latn}.po

%build
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-update-databases \
	--without-gnome2_4-mime \
	--without-gnome2_4-appreg \
	%{?with_opts:--enable-auto-optimization}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/mimetypes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_desktopdir}/bluefish-project.desktop
mv $RPM_BUILD_ROOT%{_pixmapsdir}/gnome-application-bluefish-project.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/mimetypes

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
update-mime-database %{_datadir}/mime ||:
%update_desktop_database_post

%postun
%update_desktop_database_postun
if [ $1 = 0 ]; then
    umask 022
    update-mime-database %{_datadir}/mime
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
%{_pixmapsdir}/*
