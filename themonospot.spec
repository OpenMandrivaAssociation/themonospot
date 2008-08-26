Summary:       An Avi parser and content descriptor
Name:          themonospot
Version:       0.7.1.1
Release:       %mkrel 1
License:       GPLv2
Group:         Video
Source:        http://themonospot.googlecode.com/files/themonospot-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:           http://www.integrazioneweb.com/themonospot

Buildarch    : noarch

BuildRequires: glade-sharp2 >= 2.8.3
BuildRequires: gtk-sharp2 >= 2.8.3
BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils

Requires:      glib-sharp2 >= 2.8.3
Requires:      glade-sharp2 >= 2.8.3
Requires:      gtk-sharp2 >= 2.8.3
Requires:      mono >= 1.2.3

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
(it set the value to DivX999b000p)

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std
desktop-file-install --vendor="mandriva"               \
  --dir=%{buildroot}%{_datadir}/applications    \
  %{name}-gui/resources/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme
%doc copying.gpl
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mandriva-themonospot.desktop
