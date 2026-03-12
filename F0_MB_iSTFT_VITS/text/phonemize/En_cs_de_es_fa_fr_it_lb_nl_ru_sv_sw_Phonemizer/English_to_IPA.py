import re
import itertools
from gruut import sentences
from espeak_phonemizer import Phonemizer


class G2P_US_English_to_Phoneme:
    def __init__(self):
        self.phonemizer = Phonemizer(default_voice="en-us")

    def __call__(self, text):
        text = self.phonemizer.phonemize(text.replace(" ", ""), keep_clause_breakers=True)
        text = re.sub(r"[.,!?;。、「」！？；…—～\-\s]", 'pau', text)
        text = text.replace("paupau", "pau")
        return text
    

class G2P_multilang_to_Phoneme:
    def phonemize(text, lang):
        i = []
        str_text = ""

        for sent in sentences(text, lang=lang):
            for word in sent:
                if word.phonemes:
                    i.append(word.phonemes)

        text = list(itertools.chain.from_iterable(i))

        str_text = str_text.join(text)
        str_text = str_text.replace("‖", "pau")
        return str_text


if __name__ == "__main__":
    text = "A bottle of water. tomato!!!!"
    phonemizer = G2P_US_English_to_Phoneme()

    print("us: ", phonemizer(text))
    print("gb: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="en"))

    print("Arabic: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="ar"))
    print("Czech: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="cs"))
    print("German: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="de"))
    print("Spanish: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="es"))
    print("Farsi: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="fa"))
    print("French: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="fr"))
    print("Italian: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="it"))
    print("Luxembourgish: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="lb"))
    print("Dutch: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="nl"))
    print("Russian: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="ru"))
    print("Swedish: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="sv"))
    print("Swahili: ", G2P_multilang_to_Phoneme.phonemize(text=text, lang="sw"))