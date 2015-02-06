Name:       nekobee
Summary:    Bassline DSSI plugin
Version:    0.1.7
Release:    5

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
perl -pi -e 's/GError \*gerror/GError \*gerror \= NULL/g' src/gtkknob.c

%build
%configure2_5x --with-dssi-dir=%{buildroot}%{_libdir}/dssi

%make bindir=%{_libdir}/dssi/%name

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=%{buildroot}%{_libdir}/dssi/%name

%files
%defattr(-,root,root)
%doc COPYING README
%_libdir/dssi/*



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.7-4
+ Revision: 794049
- fixed GUI binary installation path

* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.7-3
+ Revision: 793826
- rebuild, spec cleanup

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-2mdv2011.0
+ Revision: 613007
- the mass rebuild of 2010.1 packages

* Tue Apr 06 2010 Frank Kober <emuse@mandriva.org> 0.1.7-1mdv2010.1
+ Revision: 531910
- new version 0.1.7
- new version 0.1.7

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.1.6-3mdv2009.0
+ Revision: 253698
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 24 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.6-1mdv2008.1
+ Revision: 101738
- New release

* Mon May 07 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.5-1mdv2008.0
+ Revision: 24940
- import nekobee-0.1.5-1mdv2008.0


* Mon May 07 2007 Helio Chissini de Castro <helio@mandriva.com>
- Initial release on Mandriva Linux

