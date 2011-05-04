Name:           transifex-client
Version:        0.4.1
Release:        1
Summary:        Command line client for transifex 
Group:          Networking/WWW
License:        BSD
URL:            http://www.transifex.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:  python-devel python-setuptools
BuildArch:      noarch
%description
The Transifex Command-line Client is a command line tool that enables you 
to easily manage your translations within a project without the need of 
an elaborate UI system, by using Transifex hosted services, or your own
instance.

You can use the command line client to easily create new resources, map locale 
files to translations and synchronize your Transifex project with your local 
repository and vice verca. Translators and localization managers can also 
use it to handle large volumes of translation files easily and without much 
hassle.

%prep 
%setup -q

%install 
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%_bindir/tx
%py_puresitedir/*
