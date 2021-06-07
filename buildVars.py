# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# add-on Name, internal for nvda
	"addon_name" : "virtualRevision",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Virtual Review"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("Provides a simple reviewable dialog of the text of the currently focused window."),
	# version
	"addon_version" : "21.06",
	# Author(s)
	"addon_author" : "Rui Batista <ruiandrebatista@gmail.com> and NVDA Addon Team",
	# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion" : "2019.3",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion" : "2021.1",
	# Add-on update channel (default is stable)
	"addon_updateChannel" : None,
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
