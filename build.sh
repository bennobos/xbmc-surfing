#!/bin/sh

addon_id=`grep "^.* id\=" addon.xml | cut -f2 -d'"'`
version=`grep "^\s\+version" addon.xml | cut -f2 -d'"'`

echo "Building '$addon_id' version: $version"

builddir=build
dest="$builddir/$addon_id"
if [ -d $dest ]; then
    rm -r $dest
fi

mkdir -p $dest
cp addon.xml addon.py changelog.txt icon.png LICENSE.txt fanart.jpg $dest/
cp -r resources/ $dest/resources/
cd $builddir; zip -r $addon_id-$version.zip $addon_id
