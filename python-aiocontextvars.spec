# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-aiocontextvars
Epoch: 100
Version: 0.2.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Asyncio support for PEP-567 contextvars backport
License: BSD-3-Clause
URL: https://github.com/fantix/aiocontextvars/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-contextvars >= 2.4
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
IMPORTANT: This package will be deprecated after contextvars asyncio
backport is fixed. Before then, this library experimentally provides the
missing asyncio support for the contextvars backport library. Please
read more in Python 3.7 contextvars documentation.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aiocontextvars
Summary: Asyncio support for PEP-567 contextvars backport
Requires: python3
Requires: python3-contextvars >= 2.4
Provides: python3-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python3dist(aiocontextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiocontextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiocontextvars) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-aiocontextvars
IMPORTANT: This package will be deprecated after contextvars asyncio
backport is fixed. Before then, this library experimentally provides the
missing asyncio support for the contextvars backport library. Please
read more in Python 3.7 contextvars documentation.

%files -n python%{python3_version_nodots}-aiocontextvars
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-aiocontextvars
Summary: Asyncio support for PEP-567 contextvars backport
Requires: python3
Requires: python3-contextvars >= 2.4
Provides: python3-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python3dist(aiocontextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiocontextvars) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiocontextvars = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiocontextvars) = %{epoch}:%{version}-%{release}

%description -n python3-aiocontextvars
IMPORTANT: This package will be deprecated after contextvars asyncio
backport is fixed. Before then, this library experimentally provides the
missing asyncio support for the contextvars backport library. Please
read more in Python 3.7 contextvars documentation.

%files -n python3-aiocontextvars
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
