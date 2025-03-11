Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl.UTF-8):	Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	2.2.14
Release:	2
License:	GPL v3+
Group:		X11/Applications/Editors
# The master server is here
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	c99b6b1ba3e3e70b032936182bb0b387
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
#BuildRequires:	man
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
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
%patch -P 0 -p1

%{__mv} po/sr{,@Latn}.po
%{__mv} src/plugin_about/po/sr{,@Latn}.po
%{__mv} src/plugin_charmap/po/sr{,@Latn}.po
%{__mv} src/plugin_entities/po/sr{,@Latn}.po
%{__mv} src/plugin_htmlbar/po/sr{,@Latn}.po
%{__mv} src/plugin_infbrowser/po/sr{,@Latn}.po
%{__mv} src/plugin_snippets/po/sr{,@Latn}.po

for plugin in `ls -d src/plugin_*`; do
	cp %{_datadir}/gettext/po/Makefile.in.in $plugin/po
done

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      data/css_decompressor \
      data/cssmin.py \
      data/jsbeautify \
      data/jsmin.py \
      data/lorem-ipsum-generator \
      src/plugin_zencoding/zencoding/actions/__init__.py \
      src/plugin_zencoding/zencoding/actions/basic.py \
      src/plugin_zencoding/zencoding/actions/token.py \
      src/plugin_zencoding/zencoding/filters/__init__.py \
      src/plugin_zencoding/zencoding/filters/comment.py \
      src/plugin_zencoding/zencoding/filters/css.py \
      src/plugin_zencoding/zencoding/filters/escape.py \
      src/plugin_zencoding/zencoding/filters/format-css.py \
      src/plugin_zencoding/zencoding/filters/format.py \
      src/plugin_zencoding/zencoding/filters/haml.py \
      src/plugin_zencoding/zencoding/filters/html.py \
      src/plugin_zencoding/zencoding/filters/single-line.py \
      src/plugin_zencoding/zencoding/filters/trim.py \
      src/plugin_zencoding/zencoding/filters/xsl.py \
      src/plugin_zencoding/zencoding/html_matcher.py \
      src/plugin_zencoding/zencoding/resources.py \
      src/plugin_zencoding/zencoding/utils.py

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
%{_datadir}/bluefish/colorprofiles
%{_datadir}/bluefish/default_accelmap
%{_datadir}/bluefish/jsbeautifier
%{_datadir}/bluefish/templates
%{_datadir}/bluefish/ui
%attr(755,root,root) %{_datadir}/bluefish/css_decompressor
%attr(755,root,root) %{_datadir}/bluefish/cssmin.py
%attr(755,root,root) %{_datadir}/bluefish/jsbeautify
%attr(755,root,root) %{_datadir}/bluefish/jsmin.py
%attr(755,root,root) %{_datadir}/bluefish/lorem-ipsum-generator
%{_datadir}/mime/packages/bluefish.xml
%{_metainfodir}/bluefish.appdata.xml
%{_datadir}/xml/bluefish
%{_mandir}/man1/bluefish.1*
%{_iconsdir}/hicolor/*x*/apps/bluefish.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-bluefish-project.png
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
