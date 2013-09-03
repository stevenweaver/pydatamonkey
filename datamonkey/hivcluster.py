#  Datamonkey - An API for comparative analysis of sequence alignments using
#  state-of-the-art statistical models.
#
#  Copyright (C) 2013
#  Sergei L Kosakovsky Pond (spond@ucsd.edu)
#  Steven Weaver (sweaver@ucsd.edu)
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the
#  "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software, and to
#  permit persons to whom the Software is furnished to do so, subject to
#  the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import datamonkey.dm as dm
import simplejson as json

def start(fn, distance_threshold, min_overlap, ambiguity_handling, mail=''):
    u""" Starts a new analysis for the given file. """

    # We need to have an option of whether they want mail
    # and/or want the call to block until finished, or neither
    method = '/hivcluster'
    fh = {'files' : (fn, open(fn,'rb'))}

    params = {
        'files'              : fh,
        'distance_threshold' : distance_threshold,
        'min_overlap'        : min_overlap,
        'ambiguity_handling' : ambiguity_handling,
        'mail'               : mail
    }

    json = dm.post(method, params)
    return HivCluster(json)


def get(id):
    u"""Get preexisting id"""
    method = '/hivcluster/' + id
    json = dm.get(method)
    return HivCluster(json)

#We need to define datatypes and gencodes in the database
class HivCluster:
    def __init__(self, hivcluster):
        u""" Initializes HivCluster Object """
        self.id = hivcluster.get('_id')
        self.status = hivcluster.get('status')
        self.min_overlap = hivcluster.get('min_overlap')
        self.ambiguity_handling = hivcluster.get('ambiguity_handling')
        self.created = hivcluster.get('created')
        self.distance_threshold = hivcluster.get('distance_threshold')
        self.distance_threshold = hivcluster.get('distance_threshold')
        self.graph_dot = hivcluster.get('graph_dot')
        self.cluster_csv = hivcluster.get('cluster_csv')

