#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get a raw summary of the HTML-format document"""
import re

from requests.packages.idna import unicode


def get_summary(text, count, suffix=u'', wrapper=u'p'):
    assert (isinstance(text, unicode))
    summary = re.sub(r'<.*&#63;>', u'', text)  # key difference: use regex
    summary = u''.join(summary.split())[0:count]
    return u'{1}{2}'.format(wrapper, summary, suffix)
    # return u'<{0}>{1}{2}</{0}>'.format(wrapper, summary, suffix)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
