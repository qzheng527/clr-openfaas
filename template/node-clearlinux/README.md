Based on clearlinux/node:12 container image.

### node-clearlinux
1.  mkdir test && cd test
2.  `faas-cli template pull https://github.com/qzheng527/clr-openfaas`
3.  `faas-cli new --lang dockerfile-clearlinux hello-openfaas --prefix="<your-docker-username-here>"`

    Files tree as below.
>
    ├── hello-openfaas
    │   ├── handler.js
    │   └── package.json
    ├── hello-openfaas.yml
    └── template


    *  The entry is "handler.js", do any change you want in this file.


4.  `faas-cli up -f hello-openfaas.yml`

    Then you can invoke your python function by OpenFaas UI or faas-cli.

