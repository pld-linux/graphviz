# TODO
# - %{_libdir}/graphviz/config is not FHS friendly path as config
# - io language binding (waiting for swig support)
# - some plugin subpackages? (libgvplugin_*: gs=ghostscript, gtk, lasi, poppler, visio, webp)
#
# Conditional build:
# - language bindings
%bcond_without	dotnet		# C# bindings
%bcond_without	golang		# Go bindings
%bcond_without	guile		# guile bindings
%bcond_without	java		# Java bindings
%bcond_without	ocaml		# OCaml bindings
%bcond_with	php		# PHP bindings
%bcond_without	perl		# Perl bindings
%bcond_without	ruby		# Ruby bindings
%bcond_without	tcl		# Tcl bindings
%bcond_without	lua		# Lua bindings
%bcond_without	r		# R bindings
%bcond_without	python		# Python bindings
%bcond_without	python2		# Python 2 bindings
%bcond_without	python3		# Python 3 bindings
%bcond_with	io		# io language bindings (needs swig support)
# - plugins, features
%bcond_without	gd		# gd plugin and gd support in tcl package
%bcond_without	ming		# ming support
%bcond_without	devil		# DevIL plugin
%bcond_without	qt		# Qt features (gvedit utility)
%bcond_without	smyrna		# SMYRNA utility (large graph viewer)
%bcond_without	ipsepcola	# IPSEPCOLA features in neato engine [C++ portability problems]

%define		tclver	8.6

%if 0%{!?php_name:1}
%define		php_name	php73
%endif

%ifarch i386 x32
%undefine with_dotnet
%endif
%ifnarch %{ix86} %{x8664}
%undefine with_java
%endif
%ifarch i386 i486
%undefine with_java
%endif
%ifnarch %go_arches
%undefine with_golang
%endif
%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif

%{?with_java:%{?use_default_jdk}}

