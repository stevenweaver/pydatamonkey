#!/usr/bin/env python

#  Datamonkey - An API for comparative analysis of sequence alignments using
#  state-of-the-art statistical models.
#
#  Copyright (C) 2013
#  Sergei L Kosakovsky Pond (spond@ucsd.edu)
#  Steven Weaver (sweaver@ucsd.edu)
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the
#  'Software'), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to
#  permit persons to whom the Software is furnished to do so, subject to
#  the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest
import time
import requests
import datamonkey.hivcluster as hivcluster


class TestHivCluster(unittest.TestCase):

    def setUp(self):
        self.fn   = './res/INPUT.FASTA'
        self.distance_threshold = ".015"
        self.min_overlap        = "500"
        self.ambiguity_handling = "AVERAGE"
        self.created_hivcluster = hivcluster.start(self.fn,
                                    self.distance_threshold,
                                    self.min_overlap, self.ambiguity_handling)


    def test_upload(self):
        self.assertTrue(self.created_hivcluster.id is not None)
        #self.assertEqual(self.created_hivcluster.distance_threshold, self.distance_threshold)
        self.assertEqual(self.created_hivcluster.min_overlap, int(self.min_overlap))
        self.assertEqual(self.created_hivcluster.ambiguity_handling, self.ambiguity_handling)

    def test_findbyid(self):
        hivcluster_obj = hivcluster.get(self.created_hivcluster.id)
        self.assertEqual(hivcluster_obj.id, self.created_hivcluster.id)
        self.assertEqual(hivcluster_obj.distance_threshold, self.created_hivcluster.distance_threshold)
        self.assertEqual(hivcluster_obj.min_overlap, self.created_hivcluster.min_overlap)
        self.assertEqual(hivcluster_obj.ambiguity_handling, self.created_hivcluster.ambiguity_handling)

if __name__ == '__main__':
    unittest.main()

