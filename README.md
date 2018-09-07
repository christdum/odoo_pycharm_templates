# Odoo Pycharm Templates

This project add file templates and code templates on Pycharm



## Installation

    $ git clone git@github.com:christdum/odoo_pycharm_templates.git

### Easy setup  
1. Download `settings.jar` file: [click here](/../../raw/master/settings.jar)
1. Go to `File | Import Settings...` in PyCharm IDE and select the downloaded `settings.jar` file. Click `OK` in the dialog that appears.

### Manuel Install


**Linux distribution**  
  * Path: `~/.PyCharm*/config/templates`

**Mac OS X**  
  * Path: `~/Library/Preferences/PyCharm*/templates`

```bash
    $ rm -rf fileTemplates templates
    $ ln -s $GIT_CLONE_DIR$/fileTemplates fileTemplates
    $ ln -s $GIT_CLONE_DIR$/templates templates
```

## Usage

To manage and add **file templates**, go to Menu :

    Preferences... > Editor > File & Code Templates

To manage and add **live templates**, go to Menu :

    Preferences... > Editor > Live Templates