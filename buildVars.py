# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables

addon_info = {
	# add-on Name
	"addon-name" : "virtualRevision",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Virtual Revision"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("Press nvda+control+w to get a Simple review of the current window's text."),
	# version
	"addon-version" : "1.3-dev",
	# Author(s)
	"addon-author" : "Rui Batista <ruiandrebatista@gmail.com>",
	# URL for the add-on documentation support
    "addon-url" : "http://addons.nvda-project.org"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "virtualRevision", "*.py"),]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py"]

excludedFiles = []
