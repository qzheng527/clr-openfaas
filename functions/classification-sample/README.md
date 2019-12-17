# Classification sample function

Using Clear Linux* OS based OpenFaaS template python3-clearlinux to implement
a sample OpenVino picture classification function.

## build
`$ faas-cli build -f stack.yml`

## deploy
`$ faas-cli deploy --env=http_proxy=$http_proxy --env=https_proxy=$https_proxy -f stack.yml`

## use
`$ echo -n "bmp picture url" | faas-cli invoke classification-sample`

Or use OpenFaaS web UI to invoke.

