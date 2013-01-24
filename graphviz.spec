# TODO
# - %{_libdir}/graphviz/config is not FHS friendly path as config
# - go language binding [6g, 8g???]
# - io language binding: io-graphviz
# - some plugin subpackages? (libgvplugin_*: gs=ghostscript, gtk, lasi, ming, visio, webp)
# - smyrna subpackage? (R: OpenGL, glut, gtk+2, gtkglext, libglade2)
#
# Conditional build:
%bcond_without	dotnet		# don't build C# bindings
%bcond_without	java		# don't build Java bindings
%bcond_without	ocaml		# don't build ocaml bindings
%bcond_without	php		# don't build php bindings
%bcond_without	perl		# don't build perl bindings
%bcond_without	ruby		# don't build ruby bindings
%bcond_without	tcl		# don't build tcl bindings
%bcond_without	lua		# don't build lua bindings
%bcond_without	r		# don't build R bindings
%bcond_without	python 		# don't build python bindings
%bcond_with	io		# don't build io language bindings
%bcond_without	guile		# don't build guile bindings
%bcond_without	ming		# don't build ming support
%bcond_without	devil		# don't build devil plugin
%bcond_without	smyrna		# SMYRNA utility (large graph viewer)
%bcond_without	ipsepcola	# IPSEPCOLA features in neato engine [C++ portability problems]

