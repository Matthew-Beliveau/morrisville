#!/bin/env python
from lxml import etree as etree
from xml.etree import ElementTree as ET

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse('/usr/local/keycloak/keycloak-3.4.3.Final/standalone/configuration/standalone.xml', parser)
root = tree.getroot()

security_realms = root.find('./{urn:jboss:domain:5.0}management/{urn:jboss:domain:5.0}security-realms')

security_realm = etree.Element('security-realm')
security_realm.set('name', 'UndertowRealm')

server_identities = etree.Element('sever-identites')

ssl = etree.Element('ssl')

keystore = etree.Element('keystore')
keystore.set('path', 'keycloak.jks')
keystore.set('relative-to', 'jboss.server.config.dir')
keystore.set('keystore-password', 'PASSWORD')

ssl.insert(0, keystore)
server_identities.insert(0, ssl)
security_realm.insert(0, server_identities)

security_realms.insert(0, security_realm)

attribute = root.find('./{urn:jboss:domain:5.0}profile/{urn:jboss:domain:undertow:4.0}subsystem/'
                         '{urn:jboss:domain:undertow:4.0}server/{urn:jboss:domain:undertow:4.0}https-listener')

attribute.set('security-realm', 'UndertowRealm')

attribute2 = root.find('./{urn:jboss:domain:5.0}profile/{urn:jboss:domain:undertow:4.0}subsystem/'
                         '{urn:jboss:domain:undertow:4.0}server/{urn:jboss:domain:undertow:4.0}host/'
                         '{urn:jboss:domain:undertow:4.0}http-invoker')

attribute2.set('security-realm', 'UndertowRealm')
tree.write('test.xml', encoding='UTF-8', pretty_print=True)
