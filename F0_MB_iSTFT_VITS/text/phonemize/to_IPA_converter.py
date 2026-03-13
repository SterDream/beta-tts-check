import re
import torch


"""
Currently supported languages are:
    - English USA
    - English British

    - Chinese
    - Cantonese
    - Japanese
    - Korean

    - Arabic
    - Farsi/Persian
    
    - German
    - Dutch
    - French
    - Italian
    - Spanish
    - Czech
    - Luxembourgish

    - Russian
    - Swedish

    - Swahili
"""


# English
def US_English_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_US_English_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_US_English_to_Phoneme
    phonemizer = G2P_US_English_to_Phoneme()
    return phonemizer(text)

def GB_English_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "en")

# Asia
def Chinese_converter(text):
    try:
        from .Chinese_Phonemizer import G2P_Chinese_to_Phoneme
    except: 
        from Chinese_Phonemizer import G2P_Chinese_to_Phoneme
    model = G2P_Chinese_to_Phoneme()
    return model(text)

def Cantonese_converter(text):
    try:
        from .Cantonese_Phonemizer import G2P_Cantonese_to_Phoneme
    except:
        from Cantonese_Phonemizer import G2P_Cantonese_to_Phoneme
    return G2P_Cantonese_to_Phoneme.phonemize(text)

def Japanese_converter(text):
    try:
        from .Japanese_Phonemizer import G2P_Japanese_to_Phoneme
    except:
        from Japanese_Phonemizer import G2P_Japanese_to_Phoneme
    return G2P_Japanese_to_Phoneme.phonemize(text)

def Korean_converter(text):
    try: 
        from .Korean_Phonemizer import G2P_Korean_to_Phoneme
    except:
        from Korean_Phonemizer import G2P_Korean_to_Phoneme
    g2p = G2P_Korean_to_Phoneme()
    return g2p(text)

def Arabic_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "ar")

def Farsi_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "fa")

def Persian_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "fa")

# europe
def German_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "de")

def Dutch_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "de")

def French_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "fr")

def Italian_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "it")

def Spanish_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "es")

def Luxembourgish_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "lb")

def Czech_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "cs")

# russia and nordic
def Swedish_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "sv")

def Russian_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "ru")

# africa
def Swahili_converter(text):
    try:
        from .En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    except:
        from En_cs_de_es_fa_fr_it_lb_nl_ru_sv_sw_Phonemizer import G2P_multilang_to_Phoneme
    return G2P_multilang_to_Phoneme.phonemize(text, "sw")


g2p_map = {
    "en-us": US_English_converter,
    "en-gb": US_English_converter,
    "zh": Chinese_converter,
    "yue": Cantonese_converter,
    "ja": Japanese_converter,
    "ko": Korean_converter,
    "fa": Farsi_converter,
    "ar": Arabic_converter,
    "de": German_converter,
    "nl": Dutch_converter,
    "fr": French_converter,
    "it": Italian_converter,
    "es": Spanish_converter,
    "cs": Czech_converter,
    "lv": Luxembourgish_converter,
    "sv": Swedish_converter,
    "ru": Russian_converter,
    "sw": Swahili_converter,
    # ↓ Please put bellow this comment if you add to languages ↓
}

class auto_g2p:
    def __init__(self):
        self.g2p_map = g2p_map

    def __call__(self, text:str, en_type:str="us"):
        lang = self.detect_language(text, en_type)

        if lang not in self.g2p_map:
            raise ValueError(f"Sorry! unsupported language: {lang}")
        ipa_tokens = self.g2p_map[lang](text)
        
        lang_id = list(self.g2p_map.keys()).index(lang)
        lang_id = torch.tensor(lang_id)
        return ipa_tokens, lang_id
   
    def detect_language(self, text, en_type) -> str:  
        text = str(text)
        if re.search(r"[가-힣]", text):
            return "ko"
        if re.search(r"[ぁ-んァ-ン]", text):
            return "ja"
        if re.search(r"[冇咗佢哋喺咩啲嚟嘅咁喎啦呀啫]", text) or re.search(r"[嘅咗佢]", text):
            return "yue"
        if re.search(r"[一-龯]", text):
            return "zh"
        if re.search(r"[А-Яа-яЁё]", text):
            return "ru"
        if re.search(r"[گچپژکی]", text):
            return "fa"
        if re.search(r"[\u0600-\u06FF]", text):
            return "ar"
        if re.search(r"[čřšžěů]", text):
            return "cs"
        if re.search(r"[ñ¿¡]", text):
            return "es"
        if re.search(r"[ß]", text):
            return "de"
        if re.search(r"[å]", text):
            return "sv"
        if re.search(r"[ë]", text):
            return "lb"
        if re.search(r"ij", text):
            return "nl"
        if re.search(r"[àâçèéêëîïôùûÿ]", text):
            return "fr"
        if re.search(r"[àèéìòù]", text):
            return "it"
        if re.search(r"ng'", text):
            return "sw"
        if re.search(r"[a-zA-Z]", text):
            if en_type == "gb":
                return "en-gb"
            return "en-us"
        return "unknown"


if __name__ == "__main__":
    print("languages: ", len(g2p_map))

    print("US english: ", US_English_converter("A bottle of water."))
    print("GB english: ", GB_English_converter("A bottle of water."))
    print("Chinese: ", Chinese_converter("你好，世界"))
    print("Japanese: ", Japanese_converter("こんにちは、世界"))
    print("Korean: ", Korean_converter("안녕하세요, 세계"))

    print("-"*20)

    au = auto_g2p()
    ipa_tokens, lang = au("A bottle of water, tomato.", en_type="us")
    print("US English: ", ipa_tokens, lang)

    ipa_tokens, lang = au("A bottle of water, tomato.", en_type="gb")
    print("GB Rnglish: ", ipa_tokens, lang)

    ipa_tokens, lang = au("我喜歡珍茶。我每天一邊喝一邊做作業！")
    print("Chinese: ", ipa_tokens, lang)

    ipa_tokens, lang = au("我鍾意香港嘅飲茶！")
    print("Cantonese: ", ipa_tokens, lang)

    ipa_tokens, lang = au("私は緑茶が好きです。朝、緑茶を飲むのが日課です！")
    print("Japanese: ", ipa_tokens, lang)

    ipa_tokens, lang = au("저는 오미차를 좋아해요. 매일밤 오미차를 마시면서 일해요!")
    print("Korean: ", ipa_tokens, lang)

    ipa_tokens, lang = au("Я люблю́ тебя́!!")
    print("Russian: ", ipa_tokens, lang)
    