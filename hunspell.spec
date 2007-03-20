Name:      hunspell
Summary:   Hunspell is a spell checker and morphological analyzer library
Version:   1.1.5
Release:   1%{?dist}
Source:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Group:     System Environment/Libraries
URL:       http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPL

BuildRequires: libtool
Patch0: hunspell-1.1.4-defaultdictfromlang.patch
Patch1: hunspell-1.1.5-missingheaders.patch

%description
Hunspell is a spell checker and morphological analyzer library and program 
designed for languages with rich morphology and complex word compounding or 
character encoding. Hunspell interfaces: Ispell-like terminal interface using 
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

%package devel
Requires: hunspell = %{version}-%{release}, pkgconfig
Summary: Files for developing with hunspell
Group: Development/Libraries

%description devel
Includes and definitions for developing with hunspell

%prep
%setup -q
%patch0 -p1 -b .defaultdictfromlang.patch
%patch1 -p1 -b .missingheaders.patch

%build
libtoolize --automake --force
aclocal -I m4
autoconf
automake
%configure --disable-static
for i in man/*.? man/hu/*.?; do
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    mv -f $i.new $i
done
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
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
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/munch
%{_bindir}/unmunch
%{_libdir}/pkgconfig/hunspell.pc

%changelog
* Tue Mar 20 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5-1
- next version

* Fri Feb 09 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-6
- some spec cleanups

* Fri Jan 19 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-5
- .pc

* Thu Jan 11 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-4
- fix out of range

* Fri Dec 15 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-3
- hunspell#1616353 simple c api for hunspell

* Wed Nov 29 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-2
- add hunspell-1.1.4-defaultdictfromlang.patch to take locale as default
  dictionary

* Wed Oct 25 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-1
- initial version
