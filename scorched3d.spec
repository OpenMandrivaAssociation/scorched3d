%define	name	scorched3d
%define	oname	Scorched3D
%define version 40
%define release %mkrel 1
%define	Summary	Scorched Earth 3D OpenGL Remake

Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.scorched3d.co.uk/
Source0:	http://prdownloads.sourceforge.net/scorched3d/%{oname}-%{version}-src.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
#gw don't use bundled zlib
Patch1: scorched-zlib.patch
License:	GPL
Group:		Games/Arcade
Summary:	%{Summary}
BuildRequires:	Mesa-common-devel SDL_mixer-devel SDL_net-devel wxGTK2.6-devel
BuildRequires:	openal-devel
BuildRequires:	automake1.7 autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch1 -p1 -b .zlib
for i in `find -type d -name CVS`; do rm -rf $i; done

%build
#cd scripts
#perl createAMMakefile.pl
#cd ..
#aclocal-1.7
#automake-1.7 --foreign
#autoconf-2.5x
#gw work around binutils bug, use g++ for the configure call
export CC=g++ 
%configure2_5x	--bindir=%_gamesbindir --datadir=%_gamesdatadir/%name --with-wx-config=%_bindir/wx-config-ansi
%make CC=gcc

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}
%{__rm} -rf $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/{README,documentation}

%{__install} -d $RPM_BUILD_ROOT%{_menudir}
%{__cat} <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="Scorched 3D"\
		longtitle="%{Summary}" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Scorched 3D
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF



%{__install} %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README documentation/* AUTHORS TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%_datadir/applications/mandriva-*
%defattr(755,root,root,755)
%{_gamesbindir}/*

