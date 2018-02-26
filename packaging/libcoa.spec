Name:           libcoa
Version:        v0.5.0
Release:        0
License:        MIT
Url:            https://github.com/OAID/CaffeOnACL
Summary:        Caffe Machine Learning library on ARM Compute Library 
Group:          Machine Learning Framework/Libraries
Source0:        %{name}-%{version}.tar.bz2
Source1001:	%name.manifest
ExclusiveArch:	%{arm} aarch64

BuildRequires:	python-devel	
BuildRequires:	python-numpy-devel
BuildRequires:	protobuf-devel
BuildRequires:  boost-devel	
BuildRequires:  gflags-devel	
BuildRequires:  glog-devel	
BuildRequires:  libdlog
BuildRequires:  cblas-devel	
BuildRequires:  hdf5-devel	
BuildRequires:  opencv-devel	
BuildRequires:  lmdb-devel	
BuildRequires:  leveldb-devel	
BuildRequires:  snappy-devel	
BuildRequires:  openblas-devel 
BuildRequires:  libarmcl-devel
BuildRequires:	opengl-es-mali-midgard 
BuildRequires:	python-PyYAML 

%description
CaffeOnACL is a project that is maintained by OPEN AI LAB, it uses Arm Compute Library (NEON+GPU) to speed up Caffe and provide utilities to debug, profile and tune application performance.

%ifarch aarch64
%package -n %{name}-release-aarch64
%else
%package -n %{name}-release
%endif
Summary:        CaffeOnACL Library

%ifarch aarch64
%description -n %{name}-release-aarch64
%else
%description -n %{name}-release
%endif
Summary:        CaffeOnACL Library

%ifarch aarch64
%package -n %{name}-devel-aarch64
%else
%package -n %{name}-devel
%endif
Summary:        Userspace interface and Library to CaffeOnACL

%ifarch aarch64
%description -n %{name}-devel-aarch64
%else
%description -n %{name}-devel
%endif
Summary:        Userspace interface and Library to CaffeOnACL

%ifarch aarch64
%package -n %{name}-tools-aarch64
%else
%package -n %{name}-tools
%endif
Summary:	Sample application and libraries for CaffeOnACL

%ifarch aarch64
%description -n %{name}-tools-aarch64
%else
%description -n %{name}-tools
%endif
Summary:	Sample application and libraries for CaffeOnACL

%prep
%setup -q
cp %{SOURCE1001} .

%build
make proto
make all -j 5

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%install
make distribute

mkdir -p %{buildroot}%{_libdir}/distribute

cp -r %{_builddir}/%{name}-%{version}/distribute/* %{buildroot}%{_libdir}/distribute/

%ifarch aarch64
%files -n %{name}-release-aarch64
%else
%files -n %{name}-release
%endif
%manifest %{name}.manifest
%{_libdir}/distribute/lib/*

%ifarch aarch64
%files -n %{name}-devel-aarch64
%else
%files -n %{name}-devel
%endif
%manifest %{name}.manifest
%{_libdir}/distribute/lib/*
%{_libdir}/distribute/include/*

%ifarch aarch64
%files -n %{name}-tools-aarch64
%else
%files -n %{name}-tools
%endif
%manifest %{name}.manifest
%{_libdir}/distribute/bin/*
%{_libdir}/distribute/proto/*
%{_libdir}/distribute/python/*

