Summary:	Fonts protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Fonts i pomocnicze
Name:		xorg-proto-fontsproto
Version:	2.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/fontsproto-%{version}.tar.bz2
# Source0-md5:	c946f166107b016a21cc7a02e1132724
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fonts protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Fonts i pomocnicze.

%package devel
Summary:	Fonts protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Fonts i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fonts protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Fonts i pomocnicze.

%prep
%setup -q -n fontsproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/fontsproto.pc
