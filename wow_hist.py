import re
from lxml.etree import ElementTree
import numpy as np
import matplotlib

matplotlib.use('AGG')

from matplotlib import pyplot as plt

#tree = ElementTree(file='WoWWiki-20170418203257.xml')
tree = ElementTree(file='wowwiki_pages_current.xml')
root = tree.getroot()

ns = {'mw': 'http://www.mediawiki.org/xml/export-0.6/'}

pagetexts = root.xpath('//mw:page/mw:revision/mw:text', namespaces=ns)

# names = []
# healths = []
# for p in pagetexts:
#     name = re.search('name ?= ?([^|]+)', p.text)
#     health = re.search('health = ([\d,]+)', p.text)
# 
#     if name and health:
#         names.append(name.group(1))
#         healths.append(int(health.group(1).replace(',', '')))

# h = np.log10(healths)
# plt.figure(facecolor='white')
# bins = list(range(int(h.max())+1))
# plt.hist(h, bins=bins)
# plt.xlabel('log10(HP)')
# plt.xticks(bins[::2])
# plt.title('Number of hitpoints of "Level ??"\nNPCs from World of Warcraft')
# plt.tight_layout()
# plt.savefig('hist.png')
