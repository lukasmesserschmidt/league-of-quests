import customtkinter as ctk


class DigitEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.only_digit = self.register(self.only_digit_validate)
        self.configure(validate="key", validatecommand=(self.only_digit, "%S", "%s", "%d"))
        self.bind("<FocusOut>", self.on_focus_out_0)

    def only_digit_validate(self, char, text, action):
        if action == "0":
            return True
        elif char.isdigit():
            return True
        elif (char == "." and
                "." not in text):
            return True
        return False
    
    def on_focus_out_0(self, event):
        entry = event.widget
        if entry.get() == "":
            entry.insert(0, 0)


class ScaleDigitEntry(DigitEntry):
    def __init__(self, master, scale_var: ctk.StringVar, **kwargs):
        super().__init__(master, **kwargs)

        self.scale_var = scale_var
        self.base_var = ctk.StringVar(value=self._textvariable.get() or 1)
        
        self.scale_var.trace_add(mode="write", callback=lambda *args: self.scale("scale"))
        self._textvariable.trace_add(mode="write", callback=lambda *args: self.scale("textvar"))

    def scale(self, var_name, *args):
        try:
            base = float(self.base_var.get())
            scale = float(self.scale_var.get())
            textvar = float(self._textvariable.get())
            if var_name == "scale":
                self._textvariable.set(round(base * scale, 1))
            elif var_name == "textvar":
                self.base_var.set(textvar / scale)
        except:
            pass