# TODO
# - php-graphwiz and php-graphwiz-devel:
#   php glue should be installed to %{php_extensiondir} without solib name, gv.php dropped, and .h to php-graphviz-devel
#
# Conditional build:
%bcond_without	dotnet	# don't build C# binding
%bcond_without	java	# don't build Java binding
#
%ifarch i386 alpha sparc sparc64
%undefine with_dotnet
%endif
%ifnarch %{ix86} %{x8664}
%undefine with_java
%endif
%ifarch i386 i486
%undefine with_java
%endif
Summary:	Graph Visualization Tools
Summary(pl.UTF-8):   Narzędzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	2.12
Release:	3
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	e5547bc0ec47943c72f5c3e2b5dff58f
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-php.patch
Patch2:		%{name}-gd.patch
Patch3:		%{name}-tk.patch
Patch4:		%{name}-lua.patch
URL:		http://www.graphviz.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	gd-devel >= 2.0.33-5
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	guile-devel >= 1.4
#BuildRequires:	io
%if %{with java}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	ming-devel
%{?with_dotnet:BuildRequires:	mono-csharp}
BuildRequires:	ocaml
BuildRequires:	pango-devel >= 1.10
BuildRequires:	perl-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	php-program >= 4:5.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.322
BuildRequires:	ruby-devel
# swig-csharp,swig-java,swig-lua,swig-ocaml in main swig
# swig-io ???
BuildRequires:	swig
BuildRequires:	swig-guile
BuildRequires:	swig-perl
BuildRequires:	swig-php >= 1.3.30
BuildRequires:	swig-python
BuildRequires:	swig-ruby
BuildRequires:	swig-tcl
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	gd >= 2.0.33-5
Requires:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl.UTF-8
Kolekcja narzędzi oraz pakietów tcl służących do manipulacji i
rozmieszczania grafów.

%package devel
Summary:	Header files for graphviz libraries
Summary(pl.UTF-8):   Pliki nagłówkowe do bibliotek graphviz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gd-devel >= 2.0.33-5
Requires:	libltdl-devel

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do bibliotek graphviz.

%package graphs
Summary:	Demo graphs for graphviz
Summary(pl.UTF-8):   Przykładowe grafy dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description graphs
This package provides some example graphs.

%description graphs -l pl.UTF-8
Ten pakiet zawiera trochę przykładowych grafów.

%package guile
Summary:	Guile binding for graphviz
Summary(pl.UTF-8):   Wiązania Guile dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description guile
Guile binding for graphviz.

%description guile -l pl.UTF-8
Wiązania Guile dla graphviza.

%package java
Summary:	Java binding for graphviz
Summary(pl.UTF-8):   Wiązania Javy dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
Java binding for graphviz.

%description java -l pl.UTF-8
Wiązania Javy dla graphviza.

%package lua
Summary:	LUA binding for graphviz
Summary(pl.UTF-8):   Wiązania LUA dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description lua
LUA binding for graphviz.

%description lua -l pl.UTF-8
Wiązania LUA dla graphviza.

%package ocaml
Summary:	OCaml binding for graphviz
Summary(pl.UTF-8):   Wiązania OCamla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ocaml
OCaml binding for graphviz.

%description ocaml -l pl.UTF-8
Wiązania OCamla dla graphviza.

%package perl
Summary:	Perl binding for graphviz
Summary(pl.UTF-8):   Wiązania Perla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
Perl binding for graphviz.

%description perl -l pl.UTF-8
Wiązania Perla dla graphviza.

%package php
Summary:	PHP binding for graphviz
Summary(pl.UTF-8):   Wiązania PHP dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}

%description php
PHP binding for graphviz.

%description php -l pl.UTF-8
Wiązania PHP dla graphviza.

%package python
Summary:	Python binding for graphviz
Summary(pl.UTF-8):   Wiązania Pythona dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python binding for graphviz.

%description python -l pl.UTF-8
Wiązania Pythona dla graphviza.

%package ruby
Summary:	Ruby binding for graphviz
Summary(pl.UTF-8):   Wiązania Ruby'ego dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ruby
Ruby binding for graphviz.

%description ruby -l pl.UTF-8
Wiązania Ruby'ego dla graphviza.

%package sharp
Summary:	C# binding for graphviz
Summary(pl.UTF-8):   Wiązania C# dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sharp
C# binding for graphviz.

%description sharp -l pl.UTF-8
Wiązania C# dla graphviza.

%package tcl
Summary:	Tcl extension tools for graphviz
Summary(pl.UTF-8):   Rozszerzenia Tcl dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains the various Tcl packages (extensions) using
graphviz.

%description tcl -l pl.UTF-8
Ten pakiet zawiera różne pakiety (rozszerzenia) Tcl używające
graphviza.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# not used for anything
sed -i -e 's/libgnomeui-2.0/libgnomeui-disabled/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{with java}
JAVA_HOME=%{java_home}
export JAVA_HOME
CPPFLAGS="-I$JAVA_HOME/include -I$JAVA_HOME/include/linux"
export CPPFLAGS
%endif

%configure \
	LUA=/usr/bin/lua51 \
	%{!?with_java:--disable-java} \
	%{!?with_dotnet:--disable-sharp} \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_lib}" != "lib"
# tcl doesn't find pkgIndex.tcl outside /usr/lib...
install -d $RPM_BUILD_ROOT%{_prefix}/lib/graphviz
sed -e "s@\$dir @%{_libdir}/graphviz/@" $RPM_BUILD_ROOT%{_libdir}/graphviz/pkgIndex.tcl \
> $RPM_BUILD_ROOT%{_prefix}/lib/graphviz/pkgIndex.tcl
%endif

