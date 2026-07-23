Summary:		Whatsapp Desktop app for Linux
Name:	zapzap
Version:		7.0.2
Release:		1
License:		GPLv3+
Group:	Sound
Url:		https://github.com/rafatosta/zapzap
Source0:	https://github.com/rafatosta/zapzap/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:	zapzap-7.0.2-fix-webengine-dictionaries-path.patch
BuildRequires:		desktop-file-utils
BuildRequires:		python-gettext
BuildRequires:		python-pyproject-api
BuildRequires:		python-pyproject-metadata
BuildRequires:		python-qt6-webengine
BuildRequires:		python-setuptools
BuildRequires:		python-wheel
BuildRequires:		pkgconfig(dbus-python)
BuildRequires:		pkgconfig(pyside6)
BuildRequires:		pkgconfig(python)
BuildArch:		noarch

%description
WhatsApp desktop application for Linux.
Key features:
- WhatsApp Web in a native PyQt6 desktop window.
- Multiple account profiles with isolated web sessions.
- System tray integration and desktop notifications.
- Light, dark and system theme handling.
- Custom CSS and JavaScript injection, globally or per account.
- Spell checking through QtWebEngine dictionaries.
- Download handling with configurable download behavior.

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}-%{version}.dist-info
%{_datadir}/applications/com.rtosta.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.rtosta.%{name}.svg
%{_metainfodir}/com.rtosta.%{name}.appdata.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

# Fix shebangs
sed -i "s|!/usr/bin/env python|!%{_bindir}/python3|" *.py


%build
%py_build


%install
%py_install

# Install provided icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp -R share/icons/com.rtosta.%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# Install provided desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir="%{buildroot}%{_datadir}/applications/" share/applications/com.rtosta.%{name}.desktop 

# Install provided metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -m 0644 share/metainfo/com.rtosta.%{name}.appdata.xml %{buildroot}%{_metainfodir}/