%define		tclver	8.5
%ifarch i386
%undefine with_dotnet
%endif
%ifnarch %{ix86} %{x8664}
%undefine with_java
%endif
%ifarch i386 i486
%undefine with_java
%endif
%{?with_perl:%include	/usr/lib/rpm/macros.perl}
Summary:	Graph Visualization Tools
Summary(pl.UTF-8):	Narzędzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	2.30.0
Release:	2
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	967ad0a3d2bf164082e076c4416ede95
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-tk.patch
Patch2:		%{name}-bad-header.patch
Patch3:		%{name}-php.patch
Patch4:		%{name}-ltdl.patch
Patch5:		%{name}-lua51.patch
Patch6:		%{name}-php_modules_dir.patch
Patch7:		%{name}-ruby.patch
Patch8:		%{name}-guile.patch
Patch9:		%{name}-libgraph.patch
Patch10:	%{name}-ming.patch
Patch11:	%{name}-visio.patch
Patch12:	%{name}-webp.patch
Patch13:	%{name}-format.patch
URL:		http://www.graphviz.org/
%{?with_devil:BuildRequires:	DevIL-devel}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
%{?with_r:BuildRequires:	R}
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-devel
BuildRequires:	ghostscript-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	gts-devel
%{?with_guile:BuildRequires:	guile-devel >= 2.0}
#BuildRequires:	io
%if %{with java}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%endif
BuildRequires:	libLASi-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 2:2
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel
BuildRequires:	libvisio-devel
# for lua51 binary
%if %{with lua}
BuildRequires:	lua51
BuildRequires:	lua51-devel >= 5.1
%endif
%{?with_ming:BuildRequires:	ming-devel >= 0.4}
%{?with_dotnet:BuildRequires:	mono-csharp}
%{?with_ocaml:BuildRequires:	ocaml}
BuildRequires:	pango-devel >= 1:1.14.9
BuildRequires:	perl-devel
%if %{with php}
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	php-program >= 4:5.0
%endif
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	qt4-qmake >= 4
%{?with_perl:BuildRequires:	rpm-perlprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 1.519
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRequires:	sed >= 4.0
# swig-csharp,swig-go,swig-java,swig-lua,swig-ocaml in main swig
# swig-io ???
BuildRequires:	swig >= 1.3
%{?with_guile:BuildRequires:	swig-guile >= 2.0.3}
%{?with_perl:BuildRequires:	swig-perl >= 1.3}
%{?with_php:BuildRequires:	swig-php >= 1.3.40}
BuildRequires:	swig-python >= 1.3
%{?with_ruby:BuildRequires:	swig-ruby >= 1.3}
%if %{with tcl}
BuildRequires:	swig-tcl >= 1.3
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
# tested in configure, actually not used
#BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zlib-devel
%if %{with smyrna}
BuildRequires:	OpenGL-glut-devel
# only tested, actually not used
#BuildRequires:	gtkglarea-devel >= 2.0
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	libglade2-devel >= 2.0
%endif
Requires(post,postun):	/sbin/ldconfig
Requires:	fonts-Type1-urw
Requires:	gd >= 2.0.33-5
Requires:	pango >= 1:1.14.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl.UTF-8
Kolekcja narzędzi oraz pakietów tcl służących do manipulacji i
rozmieszczania grafów.

%package devel
Summary:	Header files for graphviz libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do bibliotek graphviz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gd-devel >= 2.0.34
Requires:	libltdl-devel >= 2:2

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do bibliotek graphviz.

%package doc-html
Summary:	HTML documentation for graphviz
Summary(pl.UTF-8):	Dokumentacja do graphviza w formacie HTML
Group:		Documentation

%description doc-html
HTML documentation for graphviz.

%description doc-html -l pl.UTF-8
Dokumentacja do graphviza w formacie HTML.

%package doc-pdf
Summary:	PDF documentation for graphviz
Summary(pl.UTF-8):	Dokumentacja do graphviza w formacie PDF
Group:		Documentation

%description doc-pdf
PDF documentation for graphviz.

%description doc-pdf -l pl.UTF-8
Dokumentacja do graphviza w formacie PDF.

%package graphs
Summary:	Demo graphs for graphviz
Summary(pl.UTF-8):	Przykładowe grafy dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description graphs
This package provides some example graphs.

%description graphs -l pl.UTF-8
Ten pakiet zawiera trochę przykładowych grafów.

%package -n guile-%{name}
Summary:	Guile binding for graphviz
Summary(pl.UTF-8):	Wiązania Guile dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-guile

%description -n guile-%{name}
Guile binding for graphviz.

%description -n guile-%{name} -l pl.UTF-8
Wiązania Guile dla graphviza.

%package -n java-%{name}
Summary:	Java binding for graphviz
Summary(pl.UTF-8):	Wiązania Javy dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-java

%description -n java-%{name}
Java binding for graphviz.

%description -n java-%{name} -l pl.UTF-8
Wiązania Javy dla graphviza.

%package -n lua-%{name}
Summary:	LUA binding for graphviz
Summary(pl.UTF-8):	Wiązania LUA dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-lua

%description -n lua-%{name}
LUA binding for graphviz.

%description -n lua-%{name} -l pl.UTF-8
Wiązania LUA dla graphviza.

%package -n ocaml-%{name}
Summary:	OCaml binding for graphviz
Summary(pl.UTF-8):	Wiązania OCamla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-ocaml

%description -n ocaml-%{name}
OCaml binding for graphviz.

%description -n ocaml-%{name} -l pl.UTF-8
Wiązania OCamla dla graphviza.

%package -n perl-%{name}
Summary:	Perl binding for graphviz
Summary(pl.UTF-8):	Wiązania Perla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n perl-%{name}
Perl binding for graphviz.

%description -n perl-%{name} -l pl.UTF-8
Wiązania Perla dla graphviza.

%package -n php-%{name}
Summary:	PHP binding for graphviz
Summary(pl.UTF-8):	Wiązania PHP dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-php
%{?requires_php_extension}

%description -n php-%{name}
PHP binding for graphviz.

%description -n php-%{name} -l pl.UTF-8
Wiązania PHP dla graphviza.

%package -n python-%{name}
Summary:	Python binding for graphviz
Summary(pl.UTF-8):	Wiązania Pythona dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-python

%description -n python-%{name}
Python binding for graphviz.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona dla graphviza.

%package -n ruby-%{name}
Summary:	Ruby binding for graphviz
Summary(pl.UTF-8):	Wiązania Ruby'ego dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-ruby

%description -n ruby-%{name}
Ruby binding for graphviz.

%description -n ruby-%{name} -l pl.UTF-8
Wiązania Ruby'ego dla graphviza.

%package -n dotnet-%{name}-sharp
Summary:	C# binding for graphviz
Summary(pl.UTF-8):	Wiązania C# dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-sharp
Obsoletes:	sharp-graphviz

%description -n dotnet-%{name}-sharp
C# binding for graphviz.

%description -n dotnet-%{name}-sharp -l pl.UTF-8
Wiązania C# dla graphviza.

%package -n tcl-%{name}
Summary:	Tcl extension tools for graphviz
Summary(pl.UTF-8):	Rozszerzenia Tcl dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-tcl

%description -n tcl-%{name}
This package contains the various Tcl packages (extensions) using
graphviz.

%description -n tcl-%{name} -l pl.UTF-8
Ten pakiet zawiera różne pakiety (rozszerzenia) Tcl używające
graphviza.

%package -n R-%{name}
Summary:	graphviz bindings for R language
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description -n R-%{name}
graphviz bindings for R language.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%{__sed} '1s@/usr/bin/lua$@/usr/bin/lua51@' -i tclpkg/gv/demo/modgraph.lua

%{__rm} m4/*.m4

%build
touch config/config.rpath
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

CPPFLAGS="%{rpmcppflags}"
%if %{with java}
JAVA_HOME=%{java_home}
export JAVA_HOME
CPPFLAGS="$CPPFLAGS -I$JAVA_HOME/include -I$JAVA_HOME/include/linux"
%endif

export CPPFLAGS

%configure \
	lua_suffix=51 \
	%{!?with_devil:--disable-devil} \
	%{!?with_java:--disable-java} \
	--disable-ltdl-install \
	%{!?with_lua:--disable-lua} \
	%{!?with_ocaml:--disable-ocaml} \
	%{!?with_perl:--disable-perl} \
	%{!?with_php:--disable-php} \
	%{!?with_r:--disable-r} \
	%{!?with_ruby:--disable-ruby} \
	%{!?with_dotnet:--disable-sharp} \
	%{!?with_tcl:--disable-tcl} \
	--disable-silent-rules \
	--disable-static \
	%{?with_ipsepcola:--with-ipsepcola} \
	%{?with_ming:--with-ming} \
	%{?with_smyrna:--with-smyrna} \
	--with-visio \
	--with-webp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PHP_INSTALL_DIR=%{php_extensiondir} \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with php}
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{name}.ini
; Enable gv.so extension module
extension=gv.so
EOF

# drop the symlinks and install to php dirs directly
install -d $RPM_BUILD_ROOT%{_examplesdir}/php-%{name}-%{version}
mv -f $RPM_BUILD_ROOT{%{_libdir}/%{name}/php,%{php_data_dir}}/gv.php
mv -f $RPM_BUILD_ROOT{%{_libdir}/%{name}/php/libgv_php.so,%{php_extensiondir}/gv.so}
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/php/gv.so
mv -f $RPM_BUILD_ROOT{%{_datadir}/%{name}/demo,%{_examplesdir}/php-%{name}-%{version}}/modgraph.php
%endif

# "man3/gv.3r.gz" and "man3/gv.3ruby.gz" are both manual for "gv" in "section 3" of man pages
# make manual pages unique.
for a in $RPM_BUILD_ROOT%{_mandir}/man3/gv.*; do
	m=${a##*/}
	l=${m#gv.3}
	mv $a ${a%/*}/gv_$l.3
done

# created by %{_bindir}/dot -c
touch $RPM_BUILD_ROOT%{_libdir}/graphviz/config

%{__rm} $RPM_BUILD_ROOT%{_libdir}/graphviz/*/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/graphviz/libgvplugin_*.la

rm -rf doc-html doc-pdf
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/html doc-html
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/pdf doc-pdf

cd $RPM_BUILD_ROOT
patch -p1 --no-backup-if-mismatch < %{PATCH2} || exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -c > /dev/null 2>&1

%postun	-p /sbin/ldconfig

%post -n php-%{name}
%php_webserver_restart

%postun -n php-%{name}
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/acyclic
%attr(755,root,root) %{_bindir}/bcomps
%attr(755,root,root) %{_bindir}/ccomps
%attr(755,root,root) %{_bindir}/circo
%attr(755,root,root) %{_bindir}/cluster
%attr(755,root,root) %{_bindir}/diffimg
%attr(755,root,root) %{_bindir}/dijkstra
%attr(755,root,root) %{_bindir}/dot
%attr(755,root,root) %{_bindir}/dot2gxl
%attr(755,root,root) %{_bindir}/dot_builtins
%attr(755,root,root) %{_bindir}/dotty
%attr(755,root,root) %{_bindir}/fdp
%attr(755,root,root) %{_bindir}/gc
%attr(755,root,root) %{_bindir}/gml2gv
%attr(755,root,root) %{_bindir}/graphml2gv
%attr(755,root,root) %{_bindir}/gv2gml
%attr(755,root,root) %{_bindir}/gv2gxl
%attr(755,root,root) %{_bindir}/gvcolor
%attr(755,root,root) %{_bindir}/gvedit
%attr(755,root,root) %{_bindir}/gvgen
%attr(755,root,root) %{_bindir}/gvmap
%attr(755,root,root) %{_bindir}/gvmap.sh
%attr(755,root,root) %{_bindir}/gvpack
%attr(755,root,root) %{_bindir}/gvpr
%attr(755,root,root) %{_bindir}/gxl2dot
%attr(755,root,root) %{_bindir}/gxl2gv
%attr(755,root,root) %{_bindir}/lefty
%attr(755,root,root) %{_bindir}/lneato
%attr(755,root,root) %{_bindir}/mm2gv
%attr(755,root,root) %{_bindir}/neato
%attr(755,root,root) %{_bindir}/nop
%attr(755,root,root) %{_bindir}/osage
%attr(755,root,root) %{_bindir}/patchwork
%attr(755,root,root) %{_bindir}/prune
%attr(755,root,root) %{_bindir}/sccmap
%attr(755,root,root) %{_bindir}/sfdp
%if %{with smyrna}
%attr(755,root,root) %{_bindir}/smyrna
%endif
%attr(755,root,root) %{_bindir}/tred
%attr(755,root,root) %{_bindir}/twopi
%attr(755,root,root) %{_bindir}/unflatten
%attr(755,root,root) %{_bindir}/vimdot
%attr(755,root,root) %{_libdir}/libcdt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdt.so.5
%attr(755,root,root) %{_libdir}/libcgraph.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgraph.so.6
%attr(755,root,root) %{_libdir}/libgraph.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraph.so.5
%attr(755,root,root) %{_libdir}/libgvc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvc.so.6
%attr(755,root,root) %{_libdir}/libgvpr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvpr.so.2
%attr(755,root,root) %{_libdir}/libpathplan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpathplan.so.4
%attr(755,root,root) %{_libdir}/libxdot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxdot.so.4
%dir %{_libdir}/graphviz
%ghost %{_libdir}/graphviz/config
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_core.so*
%if %{with devil}
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_devil.so*
%endif
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_dot_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gd.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gdk_pixbuf.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gs.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gtk.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_lasi.so*
%if %{with ming}
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_ming.so*
%endif
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_pango.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_rsvg.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_visio.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_webp.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_xlib.so*
%dir %{_datadir}/graphviz
%dir %{_datadir}/graphviz/demo
%if %{with ming}
# for ming plugin
%{_datadir}/graphviz/font
%endif
%{_datadir}/graphviz/gvedit
%{_datadir}/graphviz/gvpr
%{_datadir}/graphviz/lefty
%if %{with smyrna}
%{_datadir}/graphviz/smyrna
%endif
%{_mandir}/man1/acyclic.1*
%{_mandir}/man1/bcomps.1*
%{_mandir}/man1/ccomps.1*
%{_mandir}/man1/circo.1*
%{_mandir}/man1/cluster.1*
%{_mandir}/man1/diffimg.1*
%{_mandir}/man1/dijkstra.1*
%{_mandir}/man1/dot.1*
%{_mandir}/man1/dotty.1*
%{_mandir}/man1/fdp.1*
%{_mandir}/man1/gc.1*
%{_mandir}/man1/gml2gv.1*
%{_mandir}/man1/graphml2gv.1*
%{_mandir}/man1/gv2gml.1*
%{_mandir}/man1/gv2gxl.1*
%{_mandir}/man1/gvcolor.1*
%{_mandir}/man1/gvedit.1*
%{_mandir}/man1/gvgen.1*
%{_mandir}/man1/gvmap.1*
%{_mandir}/man1/gvmap.sh.1*
%{_mandir}/man1/gvpack.1*
%{_mandir}/man1/gvpr.1*
%{_mandir}/man1/gxl2gv.1*
%{_mandir}/man1/lefty.1*
%{_mandir}/man1/lneato.1*
%{_mandir}/man1/mm2gv.1*
%{_mandir}/man1/neato.1*
%{_mandir}/man1/nop.1*
%{_mandir}/man1/osage.1*
%{_mandir}/man1/patchwork.1*
%{_mandir}/man1/prune.1*
%{_mandir}/man1/sccmap.1*
%{_mandir}/man1/sfdp.1*
%{_mandir}/man1/smyrna.1*
%{_mandir}/man1/tred.1*
%{_mandir}/man1/twopi.1*
%{_mandir}/man1/unflatten.1*
%{_mandir}/man1/vimdot.1*
%{_mandir}/man7/graphviz.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdt.so
%attr(755,root,root) %{_libdir}/libcgraph.so
%attr(755,root,root) %{_libdir}/libgraph.so
%attr(755,root,root) %{_libdir}/libgvc.so
%attr(755,root,root) %{_libdir}/libgvpr.so
%attr(755,root,root) %{_libdir}/libpathplan.so
%attr(755,root,root) %{_libdir}/libxdot.so
%{_libdir}/libcdt.la
%{_libdir}/libcgraph.la
%{_libdir}/libgraph.la
%{_libdir}/libgvc.la
%{_libdir}/libgvpr.la
%{_libdir}/libpathplan.la
%{_libdir}/libxdot.la
%{_pkgconfigdir}/libcdt.pc
%{_pkgconfigdir}/libcgraph.pc
%{_pkgconfigdir}/libgraph.pc
%{_pkgconfigdir}/libgvc.pc
%{_pkgconfigdir}/libgvpr.pc
%{_pkgconfigdir}/libpathplan.pc
%{_pkgconfigdir}/libxdot.pc
%{_includedir}/graphviz
%{_mandir}/man3/cdt.3*
%{_mandir}/man3/cgraph.3*
%{_mandir}/man3/expr.3*
%{_mandir}/man3/graph.3*
%{_mandir}/man3/gvc.3*
%{_mandir}/man3/pack.3*
%{_mandir}/man3/xdot.3*

%files doc-html
%defattr(644,root,root,755)
%doc doc-html/*

%files doc-pdf
%defattr(644,root,root,755)
%doc doc-pdf/*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

%if 0
%files io-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/io
%attr(755,root,root) %{_libdir}/graphviz/io/libgv_io.so*
%{_mandir}/mann/gv_io.n*
%endif

%if %{with guile}
%files -n guile-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/guile
%attr(755,root,root) %{_libdir}/graphviz/guile/libgv_guile.so
%{_mandir}/man3/gv_guile.3*
%endif

%if %{with java}
%files -n java-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/java
%attr(755,root,root) %{_libdir}/graphviz/java/libgv_java.so
%{_libdir}/graphviz/java/*.java
%{_mandir}/man3/gv_java.3*
%endif

%if %{with lua}
%files -n lua-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/lua
%attr(755,root,root) %{_libdir}/graphviz/lua/libgv_lua.so
%attr(755,root,root) %{_libdir}/graphviz/lua/gv.so
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.lua
%attr(755,root,root) %{_libdir}/lua/gv.so
%{_mandir}/man3/gv_lua.3*
%endif

%if %{with ocaml}
%files -n ocaml-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ocaml
%attr(755,root,root) %{_libdir}/graphviz/ocaml/libgv_ocaml.so
%{_libdir}/graphviz/ocaml/META.gv
# ocamlopt temporarily disabled
#%{_libdir}/graphviz/ocaml/gv.a
%{_libdir}/graphviz/ocaml/gv.cm*
#%{_libdir}/graphviz/ocaml/gv.ml*
%{_mandir}/man3/gv_ocaml.3*
%endif

%if %{with perl}
%files -n perl-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/perl
%attr(755,root,root) %{_libdir}/graphviz/perl/libgv_perl.so
%attr(755,root,root) %{_libdir}/graphviz/perl/gv.so
%{_libdir}/graphviz/perl/gv.pm
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.pl
%attr(755,root,root) %{perl_vendorarch}/gv.so
%{perl_vendorarch}/gv.pm
%{_mandir}/man3/gv_perl.3*
%endif

%if %{with php}
%files -n php-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/gv.so
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{name}.ini
%{php_data_dir}/gv.php
%{_mandir}/man3/gv_php.3*
%{_examplesdir}/php-%{name}-%{version}
%endif

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/python
%attr(755,root,root) %{_libdir}/graphviz/python/libgv_python.so
%attr(755,root,root) %{_libdir}/graphviz/python/_gv.so
%{_libdir}/graphviz/python/gv.py
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.py
%attr(755,root,root) %{py_sitedir}/_gv.so
%{py_sitedir}/gv.py
%{_mandir}/man3/gv_python.3*
%endif

%if %{with ruby}
%files -n ruby-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ruby
%attr(755,root,root) %{_libdir}/graphviz/ruby/libgv_ruby.so
%attr(755,root,root) %{_libdir}/graphviz/ruby/gv.so
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.rb
%{ruby_vendorarchdir}/gv.so
%{_mandir}/man3/gv_ruby.3*
%endif

%if %{with dotnet}
%files -n dotnet-%{name}-sharp
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/sharp
%attr(755,root,root) %{_libdir}/graphviz/sharp/libgv_sharp.so
%{_libdir}/graphviz/sharp/*.cs
%{_mandir}/man3/gv_sharp.3*
%endif

%if %{with tcl}
%files -n tcl-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/tcl
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgdtclft.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgv_tcl.so
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot_builtin.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtclplan.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtkspline.so*
%{_libdir}/graphviz/tcl/pkgIndex.tcl
%{_libdir}/tcl%{tclver}/graphviz
%{_mandir}/man3/gv_tcl.3*
%{_mandir}/man3/gdtclft.3tcl*
%{_mandir}/man3/pathplan.3*
%{_mandir}/man3/tcldot.3tcl*
%{_mandir}/man3/tkspline.3tk*
%{_datadir}/graphviz/demo/pathplan_data
%{_datadir}/graphviz/demo/*.README
%{_datadir}/graphviz/demo/*.html
%attr(755,root,root) %{_datadir}/graphviz/demo/doted.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/entities.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/gcat.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/pathplan.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/spline.tcl
%endif

%if %{with r}
%files -n R-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/R
%attr(755,root,root) %{_libdir}/%{name}/R/gv.so
%attr(755,root,root) %{_libdir}/%{name}/R/libgv_R.so
%{_mandir}/man3/gv_r.3*
%endif
