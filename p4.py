#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dict(dict):

    def _int_(self,**kw):
        super()._init_(**kw)

    def _getattr_(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError()