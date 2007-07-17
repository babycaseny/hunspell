Name:      hunspell
Summary:   Hunspell is a spell checker and morphological analyzer library
Version:   1.1.8
Release:   1%{?dist}
Source:    http://downloads.sourceforge.net/%{name}/hunspell-%{version}.tar.gz
Group:     System Environment/Libraries
URL:       http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPL

BuildRequires: libtool, ncurses-devel

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

%build
libtoolize --automake --force
aclocal -I m4
autoconf
automake
%configure --disable-static  --with-ui --with-readline
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
mv $RPM_BUILD_ROOT/%{_includedir}/*munch* $RPM_BUILD_ROOT/%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README README.myspell COPYING COPYING.LGPL COPYING.MPL AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%{_libdir}/*.so.*
%{_datadir}/myspell
%{_bindir}/hunspell
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
* Tue Jul 17 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.8-1
- latest version

* Sat Jul 07 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.7-1
- latest version
- drop integrated hunspell-1.1.5.freem.patch

* Fri Jun 29 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.6-1
- latest version
- drop integrated hunspell-1.1.4-defaultdictfromlang.patch
- drop integrated hunspell-1.1.5-badheader.patch
- drop integrated hunspell-1.1.5.encoding.patch

* Fri Jun 29 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-5
- fix memory leak
  http://sourceforge.net/tracker/index.php?func=detail&aid=1745263&group_id=143754&atid=756395

* Wed Jun 06 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-4
- Resolves: rhbz#212984 discovered problem with missing wordchars

* Tue May 22 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-3
- Resolves: rhbz#240696 extend encoding patch to promote and add
  dictionary 8bit WORDCHARS to the ucs-2 word char list

* Mon May 21 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-2
- Resolves: rhbz#240696 add hunspell-1.1.5.encoding.patch

* Mon May 21 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-1
- patchlevel release

* Tue Mar 20 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5-2
- some junk in delivered headers

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
