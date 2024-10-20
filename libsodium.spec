%define major 26
%define oldlibname %mklibname sodium 23
%define libname %mklibname sodium
%define develname %mklibname sodium -d

Summary:	The Sodium crypto library
Name:		libsodium
Version:	1.0.20
Release:	1
License:	ISC
Group:		System/Libraries
URL:		https://libsodium.org/
Source0:	http://download.libsodium.org/libsodium/releases/%{name}-%{version}.tar.gz
Patch0:		libsodium-arm-crypto-cflags.patch
BuildSystem:	autotools

%description
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more. It is a portable, cross-compilable,
installable, packageable fork of NaCl, with a compatible API, and an extended
API to improve usability even further. Its goal is to provide all of the core
operations needed to build higher-level cryptographic tools. The design
choices emphasize security, and "magic constants" have clear rationales.

The same cannot be said of NIST curves, where the specific origins of certain
constants are not described by the standards. And despite the emphasis on
higher security, primitives are faster across-the-board than most
implementations of the NIST standards.

%package -n %{libname}
Summary:	The Sodium crypto library
Group:		System/Libraries
Obsoletes:	%{mklibname sodium 18} < 1.0.15
%rename %{oldlibname}

%description -n %{libname}
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more. It is a portable, cross-compilable,
installable, packageable fork of NaCl, with a compatible API, and an extended
API to improve usability even further. Its goal is to provide all of the core
operations needed to build higher-level cryptographic tools. The design
choices emphasize security, and "magic constants" have clear rationales.

The same cannot be said of NIST curves, where the specific origins of certain
constants are not described by the standards. And despite the emphasis on
higher security, primitives are faster across-the-board than most
implementations of the NIST standards.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name} libraries.

%if ! %{cross_compiling}
%check
cd _OMV_rpm_build
make check
%endif

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README.markdown THANKS
%{_includedir}/sodium.h
%{_includedir}/sodium/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
