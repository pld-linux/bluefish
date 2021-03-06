#
Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl.UTF-8):	Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	2.2.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	6475325565fb0a003a75f88564b7835f
# but if you want ftp: try this one
# Source0:	ftp://bluefish.advancecreations.com/bluefish/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-locales.patch
URL:		http://bluefish.openoffice.nl/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.8
BuildRequires:	enchant-devel >= 1.4
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gtk+3-devel >= 3.2.2
BuildRequires:	gucharmap-devel >= 2.20
BuildRequires:	intltool
BuildRequires:	libpng >= 1.2.5
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	man
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
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

%package -n %{name}-plugins
Summary:	Bluefish plugins
Summary(pl.UTF-8):	Wtyczki Bluefish
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{name}-plugins
Bluefish plugins.

%description -n %{name}-plugins -l pl.UTF-8
Wtyczki Bluefish.

%prep
%setup -q
%patch0 -p1

mv -f po/sr{,@Latn}.po
mv -f src/plugin_about/po/sr{,@Latn}.po
mv -f src/plugin_charmap/po/sr{,@Latn}.po
mv -f src/plugin_entities/po/sr{,@Latn}.po
mv -f src/plugin_htmlbar/po/sr{,@Latn}.po
mv -f src/plugin_infbrowser/po/sr{,@Latn}.po
mv -f src/plugin_snippets/po/sr{,@Latn}.po

for plugin in `ls -d src/plugin_*`; do
	cp %{_datadir}/gettext/po/Makefile.in.in $plugin/po
done

%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-update-databases

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d doc/bflang/
mv data/bflang/sample.bflang2 doc/bflang/
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/bluefish/
%{__rm} $RPM_BUILD_ROOT%{_libdir}/bluefish/*.la

%find_lang %{name}
# lang files for plugins
%find_lang %{name}_plugin_about -a %{name}_plugins.lang
%find_lang %{name}_plugin_charmap -a %{name}_plugins.lang
%find_lang %{name}_plugin_entities -a %{name}_plugins.lang
%find_lang %{name}_plugin_htmlbar -a %{name}_plugins.lang
%find_lang %{name}_plugin_infbrowser -a %{name}_plugins.lang
%find_lang %{name}_plugin_snippets -a %{name}_plugins.lang
%find_lang %{name}_plugin_zencoding -a %{name}_plugins.lang

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
%{_datadir}/bluefish/bflang
%{_datadir}/bluefish/bflib
%{_datadir}/bluefish/bluefish_splash.png
%{_datadir}/bluefish/default_accelmap
%{_datadir}/bluefish/templates
%{_datadir}/bluefish/ui
%{_datadir}/mime/packages/bluefish.xml
%{_datadir}/xml/bluefish
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

%files -n %{name}-plugins -f %{name}_plugins.lang
%defattr(644,root,root,755)
%{_datadir}/bluefish/encodings
%{_datadir}/bluefish/plugins
%{_datadir}/bluefish/snippets
%attr(755,root,root) %{_libdir}/bluefish/*.so
