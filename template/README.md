# OpenFaaS template based on Clear Linux

## How to use the template

Assume you already had deployed workable OpenFaaS on top of Kubernetes.

Steps could refer to

[deployment-guide-for-kubernetes](https://docs.openfaas.com/deployment/kubernetes/#deployment-guide-for-kubernetes)

[OpenFaaS workshop](https://github.com/openfaas/workshop)

### python3-clearlinux
1.  mkdir test && cd test
2.  `git clone https://gitlab.devtools.intel.com/zhengq/clearlinux-openfaas-template.git template`
3.  `faas-cli new --lang python3-clearlinux hello-openfaas --prefix="<your-docker-username-here>"`

    Files tree as below.
>  
    ├── hello-openfaas
    │   ├── bundles.txt
    │   ├── handler.py
    │   ├── helper_script.sh
    │   ├── __init__.py
    │   └── requirements.txt
    ├── hello-openfaas.yml
    └── template

    *  Put the required python packages in the "requirements.txt".
    For example,

    `echo "redis" >> hello-openfaas/requirements.txt`
    `echo "flask" >> hello-openfaas/requirements.txt`
    *  Put the required Clear Linux bundles in the "bundles.txt".
    For example,

    `echo "openblas" >> hello-openfaas/bundles.txt`
    `echo "wget" >> hello-openfaas/bundles.txt`

    *  Put any initial/helper operation in the "help_script.sh"

4.  `faas-cli up -f hello-openfaas.yml`

    Then you can invoke your python function by OpenFaas UI or faas-cli.
    
### go-clearlinux
1.  mkdir test && cd test
2.  `git clone https://gitlab.devtools.intel.com/cle-dns/clearlinux-openfaas-template.git template`
3.  `faas-cli new --lang go-clearlinux go-openfaas --prefix="<your-docker-username-here>"`

    Files tree as below.
>  
    ├── go-openfaas
    │   ├── handler.go
    ├── go-openfaas.yml
    └── template


    *  Put the required Clear Linux bundles in the "bundles.txt".
    For example,

    `echo "openblas" >> go-openfaas/bundles.txt`
    `echo "wget" >> go-openfaas/bundles.txt`
4.  `faas-cli up -f go-openfaas.yml`

    Then you can invoke your go function by OpenFaas UI or faas-cli.

    
## Proxy and Clear Linux mirror

When working behind a Proxy, you can pass proxy settings to faas-cli commands by "--build-arg".

Also to speed up the Clear Linux bundle install, you could use mirror if you are inside Intel.

For example, 

`faas-cli up --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy --build-arg swupd_args="-u http://linux-ftp.sh.intel.com/pub/mirrors/clearlinux/update/ --allow-insecure-http" -f hello-openfaas.yml`