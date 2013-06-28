#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           jasper
Version:        1.900.1
Release:        144
License:        SUSE-Public-Domain
Summary:        An Implementation of the JPEG-2000 Standard, Part 1
Url:            http://www.ece.uvic.ca/~mdadams/jasper/
Group:          Productivity/Graphics/Convertors
Source:         %{name}-%{version}.tar.bz2
Source98:       baselibs.conf
Source1001: 	jasper.manifest
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains an implementation of the image compression
standard, JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package -n libjasper
License:        SUSE-Public-Domain
Summary:        JPEG-2000 library
Group:          Productivity/Graphics/Convertors

%description -n libjasper
This package contains libjasper, a library implementing the JPEG-2000
image compression standard Part 1.

%package -n libjasper-devel
License:        SUSE-Public-Domain
Summary:        JPEG-2000 library - files mandatory for development
Group:          Development/Libraries/C and C++
Requires:       libjasper = %{version}
Requires:       libjpeg8-devel

%description -n libjasper-devel
This package contains libjasper, a library implementing the JPEG-2000
image compression standard Part 1.

%prep
%setup -q
cp %{SOURCE1001} .

%build
autoreconf -i -f
export CFLAGS="%{optflags} -Wall"
%configure --prefix=/usr --enable-shared --disable-static --libdir=%{_libdir}
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/usr/bin/tmrdemo
# compatibility link, there was no interface change
ln -s libjasper.so.1.0.0 %{buildroot}%{_libdir}/libjasper-1.701.so.1

%post -n libjasper -p /sbin/ldconfig

%postun -n libjasper -p /sbin/ldconfig

%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYRIGHT
/usr/bin/imgcmp
/usr/bin/imginfo
/usr/bin/jasper

%files -n libjasper
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libjasper*.so.*

%files -n libjasper-devel
%manifest %{name}.manifest
%defattr(-,root,root)
/usr/include/jasper
%{_libdir}/libjasper.so
