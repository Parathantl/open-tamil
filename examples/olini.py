# This Python file uses the following encoding: utf-8
#!/bin/env python3
# (C) 2020, எழில் மொழி அறக்கட்டளை
# இந்த நிரல் ஓப்பன்-தமிழ் நிரல் தொகுப்பில் சேர்ந்ததாகும்.

# உரைவழி தமிழ் எண்களினை கொண்ட கணிதவியல்
# உள்ளீடை கணக்கிடும் ஒரு கருவி.
import operator
import re
import tamil

def அச்சிடு(_): print(_)
def கணி(_): return eval(_)

செயல்சார்புகள் = {"கூட்டல்":('+',operator.add),"கழித்தல்":('-',operator.sub),
                                "பெருக்கல்":('*',operator.mul), "வகுத்தல்":('/',operator.truediv)}
அதிக_பட்சம் = 1001
இலகுவான_எண்கள் = {}
for எண் in range(அதிக_பட்சம்):
    இலகுவான_எண்கள்[ tamil.numeral.num2tamilstr(எண்) ] = எண்
வழுநீகால்_இயக்கம் = True
def கணக்கிடு( _தொடர் ):
        தமிழ்_உரை_தொடர் = re.sub('\s+',' ',_தொடர்)
        # செயல்சார்புகளை குறியீடுகளாக மாற்றவும்
        for பெயர்,எண் in செயல்சார்புகள்.items():
            தமிழ்_உரை_தொடர் = தமிழ்_உரை_தொடர்.replace(பெயர்,எண்[0])
        for பெயர்,எண் in இலகுவான_எண்கள்.items():
            தமிழ்_உரை_தொடர் = தமிழ்_உரை_தொடர்.replace(பெயர்,'%g'%எண்)
        if வழுநீகால்_இயக்கம்:
            அச்சிடு(தமிழ்_உரை_தொடர்)
        விடை = கணி(தமிழ்_உரை_தொடர்)
        அச்சிடு(tamil.numeral.num2tamilstr( விடை ) )
        return விடை

if __name__ == "__main__":
    assert 2 == கணக்கிடு("ஒன்று கூட்டல் ஒன்று")
    assert 21 == கணக்கிடு("ஒன்று கூட்டல் இரண்டு பெருக்கல் பத்து")
    assert 950 == கணக்கிடு("ஓர் ஆயிரம் கழித்தல் ஐந்து பெருக்கல் (ஒன்பது கூட்டல் ஒன்று)")