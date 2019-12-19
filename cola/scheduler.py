from functools import partial
from .widgets.remote import Fetch
from datetime import datetime
from qtpy import QtCore
from . import qtutils


class SharedScheduler:
    next_id = 0
    current_id = 0
    call_origin = "init"

    def mock_fetch(self, origin):
        if self.id == SharedScheduler.current_id:
            fetch_remote(self.context, origin)
            func = partial(self.mock_fetch, origin)
            timer = QtCore.QTimer.singleShot(3000, func)
            print("I entered the if and I'm from", origin)
        else:
            print("I was called from {} but it is not my turn", origin)

    def __init__(self, context, parent, call_origin):
        print("Shared scheduler initiation from", call_origin)
        self.id = SharedScheduler.next_id
        self.context = context

        SharedScheduler.next_id += 1
        SharedScheduler.current_id = self.id
        func = partial(self.mock_fetch, call_origin)
        t = QtCore.QTimer.singleShot(3000, func)


from .gitcmds import branch_list
import os
from .resources import share


def fetch_remote(context, call_origin):
    print(f"Receiving a fetch_remote call from {call_origin}")
    # fetch_action = Fetch(context)
    # context.model.fetch(context.model.remotes[0])
    # print(context.git)
    context.git.fetch()
    # print(context)
    # print(branch_list(context, True))
    # print(branch_list(context, False))
    # os.environ.setdefault("DISPLAY", ':0')
    #
    # print(context.model.remotes, "model")

    # fetch_action.exec()
