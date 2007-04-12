%define name    potrace
%define version 1.7
%define release 3mdk

Summary:	Utility for transforming a bitmap into a scalable image
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
URL:		http://potrace.sourceforge.net/
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

