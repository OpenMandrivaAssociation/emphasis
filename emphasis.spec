%define	name emphasis
%define	version 0.0.1
%define release %mkrel 9

Summary: 	Simple MPD (Music Player Daemon) client writen in C/Etk
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		https://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	etk-devel >= 0.1.0.002
BuildRequires:	ecore-devel >= 0.9.9.022
Buildrequires:  libmpd-devel >= 0.12.0
Buildrequires:  libxml2-devel >= 2.6.0
Buildrequires:  enhance-devel >= 0.0.1 

%description
Emphasis is a simple MPD (Music Player Daemon) client writen in C/Etk.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%if 0
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
cp -vf data/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf data/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
cp -vf data/%{name}.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/%name.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/%name.png %buildroot%_miconsdir/%name.png


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Emphasis
Comment=Emphasis
Exec=%{_gamesbindir}/emphasis
Icon=%{_datadir}/pixmaps/%{name}.png
Terminal=false
Type=Application
EOF

%endif
%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/applications/*
