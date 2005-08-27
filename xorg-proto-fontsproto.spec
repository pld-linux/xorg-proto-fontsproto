Summary:	Fonts protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fonts i pomocnicze
Name:		xorg-proto-fontsproto
Version:	2.0
Release:	0.03
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/fontsproto-%{version}.tar.bz2
# Source0-md5:	8ff6548d1c31975b832ecd4a7e7ede3d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fonts protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Fonts i pomocnicze.

%package devel
Summary:	Fonts protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fonts i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fonts protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Fonts i pomocnicze.

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
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/fontsproto.pc
