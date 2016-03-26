import sys

if __name__ == '__main__':
    if not sys.argv[1:]:
        print 'usage: python %s path_to_file' % sys.argv[0]
        sys.exit(0)
    else:
        fname = sys.argv[1]
        f = open(fname, 'r')
        data = f.read()
        f.close()
        data = data.replace('\\\"', '<<here_was_escaped_mark_symbol>>')
        data = data.decode('unicode-escape').encode('utf-8')
        res = []
        coding_page = 144
        print 'file length: ', len(data)

        choose_codepage = False
        for i, c in enumerate(data):

            #print ord(c),
            #if ord(c) == 32: print

            if ord(c) < 128:
                res.append(ord(c))
                continue

            if ord(c) == 195:
                choose_codepage = True
                continue

            if choose_codepage:
                coding_page = ord(c)
                choose_codepage = False
                continue

            if ord(c) in [194]:
                continue

            if coding_page == 144:
                r = chr(ord(c) + 48)
            elif coding_page == 145:
                r = chr(ord(c) + 112)
            elif coding_page == 162 and ord(c) == 147: # wide minus
                    r = chr(151)
            elif coding_page == 130 and ord(c) == 171: # left russian quote
                    r = c
            elif coding_page == 130 and ord(c) == 187: # right russian quote
                    r = c
            elif ord(c) == 128:
                continue
            else:
                print 'unknown letter: <', coding_page, ord(c), '>'
                r = 'X'

            res.append(ord(r))

        print
        print
        #print res

        res = map(chr, res)
        res = ''.join(res)
        res = res.decode('cp1251').encode('utf-8')
        res = res.replace('<<here_was_escaped_mark_symbol>>', '\\\"')
        fw = open('out_'+fname, 'w')
        fw.write(res)
        fw.close()
        print 'done'
        sys.exit(0)
