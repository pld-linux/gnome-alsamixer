Summary:	An ALSA mixer for GNOME written for ALSA 0.9.x
Summary(pl):	Mikser ALSA dla GNOME, napisany dla ALSy 0.9.x
Name:		gnome-alsamixer
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.paw.co.za/pub/PAW/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
URL:		http://www.paw.co.za/projects/gnome-alsamixer
BuildRequires:	alsa-lib >= 0.9.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2 >= 2.0.6
BuildRequires:	libgnomeui >= 2.0.3
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
A sound mixer for GNOME which is written for the Advanced Linux Sound
Architecture (ALSA), which supports ALSA 0.9.x.

%description -l pl
Mikser d¼wiêku dla GNOME, napisany dla architektury ALSA (Advanced
Linux Sound Architecture), obs³uguj±cy ALSê 0.9.x.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog NEWS AUTHORS INSTALL TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
