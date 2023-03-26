#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
gemfile = args.file
f = open(gemfile, "r")

specs = []
begin_record = False

while True:
  line = f.readline()
  if line == '':
    break
  line = line.strip()
  if line == "specs:":
    begin_record = True
  if line == "PLATFORMS":
    f.close()
    break
  if begin_record:
    idx = line.find("(")
    if idx == -1:
      continue
    if idx == 0:
      print("error: incorrect syntax")
      break
    spec = line[:idx].strip()
    specs.append(spec)

for spec in specs:
  print("uninstalling " + spec)
  os.system("gem uninstall --force " + spec)
