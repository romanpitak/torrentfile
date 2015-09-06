# -*- coding: utf-8 -*-

import pprint
from torrentfile import TorrentFile


# t = TorrentFile('./data/lm.torrent')
t = TorrentFile.load('./data/t.torrent')

pprint.pprint(t, compact=True, width=120)

t.save('./data/out.torrent')

pprint.pprint(TorrentFile.load('./data/out.torrent'), compact=True, width=120)
