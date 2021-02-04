H_SYLLABIC_N = 'ん'
H_SMALL_TSU = 'っ'

HIRA_TO_LATN = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "だ": "da", 'ぢ': 'ji', "づ": "zu", "で": "de", "ど": "do",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo",

    "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
    "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",

    "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
    "じゃ": "ja", "じゅ": "ju", "じょ": "jo",

    "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",

    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",

    "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
    "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
    "ぴゃ": "pya", "ぴゅ": "pyu",  "ぴょ": "pyo",

    "みゃ": "mya", "みゅ": "myu", "みょ": "myo",

    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo",


    "ー": ":", "ん": "n", "々": "qi",

    "うぁ": "ua", "うぃ": "wi", "うぅ": "wu", "うぇ": "we", "うぉ": "uo",
    "ゔぁ": "va", "ゔぃ": "vi", "ゔぇ": "ve", "ゔぉ": "vo", "ゔゅ": "vyu",

    "ふぁ": "fa", "ふぃ": "fi", "ふぇ": "fe", "ふぉ": "fo", "ふゅ": "fyu",

    "てぃ": "ti", "でぃ": "di", "でゅ": "dyu",

    "つぁ": "tsa", "つぇ": "tse",

    "しぇ": "she", "じぇ": "je",

    "ちぇ": "che", "すぇ": "swe", "りぇ": "riye", "るぇ": "ruye", "くぇ": "kwe", "いぇ": "ye",
}

LATN_TO_HIRA = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
    'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を',

    'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
    'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',

    'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
    'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',

    'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',

    'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',

    'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
    'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
    'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',

    'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',

    'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',

    'che': 'ちぇ', 'fa': 'ふぁ', 'vu': 'ゔ', 'fi': 'ふぃ', 'we': 'うぇ',
    'fo': 'ふぉ', 'fe': 'ふぇ', 'wi': 'うぃ', 'je': 'じぇ', 'fyu': 'ふゅ',
    'vi': 'ゔぃ', 'va': 'ゔぁ',

    '-': 'ー', ':': 'ー',
    'n': 'ん', 'm': 'ん', "n'": 'ん', 'f': 'っ', 'j': 'っ',
    'k': 'っ', 's': 'っ', 't': 'っ', 'h': 'っ', 'r': 'っ',
    'g': 'っ', 'z': 'っ', 'd': 'っ', 'b': 'っ', 'p': 'っ',
    'qi': '々', '・': '',

    # "ua": "うぁ", "wi": "うぃ", "wu": "うぅ", "we": "うぇ", "uo": "うぉ",
    # "va": "ゔぁ", "vi": "ゔぃ", "ve": "ゔぇ", "vo": "ゔぉ", "vyu": "ゔゅ",
    #
    # "fa": "ふぁ", "fi": "ふぃ", "fe": "ふぇ", "fo": "ふぉ", "fyu": "ふゅ",
    #
    # "ti": "てぃ", "di": "でぃ", "dyu": "でゅ",
    #
    # "tsa": "つぁ", "tse": "つぇ",
    #
    # "she": "しぇ", "je": "じぇ",
    #
    # "che": "ちぇ", "swe": "すぇ", "riye": "りぇ", "ruye": "るぇ", "kwe": "くぇ", "ye": "いぇ",
}
