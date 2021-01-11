import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow


class BunnyHopper:
    def __init__(self):
        self.dwForceJump = 0x51F4D88
        self.dwLocalPlayer = 0xD36B94
        self.m_fFlags = 0x104
        
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "self.client.dll").lpBaseOfDll
    
        while True:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                continue
    
            if keyboard.is_pressed("space"):
                self.force_jump = self.client + self.dwForceJump
                self.player = self.pm.read_int(self.client + self.dwLocalPlayer)
                if self.player:
                    self.on_ground = self.pm.read_int(self.player + self.m_fFlags)
                    if self.on_ground and self.on_ground == 257:
                        self.pm.write_int(self.force_jump, 5)
                        time.sleep(0.08)
                        self.pm.write_int(self.force_jump, 4)
    
            time.sleep(0.002)


if __name__ == '__main__':
    BunnyHopper()