Summary:	Graph Visualization Tools
Summary(pl):	Narzêdzie do wizualizacji w postaci grafów
Name:		graphviz
Version:	1.8.4
Release:	1
License:	custom (AT&T)
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/%{name}-%{version}.tar.gz
URL:		http://www.graphviz.org/
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gawk
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel >= 8.3.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in barcharts).

%description -l pl
Kolekcja narzêdzi oraz pakietów tcl s³u¿±cych do manipulacji i
rozmieszczania grafów.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure 
# \
#	--with-dynagraph
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9 AUTHORS COPYING ChangeLog FAQ.txt NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.tcl
%attr(755,root,root) %{_libdir}/%{name}/lib*.so.*.*
%{_libdir}/%{name}/graphs
%dir %{_libdir}/%{name}/lefty
%attr(755,root,root) %{_libdir}/%{name}/lefty/*

%{_mandir}/man1/*
%{_mandir}/mann/*
