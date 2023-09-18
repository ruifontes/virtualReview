# Virtual Revision NVDA plugin
#Copyright (C) 2012-2020 Rui Batista and contributors
#Copyright (C) 2021-2023 Rui Fontes, Rui Batista and contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import globalPluginHandler
import globalVars
import api
import textInfos
import ui
import scriptHandler
import addonHandler
addonHandler.initTranslation()

try:
	from globalCommands import SCRCAT_TEXTREVIEW
except:
	SCRCAT_TEXTREVIEW = None

def obtainUWPWindowText():
	foreground = api.getForegroundObject()
	desktop = api.getDesktopObject()
	uwpTextList = [foreground.name]
	curObject=foreground.firstChild
	while curObject:
		if curObject.name is not None: uwpTextList.append(curObject.name)
		if curObject.simpleFirstChild:
			curObject=curObject.simpleFirstChild
			continue
		if curObject.simpleNext:
			curObject=curObject.simpleNext
			continue
		if curObject.simpleParent:
			parent=curObject.simpleParent
			# As long as one is on current foreground object...
			#Stay within the current top-level window.
			if parent.simpleParent == desktop:
				break
			while parent and not parent.simpleNext:
				parent=parent.simpleParent
			# But sometimes, the top-level window has no sibling at all (such is the case in Windows 10 Start menu).
			try:
				curObject=parent.simpleNext
			except AttributeError:
				continue
	return uwpTextList

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = SCRCAT_TEXTREVIEW

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Opens a window containing the text of the currently focused window for easy review."),
		gesture="kb:nvda+control+w"
	)
	def script_virtualWindowReview(self, gesture):
		# Find the first focus ancestor that have any display text, according to the display model
		# This must be the root application window, or something close to that.
		# In case of universal apps, traverse child elements.
		text = None
		obj = api.getFocusObject()
		# Because it may take a while to iterate through elements, play abeep to alert users of this fact and the fact it's a UWP screen.
		if obj.windowClassName.startswith("Windows.UI.Core"):
			import tones
			tones.beep(400, 300)
			text = "\n".join(obtainUWPWindowText())
			tones.beep(400, 50)
		else:
			root = None
			for ancestor in api.getFocusAncestors():
				if ancestor.appModule and ancestor.displayText:
					root = ancestor
					break
			if root:
				info = root.makeTextInfo(textInfos.POSITION_FIRST)
				# sys.maxint is gone in Python 3 as integer bit width can grow arbitrarily.
				# Use the static value (0x7fffffff or (2^31)-1) directly.
				info.move(textInfos.UNIT_LINE, 0x7fffffff, endPoint="end")
				text = info.clipboardText.replace("\0", " ")
			if obj.windowClassName == u'ConsoleWindowClass':
				info = obj.makeTextInfo(textInfos.POSITION_FIRST)
				info.expand(textInfos.UNIT_STORY)
				text = info.clipboardText.rstrip()
		if text:
			name = api.getForegroundObject().name
			if name in (None, ""):
				# Translators: The title of the virtual review window when the foreground window has no name, commonly seen when all windows are minimized.
				name = _("No title")
			# Translators: Title of the window shown for reading text on screen via a window.
			ui.browseableMessage(text, title=_("Virtual review: {screenName}").format(screenName = name))
		else:
			# Translator: Message shown when no text can be virtualized.
			ui.message(_("No text to display"))

	#__gestures = {}

# Avoid use on secure screens
if globalVars.appArgs.secure:
	# Override the global plugin to disable it.
	GlobalPlugin = globalPluginHandler.GlobalPlugin
