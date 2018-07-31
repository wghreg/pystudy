#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: wgh
# Date: 2018/7/30 0030 下午 14:44

from tables import *

class Particle(IsDescription):
    """ definition """
    name = StringCol(16)
    id = Int64Col()
    energy = Float64Col()

h5file = open_file("tutorial.h5", mode='w', title='test file')

group = h5file.create_group('/', 'detector', 'Detector information')

table = h5file.create_table(group, 'readout', Particle, 'Readout_example')

print(h5file)

row = table.row
for i in range(10):
    particle = Particle()
    particle.name = 'particle:%6d' % (i)
    # 2**34 2的34次方
    particle.id = i*(2 **34)
    particle.energy = float(i*i)
    row['name'] = particle.name
    row['id'] = particle.id
    row['energy'] = particle.energy
    row.append()

table.flush()