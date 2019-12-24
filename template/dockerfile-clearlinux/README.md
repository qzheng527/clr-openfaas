Based on clearlinux:base image

### dockerfile-clearlinux
1.  mkdir test && cd test
2.  `faas-cli template pull https://github.com/qzheng527/clr-openfaas`
3.  `faas-cli new --lang dockerfile-clearlinux hello-openfaas --prefix="<your-docker-username-here>"`

    Files tree as below.
>
    ├── hello-openfaas
    │   ├── bundles.txt
    │   └── Dockerfile
    ├── hello-openfaas.yml
    └── template

    *  Put the required Clear Linux bundles in the "bundles.txt".
    For example,

    `echo "openblas" >> hello-openfaas/bundles.txt`
    `echo "wget" >> hello-openfaas/bundles.txt`

4.  `faas-cli up -f hello-openfaas.yml`

    Then you can invoke your python function by OpenFaas UI or faas-cli.

