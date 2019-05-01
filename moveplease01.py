#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
xname1 = input('What is the new name for raynor.obj? ')
shutil.move('ceph_storage/raynor.obj', 'ceph_storage/' + xname1')
xname2 = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname2)

