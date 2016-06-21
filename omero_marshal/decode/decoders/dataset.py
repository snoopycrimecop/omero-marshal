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
from omero.model import DatasetI


class Dataset201501Decoder(AnnotatableDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Dataset'

    OMERO_CLASS = DatasetI

    def decode(self, data):
        v = super(Dataset201501Decoder, self).decode(data)
        v.name = self.to_rtype(data.get('Name'))
        v.description = self.to_rtype(data.get('Description'))
        return v


class Dataset201606Decoder(Dataset201501Decoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2016-06#Dataset'


if SCHEMA_VERSION == '2015-01':
    decoder = (Dataset201501Decoder.TYPE, Dataset201501Decoder)
elif SCHEMA_VERSION == '2016-06':
    decoder = (Dataset201606Decoder.TYPE, Dataset201606Decoder)
DatasetDecoder = decoder[1]
