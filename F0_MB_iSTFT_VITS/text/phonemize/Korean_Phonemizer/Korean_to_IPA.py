import re
from jamo import h2j, j2hcj
from g2pk2 import G2p

HANGUL = str.maketrans({
    # 子音
    "ㄱ":"g", "ㄲ":"kʼ", "ㅋ":"kʰ",
    "ㄷ":"d", "ㄸ":"tʼ", "ㅌ":"tʰ",
    "ㅂ":"b", "ㅃ":"pʼ", "ㅍ":"pʰ",
    "ㅅ":"sʰ", "ㅆ":"sʼ",
    "ㅈ":"d͡ʑ", "ㅊ":"t͡ɕʰ", "ㅉ":"t͡ɕʼ",
    "ㅁ":"m", "ㄴ":"n", "ㅇ":"ŋ",
    "ㄹ":"ɾ",
    "ㅎ":"h",
    # 二重子音
    "ㄳ":"ks",
    "ㅄ":"bs",
    "ㄵ":"nd͡ʑ", "ㄶ":"n",
    "ㄺ":"rk", "ㄻ":"rm", "ㄼ":"rb", "ㄽ":"rs", "ㄾ":"rt", "ㄿ":"rp", "ㅀ":"r",
    # 母音
    "ㅑ":"j͡a", "ㅕ":"j͡ʌ", "ㅠ":"j͡u", "ㅛ":"j͡o",
    "ㅐ":"ɛ", "ㅔ":"e", "ㅒ":"j͡ɛ̝", "ㅖ":"j͡e",
    "ㅏ":"a", "ㅗ":"o", "ㅓ":"ʌ",
    "ㅣ":"i",
    "ㅜ":"u", "ㅡ":"ɯ",
    # 二重母音
    "ㅘ":"w͡a", "ㅝ":"w͡ʌ",
    "ㅚ":"ø", "ㅞ":"w͡e", "ㅙ":"w͡ɛ",
    "ㅟ":"w͡i", "ㅢ":"ɰ͡i",
})
MOEUM = set([
    # 母音
    "ㅑ", "ㅕ", "ㅠ", "ㅛ",
    "ㅐ", "ㅔ", "ㅒ", "ㅖ",
    "ㅏ", "ㅗ", "ㅓ",
    "ㅣ",
    "ㅜ", "ㅡ",
    # 二重母音
    "ㅘ", "ㅝ",
    "ㅚ", "ㅞ", "ㅙ",
    "ㅟ", "ㅢ",
])
WORD_INITIAL_MAP = str.maketrans({"b":"b̥", "d":"d̥", "g":"k"})


class G2P_Korean_to_Phoneme():
    def __init__(self):
        self.g2p = G2p()
    
    def __call__(self, text):
        text = self.g2p(text, descriptive=True)

        # convert special symbols to pau
        text = re.sub(r"[.,!?;。、「」！？；…—～\-\s]", 'pau', text).replace("paupau", "pau")

        # 모음이랑 자음을 분리
        text = j2hcj(h2j(text))

        # 받침이 아닌 ㅇ을 지움
        text = re.sub(r'ㅇ(?=[' + "".join(MOEUM) + '])', '', text)

        # 한글 to IPA
        text = text.translate(HANGUL)

        # 단어 머리 ㄱㅂㅈㄷ을 변환(g b d͡ʑ d -> k p t͡ɕ t)
        if text.startswith(("b", "d", "g", "d͡ʑ")): 
            text = text.translate(WORD_INITIAL_MAP).replace("d͡ʑ", "t͡ɕ")

        # 어중의 ㄹ 발음을 ɾ -> l 
        text = re.sub(r"ɾ(?=[^aeiouʌɯ])|ɾ$", "l", text)
        return text


if __name__ == "__main__":
    h = G2P_Korean_to_Phoneme()
    a = h('chili paper를 세계에서 가장 좋아하는 민족은 한국인이다.')
    print(a)
    #　--> t͡ɕʰilɾipaupʰeipʰʌɾɯlpausʰegeesʰʌpaugad͡ʑaŋpaud͡ʑoahanɯnpaumind͡ʑogɯnpauhanguginidapau