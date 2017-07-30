#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import socket
import sys
if sys.version_info.major >= 3:
    import socketserver
else:
    import SocketServer as socketserver


HOST = "localhost"
PORT = 48002


class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)


def operate_as_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(b'test')


def operate_as_server():
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', action='store_true', help='Server mode')
    parser.add_argument('-c', '--clipboard', action='store_true', help='Remote yank to clipboard')
    parser.add_argument('-p', '--pasteboard', action='store_true', help='Remote yank to tmux paste board')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.server:
        operate_as_server()
    else:
        operate_as_client()


if __name__ == '__main__':
    main()
