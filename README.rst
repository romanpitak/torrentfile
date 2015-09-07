Torrent file parser
===================

Simple library to parse `.torrent` files and extract data.

Usage
-----

.. code:: python

    t = TorrentFile.load('./path/to/some.torrent')
    print(t)

.. code:: text

    {'announce': 'http://bt1.archive.org:6969/announce',
     'announce-list': [['http://bt1.archive.org:6969/announce'], ['http://bt2.archive.org:6969/announce']],
     'comment': 'This content hosted at the Internet Archive at '
                'https://archive.org/details/Plan_9_from_Outer_Space_1959\n'
                'Files may have changed, which prevents torrents from downloading correctly or completely; please check '
                'for an updated torrent at '
                'https://archive.org/download/Plan_9_from_Outer_Space_1959/Plan_9_from_Outer_Space_1959_archive.torrent\n'
                'Note: retrieval usually requires a client that supports webseeding (GetRight style).\n'
                "Note: many Internet Archive torrents contain a 'pad file' directory. This directory and the files "
                'within it may be erased once retrieval completes.\n'
                "Note: the file Plan_9_from_Outer_Space_1959_meta.xml contains metadata about this torrent's contents.",
     'created by': 'ia_make_torrent',
     'creation date': 1434738500,
     'info': {'collections': ['org.archive.Plan_9_from_Outer_Space_1959'],
              'files': [{'crc32': '48ead77e',
                         'length': 346429,
                         'md5': '4289512bc7655cfc1d476c742fbaebf7',
                         'mtime': '1262704177',
                         'path': ['Plan_9_from_Outer_Space_1959.gif'],
                         'sha1': '5e02f9c487adb19eee27dfcd4edb57d38857d2ac'},
                        {'crc32': 'a610ba01',
                         'length': 758756235,
                         'md5': '22605836592fd8508ae3b9c4ab3e79b5',
                         'mtime': '1262702416',
                         'path': ['Plan_9_from_Outer_Space_1959.mp4'],
                         'sha1': '6253ee921b1fc0d668dcb13cecfda4352c9c0dd7'},
                        {'crc32': 'eed8e76b',
                         'length': 390383680,
                         'md5': 'cdc5fab4910ea060f4083fc74f844947',
                         'mtime': '1262710584',
                         'path': ['Plan_9_from_Outer_Space_1959.ogv'],
                         'sha1': 'f833a704914bfc332a4422533cddafb5cfb23816'},
                        {'crc32': '337324a7',
                         'length': 293299508,
                         'md5': 'e01e8372d313e06ba2a77d0e5653286d',
                         'mtime': '1262708459',
                         'path': ['Plan_9_from_Outer_Space_1959_512kb.mp4'],
                         'sha1': '6d09c0276ea4841de3627cfc2427cdb2487c83aa'},
                        {'crc32': '6973eef1',
                         'length': 4595,
                         'md5': 'dca8ef049842d13d3a355e3c9f694acf',
                         'mtime': '1318937791',
                         'path': ['Plan_9_from_Outer_Space_1959_meta.xml'],
                         'sha1': '7c7d46004ecdfbe94f81c990759a98f8977a7c2d'}],
              'name': 'Plan_9_from_Outer_Space_1959',
              'piece length': 1048576,
              'pieces': PIECES...},
     'locale': 'en',
     'title': 'Plan_9_from_Outer_Space_1959',
     'url-list': ['https://archive.org/download/', 'http://ia600401.us.archive.org/19/items/',
                  'http://ia700401.us.archive.org/19/items/']}

Notes
-----

- code suggestions welcome
