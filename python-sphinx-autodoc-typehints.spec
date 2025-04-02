# Created by pyp2rpm-3.3.5
%global module sphinx-autodoc-typehints
%global uname sphinx_autodoc_typehints
# tests disabled for abf
%bcond_with test

Name:			python-%{module}
Version:		3.1.0
Release:		1
Summary:		Type hints support for the Sphinx autodoc extension
Group:			Development/Python
License:		MIT
URL:			https://github.com/tox-dev/sphinx-autodoc-typehints/
Source0:		https://files.pythonhosted.org/packages/source/s/%{uname}/%{uname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(hatchling) >= 1.27
BuildRequires:	python%{pyver}dist(hatch-vcs) >= 0.4
Requires:	python%{pyver}dist(sphinx) >= 8.2

%if %{with test}
# for tests
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(sphinx) >= 8.2
BuildRequires:	python%{pyver}dist(sphobjinv) >= 2.3.1.2
BuildRequires:	python%{pyver}dist(typing-extensions) >= 4.12.2
%endif

%description
This extension allows you to use Python 3 annotations for documenting
acceptable argument types and return value types of functions.

See an example of the Sphinx render at the pyproject-api docs.

This allows you to use type hints in a very natural fashion

%prep
%autosetup -n %{uname}-%{version}
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
%{__python3} -m pytest tests/
%endif

%files -n python-%{module}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{uname}
%{python3_sitelib}/%{uname}-%{version}.dist-info
