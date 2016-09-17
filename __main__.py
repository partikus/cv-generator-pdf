#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'demo':
            from generator import demo
            demo.main()
        if sys.argv[1] == 'server':
            from generator import server
            server.run()
        if sys.argv[1] == 'queue':
            from generator import queue_server
            queue_server.run()
    else:
        print('pass either "demo" or "server" as an argument')


if __name__ == "__main__":
    main()
