%define module flask-mail
%define oname flask_mail
%bcond doc 1
%bcond tests 1

Name:		python-flask-mail
Version:	0.10.0
Release:	1
Summary:	Flask extension for sending email
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/pallets-eco/flask-mail
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with doc}
BuildRequires:  python%{pyver}dist(furo)
BuildRequires:  python%{pyver}dist(myst-parser)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinxcontrib-log-cabinet)
%endif
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(flask)
%endif

%description
Flask-Mail -A Flask extension for sending email messages.Please refer to the
online documentation for details.Links * documentation <

%if %{with doc}
%package doc
Summary:	Documentation for %{name}
%description doc
Documentation for %{name}.
%endif

%if %{with doc}
%install -a
# Use sphinx-build to build html docs into buildroot docdir,
# Doc generation requires the module to be installed in order to run successfully.
PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}" \
    sphinx-build -b html docs %{buildroot}%{_docdir}/%{name}-doc/html
# remove .buildinfo and .doctrees
rm -rf %{buildroot}%{_docdir}/%{name}-doc/html/{.buildinfo,.doctrees}
%endif

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# Skip broken tests - https://github.com/pallets-eco/flask-mail/issues/233
skiptests+="not test_unicode_sender and not test_unicode_sender_tuple"
pytest -k "$skiptests"
%endif

%files
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}.dist-info

%if %{with doc}
%files doc
%doc docs/_build/html CHANGES.md README.md
%license LICENSE.txt
%endif
