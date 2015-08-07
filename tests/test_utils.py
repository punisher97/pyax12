#!/usr/bin/env python3
# -*- coding : utf-8 -*-

# PyAX-12

# The MIT License
#
# Copyright (c) 2010,2015 Jeremie DECOCK (http://www.jdhp.org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
This module contains some unit tests for the general purpose utility functions
implemented in the "utils" module.
"""

from pyax12 import utils

import unittest

class TestUtils(unittest.TestCase):
    """
    Contains some unit tests for the general purpose utility functions
    implemented in the "utils" module.
    """

    # Check int_to_little_endian_bytes() ######################################

    def test_int_to_little_endian_bytes_type(self):
        """Check that the utils.int_to_little_endian_bytes() function fails
        when the "integer" argument's type is wrong (float)."""

        with self.assertRaises(TypeError):
            utils.int_to_little_endian_bytes(1.0)

        with self.assertRaises(TypeError):
            utils.int_to_little_endian_bytes("hello")

        with self.assertRaises(TypeError):
            utils.int_to_little_endian_bytes((1, ))

        with self.assertRaises(TypeError):
            utils.int_to_little_endian_bytes(bytes((1, )))

        with self.assertRaises(TypeError):
            utils.int_to_little_endian_bytes(bytearray((1, )))


    def test_int_to_little_endian_bytes_value_lo(self):
        """Check that the utils.int_to_little_endian_bytes() function fails
        when the "integer" argument's value is wrong (too low)."""

        with self.assertRaises(ValueError):
            utils.int_to_little_endian_bytes(-1)       # too low


    def test_int_to_little_endian_bytes_value_hi(self):
        """Check that the utils.int_to_little_endian_bytes() function fails
        when the "integer" argument's value is wrong (too high)."""

        with self.assertRaises(ValueError):
            utils.int_to_little_endian_bytes(0xffffff) # too high


    def test_int_to_little_endian_bytes_1(self):
        """Check the returned value of utils.int_to_little_endian_bytes()."""

        hex_tuple = utils.int_to_little_endian_bytes(0)
        expected_tuple = (0x00, 0x00)

        self.assertEqual(hex_tuple, expected_tuple)


    def test_int_to_little_endian_bytes_2(self):
        """Check the returned value of utils.int_to_little_endian_bytes()."""

        hex_tuple = utils.int_to_little_endian_bytes(0xffff)
        expected_tuple = (0xff, 0xff)

        self.assertEqual(hex_tuple, expected_tuple)


    def test_int_to_little_endian_bytes_3(self):
        """Check the returned value of utils.int_to_little_endian_bytes()."""

        hex_tuple = utils.int_to_little_endian_bytes(0x02bc)
        expected_tuple = (0xbc, 0x02)

        self.assertEqual(hex_tuple, expected_tuple)


    def test_int_to_little_endian_bytes_4(self):
        """Check the returned value of utils.int_to_little_endian_bytes()."""

        hex_tuple = utils.int_to_little_endian_bytes(0xbc)
        expected_tuple = (0xbc, 0x00)

        self.assertEqual(hex_tuple, expected_tuple)


    def test_int_to_little_endian_bytes_5(self):
        """Check the returned value of utils.int_to_little_endian_bytes()."""

        hex_tuple = utils.int_to_little_endian_bytes(1)
        expected_tuple = (0x01, 0x00)

        self.assertEqual(hex_tuple, expected_tuple)



    # Check pretty_hex_str() ##################################################

    def test_pretty_hex_str_type(self):
        """Check that the utils.pretty_hex_str() function fails when the
        "bytes_seq" argument's type is wrong (int)."""

        with self.assertRaises(TypeError):
            utils.pretty_hex_str(1.0)

        with self.assertRaises(TypeError):
            utils.pretty_hex_str("hello")


    def test_pretty_hex_str_items_type(self):
        """Check that the utils.pretty_hex_str() function fails when the
        "bytes_seq" items have wrong type (float)."""

        bytes_seq = (1.0, 0, 10)       # wrong type (float)
        with self.assertRaises(TypeError):
            utils.pretty_hex_str(bytes_seq)

        bytes_seq = ("hello", 0, 10)   # wrong type (str)
        with self.assertRaises(TypeError):
            utils.pretty_hex_str(bytes_seq)

        bytes_seq = ((1, ), 0, 10)     # wrong type (tuple)
        with self.assertRaises(TypeError):
            utils.pretty_hex_str(bytes_seq)


    def test_pretty_hex_str_items_value_lo(self):
        """Check that the utils.pretty_hex_str() function fails when the
        "bytes_seq" items's value is wrong (too low)."""

        bytes_seq = (-1, 0, 10)        # the first item is too low
        with self.assertRaises(ValueError):
            utils.pretty_hex_str(bytes_seq)


    def test_pretty_hex_str_items_value_hi(self):
        """Check that the utils.pretty_hex_str() function fails when the
        "bytes_seq" items's value is wrong (too high)."""

        bytes_seq = (0xffff, 0, 10)    # the first item is too high
        with self.assertRaises(ValueError):
            utils.pretty_hex_str(bytes_seq)


    def test_pretty_hex_str_arg_type_ok(self):
        """Check the returned value of utils.pretty_hex_str() when various
        correct arguments are given."""

        # Test with a tuple of bytes
        bytes_seq = (0xff, 0x00, 0x0a)
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff,00,0a"

        self.assertEqual(hex_str, expected_str)

        # Test with a list of bytes
        bytes_seq = [0xff, 0x00, 0x0a]
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff,00,0a"

        self.assertEqual(hex_str, expected_str)

        # Test with a bytes string
        bytes_seq = bytes((0xff, 0x00, 0x0a))
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff,00,0a"

        self.assertEqual(hex_str, expected_str)

        # Test with a bytearray
        bytes_seq = bytearray((0xff, 0x00, 0x0a))
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff,00,0a"

        self.assertEqual(hex_str, expected_str)

        # Test with an integer
        bytes_seq = 0xff
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff"

        self.assertEqual(hex_str, expected_str)


    def test_pretty_hex_str_1(self):
        """Check the returned value of utils.pretty_hex_str()."""

        bytes_seq = (0xff,)
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff"

        self.assertEqual(hex_str, expected_str)


    def test_pretty_hex_str_2(self):
        """Check the returned value of utils.pretty_hex_str()."""

        bytes_seq = (0xff,) * 10
        hex_str = utils.pretty_hex_str(bytes_seq)
        expected_str = "ff," * 9 + "ff"

        self.assertEqual(hex_str, expected_str)


if __name__ == '__main__':
    unittest.main()

