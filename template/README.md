# OpenFaaS template based on Clear Linux

## How to use the template

Assume you already had deployed workable OpenFaaS on top of Kubernetes.

Steps could refer to

[deployment-guide-for-kubernetes](https://docs.openfaas.com/deployment/kubernetes/#deployment-guide-for-kubernetes)

[OpenFaaS workshop](https://github.com/openfaas/workshop)

### how to get template
`faas-cli template pull https://github.com/qzheng527/clr-openfaas`

### templates how-to

[dockerfile-clearlinux](./dockerfile-clearlinux/README.md)

[go-clearlinux](./go-clearlinux/README.md)

[node-clearlinux](./node-clearlinux/README.md)

[numpy-mp](./numpy-mp/README.md)

[python3-clearlinux](./python3-clearlinux/README.md)

    
## Proxy and Clear Linux mirror

When working behind a Proxy, you can pass proxy settings to faas-cli commands by "--build-arg".

Also to speed up the Clear Linux bundle install, you could use mirror if you are inside Intel.

For example, 

`faas-cli up --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy --build-arg swupd_args="-u http://linux-ftp.sh.intel.com/pub/mirrors/clearlinux/update/ --allow-insecure-http" -f hello-openfaas.yml`
