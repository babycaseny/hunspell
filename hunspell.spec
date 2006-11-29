Name: hunspell
Summary: Hunspell is a spell checker and morphological analyzer library
Version: 1.1.4
Release: 2%{?dist}
Source: %{name}-%{version}.tar.gz
Group: System Environment/Libraries
URL: http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPL
BuildRequires: libtool
Patch0: hunspell-1.1.4-sharedlibs.patch
Patch1: hunspell-1.1.4-defaultdictfromlang.patch

%description
Hunspell is a spell checker and morphological analyzer library and program 
designed for languages with rich morphology and complex word compounding or 
character encoding. Hunspell interfaces: Ispell-like terminal interface using 
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

%package devel
Requires: hunspell = %{PACKAGE_VERSION}
Summary: Files for developing with hunspell
Group: Development/Libraries

%description devel
Includes and definitions for developing with hunspell

%prep
%setup -q
%patch0 -p1 -b .sharedlibs.patch
%patch1 -p1 -b .defaultdictfromlang.patch

%build
libtoolize --automake --force
aclocal -I m4
autoconf
automake
%configure
for i in man/*.? man/hu/*.?; do
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    mv -f $i.new $i
done
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_bindir}/example
mkdir $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc README README.myspell COPYING COPYING.LGPL COPYING.MPL AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%{_libdir}/*.so.*
%{_datadir}/myspell
%{_bindir}/hunmorph
%{_bindir}/hunspell
%{_bindir}/hunstem
%{_mandir}/man1/hunspell.1.gz
%{_mandir}/man4/hunspell.4.gz
%{_mandir}/*/man1/hunspell.1.gz
%{_mandir}/*/man4/hunspell.4.gz

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/munch
%{_bindir}/unmunch

%changelog
* Wed Nov 29 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-2
- add hunspell-1.1.4-defaultdictfromlang.patch to take locale as default
  dictionary

* Wed Oct 25 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-1
- initial version
