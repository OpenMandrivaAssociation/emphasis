%define	name emphasis
%define	version 0.0.1
%define release %mkrel 5

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Simple MPD (Music Player Daemon) client writen in C/Etk
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.042, etk-devel >= 0.1.0.042
BuildRequires:	ecore-devel >= 0.9.9.042, edje-devel >= 0.5.0.042, edje >= 0.5.0.042
Buildrequires:  libmpd-devel
Buildrequires:  ecore >= 0.9.9.042, %{mklibname xml2}-devel
Buildrequires:  enhance-devel >= 0.0.1 
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils


%description
Emphasis is a simple MPD (Music Player Daemon) client writen in C/Etk.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}
for mo in `ls %buildroot%_datadir/locale/` ;
do Y=`echo -n $mo | sed -e "s|/||"`;
echo "%lang($Y) $(echo %_datadir/locale/${mo}/LC_MESSAGES/%{name}.mo)" >> $RPM_BUILD_DIR/%{name}-%{version}/%{name}.lang
done



mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
cp -vf data/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Audio" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/haricot_musique.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/haricot_musique.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/images/haricot_musique.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/haricot_musique.png %buildroot%{_datadir}/pixmaps/%name.png

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
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%_datadir/pixmaps/%name.svg
%{_datadir}/applications/*

