#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from ... import SCHEMA_VERSION
from .annotation import AnnotatableDecoder
from omero.model import WellI


class Well201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Well'

    OMERO_CLASS = WellI

    def decode(self, data):
        v = super(Well201501Decoder, self).decode(data)
        self.set_property(v, 'column', data.get('Column'))
        self.set_property(v, 'row', data.get('Row'))
        self.set_property(
            v, 'externalDescription', data.get('ExternalDescription')
        )
        self.set_property(
            v, 'externalIdentifier', data.get('ExternalIdentifier')
        )
        self.set_property(v, 'type', data.get('Type'))
        self.set_property(v, 'alpha', data.get('Alpha'))
        self.set_property(v, 'red', data.get('Red'))
        self.set_property(v, 'green', data.get('Green'))
        self.set_property(v, 'blue', data.get('Blue'))
        self.set_property(v, 'status', data.get('omero:status'))

        for wellsample in data.get('WellSamples', list()):
            wellsample_decoder = self.ctx.get_decoder(wellsample['@type'])
            v.linkWellSample(wellsample_decoder.decode(wellsample))
        return v


class Well201606Decoder(Well201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Well'


if SCHEMA_VERSION == '2015-01':
    decoder = (Well201501Decoder.TYPE, Well201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Well201606Decoder.TYPE, Well201606Decoder)
WellDecoder = decoder[1]
