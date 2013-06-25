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

import datamonkey.msa as msa
import datamonkey.analysis as analysis
import time

mail = 'sweaver@ucsd.edu'
fn   = './res/HIV_gp120.nex'

msa_obj = msa.upload_file(fn, 0, 0, mail)

bsrel_params = {
    'treemode'    : 0,
}

# Create a new analysis and poll
bsrel_analysis = analysis.create_analysis(msa_obj.id, 'bsrel', bsrel_params)
bsrel_analysis.poll()
print bsrel_analysis.json

## Get an existing analysis and print results
#bsrel_analysis = analysis.get_by_id(1, 'upload.958520133127023.1', 'bsrel' )
#results = bsrel_analysis.json['bsrelresults']
#print len(results)

