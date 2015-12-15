%global modname nilearn

Name:           python-%{modname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

License:        BSD
URL:            http://nilearn.github.io/
Source0:        https://github.com/nilearn/nilearn/archive/%{version}/%{modname}-%{version}.tar.gz

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
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy python2-scipy
Requires:       python2-numpy python2-scipy
%else
BuildRequires:  numpy scipy
Requires:       numpy scipy
%endif
BuildRequires:  python-scikit-learn python2-joblib
BuildRequires:  python2-nibabel
BuildRequires:  python-sphinx
# Test deps
BuildRequires:  python2-nose
BuildRequires:  python-matplotlib
Requires:       python-scikit-learn python2-joblib
Requires:       python2-nibabel
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
BuildRequires:  python3-numpy python3-scipy
BuildRequires:  python3-scikit-learn python3-joblib
BuildRequires:  python3-nibabel
BuildRequires:  python3-sphinx
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-matplotlib
Requires:       python3-numpy python3-scipy
Requires:       python3-scikit-learn python3-joblib
Requires:       python3-nibabel
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
%autosetup -n %{modname}-%{version}

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
%doc README.rst AUTHORS.rst examples
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst AUTHORS.rst examples
%{python3_sitelib}/%{modname}*

%changelog
* Tue Dec 15 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.2git78f1cb0
- 78f1cb0

* Tue Nov 03 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.1git1f14723
- Enable python3 support

* Mon Nov 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1.5-0.dev.0git1f14723
- Initial package
