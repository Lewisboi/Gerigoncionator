import silabeador

VOWELS = "aeiouáéíóúAEIOUÁÉÍÓÚ"

VANILLA_VOWELS = {
    "a": "a",
    "e": "e",
    "i": "i",
    "o": "o",
    "u": "u",
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "A": "a",
    "E": "e",
    "I": "i",
    "O": "o",
    "U": "u",
    "Á": "a",
    "É": "e",
    "Í": "i",
    "Ó": "o",
    "Ú": "u",
}


class Gerigoncionator:
    def gerigoncify(self, text: str) -> str:
        # return WORD_SEPARATOR.join(self.gerigoncify_word(w) for w in words(text))
        gerigoncified_words = []
        for w in words(text):
            gerigoncified = self.gerigoncify_word(w)
            gerigoncified_words.append(gerigoncified)
        return DEFAULT_WORD_SEPARATOR.join(gerigoncified_words)

    def gerigoncify_word(self, word: str) -> str:
        pre, word, post = self.prefix_word_postfix(word)
        if not self.is_gerigonciable(word):
            return word
        gerigoncified = "".join(
            self.gerigoncify_syllable(s) for s in self.get_syllables(word)
        )
        return f"{pre}{gerigoncified}{post}"

    def get_syllables(self, word: str) -> list[str]:
        return silabeador.syllabify(word)

    def gerigoncify_syllable(self, syllable: str) -> str:
        start, end = self.separate_by_last_vowel(syllable)
        *_, last_vowel = start
        last_vowel = VANILLA_VOWELS[last_vowel]
        return f"{start}p{last_vowel}{end}"

    def separate_by_last_vowel(self, syllable: str) -> tuple[str, str]:
        last_vowel_index = len(syllable)
        for i, char in enumerate(reversed(syllable)):
            if char in VOWELS:
                last_vowel_index -= i
                break
        return syllable[:last_vowel_index], syllable[last_vowel_index:]

    def is_gerigonciable(self, word: str) -> bool:
        return any(vowel in word for vowel in VOWELS)

    def prefix_word_postfix(self, word: str) -> tuple[str, str, str]:
        if len(word) == 1:
            return "", word, ""
        first, *middle, last = word
        if first.isalpha():
            middle = [first] + middle
            first = ""
        if last.isalpha():
            middle = middle + [last]
            last = ""
        return first, "".join(middle), last


WORD_SEPARATORS = [
    " ",
    "\n",
    "\t",
]

DEFAULT_WORD_SEPARATOR = " "


def words(text: str):
    curr_start = 0
    for i, char in enumerate(text):
        if char in WORD_SEPARATORS:
            yield text[curr_start:i]
            curr_start = i + 1
    yield text[curr_start:]


if __name__ == "__main__":
    gerigonciador = Gerigoncionator()
    gerigoncificado = gerigonciador.gerigoncify("thalia, luismi y a titan\n")
    print(gerigoncificado)
