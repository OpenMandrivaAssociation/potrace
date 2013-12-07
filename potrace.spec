Summary:	Utility for transforming a bitmap into a scalable image
Name:		potrace
Version:	1.10
Release:	5
License:	GPLv2
Group:		Graphics
Url:		http://potrace.sourceforge.net/
Source0:	http://potrace.sourceforge.net/download/%{name}-%{version}.tar.gz
Buildrequires:	pkgconfig(zlib)
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
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README NEWS
%{_bindir}/*
%{_mandir}/man1/*

