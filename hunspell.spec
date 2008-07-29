Name:      hunspell
Summary:   Hunspell is a spell checker and morphological analyzer library
Version:   1.2.6
Release:   1%{?dist}
Source0:   http://downloads.sourceforge.net/%{name}/hunspell-%{version}.tar.gz
Source1:   http://people.debian.org/~agmartin/misc/ispellaff2myspell
Group:     System Environment/Libraries
URL:       http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+ or GPLv2+ or MPLv1.1
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
# Filter unwanted Requires for the "use explicitely" string in ispellaff2myspell
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(explicitely)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

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
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/ispellaff2myspell

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
%lang(hu) %{_mandir}/hu/man1/hunspell.1.gz
%lang(hu) %{_mandir}/hu/man4/hunspell.4.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/hzip
%{_bindir}/hunzip
%{_bindir}/ispellaff2myspell
%{_libdir}/pkgconfig/hunspell.pc
%{_mandir}/man1/hunzip.1.gz
%{_mandir}/man1/hzip.1.gz
%{_mandir}/man3/hunspell.3.gz

%changelog
* Tue Jul 29 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.6-1
- latest version

* Sun Jul 27 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.5-1
- latest version

* Tue Jul 22 2008 Kristian Høgsberg <krh@redhat.com> - 1.2.4.2-2
- Drop ABI breaking hunspell-1.2.2-xulrunner.pita.patch and fix the
  hunspell include in xulrunner.

* Fri Jun 18 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.4.2-1
- latest version

* Thu Jun 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.4-1
- latest version

* Fri May 16 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-3
- Resolves: rhbz#446821 fix crash

* Wed May 14 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-2
- give xulrunner what it needs so we can get on with it

* Fri Apr 18 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version
- drop integrated hunspell-1.2.1-1863239.badstructs.patch

* Wed Mar 05 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.1-6
- add ispellaff2myspell to devel

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-5
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.1-4
- add hunspell-1.2.1-1863239.badstructs.patch

* Fri Nov 09 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-2
- pkg-config cockup

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Mon Oct 08 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.12.2-2
- lang fix for man pages from Ville Skyttä

* Wed Sep 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.12.2-1
- next version

* Tue Aug 28 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.11.2-1
- next version

* Fri Aug 24 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.10-1
- next version

* Thu Aug 02 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.9-2
- clarify license

* Wed Jul 25 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.9-1
- latest version

* Wed Jul 18 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.8.2-1
- latest version

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
