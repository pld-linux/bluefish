#
# Conditional build:
%bcond_with	python	# enable python integration (HIGHLY EXPERIMENTAL)
#
Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl.UTF-8):	Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	2.0.0
Release:	2
License:	GPL
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	ac9b1e8ef6d5691718a0daa6c78d5618
# but if you want ftp: try this one
# Source0:	ftp://bluefish.advancecreations.com/bluefish/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-locales.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gnome-vfs2-devel >= 2.2
BuildRequires:	gtk+2-devel	>= 2.14
BuildRequires: intltool
BuildRequires:	libbonobo-devel >= 2.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtiff-devel
BuildRequires: libtool
BuildRequires:	pcre-devel	>=	3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	gnome-vfs2 >= 2.2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%patch0 -p0
%patch1 -p1

mv -f po/ko{_KR,}.po
mv -f po/sr{,@Latn}.po
mv -f src/plugin_about/po/sr{,@Latn}.po  
mv -f src/plugin_charmap/po/sr{,@Latn}.po  
mv -f src/plugin_entities/po/sr{,@Latn}.po  
mv -f src/plugin_htmlbar/po/sr{,@Latn}.po  
mv -f src/plugin_infbrowser/po/sr{,@Latn}.po  
mv -f src/plugin_snippets/po/sr{,@Latn}.po

%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-update-databases \
	%{?with_python:--enable-python}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir -p doc/bflang/
mv data/bflang/sample.bflang2 doc/bflang/
rm -r %{buildroot}%{_docdir}/bluefish/

%find_lang %{name} --all-name

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
%doc AUTHORS README TODO doc/
%attr(755,root,root) %{_bindir}/bluefish
%dir %{_datadir}/%{name}
%{_datadir}/mime/packages/bluefish.xml
%dir %{_datadir}/xml/bluefish
%{_datadir}/xml/bluefish/catalog.xml
%{_datadir}/xml/bluefish/2.0/bflang2.rng
%{_datadir}/bluefish/bflang
%{_datadir}/bluefish/bflib
%{_datadir}/bluefish/bluefish_splash.png
%{_datadir}/bluefish/encodings
%{_mandir}/man1/bluefish.1*
%{_iconsdir}/hicolor/128x128/apps/bluefish.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/16x16/apps/bluefish.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/192x192/apps/bluefish.png
%{_iconsdir}/hicolor/192x192/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/22x22/apps/bluefish.png
%{_iconsdir}/hicolor/22x22/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/32x32/apps/bluefish.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/36x36/apps/bluefish.png
%{_iconsdir}/hicolor/36x36/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/48x48/apps/bluefish.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/64x64/apps/bluefish.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/72x72/apps/bluefish.png
%{_iconsdir}/hicolor/72x72/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/96x96/apps/bluefish.png
%{_iconsdir}/hicolor/96x96/mimetypes/application-x-bluefish-project.png
%{_iconsdir}/hicolor/scalable/apps/bluefish-icon.svg
%{_iconsdir}/hicolor/scalable/mimetypes/bluefish-project.svg
%{_desktopdir}/bluefish.desktop
%{_pixmapsdir}/application-x-bluefish-project.png
%{_pixmapsdir}/bluefish.png
%dir %{_libdir}/bluefish
%attr(755,root,root) %{_libdir}/bluefish/*.so
