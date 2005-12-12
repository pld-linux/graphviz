#
# Conditional build:
%bcond_with	java	# build Java binding
#
Summary:	Graph Visualization Tools
Summary(pl):	Narzêdzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	2.6
Release:	4
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	0d61fc4f8660be31503d4f9ab6f26bf0
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-php.patch
Patch2:		%{name}-gd.patch
URL:		http://www.graphviz.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	gd-devel >= 2.0.33-5
BuildRequires:	gettext-devel
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	php-program >= 3:5.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	gd >= 2.0.33-5
Requires:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl
Kolekcja narzêdzi oraz pakietów tcl s³u¿±cych do manipulacji i
rozmieszczania grafów.

%package devel
Summary:	Header files for graphviz libraries
Summary(pl):	Pliki nag³ówkowe do bibliotek graphviz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gd-devel >= 2.0.33-5
Requires:	libltdl-devel

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do bibliotek graphviz.

%package graphs
Summary:	Demo graphs for graphviz
Summary(pl):	Przyk³adowe grafy dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description graphs
This package provides some example graphs.

%description graphs -l pl
Ten pakiet zawiera trochê przyk³adowych grafów.

%package java
Summary:	Java binding for graphviz
Summary(pl):	Wi±zania Javy dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
Java binding for graphviz.

%description java -l pl
Wi±zania Javy dla graphviza.

%package perl
Summary:	Perl binding for graphviz
Summary(pl):	Wi±zania Perla dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
Perl binding for graphviz.

%description perl -l pl
Wi±zania Perla dla graphviza.

%package php
Summary:	PHP binding for graphviz
Summary(pl):	Wi±zania PHP dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}

%description php
PHP binding for graphviz.

%description php -l pl
Wi±zania PHP dla graphviza.

%package python
Summary:	Python binding for graphviz
Summary(pl):	Wi±zania Pythona dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Python binding for graphviz.

%description python -l pl
Wi±zania Pythona dla graphviza.

%package ruby
Summary:	Ruby binding for graphviz
Summary(pl):	Wi±zania Ruby'ego dla graphviza
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ruby
Ruby binding for graphviz.

%description ruby -l pl
Wi±zania Ruby'ego dla graphviza.

%package tcl
Summary:	Tcl extension tools for graphviz
Summary(pl):	Rozszerzenia Tcl dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains the various Tcl packages (extensions) using
graphviz.

%description tcl -l pl
Ten pakiet zawiera ró¿ne pakiety (rozszerzenia) Tcl u¿ywaj±ce
graphviza.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_libdir}" != "/usr/lib"
# tcl doesn't find pkgIndex.tcl outside /usr/lib...
install -d $RPM_BUILD_ROOT/usr/lib/graphviz
sed -e "s@\$dir @%{_libdir}/graphviz/@" $RPM_BUILD_ROOT%{_libdir}/graphviz/pkgIndex.tcl \
	> $RPM_BUILD_ROOT/usr/lib/graphviz/pkgIndex.tcl
%endif

# replace dead (after compression) softlinks by groff redirections
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{circo,fdp,neato,twopi}.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/circo.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/fdp.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/neato.1
echo ".so dot.1" >$RPM_BUILD_ROOT%{_mandir}/man1/twopi.1

# created by %{_bindir}/dot -c
touch $RPM_BUILD_ROOT%{_libdir}/graphviz/config

rm -f $RPM_BUILD_ROOT%{_libdir}/graphviz/libgv_{java,perl,php,python,ruby,tcl}.la

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
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/config
# linkable libs
%attr(755,root,root) %{_libdir}/graphviz/libagraph.so.*
%attr(755,root,root) %{_libdir}/graphviz/libcdt.so.*
%attr(755,root,root) %{_libdir}/graphviz/libexpr.so.*
%attr(755,root,root) %{_libdir}/graphviz/libgraph.so.*
%attr(755,root,root) %{_libdir}/graphviz/libgvc.so.*
%attr(755,root,root) %{_libdir}/graphviz/libpack.so.*
%attr(755,root,root) %{_libdir}/graphviz/libpathplan.so.*
# plugins
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_dot_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_neato_layout.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvplugin_usershape_gd.so*
# ??? (some *.so links are needed here for tcl, the rest "just in case")
%attr(755,root,root) %{_libdir}/graphviz/libgdtclft.so*
%attr(755,root,root) %{_libdir}/graphviz/libgvc_builtins.so*
%attr(755,root,root) %{_libdir}/graphviz/libtcldot.so*
%attr(755,root,root) %{_libdir}/graphviz/libtclplan.so*
%attr(755,root,root) %{_libdir}/graphviz/libtkspline.so*
# what about the rest of *.la?
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/lefty
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libagraph.so
%attr(755,root,root) %{_libdir}/graphviz/libcdt.so
%attr(755,root,root) %{_libdir}/graphviz/libexpr.so
%attr(755,root,root) %{_libdir}/graphviz/libgraph.so
%attr(755,root,root) %{_libdir}/graphviz/libgvc.so
%attr(755,root,root) %{_libdir}/graphviz/libpack.so
%attr(755,root,root) %{_libdir}/graphviz/libpathplan.so
%{_libdir}/graphviz/libagraph.la
%{_libdir}/graphviz/libcdt.la
%{_libdir}/graphviz/libexpr.la
%{_libdir}/graphviz/libgraph.la
%{_libdir}/graphviz/libgvc.la
%{_libdir}/graphviz/libpack.la
%{_libdir}/graphviz/libpathplan.la
%{_pkgconfigdir}/*.pc
%{_includedir}/graphviz
%{_mandir}/man3/*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_java.so*
%endif

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_perl.so*

%files php
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_php.so*

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_python.so*

%files ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_ruby.so*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/libgv_tcl.so*
%if "%{_libdir}" != "/usr/lib"
%dir /usr/lib/graphviz
%endif
/usr/lib/graphviz/pkgIndex.tcl
%{_mandir}/mann/*
%dir %{_datadir}/graphviz/demo
%{_datadir}/graphviz/demo/pathplan_data
%{_datadir}/graphviz/demo/*.*
%attr(755,root,root) %{_datadir}/graphviz/demo/doted
%attr(755,root,root) %{_datadir}/graphviz/demo/entities
%attr(755,root,root) %{_datadir}/graphviz/demo/gcat
%attr(755,root,root) %{_datadir}/graphviz/demo/pathplan
%attr(755,root,root) %{_datadir}/graphviz/demo/spline
