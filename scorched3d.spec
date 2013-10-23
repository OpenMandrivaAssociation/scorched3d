%define oname Scorched3D

Summary:	Scorched Earth 3D OpenGL Remake
Name:		scorched3d
Version:	43.3
Release:	6
License:	GPLv1+
Group:		Games/Arcade
URL:		http://www.scorched3d.co.uk
Source0:	http://prdownloads.sourceforge.net/scorched3d/%{oname}-%{version}-src.tar.gz
# openal-soft does not provide openal-config, so fake it
Source1:	openal-config
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		scorched3d-gcc47.patch
Patch1:		scorched3d-help.patch
Patch2:		scorched3d-libpng15.patch
Patch3:		scorched3d-syslibs.patch
BuildRequires:	mesa-common-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	openal-devel
BuildRequires:	freealut-devel
BuildRequires:	fftw-devel
BuildRequires:	expat-devel
BuildRequires:	glew-devel

%description
Scorched is a game based loosely on the classic DOS game Scorche
d Earth "The Mother Of All Games".

"Scorched Earth is a simple, yet exciting artillery combat game,
based on an auspicious history of artillery games."
(Review of Scorched Earth at ClassicGaming.com)

In its simplest form Scorched is an artillery game.
Tanks take turns to earn money by destroying opponents in an arena.
Scorched attempts to recreate the simple yet addictive game play
of the original game, adding amongst other new features a 3D island
environment and LAN and internet play.

%prep
%setup -q -n scorched
for i in `find -type d -name CVS`; do %__rm -rf $i; done
install -m 755 %{SOURCE1} .
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0

%build
export OPENAL_CONFIG=$PWD/openal-config 
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}/%{name} \
	--with-wx-config=%{_bindir}/wx-config-unicode \
	--disable-openaltest \
	--enable-dependency-tracking

%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_gamesdatadir}/%{name}/{README,documentation}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Scorched 3D
Comment=Scorched Earth 3D OpenGL Remake
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%files
%doc README documentation/*
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop


%changelog
* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 43.3-1
+ Revision: 773956
- New version 43.3, switch to system glew (use patch from Fedora)

* Sat Jul 02 2011 Zombie Ryushu <ryushu@mandriva.org> 43.2a-1
+ Revision: 688536
- Security Update for scorched3d
- Security Update for scorched3d

* Sun Nov 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 43.2-1mdv2011.0
+ Revision: 602358
- update to new version 43.2

* Sat Jul 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 43.1c-1mdv2011.0
+ Revision: 554582
- update to new version 4.31c
- add a workaround for missing openal-config

* Wed Apr 07 2010 Samuel Verschelde <stormi@mandriva.org> 43.1b-1mdv2010.1
+ Revision: 532861
- update to new version 43.1b

* Mon Apr 05 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 43-1mdv2010.1
+ Revision: 531574
- update to new version 43

* Mon Oct 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 42.1-3mdv2010.0
+ Revision: 454295
- rebuild for new libopenal

* Mon Aug 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 42.1-2mdv2010.0
+ Revision: 417441
- rebuild for new libjpeg

* Fri Mar 20 2009 Frederik Himpe <fhimpe@mandriva.org> 42.1-1mdv2009.1
+ Revision: 359080
- Update to new version 42.1
- Remove gcc 4.3 patch: not needed anymore

* Sat Feb 21 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 42-2mdv2009.1
+ Revision: 343535
- Fix desktop file

* Tue Feb 17 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 42-1mdv2009.1
+ Revision: 341168
- update to new version 42
- add buildrequires on expat-deve
- Patch0: rediff

* Thu Sep 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 41.3-5mdv2009.0
+ Revision: 288075
- patch to make it build
- switch to unicode version of wxgtk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jan 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 41.3-1mdv2008.1
+ Revision: 156014
- new version

* Thu Jan 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 41.2-2mdv2008.1
+ Revision: 153940
- rebuild due to wrong tag

* Tue Jan 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 41.2-1mdv2008.1
+ Revision: 152004
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 41.1-1mdv2008.1
+ Revision: 104518
- set buildrequires on fftw-devel
- disable openal test
- drop old menu
- move icons to fd.o compiliant directory
- spec file clean
- new version
- set buildrequires on freealut-devel
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sun Jul 16 2006 Götz Waschk <waschk@mandriva.org> 40-1mdv2007.0
- update patch 1
- drop patch 0
- New release 40

* Fri Jul 14 2006 Götz Waschk <waschk@mandriva.org> 39.1-3mdv2007.0
- fix menu

* Thu Jul 06 2006 Götz Waschk <waschk@mandriva.org> 39.1-2mdv2007.0
- xdg menu
- fix build with gcc 4.1

* Wed Aug 31 2005 Götz Waschk <waschk@mandriva.org> 39.1-1mdk
- fix buildrequires
- New release 39.1

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 38.1-3mdk
- work around broken wx-config

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 38.1-2mdk
- rebuild for new wxGTK

* Mon Feb 14 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 38.1-1mdk
- New release 38.1

* Sun Dec 05 2004 Goetz Waschk <waschk@linux-mandrake.com> 38-1mdk
- New release 38

* Fri Aug 27 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 37.2-3mdk
- rebuild for new menu

* Mon Jun 07 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 37.2-2mdk
- rebuild for new g++

* Tue Jun 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 37.2-1mdk
- 37.2

* Tue May 04 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 37.1-1mdk
- fix installation
- we really require wxGTK 2.4
- new version

* Thu Jan 15 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 36.2-1mdk
- 36.2
- fix buildrequires

* Wed Dec 10 2003 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 36-2mdk
- update from cvs (after author's advice)

* Mon Dec 08 2003 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 36-1mdk
- build 36
- drop P0 (merged upstream)

* Sun Aug 03 2003 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 35-1mdk
- initial mdk release

