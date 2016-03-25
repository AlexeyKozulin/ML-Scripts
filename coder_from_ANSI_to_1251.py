import sys

if __name__ == '__main__':
    if not sys.argv[1:]:
        print 'usage: python %s path_to_file'%sys.argv[0]
        sys.exit(0)
    else:
        f = open(sys.argv[1], 'r')
        fw = open('out.txt', 'w')
        data = f.read()
        res = []
        coding_page = 144
        print 'file length: ', len(data)
        for i, c in enumerate(data):

            if ord(c) == 144:
                coding_page = 144
            if ord(c) == 145:
                coding_page = 145

            if ord(c) in [195,194,144,145]:
                continue

            if coding_page == 144:
                if ord(c) > 145:
                    r = chr(ord(c) + 48)
                else:
                    r = c
            else:
                if ord(c) > 127 and ord(c) < 144:
                    r = chr(ord(c) + 112)
                else:
                    r = c

            fw.write(r)
            res.append(ord(r))
            continue

        f.close()
        fw.close()
        print 'done'
        sys.exit(0)
