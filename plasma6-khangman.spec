%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Classical hangman game
Name:		plasma6-khangman
Version:	24.01.90
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/khangman
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/khangman-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)

Obsoletes:		%{mklibname khangmanengine 4} < 16.04.2
Obsoletes:		khangman-devel  < 16.04.2

%description
KHangman is the classical hangman game. The child should guess a word
letter by letter. At each miss, the picture of a hangman appears. After
10 tries, if the word is not guessed, the game is over and the answer
is displayed.

%files -f khangman.lang
%doc COPYING COPYING.DOC README
%{_bindir}/khangman
%{_datadir}/applications/org.kde.khangman.desktop
%{_datadir}/config.kcfg/khangman.kcfg
%{_iconsdir}/hicolor/*/apps/*.*[gz]
%{_datadir}/khangman
%{_mandir}/man6/khangman.6.*
%{_datadir}/metainfo/*.xml
%{_datadir}/knsrcfiles/khangman.knsrc

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n khangman-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang khangman --with-html --with-man
