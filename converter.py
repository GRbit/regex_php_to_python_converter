import re


php_flags_dict = {
    "i": re.IGNORECASE,
    "U": re.UNICODE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
    "x": re.VERBOSE
}


def php_regex_parser(r, return_compiled=False):
    def parse_flags(php_flags):
        ret = 0
        for c in php_flags:
            if c in php_flags_dict:
                ret |= php_flags_dict[c]
        return ret

    regex = r[1:r.rfind(r[0])]
    flags = r[r.rfind(r[0])+1:]
    if return_compiled:
        return re.compile(regex, parse_flags(flags))
    return regex, parse_flags(flags)
