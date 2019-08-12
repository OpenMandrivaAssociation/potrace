%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d


Summary:	Utility for transforming a bitmap into a scalable image
Name:		potrace
Version:	1.15
Release:	1
License:	GPLv2
Group:		Graphics/Utilities
URL:		http://potrace.sourceforge.net/
Source0:	http://potrace.sourceforge.net/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(zlib)
Provides:	fonttracer

%description
potrace is a utility for tracing a bitmap, which means, transforming
a bitmap into a smooth, scalable image. The input is a bitmap (PBM,
PGM, PPM, or BMP format), and the output can be EPS (default),
Postscript, SVG ou PGM (for easy antialiasing). A typical use is to
create EPS files from scanned data, such as company or university logos,
handwritten notes, etc. The resulting image is not "jaggy" like a bitmap,
but smooth. It can then be rendered at any resolution.

%package -n	%{libname}
Summary:	Shared library for potrace
Group:		System/Libraries

%description -n	%{libname}
Libpotrace is the library for potrace.


%package -n	%{devname}
Summary:	Development files for lib%{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Libpotrace is the library for potrace.

This package contains the files for developing applications which
will use libpotrace.


%prep
%setup -q
%autopatch -p1

# fix file perm
chmod -R go+rX .

%build
%configure \
	--with-libpotrace \
	--disable-static

%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog README NEWS doc/placement.pdf
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_includedir}/potracelib.h
