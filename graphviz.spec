# TODO:
# - linking (duplicate code, somewhere linked dynamically, somewhere statically)
#
# Conditional build:
%bcond_without	dynagraph	# without dynagraph program (they say it requires gcc 3.1)
#
Summary:	Graph Visualization Tools
Summary(pl):	Narzêdzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	2.2.1
Release:	2
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	bb46d8ada39436cb672922f0c8b1339c
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-cairo.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.graphviz.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
%{?with_dynagraph:BuildRequires:	gcc-c++ >= 5:3.1}
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libsvg-cairo-devel >= 0.1.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	tk-devel >= 8.3.0
BuildRequires:	zlib-devel
Requires:	gd >= 2.0.33
Requires:	libsvg-cairo >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl
Kolekcja narzêdzi oraz pakietów tcl s³u¿±cych do manipulacji i
rozmieszczania grafów.

%package graphs
Summary:	Demo graphs for graphviz
Summary(pl):	Przyk³adowe grafy dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description graphs
This package provides some example graphs.

%description graphs -l pl
Ten pakiet zawiera trochê przyk³adowych grafów.

%package tcl
Summary:	Tcl extension tools for graphviz
Summary(pl):	Rozszerzenia Tcl dla graphviza
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description tcl
This package contains the various tcl packages (extensions) using
graphviz.

%description tcl -l pl
Ten pakiet zawiera ró¿ne pakiety (rozszerzenia) tcl u¿ywaj±ce
graphviza.

%package devel
Summary:	Header files for graphviz libraries
Summary(pl):	Pliki nag³ówkowe do bibliotek graphviz
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for graphviz libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do bibliotek graphviz.

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
	%{?with_dynagraph:--enable-dynagraph} \
	--enable-gvrender

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# tcl doesn't find pkgIndex.tcl outside /usr/lib...
install -d $RPM_BUILD_ROOT{/usr/lib/graphviz,%{_pkgconfigdir}}
sed -e "s@\$dir @%{_libdir}/graphviz/@" $RPM_BUILD_ROOT%{_libdir}/graphviz/pkgIndex.tcl \
	> $RPM_BUILD_ROOT/usr/lib/graphviz/pkgIndex.tcl

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/pkgconfig/*.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/dotneato-config
%dir %{_libdir}/graphviz
# *.so links are needed here for tcl
%attr(755,root,root) %{_libdir}/graphviz/lib*.so*
%dir %{_datadir}/graphviz
%{_datadir}/graphviz/lefty
%{_mandir}/man1/*
%exclude %{_mandir}/man1/dotneato-config.1*

%files graphs
%defattr(644,root,root,755)
%{_datadir}/graphviz/graphs

%files tcl
%defattr(644,root,root,755)
%dir /usr/lib/graphviz
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dotneato-config
%{_libdir}/graphviz/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/graphviz
%{_mandir}/man1/dotneato-config.1*
%{_mandir}/man3/*
