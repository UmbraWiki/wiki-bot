# -*- coding: utf-8  -*-

# this file implements custom pywikibot fixes

# parts of this code comes from
# https://github.com/pokemoncentral/wiki-util/blob/master/bot/user-fixes.py

except_inside = [
    r"'{2,3}.+?'{2,3}",
    r'".+?"',
    r'\[\[\w{2}:.+?\]\]',
]

def simplify_link(match, text=None):
    """Simplify a link.
    This function returns the link in its simplets possible form. This means
    that, given link text and target, it returns '[[target|text]]' if the two
    are different, and '[[target]]' if they are equal.
    It can be passed a match object, from which link target and text will be
    extracted as groups 1 and 2 respectively. Alternatively, link target and
    text can be passed directly as arguments.
    :param match: The match object to operate on, or the link target.
    :type match: re.Match or string.
    :param text: The link text.
    :type text: string or None.
    :return string: The simplified link.
    """

    if text is None:
        target = match.group(1)
        text = match.group(2)

    # If link target and displayed text are the same, only one value is
    # interpolated. Two are necessary otherwise.
    return ('[[{0:s}]]'.format(target)
            if target == text
            else '[[{0:s}|{1:s}]]'.format(target, text))

# to invoke these functions:
# python pwb.py replace -fix:<name> -start:! -always

# removes interwiki.

fixes['interwiki'] = {
	'regex': True,
	'msg': {
            'it': 'Bot: removing interwiki',
        },
	'replacements': [
	    (r'\[\[\w\w:[^\n[\]]+]]', r""),
	]
}

# removes contiguous multiple and useless spaces.

fixes['spaces'] = {
	'regex': True,
	'msg': {
            'it': 'Bot: removing useless spaces',
        },
	'replacements': [
	    (r' +', r" "),
            (r'^\s+$', r'\n'),
	]
}

# This fix updates redundant code
fixes['redundant-code'] = {
    'regex': True,
    'msg': {
        'it': 'Bot: Fixing redundant code',
    },
    'replacements': [
        (r'\[\[(.+?)\|(.+?)\]\]', simplify_link),
        ('<div></div>', '<br>'),
	('>==', r'>\n=='),
	('<!-- Titolo generato automaticamente -->', '') #remove comment from refLinks
    ]
}

# This fix fixes grammatically incorrect text and general misspellings.
fixes['grammar'] = {
    'regex': True,
    'exceptions': {
        'inside': except_inside,
    },
    'msg': {
        'it': 'Bot: Fixing spelling',
    },
    'replacements': [
        (ur'chè\b', u'ché'),
        (ur'\bpò\b', "po'"),
        (ur'\bsè\b', u'sé'),
        (ur'\bsé\s+stess', 'se stess'),
        (ur'\bquì\b', 'qui'),
        (ur'\bquà\b', 'qua'),
        (ur'\bfà\b', 'fa'),
        ('metereologic', 'meteorologic'),
        ('obbiettiv', 'obiettiv'),
        (u"qual'è", u'qual è'),
        ('eventualmente', 'infine'),
        ('sopratutto', 'soprattutto'),
    ],
}
