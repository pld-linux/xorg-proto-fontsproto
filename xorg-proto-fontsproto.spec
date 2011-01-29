Summary:	Fonts extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Fonts
Name:		xorg-proto-fontsproto
Version:	2.1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/fontsproto-%{version}.tar.bz2
# Source0-md5:	37102ffcaa73f77d700acd6f7a25d8f0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fonts extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Fonts.

%package devel
Summary:	Fonts extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Fonts
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Fonts extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Fonts.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/*.{html,css}
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/FS*.h
%{_includedir}/X11/fonts/font*.h
%{_includedir}/X11/fonts/fsmasks.h
%{_pkgconfigdir}/fontsproto.pc
