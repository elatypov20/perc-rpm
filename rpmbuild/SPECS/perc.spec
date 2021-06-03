Summary:        Tool for scanning directories for accessible files
Name:           perc
Version:        0.1.0
Release:        0
License:        GPL
URL:            https://github.com/elatypov20/perc
Group:          File tools
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      x86_64
#BuildArch: 	armv7hl

Requires: 	gcc

%description
perc is a tool for recursively detecting to which files user and group can write in some path.

%prep
rm -rf %{_topdir}/BUILD/*

%setup -q

%build
make

%install
sudo cp bin/perc /usr/bin/perc
