#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libfreehand
Version  : 0.1.2
Release  : 5
URL      : https://dev-www.libreoffice.org/src/libfreehand-0.1.2.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libfreehand-0.1.2.tar.xz
Summary  : Library for parsing the FreeHand file format structure
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libfreehand-bin = %{version}-%{release}
Requires: libfreehand-lib = %{version}-%{release}
Requires: libfreehand-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : gperf
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed

%description


%package bin
Summary: bin components for the libfreehand package.
Group: Binaries
Requires: libfreehand-license = %{version}-%{release}

%description bin
bin components for the libfreehand package.


%package dev
Summary: dev components for the libfreehand package.
Group: Development
Requires: libfreehand-lib = %{version}-%{release}
Requires: libfreehand-bin = %{version}-%{release}
Provides: libfreehand-devel = %{version}-%{release}
Requires: libfreehand = %{version}-%{release}

%description dev
dev components for the libfreehand package.


%package doc
Summary: doc components for the libfreehand package.
Group: Documentation

%description doc
doc components for the libfreehand package.


%package lib
Summary: lib components for the libfreehand package.
Group: Libraries
Requires: libfreehand-license = %{version}-%{release}

%description lib
lib components for the libfreehand package.


%package license
Summary: license components for the libfreehand package.
Group: Default

%description license
license components for the libfreehand package.


%prep
%setup -q -n libfreehand-0.1.2
cd %{_builddir}/libfreehand-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592623699
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-werror
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592623699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libfreehand
cp %{_builddir}/libfreehand-0.1.2/COPYING %{buildroot}/usr/share/package-licenses/libfreehand/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fh2raw
/usr/bin/fh2svg
/usr/bin/fh2text

%files dev
%defattr(-,root,root,-)
/usr/include/libfreehand-0.1/libfreehand/FreeHandDocument.h
/usr/include/libfreehand-0.1/libfreehand/libfreehand.h
/usr/lib64/libfreehand-0.1.so
/usr/lib64/pkgconfig/libfreehand-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libfreehand/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreehand-0.1.so.1
/usr/lib64/libfreehand-0.1.so.1.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libfreehand/9744cedce099f727b327cd9913a1fdc58a7f5599
