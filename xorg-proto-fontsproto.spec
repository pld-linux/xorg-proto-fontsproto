Summary:	Fonts protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Fonts i pomocnicze
Name:		xorg-proto-fontsproto
Version:	2.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/fontsproto-%{version}.tar.bz2
# Source0-md5:	ec23e17f0cb54b15ff31e846704c849f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
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
