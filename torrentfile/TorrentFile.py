"""
TorrentFile module
"""
__author__ = "Roman Piták <roman@pitak.net>"
__version__ = "$Revision$"


class String(str):

    def bencode(self):
        return '{}:{}'.format(len(self), self)


class Int(int):

    def bencode(self):
        return 'i{}e'.format(self)


class List(list):

    def bencode(self):
        content = ''.join([item.bencode() for item in self])
        return 'l{}e'.format(content)


class Pieces(String):

    def __init__(self, data: String):
        super().__init__()
        self.data = [data[x:x+20] for x in range(0, len(data), 20)]

    def __repr__(self):
        return 'PIECES...'


class Dict(dict):

    def __setitem__(self, key, value):
        if 'pieces' == key and not isinstance(value, Pieces):
            value = Pieces(value)
        super().__setitem__(key, value)

    def bencode(self) -> str:
        """bencode the object

        Represents the object as a string adhering to the specification
        provided in The BitTorrent Protocol Specification
        http://www.bittorrent.org/beps/bep_0003.html#bencoding

        Returns:
            str
        """
        content = ''.join([
            key.bencode() + self[key].bencode()
            for key in sorted(self.keys())  # TODO verify sorting
        ])
        return 'd{}e'.format(content)


class TorrentFile(Dict):
    """TorrentFile class."""

    def __init__(self, data: dict = None):
        super().__init__()
        if not data:
            data = {}
        self.update(data)

    @classmethod
    def load(cls, file_name: str):
        """Load .torrent file.

        Args:
            file_name (str): Torrent file name
        Returns:
            TorrentFile
        """
        with open(file_name, 'rb') as file_handle:
            data = file_handle.read()
        return cls(bdecode(data))


def bdecode(data: bytes):
    """bencode format parser

    Parses a binary string according to the specification provided in
    The BitTorrent Protocol Specification
    http://www.bittorrent.org/beps/bep_0003.html#bencoding

    Args:
        data (bytes): .torrent file contents
    Returns:
        dict
    """
    index = 0
    data_length = len(data)

    def valid_index():
        return index < data_length

    def next_():
        nonlocal index
        if not valid_index():
            raise Exception('EOF')
        return_index = index
        index += 1
        return data[return_index]

    def assert_next(value):
        c = chr(next_())
        assert value == c, (value, c)

    def not_(value):
        return valid_index() and value != chr(data[index])

    def read_string():
        length_string = ''
        while valid_index() and chr(data[index]).isdigit():
            length_string += chr(next_())
        assert length_string.isdigit(), length_string
        length = int(length_string)
        assert length >= 0, length
        assert_next(':')
        return String(''.join([chr(next_()) for __ in range(length)]))

    def read_int():
        assert_next('i')
        result = ''
        while not_('e'):
            result += chr(next_())
        assert_next('e')
        assert result.isdigit(), result
        return Int(int(result))

    def read_list():
        assert_next('l')
        result = List()
        while not_('e'):
            result.append(read_next())
        assert_next('e')
        return result

    def read_dict():
        assert_next('d')
        result = Dict()
        while not_('e'):
            key = read_next()
            assert isinstance(key, String), key
            result[key] = read_next()
        assert_next('e')
        return result

    def read_next():
        if not valid_index():
            return None  # TODO raise here?
        c = chr(data[index])
        if c.isdigit():
            return read_string()
        elif 'l' == c:
            return read_list()
        elif 'i' == c:
            return read_int()
        elif 'd' == c:
            return read_dict()
        else:
            raise Exception(c)

    return read_next()
