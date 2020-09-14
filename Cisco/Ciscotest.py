from ncclient import manager

host='192.168.102.254'
with manager.connect(host='192.168.102.254', port=830, username='root',password='hong', hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    print(c)
    with open("%s.xml" % host, 'w') as f:
        f.write(c)