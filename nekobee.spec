
Name: nekobee
Summary: Bassline DSSI plugin
Version: 0.1.5
Release: %mkrel 1
Source: http://static.nekosynth.co.uk/releases/nekobee-%{version}.tar.gz
URL: http://www.nekosynth.co.uk/wiki/nekobee
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: dssi-devel
BuildRequires: liblo-devel
BuildRequires: ladspa-devel
BuildRequires: libalsa-devel
BuildRequires: gtk2-devel

%description
Bassline DSSI plugin

%prep
%setup -q

%build
%configure2_5x

make
								
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%_bindir/*
%_libdir/dssi/*
	      
