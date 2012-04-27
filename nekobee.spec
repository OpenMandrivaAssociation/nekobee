Name:       nekobee
Summary:    Bassline DSSI plugin
Version:    0.1.7
Release:    3

Source: http://static.nekosynth.co.uk/releases/nekobee-%{version}.tar.gz
URL: http://www.nekosynth.co.uk/wiki/nekobee
License:    GPLv2
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Bassline DSSI plugin

%prep
%setup -q

%build
%configure2_5x --with-dssi-dir=%{buildroot}%{_libdir}/dssi

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%doc COPYING README
%_bindir/*
%_libdir/dssi/*

