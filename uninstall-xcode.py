#!/usr/bin/env python3

import os

files = [
  "/Applications/Xcode.app",
  "/Library/Preferences/com.apple.dt.Xcode.plist",
  "~/Library/Preferences/com.apple.dt.Xcode.plist",
  "~/Library/Caches/com.apple.dt.Xcode",
  "~/Library/Application Support/Xcode",
  "~/Library/Developer/Xcode",
  "~/Library/Developer/CoreSimulator",
  "~/Library/Developer/XCPGDevices",
  "~/Library/Developer/Xcode/DerivedData"
]

for f in files:
  f = f.replace("~", "/Users/buba")
  print("removing " + f)
  os.system("rm -fr " + f)
