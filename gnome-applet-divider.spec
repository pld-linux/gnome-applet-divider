%define		_realname	divider-applet

Summary:	Divider like those between icons on toolbars
Summary(pl):	Podzielnik, jak te pomiêdzy ikonami na paskach narzêdziowych
Name:		gnome-applet-divider
Version:	1.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gqapplets/%{_realname}-%{version}.tar.gz
# Source0-md5:	a3d8385f6639b3817a4d96a8220180b7
URL:		http://gqapplets.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/gconf

%description
This applet is a simple divider like those between icons on toolbars.
The style, color, and strength of effect (transparency) can be
adjusted on the properties dialog.

%description -l pl
Ten aplet jest prostym podzielnikiem jak te pomiêdzy ikonami na
paskach narzêdziowych. Styl, kolor i natê¿enie efektu
(przezroczysto¶æ) mo¿na dostosowywaæ w okienku dialogowym w³a¶ciwo¶ci.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --with-gconf-schema-file-dir=%{_sysconfdir}/schemas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%{_sysconfdir}/schemas/divider-applet.schemas
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/divider_applet2
%{_datadir}/gnome-2.0/ui/GNOME_DividerApplet.xml
%{_pixmapsdir}/*.png
%{_datadir}/divider-applet/*
