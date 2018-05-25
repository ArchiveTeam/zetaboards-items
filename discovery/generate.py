import sys


def main():
    assert len(sys.argv) == 4
    with open('{}_forumids_{}_{}.txt'.format(sys.argv[1].zfill(4),
                                             *sys.argv[2:]), 'w') as f:
        f.write('\n'.join(['forumids:{}-{}'.format(i, i+99)
                           for i in range(int(sys.argv[2]),
                                          int(sys.argv[3]), 100)]))

if __name__ == '__main__':
    main()

