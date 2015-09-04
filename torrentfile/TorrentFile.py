# -*- coding: utf-8 -*-


class TorrentFile:

    def __init__(self, file_name):
        with open(file_name, 'rb') as file_handle:
            data = file_handle.read()

        self.__index = 0
        self.__data = data
        self.__data_length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__valid_index():
            raise StopIteration()
        index = self.__index
        self.__index += 1
        return self.__data[index]

    def parse(self):
        result = self.__read_next()
        self.__index = 0
        return result

    #
    # Private
    #

    # helpers

    def __valid_index(self, index=None):
        if not index:
            index = self.__index
        return index < self.__data_length

    def __assert_next(self, value):
        c = chr(next(self))
        assert value == c, (value, c)

    def __not(self, value):
        return self.__valid_index() and value != chr(self.__data[self.__index])

    # parsers

    def __read_string(self):
        length_string = ''
        while self.__valid_index() and chr(self.__data[self.__index]).isdigit():
            length_string += chr(next(self))
        assert length_string.isdigit(), length_string
        length = int(length_string)
        assert length >= 0, length
        self.__assert_next(':')
        return ''.join([chr(next(self)) for __ in range(length)])

    def __read_int(self):
        self.__assert_next('i')
        result = ''
        while self.__not('e'):
            result += chr(next(self))
        self.__assert_next('e')
        assert result.isdigit(), result
        return int(result)

    def __read_list(self):
        self.__assert_next('l')
        result = []
        while self.__not('e'):
            result.append(self.__read_next())
        self.__assert_next('e')
        return result

    def __read_dictionary(self):
        self.__assert_next('d')
        result = {}
        while self.__not('e'):
            key = self.__read_next()
            assert isinstance(key, str), key
            value = self.__read_next()
            if 'pieces' == key:  # TODO deal with the pieces
                    value = None
            result[key] = value
        self.__assert_next('e')
        return result

    def __read_next(self):
        if not self.__valid_index():
            return None  # TODO raise here?
        c = chr(self.__data[self.__index])
        if c.isdigit():
            return self.__read_string()
        elif 'l' == c:
            return self.__read_list()
        elif 'i' == c:
            return self.__read_int()
        elif 'd' == c:
            return self.__read_dictionary()
        else:
            raise Exception(c)
