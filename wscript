# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('ysxroute', ['core', 'internet', 'network'])
    module.source = [
        'model/ysxroute.cc',
        'helper/ysxroute-helper.cc',
        'model/ysxroute-header.cc',
        ]

    module_test = bld.create_ns3_module_test_library('ysxroute')
    module_test.source = [
        'test/ysxroute-test-suite.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'ysxroute'
    headers.source = [
        'model/ysxroute.h',
        'helper/ysxroute-helper.h',
        'model/ysxroute-header.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

