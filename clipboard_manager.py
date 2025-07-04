# clipboard_manager.py (Corrected Version to Fix Launch Crash)

import rumps
import pyperclip
import os
import json

HISTORY_FILE = os.path.expanduser("~/.clipboard_history.json")

def save_history(items):
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(items, f, indent=2)
    except Exception as e:
        print(f"Error saving history: {e}")

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r') as f:
            content = f.read()
            if not content: return []
            return json.loads(content)
    except Exception as e:
        print(f"Error loading history file: {e}")
        return []

class ClipboardApp(rumps.App):
    def __init__(self):
        # We only set the title here. The menu is built entirely by update_menu.
        super(ClipboardApp, self).__init__(name="Clipboard Manager", title="📋")
        self.dashboard_items = load_history()
        self.deleting_mode = False
        self.update_menu()

    def update_menu(self):
        """Rebuilds the entire menu from scratch using the correct API."""
        self.menu.clear() # Start with an empty menu

        if self.deleting_mode:
            # --- Build the "Delete Mode" Menu ---
            self.menu.add(rumps.MenuItem("✅ Done Deleting", callback=self.exit_delete_mode))
            self.menu.add(rumps.separator)

            for item_content in self.dashboard_items:
                display_text = item_content.replace('\n', ' ').replace('\r', '')[:40]
                if len(item_content) > 40: display_text += "..."

                delete_item = rumps.MenuItem(f"❌ {display_text}", callback=self.delete_this_item_action)
                delete_item.represented_object = item_content
                self.menu.add(delete_item)
        else:
            # --- Build the Normal Menu ---
            self.menu.add(rumps.MenuItem("Save Current Clipboard", callback=self.save_clipboard_action))
            self.menu.add(rumps.MenuItem("Clear All Items", callback=self.clear_all_action))
            self.menu.add(rumps.MenuItem("Delete Specific Item...", callback=self.enter_delete_mode))
            self.menu.add(rumps.separator)

            if not self.dashboard_items:
                self.menu.add(rumps.MenuItem("Dashboard is empty"))
            else:
                for i, item_content in enumerate(self.dashboard_items):
                    display_text = item_content.replace('\n', ' ').replace('\r', '')[:40]
                    if len(item_content) > 40: display_text += "..."
                    copy_item = rumps.MenuItem(f"{i + 1}. {display_text}", callback=self.copy_item_action)
                    copy_item.represented_object = item_content
                    self.menu.add(copy_item)

            self.menu.add(rumps.separator)
            self.menu.add(rumps.MenuItem("Quit", callback=rumps.quit_application))

    def save_clipboard_action(self, _):
        content = pyperclip.paste()
        if not content:
            rumps.notification("Clipboard App", "Clipboard is empty")
            return

        if content in self.dashboard_items:
            self.dashboard_items.remove(content)

        self.dashboard_items.insert(0, content)
        save_history(self.dashboard_items)
        self.update_menu()

    def clear_all_action(self, _):
        if not self.dashboard_items:
            return
        self.dashboard_items.clear()
        save_history(self.dashboard_items)
        self.update_menu()

    def copy_item_action(self, sender):
        if hasattr(sender, 'represented_object'):
            pyperclip.copy(sender.represented_object)
            rumps.notification("Clipboard App", "Item Copied!")

    def enter_delete_mode(self, _):
        if not self.dashboard_items:
            rumps.alert("No items to delete!")
            return
        self.deleting_mode = True
        self.update_menu()

    def exit_delete_mode(self, _):
        self.deleting_mode = False
        self.update_menu()

    def delete_this_item_action(self, sender):
        if hasattr(sender, 'represented_object'):
            self.dashboard_items.remove(sender.represented_object)
            save_history(self.dashboard_items)
            self.update_menu()

if __name__ == "__main__":
    app = ClipboardApp()
    app.run()
