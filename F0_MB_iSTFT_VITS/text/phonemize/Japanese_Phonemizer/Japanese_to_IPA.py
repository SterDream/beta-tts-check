import re
import pyopenjtalk

JTALK_TO_IPA = {
    # 母音
    "u": "ɯ",
    # 子音
    "ky": "kʲ", "gy": "gʲ", "ny": "ɲ", "y": "j",
    "sh": "ɕ", "ch": "t͡ɕ", "ts": "t͡s",
    "j": "d͡ʑ", "f": "ɸ", "my": "mʲ",
    "r": "ɾ", "ry": "ɾʲ",
}

class G2P_Japanese_to_Phoneme:
    def phonemize(text):
        base = text
        text = pyopenjtalk.g2p(text)
        text = text.replace(" ", "").translate(JTALK_TO_IPA).replace("paɯ", "pau")

        if re.search(r"[.,!?;。、「」！？；…—～\-\s]$", base):
            text += "pau"
        return text


if __name__ == "__main__":
    text = G2P_Japanese_to_Phoneme.phonemize("私は、アメリカ人です！")
    print(text)
