try:
    import tkinter as tk
    from tkinter import ttk
    import time
    from pynput.keyboard import Key, Controller, Listener
    import threading
except ImportError as error:
    print("Importing error: " + error)
    
def main():
    MainMenu()
    
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x100")
        self.title("Autofarming Menu")
        self.resizable(False, False)
        self.keyboard = Controller()
        self.unbind_class("Button", "<Key-space")

        self.quitSignal = False
        
        self.movementTime = 0
        self.loopCount = 0
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        farmablesAmount = ["Laser Grid", "Pepper Trees", "Chandeliers", "Grass", "Sugar Cane"]
        
        topFrame = tk.Frame(self)
        topFrame.grid(row=0, column=0, sticky="news")
        bottomFrame = tk.Frame(self)
        bottomFrame.grid(row=1, column=0, sticky="news")
        
        topFrame.columnconfigure(0, weight=1)
        topFrame.columnconfigure(1, weight=1)
        topFrame.rowconfigure(0, weight=1)
        bottomFrame.rowconfigure(0, weight=1)
        bottomFrame.columnconfigure(0, weight=1)
        
        
        selectorFrame = tk.Frame(topFrame, padx=5, pady=2)
        selectorFrame.grid(row=0, column=0, sticky="news")
        ttk.Label(selectorFrame, text="Farmable Selector:").grid(row=0, column=0)
        farmableSelector = ttk.Combobox(selectorFrame, values=farmablesAmount, state="readonly")
        farmableSelector.grid(row=1, column=0)
        
        informationFrame = tk.Frame(topFrame, padx=5, pady=2)
        informationFrame.grid(row=0, column=1, sticky="news")
        self.movementTimeLabel = ttk.Label(informationFrame, text=f"Action Interval: {self.movementTime}s")
        self.movementTimeLabel.grid(row=0, column=0)
        self.loopCounterLabel = ttk.Label(informationFrame, text=f"Loop Count: {self.loopCount}")
        self.loopCounterLabel.grid(row=1, column=0)
        
        self.startFarming = ttk.Button(bottomFrame, text="Start Farming", command=lambda: self.StartFarming(farmableSelector.get()))
        self.startFarming.grid(row=0, column=0)
        self.infoLabel = ttk.Label(bottomFrame, text=" ")
        self.infoLabel.grid(row=1, column=0)
        
        
        
        self.mainloop()
            
    def on_press(self, key):
        if key == Key.esc:
            self.quitSignal = True
            if self.listener_thread:
                self.listener_thread.join()
            
    def MoveAndBreak(self, pauseTime, punchKey, moveKey):
        self.keyboard.press(punchKey)
        self.keyboard.press(moveKey)
        time.sleep(.1)
        self.keyboard.release(moveKey)
        time.sleep(pauseTime)
        self.keyboard.release(punchKey)
        
    def StartFarming(self, farmable):
        self.listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        self.listener_thread.start()
        self.movementTimeLabel.focus_set()
        
        farming_thread = threading.Thread(target=self.FarmingLoop, args=[farmable], daemon=True)
        farming_thread.start()
        
        
    def FarmingLoop(self, farmable):
        if farmable == "Laser Grid":
            self.movementTime = 0.250
            self.movementTimeLabel.config(text=f"Action Interval: {self.movementTime}s")
            self.movementTimeLabel.update()
            self.infoLabel.config(text="Hold down 'Escape' to exit the loop.")
            self.infoLabel.update()
            while not self.quitSignal:
                print("Loop running...")
                
                self.loopCount += 1
                self.loopCounterLabel.config(text=f"Loop Count: {self.loopCount}")
                self.loopCounterLabel.update()
                
                self.MoveAndBreak(self.movementTime, Key.space, 'd')
            self.quitSignal = False
            self.loopCount = 0
            self.infoLabel.config(text=" ")
            self.infoLabel.update()
        elif farmable == "Pepper Trees":
            self.movementTime = 0.175
            self.movementTimeLabel.config(text=f"Action Interval: {self.movementTime}s")
            self.movementTimeLabel.update()
            self.infoLabel.config(text="Hold down 'Escape' to exit the loop.")
            self.infoLabel.update()
            while not self.quitSignal:
                print("Loop running...")
                
                self.loopCount += 1
                self.loopCounterLabel.config(text=f"Loop Count: {self.loopCount}")
                self.loopCounterLabel.update()
                
                self.MoveAndBreak(self.movementTime, Key.space, 'd')
            self.quitSignal = False
            self.loopCount = 0
            self.infoLabel.config(text=" ")
            self.infoLabel.update()
        elif farmable == "Sugar Cane" or farmable == "Grass":
            self.movementTime = 0.125
            self.movementTimeLabel.config(text=f"Action Interval: {self.movementTime}s")
            self.movementTimeLabel.update()
            self.infoLabel.config(text="Hold down 'Escape' to exit the loop.")
            self.infoLabel.update()
            while not self.quitSignal:
                print("Loop running...")
                
                self.loopCount += 1
                self.loopCounterLabel.config(text=f"Loop Count: {self.loopCount}")
                self.loopCounterLabel.update()
                
                self.MoveAndBreak(self.movementTime, Key.space, 'd')
            self.quitSignal = False
            self.loopCount = 0
            self.infoLabel.config(text=" ")
            self.infoLabel.update()
        elif farmable == "Chandeliers":
            self.movementTime = 0.475
            self.movementTimeLabel.config(text=f"Action Interval: {self.movementTime}s")
            self.movementTimeLabel.update()
            self.infoLabel.config(text="Hold down 'Escape' to exit the loop.")
            self.infoLabel.update()
            while not self.quitSignal:
                print("Loop running...")
                
                self.loopCount += 1
                self.loopCounterLabel.config(text=f"Loop Count: {self.loopCount}")
                self.loopCounterLabel.update()
                
                self.MoveAndBreak(self.movementTime, Key.space, 'd')
            self.quitSignal = False
            self.loopCount = 0
            self.infoLabel.config(text=" ")
            self.infoLabel.update()
                
        
    def start_listener(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
        
        
if __name__ == "__main__":
    main()