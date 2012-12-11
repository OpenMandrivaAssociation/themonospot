Summary: Avi and Mkv parser/editor and content descriptor
Name: themonospot
Version: 0.7.3.1
Release: %mkrel 2
License: GPLv2
Group: Video
Source: http://www.integrazioneweb.com/repository/SOURCES/themonospot-%{version}.tar.gz
Patch0: themonospot-0.7.3.1-fix-default-lang-name.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.integrazioneweb.com/themonospot

BuildRequires: gtk-sharp2 >= 2.8.3
BuildRequires: glade-sharp2 >= 2.8.3
BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig

Requires: gtk-sharp2 >= 2.8.3
Requires: glade-sharp2 >= 2.8.3
Requires: glib-sharp2 >= 2.8.3
Requires: mono >= 1.2.3

%description
themonospot is a simple application that can be used to scan an avi
file and extract some informations about audio and video data flow:

    - Video codec used
    - Frame size
    - Average video bitrate
    - File size
    - Total time
    - Frame rate
    - Total frames
    - Info data
    - Packet Bitstream
    - User data (in MOVI chunk)
    - Audio codec used
    - Average audio bitrate
    - Audio channels

Using themonospot it is also possible to modify FourCC informations
(FourCC code in video chunk and FourCC description in stream header)
and also change some problematic UserData values for table players 
(it set the value to DivX999b000p). This features are available only
for avi file type.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme copying.gpl
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/pkgconfig/%{name}-base.pc



%changelog
* Wed Oct 07 2009 Funda Wang <fundawang@mandriva.org> 0.7.3.1-2mdv2010.0
+ Revision: 455439
- fix default language name (bug#54350)

* Thu Jun 25 2009 Armando Basile <hman@mandriva.org> 0.7.3.1-1mdv2010.0
+ Revision: 389197
- 0.7.3 release (bug fixed and new features added)

* Sat Dec 20 2008 Armando Basile <hman@mandriva.org> 0.7.1.1-1mdv2009.1
+ Revision: 316817
- 2009.1 commit

* Wed Aug 27 2008 Armando Basile <hman@mandriva.org> 0.7.1.1-1mdv2009.0
+ Revision: 276427
- bug fix release

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.0.1-4mdv2009.0
+ Revision: 269425
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Funda Wang <fundawang@mandriva.org> 0.7.0.1-3mdv2009.0
+ Revision: 206531
- there is no more info file

* Sun May 11 2008 Funda Wang <fundawang@mandriva.org> 0.7.0.1-2mdv2009.0
+ Revision: 205513
- should not be noarch

* Sun May 04 2008 Funda Wang <fundawang@mandriva.org> 0.7.0.1-1mdv2009.0
+ Revision: 200975
- New version 0.7.0.1

* Thu Jan 17 2008 Stéphane Téletchéa <steletch@mandriva.org> 0.6.5-1mdv2008.1
+ Revision: 154160
- according to the author tagging as noarch
- revised tarball from upstream
- Update spec file to conform to our policies
- Add buildrequire for glade-sharp2
- Add the version for the license (as confirmed by the developper)
- import themonospot


* Fri Jan 04 2008 Armando Basile <hmandevteam@gmail.com> 0.6.5-2
- bug fixed: Issue 007 [Wrong AudioRate value]
- bug fixed: Issue 008 [Calculate VideoRate]
- new feature: Multilanguage with language files (*.lf in languages folder)
- bug fixed: minor bugs

* Sun Dec 23 2007 Armando Basile <hmandevteam@gmail.com> 0.6.2-1
- bug fixed: Issue 004 [Array index is out of range]

* Mon Jul 30 2007 Armando Basile <hmandevteam@gmail.com> 0.6.0-1
- added extraction of Packet Bitstream  infos from MOVI Chunk
- added Change problematic UserData values and save file function

* Fri Jul 20 2007 Armando Basile <hmandevteam@gmail.com> 0.4.0-1
- added autosave of last folder used
- added extraction of USER DATA infos from MOVI Chunk
- added FourCC change function (fourCC Code and Description)

* Wed Jul 06 2007 Armando Basile <hmandevteam@gmail.com> 0.3.0-1
- new layout
- some bugs fixed
- optimization code 
