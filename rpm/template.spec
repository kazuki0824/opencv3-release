Name:           ros-kinetic-opencv3
Version:        3.3.1
Release:        4%{?dist}
Summary:        ROS opencv3 package

Group:          Development/Libraries
License:        BSD
URL:            http://opencv.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       libwebp-devel
Requires:       numpy
Requires:       protobuf
Requires:       python-devel
Requires:       ros-kinetic-catkin
Requires:       vtk-qt
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  ffmpeg-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff
BuildRequires:  libv4l-devel
BuildRequires:  libwebp-devel
BuildRequires:  numpy
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  python-devel
BuildRequires:  vtk-qt
BuildRequires:  zlib-devel

%description
OpenCV 3.x

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Mar 14 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-4
- Autogenerated by Bloom

* Fri Feb 23 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-3
- Autogenerated by Bloom

* Fri Feb 23 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-2
- Autogenerated by Bloom

* Sun Jan 14 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-1
- Autogenerated by Bloom

* Wed Nov 01 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.3.1-0
- Autogenerated by Bloom

* Mon Jun 05 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-5
- Autogenerated by Bloom

* Wed Mar 15 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-4
- Autogenerated by Bloom

* Tue Mar 14 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-3
- Autogenerated by Bloom

* Mon Feb 27 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-2
- Autogenerated by Bloom

* Sun Feb 26 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-1
- Autogenerated by Bloom

* Sun Jan 29 2017 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.2.0-0
- Autogenerated by Bloom

* Sun Dec 04 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-18
- Autogenerated by Bloom

* Sun Dec 04 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-17
- Autogenerated by Bloom

* Sun Jul 24 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-16
- Autogenerated by Bloom

* Sun Jul 24 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-15
- Autogenerated by Bloom

* Tue May 31 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-14
- Autogenerated by Bloom

* Tue May 10 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-13
- Autogenerated by Bloom

* Fri Apr 22 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-12
- Autogenerated by Bloom

* Sat Apr 16 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-11
- Autogenerated by Bloom

* Thu Apr 14 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-10
- Autogenerated by Bloom

* Thu Apr 07 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-9
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-8
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-7
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-6
- Autogenerated by Bloom

* Thu Mar 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-3
- Autogenerated by Bloom

* Thu Mar 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-2
- Autogenerated by Bloom

