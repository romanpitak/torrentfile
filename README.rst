Torrent file parser
===================

Simple library to parse `.torrent` files and extract data.

Usage
-----

.. code:: python

    import torrentfile
    torrentfile = TorrentFile('./path/to/some.torrent')
    pprint.pprint(torrentfile.parse(), compact=True, width=120)


Notes
-----

- code suggestions welcome
