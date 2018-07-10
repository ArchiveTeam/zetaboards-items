import sys


def write_items(items, num):
    with open(str(num).zfill(2) + '_forumpage.txt', 'w') as f2:
        f2.write('\n'.join(items))


def main():
    assert len(sys.argv) == 3
    items = []
    num = int(sys.argv[2])
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip().split(':')
            if line[0] == 'memberpages' or len(line) == 0:
                continue
            site, forum, pages = line[1:]
            for i in range(1, int(pages)+1, 3):
                items.append(':'.join(['forumpage', site, forum, str(i) + '-' \
                                       + str(i+2)]))
            if len(items) == 200000:
                write_items(items, num)
                num += 1
                items = []
    write_items(items, num)

if __name__ == '__main__':
    main()

