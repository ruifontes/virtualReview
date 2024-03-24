# Virtual Review


* Authors: Rui Batista and NVDA Addon Team
* Download [stable version][1]
* NVDA compatibility: 2019.3 and beyond

This Addon allows NVDA users to review a Window content in a text box, similar to window virtualization of JAWS for Windows.
Note, however, that this is just a convenience for users and does not replace NVDA's excellent review modes and object navigation support.


## Usage ##

Press NVDA+control+w to open the virtual revision Window.
Then simply navigate the shown textbox as you do in any other text content.
You can press Escape to close the virtual revision window.


## Changes for 3.0

* Requires NVDA 2019.3 or later.

## Changes for 2.3

* Internal changes to support future NVDA releases.

## Changes for 2.2

* When windows are minimized or if the foreground window has no title, NVDA will record this fact when displaying virtual review window.

## Changes for 2.1

* The title of the screen under virtual review will be included.
* It is now possible to review contents of Universal Windows Platform (UWP) apps in Windows 10 and most modern apps in Windows 8.x.
* When obtaining screen contents for modern and universal apps, a beep will be heard to indicate when the virtual review window is ready.

## Changes for 2.0

* New name: Virtual Review.
* Due to changes in how content is shown, NVDA 2015.2 or later is required.
* Thanks to new features in 2015.2 and later, you can now find text in virtualized windows.
* Fixed the add-on functionality with non-console window.
* Removed useless blank lines at bottom of virtualized console window.
* Some minor adjustments.
* Translations added.

## Changes for 1.2

* Support virtualizing of console windows

## Changes for 1.1

* Converted virtual revision to an add-on.

## Changes for 1.0

* Initial Release

[1]: https://github.com/ruifontes/virtualReview/releases/download/2024.03.24/virtualRevision-2024.03.24.nvda-addon
