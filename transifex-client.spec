Name:           transifex-client
Version:        0.8
Release:        2
Summary:        Command line client for transifex 
Group:          Networking/WWW
License:        BSD
URL:            http://www.transifex.org/
Source0:        %{name}-%{version}.tar.gz
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
python setup.py install --root=%{buildroot}

%clean

%files
%_bindir/tx
%py_puresitedir/*


%changelog
* Wed May 04 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0.4.1-1
+ Revision: 667186
- new version 0.4.1

* Thu Dec 16 2010 Michael Scherer <misc@mandriva.org> 0.3-1mdv2011.0
+ Revision: 622195
- import transifex-client

