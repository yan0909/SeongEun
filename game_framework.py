from pico2d import *
import main_state
import start_menu

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw

class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)

stack = None
running = None

def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()



def quit():
    global running
    running = False


def run(start_state):
    global stack, running
    running = True

    stack = [start_state]
    start_state.enter()
    while running:
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    pass
    #run(GameState(main_state))




if __name__ == '__main__':
    pass
    #open_canvas()
    #state = GameState(start_menu)
    #run(state)
    #close_canvas()