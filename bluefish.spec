#
# Conditional build:
%bcond_with	opts	# use extra optimizations
#
# note: optflags used with this bcond are very strong, and partially
#	obsoleted for C (like -fno-rtti) - use at own risk!
#
Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl.UTF-8):   Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	1.0.7
Release:	2
License:	GPL
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	2c3b3c9c8f8e32b9473dfd879f216dea
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
BuildRequires:	home-etc-devel
BuildRequires:	libbonobo-devel >= 2.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluefish is a GTK+ based HTML editor designed for the experienced web
designer.

%description -l pl.UTF-8
Bluefish jest opartym na GTK+ edytorem HTML-a, przeznaczonym dla
doświadczonych projektantów stron WWW.

%description -l pt_BR.UTF-8
O bluefish é um editor HTML feito com GTK+ para web designers
experientes. Atualmente ele está em estágio alfa, mas já está bastante
usável. Algumas opções ainda não estão completamente finalizadas.
Bluefish é liberado sob a licença GPL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po
mv -f po/sr{,@Latn}.po

%build
%{__aclocal}
%{__autoconf}
%configure \
	--disable-update-databases \
	--with-freedesktop_org-mime=/usr/share/mime \
	--without-gnome2_4-mime \
	--without-gnome2_4-appreg \
	%{?with_opts:--enable-auto-optimization}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/mimetypes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/gnome-mime-application-bluefish-project.png \
    $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-bluefish-project.png
rm -f $RPM_BUILD_ROOT%{_desktopdir}/bluefish-project.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/bluefish
%{_datadir}/%{name}
%{_datadir}/mime/packages/bluefish.xml
%{_mandir}/man1/bluefish.1*
%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-bluefish-project.png
%{_desktopdir}/bluefish.desktop
%{_pixmapsdir}/bluefish-icon.png
