# -*- coding: utf-8 -*-

import pprint
from torrentfile import TorrentFile


# t = TorrentFile('./data/lm.torrent')
t = TorrentFile.load('./data/t.torrent')

pprint.pprint(t, compact=True, width=120)
