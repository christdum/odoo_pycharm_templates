#!/bin/bash

# Create tmp folder
TMP_FOLDER=tmp
mkdir ${TMP_FOLDER}

# Copy the Odoo files to templates folder
cp -R fileTemplates ${TMP_FOLDER}
cp -R templates ${TMP_FOLDER}

# Create an empty "IntelliJ IDEA Global Settings" file,
# needed to be able to import the JAR using "Import Settings..."
IntelliJ="IntelliJ IDEA Global Settings"
touch ${TMP_FOLDER}/"${IntelliJ}"
jar cvfM settings.jar -C ${TMP_FOLDER}/ .

# Remove temporary folders and files
rm -rf ${TMP_FOLDER}