# replace dead (after compression) softlinks by groff redirections
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{circo,fdp,neato,twopi,dot2gxl}.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/circo.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/fdp.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/neato.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/twopi.1
echo ".so gxl2dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/dot2gxl.1

install -d $RPM_BUILD_ROOT%{_mandir}/man3
for f in $RPM_BUILD_ROOT%{_libdir}/graphviz/*/gv_*.man ; do
	mv $f $RPM_BUILD_ROOT%{_mandir}/man3/`basename $f .man`.3
done

# created by %{_bindir}/dot -c
touch $RPM_BUILD_ROOT%{_libdir}/graphviz/config

rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/*/libgv_*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -c > /dev/null 2>&1

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libagraph.so.*.*.*
%attr(755,root,root) %{_libdir}/libcdt.so.*.*.*
%attr(755,root,root) %{_libdir}/libexpr.so.*.*.*
%attr(755,root,root) %{_libdir}/libgraph.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvc.so.*.*.*
%attr(755,root,root) %{_libdir}/libgvc_builtins.so.*.*.*
%attr(755,root,root) %{_libdir}/libpathplan.so.*.*.*
%dir %{_libdir}/graphviz
%ghost %{_libdir}/graphviz/config
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_core.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_dot_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gd.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gtk.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_pango.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_xlib.so*
# what about the rest of *.la?
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/lefty
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libagraph.so
%attr(755,root,root) %{_libdir}/libcdt.so
%attr(755,root,root) %{_libdir}/libexpr.so
%attr(755,root,root) %{_libdir}/libgraph.so
%attr(755,root,root) %{_libdir}/libgvc.so
%attr(755,root,root) %{_libdir}/libgvc_builtins.so
%attr(755,root,root) %{_libdir}/libpathplan.so
%{_libdir}/libagraph.la
%{_libdir}/libcdt.la
%{_libdir}/libexpr.la
%{_libdir}/libgraph.la
%{_libdir}/libgvc.la
%{_libdir}/libgvc_builtins.la
%{_libdir}/libpathplan.la
%{_pkgconfigdir}/libagraph.pc
%{_pkgconfigdir}/libcdt.pc
%{_pkgconfigdir}/libexpr.pc
%{_pkgconfigdir}/libgraph.pc
%{_pkgconfigdir}/libgvc.pc
%{_pkgconfigdir}/libgvc_builtins.pc
%{_pkgconfigdir}/libpathplan.pc
%{_includedir}/graphviz
%{_mandir}/man3/*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

%if 0
%files io
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/io
%attr(755,root,root) %{_libdir}/graphviz/io/libgv_io.so*
%{_mandir}/man3/gv_io.3*
%endif

%files guile
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/guile
%attr(755,root,root) %{_libdir}/graphviz/guile/libgv_guile.so*
%{_mandir}/man3/gv_guile.3*

%if %{with java}
%files java
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/java
%attr(755,root,root) %{_libdir}/graphviz/java/libgv_java.so*
%{_libdir}/graphviz/java/*.java
%{_mandir}/man3/gv_java.3*
%endif

%files lua
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/lua
%attr(755,root,root) %{_libdir}/graphviz/lua/libgv_lua.so*
%attr(755,root,root) %{_libdir}/graphviz/lua/gv.so
%{_mandir}/man3/gv_lua.3*

%files ocaml
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ocaml
%attr(755,root,root) %{_libdir}/graphviz/ocaml/libgv_ocaml.so*
%{_libdir}/graphviz/ocaml/gv.ml*
%{_mandir}/man3/gv_ocaml.3*

%files perl
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/perl
%attr(755,root,root) %{_libdir}/graphviz/perl/libgv_perl.so*
%attr(755,root,root) %{_libdir}/graphviz/perl/gv.so
%{_libdir}/graphviz/perl/gv.pm
%{_mandir}/man3/gv_perl.3*

%files php
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/php
%attr(755,root,root) %{_libdir}/graphviz/php/libgv_php.so*
%{_libdir}/graphviz/php/gv.php
%{_libdir}/graphviz/php/php_gv.h
%{_mandir}/man3/gv_php.3*

%files python
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/python
%attr(755,root,root) %{_libdir}/graphviz/python/libgv_python.so*
%attr(755,root,root) %{_libdir}/graphviz/python/_gv.so
%{_libdir}/graphviz/python/gv.py
%{_mandir}/man3/gv_python.3*

%files ruby
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ruby
%attr(755,root,root) %{_libdir}/graphviz/ruby/libgv_ruby.so*
%attr(755,root,root) %{_libdir}/graphviz/ruby/gv.so
%{_mandir}/man3/gv_ruby.3*

%if %{with dotnet}
%files sharp
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/sharp
%attr(755,root,root) %{_libdir}/graphviz/sharp/libgv_sharp.so*
%{_libdir}/graphviz/sharp/*.cs
%{_mandir}/man3/gv_sharp.3*
%endif

%files tcl
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/tcl
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgdtclft.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libgv_tcl.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtcldot_builtin.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtclplan.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/libtkspline.so*
%attr(755,root,root) %{_libdir}/graphviz/tcl/gv.so
%if "%{_lib}" != "lib"
%dir %{_prefix}/lib/graphviz
%endif
%{_prefix}/lib/graphviz/pkgIndex.tcl
%{_mandir}/mann/*
%dir %{_datadir}/graphviz/demo
%{_datadir}/graphviz/demo/pathplan_data
%{_datadir}/graphviz/demo/*.*
%attr(755,root,root) %{_datadir}/graphviz/demo/doted
%attr(755,root,root) %{_datadir}/graphviz/demo/entities
%attr(755,root,root) %{_datadir}/graphviz/demo/gcat
%attr(755,root,root) %{_datadir}/graphviz/demo/pathplan
%attr(755,root,root) %{_datadir}/graphviz/demo/spline
