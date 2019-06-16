Name:           hello
Version:	0.1        
Release:        1%{?dist}
Summary:        example python3 hello package 

License:       GPLv3+        
URL:           https://example.com/%{name} 
Source0:       https://example.com/%{name}/release/%{name}-%{version}.tar.gz  

BuildRequires: python  
Requires:      python bash 
BuildArch:     noarch

%description
The long-tail description for our Hello World Example implemented in
Python.


%prep
%setup -q


%build

python3 -m compileall %{name}.py


%install
rm -rf $RPM_BUILD_ROOT


mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}
cat > %{buildroot}/%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/



%files
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*
%doc



%changelog
