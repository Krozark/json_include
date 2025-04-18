#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.insert(0, '..')

import os
from json_include import build_str


root_path = os.path.dirname(__file__)


def _path(dir):
    return os.path.join(root_path, dir)


def get_files(dirpath):
    return next(os.walk(dirpath))[2]

def run_build_json_include(dirpath, i):
    print("Process file %s/%s" % (dirpath, i))
    rv_1 = build_str(dirpath, i, CHECK_OS="linux")
    with open(os.path.join(_path('expect'), i)) as f:
        expect = f.read()
    print(rv_1)
    assert rv_1.strip() == expect.strip()


if __name__ == "__main__":
    dirpath = _path('source')
    for i in get_files(dirpath):
        run_build_json_include(dirpath, i)
