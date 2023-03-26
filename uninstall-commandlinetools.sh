#!/bin/sh

cmd="rm -fr"

$cmd /Library/Developer/CommandLineTools

cd /Library/Apple/System/Library/Receipts

$cmd com.apple.pkg.CLTools_Executables.{bom,plist}
$cmd com.apple.pkg.CLTools_SDK_macOS*.{bom,plist}
$cmd com.apple.pkg.CLTools_macOs_SDK.{bom,plist}
