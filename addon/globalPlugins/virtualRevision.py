# Virtual Revision NVDA plugin
#Copyright (C) 2012-2017 Rui Batista and contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import sys
import globalPluginHandler
import api
import textInfos
import ui
import addonHandler
addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_TEXTREVIEW
except:
	SCRCAT_TEXTREVIEW = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_TEXTREVIEW

	def script_virtualWindowReview(self, gesture):
		# Find the first focus ancestor that have any display text, according to the display model
		# This must be the root application window, or something close to that.
		text = None
		root = None
		for ancestor in api.getFocusAncestors():
			if ancestor.appModule and ancestor.displayText:
				root = ancestor
				break
		if root:
			info = root.makeTextInfo(textInfos.POSITION_FIRST)
			info.move(textInfos.UNIT_LINE, sys.maxint, endPoint="end")
			text = info.clipboardText.replace("\0", " ")
		obj = api.getFocusObject()
		if obj.windowClassName == u'ConsoleWindowClass':
			info = obj.makeTextInfo(textInfos.POSITION_FIRST)
			info.expand(textInfos.UNIT_STORY)
			text = info.clipboardText.rstrip()
		if text:
			# Translators: Title of the window shown for reading text on screen via a window.
			ui.browseableMessage(text, title=_("Virtual review"))
		else:
			# Translator: Message shown when no text can be virtualized.
			ui.message(_("No text to display"))
	# Translators: Message presented in input help mode.
	script_virtualWindowReview.__doc__ = _("Opens a window containing the text of the currently focused window for easy review.")

	__gestures = {
		"kb:nvda+control+w" : "virtualWindowReview"
	}
