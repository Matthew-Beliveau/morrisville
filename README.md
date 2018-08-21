# Morrisville

This is an ansible playbook for setting up a minimal Keycloak server that is integrated with FreeIPA.


## How to use:

```shell
cd $YOURPATH/morrisville

ansible-playbook -i $YOURINVENTORYPATH /playbooks/ipa.yml

ansible-playbook -i $YOURINVENTORYPATH /playbooks/keycloak.yml
```

To ensure that it runs correctly go into the playbooks and change the remote_user to suit your needs. You also need to go into /roles/ipaclient/defaults/main.yml and change the IPA server address to the ipv4 address of your IPA VM.

After running these commands you should have a keycloak server and an ipa server. To be able to view your webservers on your local machine be sure to edit your /etc/hosts
with this format : `ipa.keycloak.test $IP`

An example inventory file looks like this:

```
[ipa]
192.168.100.195

[keycloak]
192.168.100.210
```

Also if yum breaks the play book, switch all the yum's to dnf or vice versa.
