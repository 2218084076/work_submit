import yaml

urls = []
for i in range(1, 281):
    url = 'https://proxy.mimvp.com/freeopen?proxy=out_hp&sort=p_ip&page=%s' % i
    urls.append(url)

adict = {
    'name': 'mimvp',
    'urls': urls,
    'allowed_domains': 'mimvp.org'
}

ayml = yaml.dump(adict)

print(ayml)

with open("setting.yml", "w") as f:
    yaml.dump(adict, f)
