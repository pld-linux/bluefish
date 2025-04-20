Summary:	Bluefish - HTML editor for the experienced web designer
Summary(pl.UTF-8):	Bluefish - Edytor HTML-a dla zaawansowanych
Name:		bluefish
Version:	2.2.17
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
# The master server is here
Source0:	https://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
# Source0-md5:	7b19a3691c7c5787e98174e58bd6d652
URL:		https://bluefish.openoffice.nl/index.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.8
BuildRequires:	enchant2-devel >= 1.4
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.20
BuildRequires:	glib2-devel >= 1:2.24
BuildRequires:	gtk+3-devel >= 3.2.2
BuildRequires:	gucharmap-devel >= 3.0
BuildRequires:	libtool >= 1.4
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxml2-progs
#BuildRequires:	man
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	glib2 >= 1:2.24
Requires:	hicolor-icon-theme
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

%package plugins
Summary:	Bluefish plugins
Summary(pl.UTF-8):	Wtyczki Bluefish
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description plugins
Bluefish plugins.

%description plugins -l pl.UTF-8
Wtyczki Bluefish.

%prep
%setup -q

# missing after gettext update
%{__sed} -ne '/define(\[_BF_LINGUAS/ s/.*, \[\([A-Za-z_ ]\+\)\])$/\1/p' configure.ac > po/LINGUAS
for dir in src/plugin_*/po ; do
	cp -p po/LINGUAS $dir
done

# disable enchant 1.x dependency, fallthrough to enchant-2 check
%{__sed} -i -e 's/\[enchant\]/[enchant-disabled]/' configure.ac

%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' \
	data/css_decompressor \
	data/json_prettyprint.py

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' \
      data/cssmin.py \
      data/jsmin.py \
      data/lorem-ipsum-generator

# not executable actually
%{__sed} -i -e '/^#!\/usr\/bin\/env python/d' \
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

for plugin in `ls -d src/plugin_*`; do
	cp %{_datadir}/gettext/po/Makefile.in.in $plugin/po
done

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-update-databases

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d doc/bflang
%{__mv} data/bflang/sample.bflang2 doc/bflang
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/bluefish
%{__rm} $RPM_BUILD_ROOT%{_libdir}/bluefish/*.la

# actually it's latin variant
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr,sr@latin}

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
%{_datadir}/bluefish/templates
%{_datadir}/bluefish/ui
%attr(755,root,root) %{_datadir}/bluefish/css_decompressor
%attr(755,root,root) %{_datadir}/bluefish/cssmin.py
%attr(755,root,root) %{_datadir}/bluefish/jsmin.py
%attr(755,root,root) %{_datadir}/bluefish/json_prettyprint.py
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

%files plugins -f %{name}_plugins.lang
%defattr(644,root,root,755)
%{_datadir}/bluefish/encodings
%{_datadir}/bluefish/plugins
%{_datadir}/bluefish/snippets
%attr(755,root,root) %{_libdir}/bluefish/*.so
