%define pkgname edrip-ttf

Summary: contrast sans-serif font
Name: fonts-ttf-edrip
Version: r6
Release: 2
License: OFL
Group: System/Fonts/True type
URL: http://code.google.com/p/edrip/
Source0: http://edrip.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: freetype-tools

%description
Edrip font is a contrast sans-serif font. It is based on the Teams font
released on 2000 by TopTeam Co. which can be found in Debian:
http://packages.debian.org/sarge/t1-teams. The font is distributed under the
terms of SIL Open Font License. Up to now this font contains symbols for
Cyrillic and basic Latin alphabets.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/edrip

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/edrip
ttmkfdir %{buildroot}%{_xfontdir}/TTF/edrip > %{buildroot}%{_xfontdir}/TTF/edrip/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/edrip/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/edrip \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-edrip:pri=50

%files
%defattr(-,root,root,-)
%doc README OFL.txt OFL-FAQ.txt FontLog.txt
%dir %{_xfontdir}/TTF/edrip
%{_xfontdir}/TTF/edrip/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/edrip/fonts.dir
%{_xfontdir}/TTF/edrip/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-edrip:pri=50





%changelog
* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> r6-1mdv2012.0
+ Revision: 690968
- imported package fonts-ttf-edrip

