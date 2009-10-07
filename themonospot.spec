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

