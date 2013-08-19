#
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
import datamonkey.msa as msa
import time

def create_analysis(upload_id, type, params):
    u""" Starts a new analysis for the given file. """
    # We need to have an option of whether they want mail
    # and/or want the call to block until finished, or neither
    method = '/msa/{0}/{1}'.format(upload_id, type)
    params["upload_id"] = upload_id
    json = dm.post(method, params)
    return Analysis(json)

def get_by_id(id, upload_id, type):
    u""" Starts a new analysis for the given file. """
    # We need to have an option of whether they want mail
    # and/or want the call to block until finished, or neither
    method = '/msa/{0}/{1}/{2}'.format(upload_id, type, id)
    json = dm.get(method)
    return Analysis(json)

def delete(id, upload_id, type):
    u""" Starts a new analysis for the given file. """
    # We need to have an option of whether they want mail
    # and/or want the call to block until finished, or neither
    method = '/msa/{0}/{1}/{2}'.format(upload_id, type, id)
    json = dm.delete(method)
    return json


#Replace all the python files with single analysis python script
class Analysis:
    def __init__(self, json):
        u""" Starts a new asr for the given sequence."""
        self.json = json
        self.update(json)

    def update(self, json):
        u""" Starts a new asr for the given sequence."""
        self.json     = json
        self.id       = json.get("id")
        self.type     = json.get("type")
        self.upload_id    = json.get("upload_id")
        self.status   = json.get("status")
        self.sendmail = json.get("sendmail")

    def poll(self):
        while 1:
            time.sleep(5)
            self.get_status()
            if self.status != "queueing" and self.status != "running":
                self.update_with_latest()
                return

    def update_with_latest(self):
        u""" Returns current status of job """
        method = '/msa/{0}/{1}/{2}'.format(self.upload_id, self.type,
                                                  self.id)
        json = dm.get(method, params=None)
        self.update(json)


    def get_status(self):
        u""" Returns current status of job """
        method = '/msa/{0}/{1}/{2}/status'.format(self.upload_id, self.type,
                                                  self.id)
        response = dm.get(method, params=None)
        self.status = response.get('status')
        return response.get('status')

