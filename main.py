"""
A tiny UI state helper that allows registering callbacks for state transitions.
"""

from collections import defaultdict
import tkinter as tk


class UIStateHelper:
    """Track UI state and run callbacks on state changes."""

    def __init__(self, initial="idle"):
        self._state = initial
        self._callbacks = defaultdict(list)

    def on_enter(self, state, callback):
        """Register a callback to run when entering `state`."""
        self._callbacks[state].append(callback)

    def set_state(self, new_state):
        """Change state and run registered callbacks."""
        if new_state == self._state:
            return
        self._state = new_state
        for cb in self._callbacks.get(new_state, []):
            cb()

    def get_state(self):
        return self._state


def main():
    root = tk.Tk()
    root.title("UI State Demo")
    helper = UIStateHelper("idle")

    label = tk.Label(root, text="Idle", font=("Arial", 20))
    label.pack(padx=20, pady=20)

    def show_processing():
        label.config(text="Processing...")

    def show_done():
        label.config(text="Done")

    helper.on_enter("processing", show_processing)
    helper.on_enter("done", show_done)

    def start():
        helper.set_state("processing")
        root.after(2000, finish)  # simulate work

    def finish():
        helper.set_state("done")

    btn = tk.Button(root, text="Start", command=start)
    btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()