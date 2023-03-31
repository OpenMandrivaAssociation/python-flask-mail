# Created by pyp2rpm-3.3.5
%global pypi_name Flask-Mail
%global om_name flask-mail

Name:           python-%{om_name}
Version:        0.9.1
Release:        2
Summary:        Flask extension for sending email
Group:          Development/Python
License:        BSD
URL:            https://github.com/rduplain/flask-mail
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(blinker)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(speaklater)
BuildRequires:  python3dist(sphinx)

%description
Flask-Mail -A Flask extension for sending email messages.Please refer to the
online documentation for details.Links * documentation <
%package -n python-%{om_name}-doc
Summary:        Flask-Mail documentation
%description -n python-%{om_name}-doc
Documentation for Flask-Mail

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{om_name}
%license docs/_themes/LICENSE LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flask_mail.py
%{python3_sitelib}/Flask_Mail-%{version}-py%{python3_version}.egg-info

%files -n python-%{om_name}-doc
%doc html
%license docs/_themes/LICENSE LICENSE
