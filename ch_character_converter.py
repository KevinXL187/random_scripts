import opencc
from pyunihan import Query

# character dectection (simplified, tradtional)
def char_detection(char_ch):
    result = Query(char_ch)
    if 'kSimplifiedVariant' in result: return "Simplified"
    elif 'kTraditionalVariant' in result: return "Traditional"
    else: return "Unknown or Mixed"
   
# convert to simplified
def trad_simp(text):
    t2s = opencc.OpenCC('t2s')
    simplified = t2s.convert(text)
    return simplified

# convert to traditional
def simp_trad(text):
    s2t = opencc.OpenCC('s2t')
    traditional = s2t.convert(text)
    return traditional