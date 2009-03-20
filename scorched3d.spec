%define	oname	Scorched3D

Summary:	Scorched Earth 3D OpenGL Remake
Name:		scorched3d
Version:	42.1
Release:	%mkrel 1
License:	GPLv1+
Group:		Games/Arcade
URL:		http://www.scorched3d.co.uk
Source0:	http://prdownloads.sourceforge.net/scorched3d/%{oname}-%{version}-src.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
BuildRequires:	Mesa-common-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	openal-devel
BuildRequires:	freealut-devel
BuildRequires:	fftw-devel
BuildRequires:	expat-devel
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
for i in `find -type d -name CVS`; do rm -rf $i; done

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}/%{name} \
	--with-wx-config=%{_bindir}/wx-config-unicode \
	--disable-openaltest \
	--enable-dependency-tracking
%make 

%install
rm -rf %{buildroot}
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

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README documentation/* 
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop
