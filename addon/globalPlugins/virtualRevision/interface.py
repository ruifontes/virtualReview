import addonHandler
import config
import gui
import wx

addonHandler.initTranslation()


class VirtualRevisionSettingsPanel(gui.settingsDialogs.SettingsPanel):
    title = addonHandler.getCodeAddon().manifest['summary']

    def makeSettings(self, settings_sizer):
        self.config = config.conf[addonHandler.getCodeAddon().name]
        sizer = gui.guiHelper.BoxSizerHelper(self, sizer=settings_sizer)
        self.UIAConsoleGrabbingCB = sizer.addItem(wx.CheckBox(
            self,
            label=_('Always use UIA implementation for consoles (gets more text)'),
        ))
        self.UIAConsoleGrabbingCB.SetValue(self.config['UIAConsoleGrabbing'])

    def onSave(self):
        self.config['UIAConsoleGrabbing'] = self.UIAConsoleGrabbingCB.IsChecked()

    @classmethod
    def addSettingsPanel(cls):
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(VirtualRevisionSettingsPanel)

    @classmethod
    def removeSettingsPanel(cls):
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(cls)
