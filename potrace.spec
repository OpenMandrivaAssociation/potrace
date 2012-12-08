%define name	potrace
%define version 1.8

Summary:	Utility for transforming a bitmap into a scalable image
Name:		potrace
Version:	1.9
Release:	%mkrel 3
License:	GPLv2
Group:		Graphics
URL:		http://potrace.sourceforge.net/
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
Buildrequires:	zlib-devel
Provides:	fonttracer

%description
potrace is a utility for tracing a bitmap, which means, transforming 
a bitmap into a smooth, scalable image. The input is a bitmap (PBM, 
PGM, PPM, or BMP format), and the output can be EPS (default), 
Postscript, SVG ou PGM (for easy antialiasing). A typical use is to 
create EPS files from scanned data, such as company or university logos, 
handwritten notes, etc. The resulting image is not "jaggy" like a bitmap, 
but smooth. It can then be rendered at any resolution.

%prep
%setup -q

# fix file perm
chmod -R go+rX .

%build
%configure2_5x --enable-a4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu May 12 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.9-1mdv2011.0
+ Revision: 673944
- update to 1.9

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8-7
+ Revision: 667810
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8-6mdv2011.0
+ Revision: 607196
- rebuild

* Mon Feb 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.8-5mdv2010.1
+ Revision: 499132
- fix licence and rpmlint warning

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.8-4mdv2010.0
+ Revision: 426773
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.8-3mdv2009.0
+ Revision: 225027
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8-2mdv2008.1
+ Revision: 179256
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.8-1mdv2008.0
+ Revision: 37054
- new release 1.8; rebuild for new era


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.7-3mdk
- Rebuild

* Wed Aug 10 2005 Abel Cheung <deaddog@mandriva.org> 1.7-2mdk
- Rebuild

* Mon Mar 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.7-1mdk
- 1.7

* Mon Dec 27 2004 Abel Cheung <deaddog@mandrake.org> 1.5-3mdk
- Provides "fonttracer" (autotrace has same function)

* Sat Dec 11 2004 Abel Cheung <deaddog@mandrake.org> 1.5-2mdk
- Fix file permission

* Fri Dec 10 2004 Abel Cheung <deaddog@mandrake.org> 1.5-1mdk
- New version
- Doesn't need ncompress now

* Tue Jun 22 2004 Blaise Tramier <meles@free.fr> 1.4-1mdk
- first mdk package.

