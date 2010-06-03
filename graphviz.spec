# TODO
# - %{_libdir}/graphviz/config is not FHS friendly path as config
# - io language bindings: io-graphviz
# - ghostscript subpackage?
#   /usr/lib64/graphviz/libgvplugin_gs.so
#   /usr/lib64/graphviz/libgvplugin_gs.so.6
#   /usr/lib64/graphviz/libgvplugin_gs.so.6.0.0
#
# Conditional build:
%bcond_without	dotnet	# don't build C# bindings
%bcond_without	java	# don't build Java bindings
%bcond_without	ocaml	# don't build ocaml bindings
%bcond_without	php		# don't build php bindings
%bcond_without	perl	# don't build perl bindings
%bcond_without	ruby	# don't build ruby bindings
%bcond_without	tcl		# don't build tcl bindings
%bcond_without	lua		# don't build lua bindings
%bcond_without	r		# don't build R bindings
%bcond_without	python 	# don't build python bindings
%bcond_with		io		# don't build io language bindings
%bcond_without	guile	# don't build guile bindings
%bcond_without	ming	# don't build ming support
%bcond_without	devil	# don't build devil plugin

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
Version:	2.26.3
Release:	1
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	6f45946fa622770c45609778c0a982ee
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-tk.patch
Patch2:		%{name}-bad-header.patch
Patch3:		%{name}-php.patch
Patch5:		%{name}-lua51.patch
Patch6:		%{name}-php_modules_dir.patch
Patch7:		gv.i.patch
Patch8:		swig_php5.patch
URL:		http://www.graphviz.org/
%{?with_devil:BuildRequires:	DevIL-devel}
%{?with_r:BuildRequires:	R}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	gd-devel >= 2.0.34
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
%{?with_guile:BuildRequires:	guile-devel >= 1.4}
#BuildRequires:	io
%if %{with java}
BuildRequires:	jdk
BuildRequires:	jpackage-utils
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
# for lua51 binary
%if %{with lua}
BuildRequires:	lua51
BuildRequires:	lua51-devel >= 5.1
%endif
%{?with_ming:BuildRequires:	ming-devel}
%{?with_dotnet:BuildRequires:	mono-csharp}
%{?with_ocaml:BuildRequires:	ocaml}
BuildRequires:	pango-devel >= 1.10
BuildRequires:	perl-devel
%if %{with php}
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	php-program >= 4:5.0
%endif
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
%{?with_perl:BuildRequires:	rpm-perlprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 1.519
%{?with_ruby:BuildRequires:	ruby-devel}
# swig-csharp,swig-java,swig-lua,swig-ocaml in main swig
# swig-io ???
BuildRequires:	swig
%{?with_guile:BuildRequires:	swig-guile}
%{?with_perl:BuildRequires:	swig-perl}
%{?with_php:BuildRequires:	swig-php >= 1.3.40}
BuildRequires:	swig-python
%{?with_ruby:BuildRequires:	swig-ruby}
%if %{with tcl}
BuildRequires:	swig-tcl
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	fonts-Type1-urw
Requires:	gd >= 2.0.33-5
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
Requires:	libltdl-devel

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do bibliotek graphviz.

%package doc-html
Summary:	HTML documentation for graphviz
Group:		Documentation

%description doc-html
HTML documentation for graphviz.

%package doc-pdf
Summary:	PDF documentation for graphviz
Group:		Documentation

%description doc-pdf
PDF documentation for graphviz.

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

%package -n sharp-%{name}
Summary:	C# binding for graphviz
Summary(pl.UTF-8):	Wiązania C# dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	graphviz-sharp

%description -n sharp-%{name}
C# binding for graphviz.

%description -n sharp-%{name} -l pl.UTF-8
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
%patch5 -p1
%patch6 -p1
#%patch7 -p1
#%patch8 -p1

# not used for anything
sed -i -e 's/libgnomeui-2.0/libgnomeui-disabled/' configure.ac

%{__sed} '1s@/usr/bin/lua$@/usr/bin/lua51@' -i tclpkg/gv/demo/modgraph.lua

%build
rm -f m4/*.m4
touch config/config.rpath
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

CPPFLAGS="%{rpmcppflags}"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/ruby-1.9 -I%{_includedir}/ruby-1.9/%{_target}"

%if %{with java}
JAVA_HOME=%{java_home}
export JAVA_HOME
CPPFLAGS="$CPPFLAGS -I$JAVA_HOME/include -I$JAVA_HOME/include/linux"
%endif

export CPPFLAGS

%configure \
	lua_suffix=51 \
	--disable-ltdl-install \
	%{!?with_java:--disable-java} \
	%{!?with_ocaml:--disable-ocaml} \
	%{!?with_dotnet:--disable-sharp} \
	%{!?with_perl:--disable-perl} \
	%{!?with_php:--disable-php} \
	%{!?with_ruby:--disable-ruby} \
	%{!?with_tcl:--disable-tcl} \
	%{!?with_ming:--disable-ming} \
	%{!?with_devil:--disable-devil} \
	%{!?with_lua:--disable-lua} \
	%{!?with_r:--disable-r} \
	--disable-static

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

rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/*/lib*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/libgvplugin_*.la

#patch -p1 < %{PATCH2} || exit 1

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
#%doc AUTHORS COPYING ChangeLog NEWS doc/*.pdf
%attr(755,root,root) %{_bindir}/*
#%attr(755,root,root) %{_libdir}/libagraph.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libagraph.so.4
%attr(755,root,root) %{_libdir}/libcdt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdt.so.4
%attr(755,root,root) %{_libdir}/libcgraph.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcgraph.so.5
%attr(755,root,root) %{_libdir}/libgraph.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraph.so.4
%attr(755,root,root) %{_libdir}/libgvc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvc.so.5
%attr(755,root,root) %{_libdir}/libgvpr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvpr.so.1
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
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_gtk.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_pango.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_rsvg.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_xlib.so*
# what about the rest of *.la?
%dir %{_datadir}/graphviz
%dir %{_datadir}/graphviz/demo
%{_datadir}/graphviz/lefty
%{_mandir}/man1/*
%{_mandir}/man7/graphviz.7*

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libagraph.so
%attr(755,root,root) %{_libdir}/libcdt.so
%attr(755,root,root) %{_libdir}/libcgraph.so
%attr(755,root,root) %{_libdir}/libgraph.so
%attr(755,root,root) %{_libdir}/libgvc.so
%attr(755,root,root) %{_libdir}/libgvpr.so
%attr(755,root,root) %{_libdir}/libpathplan.so
%attr(755,root,root) %{_libdir}/libxdot.so
#%{_libdir}/libagraph.la
%{_libdir}/libcdt.la
%{_libdir}/libcgraph.la
%{_libdir}/libgraph.la
%{_libdir}/libgvc.la
%{_libdir}/libgvpr.la
%{_libdir}/libpathplan.la
%{_libdir}/libxdot.la
#%{_pkgconfigdir}/libagraph.pc
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
%{_mandir}/man3/graph.3*
%{_mandir}/man3/gvc.3*
%{_mandir}/man3/xdot.3*

%files doc-html
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/doc/html/*

%files doc-pdf
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/doc/pdf/*

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
%{_mandir}/man3/gv_guile.*
%endif

%if %{with java}
%files -n java-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/java
%attr(755,root,root) %{_libdir}/graphviz/java/libgv_java.so
%{_libdir}/graphviz/java/*.java
%{_mandir}/man3/gv_java.*
%endif

%if %{with lua}
%files -n lua-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/lua
%attr(755,root,root) %{_libdir}/graphviz/lua/libgv_lua.so
%attr(755,root,root) %{_libdir}/graphviz/lua/gv.so
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.lua
%attr(755,root,root) %{_libdir}/lua/gv.so
%{_mandir}/man3/gv_lua.*
%endif

%if %{with ocaml}
%files -n ocaml-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ocaml
%attr(755,root,root) %{_libdir}/graphviz/ocaml/libgv_ocaml.so
%{_libdir}/graphviz/ocaml/META.gv
%{_libdir}/graphviz/ocaml/gv.a
%{_libdir}/graphviz/ocaml/gv.cm*
%{_libdir}/graphviz/ocaml/gv.ml*
%{_mandir}/man3/gv_ocaml.*
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
%{_mandir}/man3/gv_perl.*
%endif

%if %{with php}
%files -n php-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{php_extensiondir}/gv.so
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{name}.ini
%{php_data_dir}/gv.php
%{_mandir}/man3/gv_php.*
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
%{_mandir}/man3/gv_python.*
%endif

%if %{with ruby}
%files -n ruby-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/ruby
%attr(755,root,root) %{_libdir}/graphviz/ruby/libgv_ruby.so
%attr(755,root,root) %{_libdir}/graphviz/ruby/gv.so
%attr(755,root,root) %{_datadir}/graphviz/demo/modgraph.rb
%{ruby_sitearchdir}/gv.so
%{_mandir}/man3/gv_ruby.*
%endif

%if %{with dotnet}
%files -n sharp-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/graphviz/sharp
%attr(755,root,root) %{_libdir}/graphviz/sharp/libgv_sharp.so
%{_libdir}/graphviz/sharp/*.cs
%{_mandir}/man3/gv_sharp.*
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
%{_libdir}/tcl*/*
%{_mandir}/man3/gv_tcl.*
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
%{_mandir}/man3/gv_r.*
%endif
