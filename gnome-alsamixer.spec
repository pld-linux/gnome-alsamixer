Summary:	An ALSA mixer for GNOME
Summary(pl):	Mikser ALSA dla GNOME
Name:		gnome-alsamixer
Version:	0.9.6
Release:	4
License:	GPL
Group:		X11/Applications/Sound
Source0:	ftp://ftp.paw.co.za/pub/PAW/sources/%{name}-%{version}.tar.gz
# Source0-md5:	387623cfeb079d78325eed2d6bc94251
Source1:	%{name}.desktop
Patch0:		%{name}-gtk24.patch
Patch1:		%{name}-paths.patch
URL:		http://www.paw.co.za/projects/gnome-alsamixer/
BuildRequires:	alsa-lib >= 0.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sound mixer for GNOME which is written for the Advanced Linux Sound
Architecture (ALSA), which supports ALSA 0.9.x.

%description -l pl
Mikser d¼wiêku dla GNOME, napisany dla architektury ALSA (Advanced
Linux Sound Architecture), obs³uguj±cy ALSê 0.9.x.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/%{name}-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
rm -rf $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
