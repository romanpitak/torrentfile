Torrent file parser
===================

Simple library to parse `.torrent` files and extract data.

Usage
-----

.. code:: python

    torrent_data = TorrentFile('./path/to/some.torrent').parse()
    pprint(torrent_data, compact=True, width=120)

Notes
-----

- code suggestions welcome
