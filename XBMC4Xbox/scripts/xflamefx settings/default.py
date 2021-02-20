'''
  by Frost
'''

import os
import xbmc

xbmc.executebuiltin('ActivateWindow(appearancesettings)')
xbmc.sleep(1000)
xbmc.executebuiltin('SetFocus(-36)')
xbmc.sleep(100)
xbmc.executebuiltin('SetFocus(-12)')
xbmc.sleep(100)

root = os.getcwd()
settings = xbmc.Settings(root)

ok = settings.openSettings()

if ok:
    import re
    ok = False
    with open(root+"\\xflamefx.xml") as x:
        xml = re.sub("<FireEffect>(\d+)</FireEffect>", "<FireEffect>%s</FireEffect>" % settings.getSetting('FireEffect'), x.read())
        xml = re.sub("<Divisor>(\d+)</Divisor>", "<Divisor>%s</Divisor>" % settings.getSetting('Divisor'), xml)
        palette = settings.getSetting('Palette')
        xml = re.sub("<Palette>(\d+)</Palette>", "<Palette>%s</Palette>" % palette, xml)
        custompalette = "FFD100"
        if palette == "5":
            custompalette = settings.getSetting('CustomPalette')[9:15].upper() or "FFD100"
        xml = re.sub("<CustomPalette>(.*?)</CustomPalette>", "<CustomPalette>0x00%s</CustomPalette>" % custompalette, xml)
        xml = re.sub("<9HorizontalSpread>(\d+)</9HorizontalSpread>", "<9HorizontalSpread>%s</9HorizontalSpread>" % settings.getSetting('9HorizontalSpread'), xml)
        xml = re.sub("<9VerticalSpread>(\d+)</9VerticalSpread>", "<9VerticalSpread>%s</9VerticalSpread>" % settings.getSetting('9VerticalSpread'), xml)
        xml = re.sub("<9Residual>(\d+)</9Residual>", "<9Residual>%s</9Residual>" % settings.getSetting('9Residual'), xml)
        xml = re.sub("<9Variance>(\d+)</9Variance>", "<9Variance>%s</9Variance>" % settings.getSetting('9Variance'), xml)
        xml = re.sub("<9Vartrend>(\d+)</9Vartrend>", "<9Vartrend>%s</9Vartrend>" % settings.getSetting('9Vartrend'), xml)
        if xml:
            with open(root+"\\xflamefx.tmp", "w") as tmp:
                tmp.write(xml)
                ok = True
    if ok:
        import shutil
        shutil.copy(root+"\\xflamefx.tmp", "Q:\\screensavers\\xflamefx.xml")

del settings
