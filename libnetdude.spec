#
# TODO: pl desc
#
Summary:	Packet manipulation backend of the Netdude trace file editing framework
#Summary(p7l.UTF-8):
Name:		libnetdude
Version:	0.11
Release:	1
License:	Distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/netdude/libnetdude/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8859cdc23d56e1a8f392a8c365079f83
Patch0:		%{name}-libltdl.patch
Patch1:		%{name}-duplicate_files.patch
Patch2:		%{name}-paths.patch
URL:		http://netdude.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	libpcapnav-devel
BuildRequires:	libtool
BuildRequires:	tcpdump
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetdude is the packet manipulation backend of the Netdude trace
file editing framework. It allows you to perform trace file
manipulations at a much higher level of abstraction than code written
directly for the pcap interface. It also supports plugins (dynamically
loaded libraries) that can essentially do whatever the programmer
desires. When developers write their packet manipulation code as
libnetdude plugins, this instantly allows other developers to use
their tools. It provides data types and APIs for the most common
situations when dealing with libpcap trace files: trace files of
arbitrary size, packets, network protocols, packet iterators, and
packet filters, just to name a few.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for libnetdude library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetdude
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnetdude library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetdude.

%package static
Summary:	Static libnetdude library
Summary(pl.UTF-8):	Statyczna biblioteka libnetdude
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetdude library.

%description static -l pl.UTF-8
Statyczna biblioteka libnetdude.

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS TODO docs
%attr(755,root,root) %{_bindir}/lndtool
%attr(755,root,root) %{_libdir}/libnetdude.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetdude.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnetdude.so
%{_libdir}/libnetdude.la
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnd_*.so
%dir %{_libdir}/%{name}/protocols
%attr(755,root,root) %{_libdir}/%{name}/protocols/libnd_*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*/libnd*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetdude.a
%{_libdir}/%{name}/*/libnd*.a
