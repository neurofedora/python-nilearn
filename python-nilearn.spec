%global modname nilearn
%global commit 78f1cb0cf6c929a540cc5f90e5ea052caa47383a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        0.1.5
Release:        0.dev.2git%{shortcommit}%{?dist}
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

License:        BSD
URL:            http://nilearn.github.io/
Source0:        https://github.com/nilearn/nilearn/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Nilearn is a Python module for fast and easy statistical learning on
NeuroImaging data.

It leverages the scikit-learn Python toolbox for multivariate statistics with
applications such as predictive modelling, classification, decoding, or
connectivity analysis.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python-setuptools
BuildRequires:  numpy scipy python-scikit-learn python2-nibabel
BuildRequires:  python-sphinx
# Test deps
BuildRequires:  python-nose
BuildRequires:  python-matplotlib
Requires:       numpy scipy python-scikit-learn python2-nibabel
# For plotting functionality and examples
Recommends:     python-matplotlib
Suggests:       ipython

%description -n python2-%{modname}
Nilearn is a Python module for fast and easy statistical learning on
NeuroImaging data.

It leverages the scikit-learn Python toolbox for multivariate statistics with
applications such as predictive modelling, classification, decoding, or
connectivity analysis.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-numpy python3-scipy python3-scikit-learn python3-nibabel
BuildRequires:  python3-sphinx
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-matplotlib
Requires:       python3-numpy python3-scipy python3-scikit-learn python3-nibabel
# For plotting functionality and examples
Recommends:     python3-matplotlib
Suggests:       python3-ipython

%description -n python3-%{modname}
Nilearn is a Python module for fast and easy statistical learning on
NeuroImaging data.

It leverages the scikit-learn Python toolbox for multivariate statistics with
applications such as predictive modelling, classification, decoding, or
connectivity analysis.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
export LC_ALL="en_US.UTF-8"
%py2_build
%py3_build

%install
export LC_ALL="en_US.UTF-8"
%py2_install
%py3_install

%check
export LC_ALL="en_US.UTF-8"
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%doc README.rst examples
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/%{modname}*

%changelog
* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.2git78f1cb0
- 78f1cb0

* Tue Nov 03 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.1git1f14723
- Enable python3 support

* Mon Nov 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.0git1f14723
- Initial package