Summary:	Graph Visualization Tools
Summary(pl.UTF-8):	Narzędzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	2.47.2
Release:	6
License:	EPL v1.0
Group:		X11/Applications/Graphics
#Source0Download: https://graphviz.org/download/source/
Source0:	https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4b60526ed7a6a43dfb23b5c175286cd8
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-bad-header.patch
Patch3:		%{name}-php.patch
Patch4:		%{name}-ltdl.patch
Patch7:		%{name}-ruby.patch
Patch10:	%{name}-ming.patch
Patch12:	%{name}-webp.patch
Patch14:	python-paths.patch
Patch15:	ghostscript918.patch
Patch16:	java.patch
Patch17:	cppflags.patch
URL:		http://www.graphviz.org/
%{?with_devil:BuildRequires:	DevIL-devel}
%{?with_r:BuildRequires:	R}
BuildRequires:	ann-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bison >= 3.0
BuildRequires:	cairo-devel >= 1.0.0
# for tests
#BuildRequires:	criterion-devel
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex >= 2.5.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	gcc >= 5:3.2
%{?with_gd:BuildRequires:	gd-devel >= 2.0.34}
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	ghostscript-devel
%{?with_golang:BuildRequires:	golang}
BuildRequires:	gtk+2-devel >= 2:2.8.0
# only tested, actually not used
#BuildRequires:	gtkglarea-devel >= 2.0
BuildRequires:	gts-devel
%{?with_guile:BuildRequires:	guile-devel >= 2.0}
#BuildRequires:	io
%if %{with java}
%buildrequires_jdk
BuildRequires:	jpackage-utils
%endif
BuildRequires:	libLASi-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel >= 2:2.2
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.36.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwebp-devel
# currently external library is not used
#BuildRequires:	libvisio-devel
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
BuildRequires:	%{php_name}-devel
BuildRequires:	%{php_name}-program
BuildRequires:	rpm-build >= 4.6
BuildRequires:	swig-php >= 3.0.11
%endif
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
%{?with_python:BuildRequires:	python-devel >= 1:2.3}
%{?with_python2:BuildRequires:	python-devel >= 1:2.3}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.6}
%{?with_perl:BuildRequires:	rpm-perlprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 2.021
%{?with_ruby:BuildRequires:	ruby-devel >= 1.9}
BuildRequires:	sed >= 4.0
# swig-csharp,swig-go,swig-java,swig-lua,swig-ocaml in main swig
# swig-io ???
BuildRequires:	swig >= 1.3
%{?with_guile:BuildRequires:	swig-guile >= 2.0.3}
%{?with_perl:BuildRequires:	swig-perl >= 1.3}
%{?with_python:BuildRequires:	swig-python >= 1.3}
%{?with_ruby:BuildRequires:	swig-ruby >= 1.3}
BuildRequires:	tar >= 1:1.22
%if %{with tcl}
BuildRequires:	swig-tcl >= 1.3
BuildRequires:	tcl-devel >= %{tcl_ver}
BuildRequires:	tk-devel >= 8.6.0
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
# tested in configure to enable ghostscript plugin build, actually not used
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
%if %{with smyrna}
BuildRequires:	OpenGL-glut-devel
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	libglade2-devel >= 2.0
%endif
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
Requires(post,postun):	/sbin/ldconfig
# gd plugin is required by dot command (if graphviz is built with gd support)
%{?with_gd:Requires:	%{name}-gd = %{version}-%{release}}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo >= 1.0.0
Requires:	fonts-Type1-urw
Requires:	gtk+2 >= 2:2.8.0
Requires:	libltdl >= 2:2.2
Requires:	librsvg >= 2.36.0
Requires:	pango >= 1:1.14.9
%{!?with_golang:Obsoletes:	golang-graphviz < %{version}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl.UTF-8
Kolekcja narzędzi oraz pakietów tcl służących do manipulacji i
rozmieszczania grafów.

%package libs
Summary:	Graphviz shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone graphviza
Group:		Libraries
Conflicts:	graphviz < 2.40.1-1

%description libs
Graphviz shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone graphviza.

%package devil
Summary:	Graphviz plugin for renderers based on DevIL
Summary(pl.UTF-8):	Wtyczka Graphviza do renderowania w oparciu o bibliotekę DevIL
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}

%description devil
Graphviz plugin for renderers based on DevIL. (Unless you absolutely
have to use BMP, TIF, or TGA, you are recommended to use the PNG
format instead supported directly by the cairo+pango based renderer in
the base graphviz rpm.)

%description devil -l pl.UTF-8
Wtyczka Graphviza do renderowania w oparciu o bibliotekę DevIL (jeśli
nie ma absolutnej konieczności używania formatu BMP, TIF lub TGA,
zalecane jest używanie format PNG bezpośrednio z renderera cairo+pango
obecnego w podstawowym pakiecie graphviz.

%package gd
Summary:	Graphviz plugin for renderers based on GD
Summary(pl.UTF-8):	Wtyczka Graphviza do renderowania w oparciu o bibliotekę GD
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gd >= 2.0.33-5

%description gd
Graphviz plugin for renderers based on gd. (Unless you absolutely have
to use GIF, you are recommended to use the PNG format instead because
of the better quality anti-aliased lines provided by the cairo+pango
based renderer.)

%description gd -l pl.UTF-8
Wtyczka Graphviza do renderowania w oparciu o bibliotekę DevIL (jeśli
nie ma absolutnej konieczności używania formatu GIF, zalecane jest
używanie format PNG bezpośrednio z renderera cairo+pango obecnego w
podstawowym pakiecie graphviz.

%package ming
Summary:	Graphviz plugin for flash renderer based on ming
Summary(pl.UTF-8):	Wtyczka Graphviza do renderowania w oparciu o bibliotekę ming
Group:		Applications/Multimedia
Requires:	%{name}-libs = %{version}-%{release}

%description ming
Graphviz plugin for -Tswf (flash) renderer based on ming.

%description ming -l pl.UTF-8
Wtyczka Graphviza do renderowania z opcją -Tswf (flash) w oparciu o
bibliotekę ming.

%package devel
Summary:	Header files for graphviz libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do bibliotek graphviz
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libltdl-devel >= 2:2

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do bibliotek graphviz.

%package gvedit
Summary:	gvedit - simple graph editor and viewer based on Qt
Summary(pl.UTF-8):	gvedit - prosty edytor i przeglądarka grafów oparta na Qt
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description gvedit
gvedit provides a simple Qt-based graph editor and viewer.

%description gvedit -l l.UTF-8
gvedit to prosty edytor i przeglądarka grafów oparta na Qt.

%package smyrna
Summary:	SMYRNA large graph viewer
Summary(pl.UTF-8):	SMYRNA - przeglądarka dużych grafów
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	gtkglext >= 1.0

%description smyrna
SMYRNA is an interactive viewer for graphs in the DOT format. It is
especially designed to handle large graphs, and allows flat and
topological fisheye views.

%description smyrna -l pl.UTF-8
SMYRNA to interaktywna przeglądarka grafów w formacie DOT. Jest
przeznaczona szczególnie do obsługi dużych grafów, udostępnia widok
płaski oraz topologiczny typu "rybie oko".

%package doc-html
Summary:	HTML documentation for graphviz
Summary(pl.UTF-8):	Dokumentacja do graphviza w formacie HTML
Group:		Documentation
BuildArch:	noarch

%description doc-html
HTML documentation for graphviz.

%description doc-html -l pl.UTF-8
Dokumentacja do graphviza w formacie HTML.

%package doc-pdf
Summary:	PDF documentation for graphviz
Summary(pl.UTF-8):	Dokumentacja do graphviza w formacie PDF
Group:		Documentation
BuildArch:	noarch

%description doc-pdf
PDF documentation for graphviz.

%description doc-pdf -l pl.UTF-8
Dokumentacja do graphviza w formacie PDF.

%package graphs
Summary:	Demo graphs for graphviz
Summary(pl.UTF-8):	Przykładowe grafy dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description graphs
This package provides some example graphs.

%description graphs -l pl.UTF-8
Ten pakiet zawiera trochę przykładowych grafów.

%package -n golang-%{name}
Summary:	Go binding for graphviz
Summary(pl.UTF-8):	Wiązania języka Go dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	golang

%description -n golang-%{name}
Go binding for graphviz.

%description -n golang-%{name} -l pl.UTF-8
Wiązania języka Go dla graphviza.

%package -n io-%{name}
Summary:	Io binding for graphviz
Summary(pl.UTF-8):	Wiązania języka Io dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	io

%description -n io-%{name}
Io binding for graphviz.

%description -n io-%{name} -l pl.UTF-8
Wiązania języka Io dla graphviza.

%package -n guile-%{name}
Summary:	Guile binding for graphviz
Summary(pl.UTF-8):	Wiązania Guile dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-guile < 2.26.3-1

%description -n guile-%{name}
Guile binding for graphviz.

%description -n guile-%{name} -l pl.UTF-8
Wiązania Guile dla graphviza.

%package -n java-%{name}
Summary:	Java binding for graphviz
Summary(pl.UTF-8):	Wiązania Javy dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-java < 2.26.3-1

%description -n java-%{name}
Java binding for graphviz.

%description -n java-%{name} -l pl.UTF-8
Wiązania Javy dla graphviza.

%package -n lua-%{name}
Summary:	LUA binding for graphviz
Summary(pl.UTF-8):	Wiązania LUA dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-lua < 2.26.3-1

%description -n lua-%{name}
LUA binding for graphviz.

%description -n lua-%{name} -l pl.UTF-8
Wiązania LUA dla graphviza.

%package -n ocaml-%{name}
Summary:	OCaml binding for graphviz
Summary(pl.UTF-8):	Wiązania OCamla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-ocaml < 2.26.3-1

%description -n ocaml-%{name}
OCaml binding for graphviz.

%description -n ocaml-%{name} -l pl.UTF-8
Wiązania OCamla dla graphviza.

%package -n perl-%{name}
Summary:	Perl binding for graphviz
Summary(pl.UTF-8):	Wiązania Perla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ocmal-perl < 2.26.3-1

%description -n perl-%{name}
Perl binding for graphviz.

%description -n perl-%{name} -l pl.UTF-8
Wiązania Perla dla graphviza.

%package -n %{php_name}-%{name}
Summary:	PHP binding for graphviz
Summary(pl.UTF-8):	Wiązania PHP dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-php < 2.26.3-1
%{?requires_php_extension}

%description -n %{php_name}-%{name}
PHP binding for graphviz.

%description -n %{php_name}-%{name} -l pl.UTF-8
Wiązania PHP dla graphviza.

%package -n python-libgraphviz
Summary:	Python 2 binding for graphviz
Summary(pl.UTF-8):	Wiązania Pythona 2 dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-python < 2.26.3-1
Obsoletes:	python-graphviz < 2.44.1-10

%description -n python-libgraphviz
Python 2 binding for graphviz.

%description -n python-libgraphviz -l pl.UTF-8
Wiązania Pythona 2 dla graphviza.

%package -n python3-libgraphviz
Summary:	Python 3 binding for graphviz
Summary(pl.UTF-8):	Wiązania Pythona 3 dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python3-graphviz < 2.44.1-10

%description -n python3-libgraphviz
Python 3 binding for graphviz.

%description -n python3-libgraphviz -l pl.UTF-8
Wiązania Pythona 3 dla graphviza.

%package -n ruby-%{name}
Summary:	Ruby binding for graphviz
Summary(pl.UTF-8):	Wiązania Ruby'ego dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-ruby < 2.26.3-1

%description -n ruby-%{name}
Ruby binding for graphviz.

%description -n ruby-%{name} -l pl.UTF-8
Wiązania Ruby'ego dla graphviza.

%package -n dotnet-%{name}-sharp
Summary:	C# binding for graphviz
Summary(pl.UTF-8):	Wiązania C# dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-sharp < 2.26.3-1
Obsoletes:	sharp-graphviz < 2.26.3-6

%description -n dotnet-%{name}-sharp
C# binding for graphviz.

%description -n dotnet-%{name}-sharp -l pl.UTF-8
Wiązania C# dla graphviza.

%package -n tcl-%{name}
Summary:	Tcl extension tools for graphviz
Summary(pl.UTF-8):	Rozszerzenia Tcl dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-tcl < 2.26.3-1

%description -n tcl-%{name}
This package contains the various Tcl packages (extensions) using
graphviz.

%description -n tcl-%{name} -l pl.UTF-8
Ten pakiet zawiera różne pakiety (rozszerzenia) Tcl używające
graphviza.

%package -n R-%{name}
Summary:	graphviz bindings for R language
Summary(pl.UTF-8):	Wiązania graphviza dla języka R
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description -n R-%{name}
graphviz bindings for R language.

%description -n R-%{name} -l pl.UTF-8
Wiązania graphviza dla języka R.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch7 -p1
%patch10 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%{__sed} '1s@/usr/bin/lua$@/usr/bin/lua5.1@' -i tclpkg/gv/demo/modgraph.lua

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python}\1,' \
	tclpkg/gv/demo/modgraph.py

%build
touch config/config.rpath
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

CPPFLAGS="%{rpmcppflags}"
%if %{with java}
CPPFLAGS="$CPPFLAGS -I%{java_home}/include -I%{java_home}/include/linux"
%endif
export CPPFLAGS

%configure \
%ifarch %{x8664} aarch64 ppc64 sparc64 s390x
	LIBPOSTFIX="64" \
%endif
%ifarch x32
	LIBPOSTFIX="x32" \
%endif
%if %{with java}
	JAVA="%{java_home}/bin/java" \
	JAVAC="%{java_home}/bin/javac" \
%endif
	LUA=/usr/bin/lua5.1 \
	PHP=%{__php} \
	%{?with_ruby:RUBY_VER=%{ruby_abi}} \
	ac_cv_lib_criterion_main=no \
	lua_suffix=51 \
	%{!?with_golang:--disable-go} \
	%{!?with_guile:--disable-guile} \
	%{?with_io:--enable-io} \
	%{!?with_java:--disable-java} \
	--disable-ltdl-install \
	%{!?with_lua:--disable-lua} \
	%{!?with_ocaml:--disable-ocaml} \
	%{!?with_perl:--disable-perl} \
	%{!?with_php:--disable-php} \
	%{!?with_python:--disable-python} \
	%{!?with_python2:--disable-python2} \
	%{!?with_python3:--disable-python3} \
	%{!?with_r:--disable-r} \
	%{!?with_ruby:--disable-ruby} \
	%{!?with_dotnet:--disable-sharp} \
	%{!?with_tcl:--disable-tcl} \
	--disable-silent-rules \
	--disable-static \
	%{!?with_devil:--without-devil} \
	%{!?with_ipsepcola:--without-ipsepcola} \
	%{!?with_gd:--without-libgd} \
	%{?with_ming:--with-ming} \
	%{!?with_qt:--without-qt} \
	%{!?with_smyrna:--without-smyrna} \
	--with-visio \
	--with-webp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with php}
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{name}.ini
; Enable gv.so extension module
extension=gv.so
EOF

# drop the symlinks and install to php dirs directly
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{php_name}-%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT{%{_libdir}/%{name}/php,%{php_data_dir}}/gv.php
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/php/libgv_php.so
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/php/gv.so
%{__mv} $RPM_BUILD_ROOT{%{_datadir}/%{name}/demo,%{_examplesdir}/%{php_name}-%{name}-%{version}}/modgraph.php
%endif

# "man3/gv.3r.gz" and "man3/gv.3ruby.gz" are both manual for "gv" in "section 3" of man pages
# make manual pages unique.
for a in $RPM_BUILD_ROOT%{_mandir}/man3/gv.*; do
	m=${a##*/}
	l=${m#gv.3}
	%{__mv} $a ${a%/*}/gv_$l.3
done

# created by %{_bindir}/dot -c
touch $RPM_BUILD_ROOT%{_libdir}/graphviz/config

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/graphviz/libgvplugin_*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/graphviz/*/lib*.la
%if %{with java}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/graphviz/java/org/graphviz/lib*.la
%endif

rm -rf doc-html doc-pdf
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/html doc-html
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/pdf doc-pdf
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
%{?with_smyrna:%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/examples}

cd $RPM_BUILD_ROOT
patch -p1 --no-backup-if-mismatch < %{PATCH2} || exit 1

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -c > /dev/null 2>&1

%postun	-p /sbin/ldconfig

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post -n %{php_name}-%{name}
%php_webserver_restart

%postun -n %{php_name}-%{name}
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md COPYING README
%attr(755,root,root) %{_bindir}/acyclic
%attr(755,root,root) %{_bindir}/bcomps
%attr(755,root,root) %{_bindir}/ccomps
%attr(755,root,root) %{_bindir}/circo
%attr(755,root,root) %{_bindir}/cluster
%attr(755,root,root) %{_bindir}/dijkstra
%attr(755,root,root) %{_bindir}/dot
%attr(755,root,root) %{_bindir}/dot2gxl
%attr(755,root,root) %{_bindir}/dot_builtins
%attr(755,root,root) %{_bindir}/dotty
%attr(755,root,root) %{_bindir}/edgepaint
%attr(755,root,root) %{_bindir}/fdp
%attr(755,root,root) %{_bindir}/gc
%attr(755,root,root) %{_bindir}/gml2gv
%attr(755,root,root) %{_bindir}/graphml2gv
%attr(755,root,root) %{_bindir}/gv2gml
%attr(755,root,root) %{_bindir}/gv2gxl
%attr(755,root,root) %{_bindir}/gvcolor
%attr(755,root,root) %{_bindir}/gvgen
%attr(755,root,root) %{_bindir}/gvmap
%attr(755,root,root) %{_bindir}/gvmap.sh
%attr(755,root,root) %{_bindir}/gvpack
%attr(755,root,root) %{_bindir}/gvpr
%attr(755,root,root) %{_bindir}/gxl2dot
%attr(755,root,root) %{_bindir}/gxl2gv
%attr(755,root,root) %{_bindir}/lefty
%attr(755,root,root) %{_bindir}/lneato
%attr(755,root,root) %{_bindir}/mingle
%attr(755,root,root) %{_bindir}/mm2gv
%attr(755,root,root) %{_bindir}/neato
%attr(755,root,root) %{_bindir}/nop
%attr(755,root,root) %{_bindir}/osage
%attr(755,root,root) %{_bindir}/patchwork
%attr(755,root,root) %{_bindir}/prune
%attr(755,root,root) %{_bindir}/sccmap
%attr(755,root,root) %{_bindir}/sfdp
%attr(755,root,root) %{_bindir}/tred
%attr(755,root,root) %{_bindir}/twopi
%attr(755,root,root) %{_bindir}/unflatten
%attr(755,root,root) %{_bindir}/vimdot
%ghost %{_libdir}/graphviz/config
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_core.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_dot_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gdk.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gs.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gtk.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_lasi.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_pango.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_poppler.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_rsvg.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_visio.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_webp.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_xlib.so*
%dir %{_datadir}/graphviz
%dir %{_datadir}/graphviz/demo
%{_datadir}/graphviz/gvpr
%{_datadir}/graphviz/lefty
%{_mandir}/man1/acyclic.1*
%{_mandir}/man1/bcomps.1*
%{_mandir}/man1/ccomps.1*
%{_mandir}/man1/circo.1*
%{_mandir}/man1/cluster.1*
%{_mandir}/man1/dijkstra.1*
%{_mandir}/man1/dot.1*
%{_mandir}/man1/dot2gxl.1*
%{_mandir}/man1/dotty.1*
%{_mandir}/man1/edgepaint.1*
%{_mandir}/man1/fdp.1*
%{_mandir}/man1/gc.1*
%{_mandir}/man1/gml2gv.1*
%{_mandir}/man1/graphml2gv.1*
%{_mandir}/man1/gv2gml.1*
%{_mandir}/man1/gv2gxl.1*
%{_mandir}/man1/gvcolor.1*
%{_mandir}/man1/gvgen.1*
%{_mandir}/man1/gvmap.1*
%{_mandir}/man1/gvmap.sh.1*
%{_mandir}/man1/gvpack.1*
%{_mandir}/man1/gvpr.1*
%{_mandir}/man1/gxl2dot.1*
%{_mandir}/man1/gxl2gv.1*
%{_mandir}/man1/lefty.1*
%{_mandir}/man1/lneato.1*
%{_mandir}/man1/mingle.1*
%{_mandir}/man1/mm2gv.1*
%{_mandir}/man1/neato.1*
%{_mandir}/man1/nop.1*
%{_mandir}/man1/osage.1*
%{_mandir}/man1/patchwork.1*
%{_mandir}/man1/prune.1*
%{_mandir}/man1/sccmap.1*
%{_mandir}/man1/sfdp.1*
%{_mandir}/man1/tred.1*
%{_mandir}/man1/twopi.1*
%{_mandir}/man1/unflatten.1*
%{_mandir}/man1/vimdot.1*
%{_mandir}/man7/graphviz.7*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdt.so.5
%attr(755,root,root) %{_libdir}/libcgraph.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgraph.so.6
%attr(755,root,root) %{_libdir}/libgvc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvc.so.6
%attr(755,root,root) %{_libdir}/libgvpr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvpr.so.2
%attr(755,root,root) %{_libdir}/liblab_gamut.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblab_gamut.so.1
%attr(755,root,root) %{_libdir}/libpathplan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpathplan.so.4
%attr(755,root,root) %{_libdir}/libxdot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxdot.so.4
%dir %{_libdir}/graphviz

%if %{with devil}
%files devil
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_devil.so*
%endif

%if %{with gd}
%files gd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/diffimg
%{_mandir}/man1/diffimg.1*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gd.so*
%endif

%if %{with ming}
%files ming
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_ming.so*
%{_datadir}/graphviz/font
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdt.so
%attr(755,root,root) %{_libdir}/libcgraph.so
%attr(755,root,root) %{_libdir}/libgvc.so
%attr(755,root,root) %{_libdir}/libgvpr.so
%attr(755,root,root) %{_libdir}/liblab_gamut.so
%attr(755,root,root) %{_libdir}/libpathplan.so
%attr(755,root,root) %{_libdir}/libxdot.so
%{_pkgconfigdir}/libcdt.pc
%{_pkgconfigdir}/libcgraph.pc
%{_pkgconfigdir}/libgvc.pc
%{_pkgconfigdir}/libgvpr.pc
%{_pkgconfigdir}/liblab_gamut.pc
%{_pkgconfigdir}/libpathplan.pc
%{_pkgconfigdir}/libxdot.pc
%{_includedir}/graphviz
%{_mandir}/man3/cdt.3*
%{_mandir}/man3/cgraph.3*
%{_mandir}/man3/expr.3*
%{_mandir}/man3/gvc.3*
%{_mandir}/man3/gvpr.3*
%{_mandir}/man3/pack.3*
%{_mandir}/man3/xdot.3*

%if %{with qt}
%files gvedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvedit
%{_datadir}/graphviz/gvedit
%{_mandir}/man1/gvedit.1*
%endif

%if %{with smyrna}
%files smyrna
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smyrna
%{_datadir}/graphviz/smyrna
%{_mandir}/man1/smyrna.1*
%endif

%files doc-html
%defattr(644,root,root,755)
%doc doc-html/*

%files doc-pdf
%defattr(644,root,root,755)
%doc doc-pdf/*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

%if %{with golang}
%files -n golang-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/go
%attr(755,root,root) %{_libdir}/graphviz/go/libgv_go.so
%{_libdir}/graphviz/go/gv.go
%{_libdir}/graphviz/go/runtime.h
%{_mandir}/man3/gv_go.3*
%endif

%if %{with guile}
%files -n guile-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/guile
%attr(755,root,root) %{_libdir}/graphviz/guile/libgv_guile.so
%{_mandir}/man3/gv_guile.3*
%endif

%if %{with io}
%files -n io-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/io
%attr(755,root,root) %{_libdir}/graphviz/io/libgv_io.so*
%{_mandir}/mann/gv_io.n*
%endif

%if %{with java}
%files -n java-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/java
%attr(755,root,root) %{_libdir}/graphviz/java/libgv.so
%dir %{_libdir}/graphviz/java/org
%dir %{_libdir}/graphviz/java/org/graphviz
%attr(755,root,root) %{_libdir}/graphviz/java/org/graphviz/libgv_java.so
%{_libdir}/graphviz/java/org/graphviz/*.class
%{_libdir}/graphviz/java/org/graphviz/*.java
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
%files -n %{php_name}-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/gv.so
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{name}.ini
%{php_data_dir}/gv.php
%{_mandir}/man3/gv_php.3*
%{_examplesdir}/%{php_name}-%{name}-%{version}
%endif

%if %{with python}
%files -n python-libgraphviz
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/python
%attr(755,root,root) %{_libdir}/graphviz/python/libgv_python.so
%attr(755,root,root) %{_libdir}/graphviz/python/_gv.so
%{_libdir}/graphviz/python/gv.py
%if %{with python2}
%dir %{_libdir}/graphviz/python2
%attr(755,root,root) %{_libdir}/graphviz/python2/libgv_python2.so
%attr(755,root,root) %{_libdir}/graphviz/python2/_gv.so
%{_libdir}/graphviz/python2/gv.py
%endif
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.py
%attr(755,root,root) %{py_sitedir}/_gv.so
%{py_sitedir}/gv.py
%{_mandir}/man3/gv_python.3*
%endif

%if %{with python3}
%files -n python3-libgraphviz
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/python3
%attr(755,root,root) %{_libdir}/graphviz/python3/libgv_python3.so
%attr(755,root,root) %{_libdir}/graphviz/python3/_gv.so
%{_libdir}/graphviz/python3/gv.py
%attr(755,root,root) %{py3_sitedir}/_gv.so
%{py3_sitedir}/gv.py
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
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgv_tcl.so
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot_builtin.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtclplan.so*
%{_libdir}/graphviz/tcl/pkgIndex.tcl
%{_libdir}/tcl%{tclver}/graphviz
%{_mandir}/man3/gv_tcl.3*
%{_mandir}/man3/pathplan.3*
%{_mandir}/man3/tcldot.3tcl*
%{_datadir}/graphviz/demo/pathplan_data
%{_datadir}/graphviz/demo/*.README
%{_datadir}/graphviz/demo/*.html
%attr(755,root,root) %{_datadir}/graphviz/demo/doted.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/entities.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/gcat.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.tcl
%attr(755,root,root) %{_datadir}/graphviz/demo/pathplan.tcl
%if %{with gd}
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgdtclft.so*
%{_mandir}/man3/gdtclft.3tcl*
%endif
%endif

%if %{with r}
%files -n R-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/R
%attr(755,root,root) %{_libdir}/%{name}/R/gv.so
%attr(755,root,root) %{_libdir}/%{name}/R/libgv_R.so
%{_mandir}/man3/gv_r.3*
%endif
