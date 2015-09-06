"""
TorrentFile module
"""
__author__ = "Roman Piták <roman@pitak.net>"
__version__ = "$Revision$"


class TorrentFile:
    """TorrentFile class."""

    def __init__(self, data: bytes):
        self.__data = data

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
        return cls(data)

    def parse(self):
        """Runs the parser

        Returns:
            dict
        """
        return bdecode(self.__data)


def bdecode(data: bytes, index: int = 0):
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
        return ''.join([chr(next_()) for __ in range(length)])

    def read_int():
        assert_next('i')
        result = ''
        while not_('e'):
            result += chr(next_())
        assert_next('e')
        assert result.isdigit(), result
        return int(result)

    def read_list():
        assert_next('l')
        result = []
        while not_('e'):
            result.append(read_next())
        assert_next('e')
        return result

    def read_dictionary():
        assert_next('d')
        result = {}
        while not_('e'):
            key = read_next()
            assert isinstance(key, str), key
            value = read_next()
            if 'pieces' == key:  # TODO deal with the pieces
                    value = None
            result[key] = value
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
            return read_dictionary()
        else:
            raise Exception(c)

    return read_next()

