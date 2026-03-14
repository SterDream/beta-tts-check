import pycantonese
from chinese_converter import to_traditional

TONE = (
    {
        "1":"˥",
        "2":"˧˥",
        "3":"˧",
        "4":"˨˩",
        "5":"˩˧",
        "6":"˨"
    }
)


class G2P_Cantonese_to_Phoneme:
    def phonemize(text: str):
        text = to_traditional(text)

        # chinese character to jyutping
        pairs = pycantonese.characters_to_jyutping(text)
        result = []

        # mark to pau
        for char, jyut in pairs:
            if jyut is None:
                if char in "。！？":
                    result.append("pau")
                else:
                    result.append("pau")
                continue

            ipa = pycantonese.jyutping_to_ipa(jyut, tones=TONE, return_as="string")
            result.append(ipa.replace(" ", ""))
        return "".join(result)


if __name__ == "__main__":
    text = "香港人講廣東話、中國人講中文。"
    print("Cantonese: ", G2P_Cantonese_to_Phoneme.phonemize(text=text))