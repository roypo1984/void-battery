import json
import collections

with open('out/extracted/Words.tc.json') as file:
    data = json.load(file)

words = {}

for m in data[0]['data']:
    words[m[-2].strip()] = m[1].strip()


with open('out/release/words.json', 'wt') as file:
    json.dump(words, file, ensure_ascii=False, indent=0, sort_keys=True)


with open('out/extracted/BaseItemTypes.tc.json') as file:
    data = json.load(file)
z = [m[4].strip() for m in data[0]['data']]


with open('out/extracted/BaseItemTypes.en.json') as file:
    data = json.load(file)
e = [m[4].strip() for m in data[0]['data']]


ze = collections.defaultdict(list)
for k, v in zip(z, e):
    ze[k].append(v)

for k, v in ze.items():
    v = set(v)
    if len(v) > 1:
        print(f'WARNING: {k} has multiple mathces: {v}')


# XXX Overrides
ze['龍骨細劍'] = ['Dragonbone Rapier']
ze['鏽劍'] = ['Rusted Sword']


with open('out/release/bases.json', 'wt') as file:
    json.dump({k: v[0] for (k, v) in ze.items()}, file, ensure_ascii=False, indent=0, sort_keys=True)
