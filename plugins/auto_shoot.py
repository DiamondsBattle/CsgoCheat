import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow

class AutoShoot:
    def __init__(self):
        self.dwEntityList = 0x4D4B104
        self.dwForceAttack = 0x317C6EC
        self.dwLocalPlayer = 0xD36B94
        self.m_fFlags = 0x104
        self.m_iCrosshairId = 0xB3D4
        self.m_iTeamNum = 0xF4
        
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "self.client.dll").lpBaseOfDll
    
        while True:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                continue

            self.player = self.pm.read_int(self.client + self.dwLocalPlayer)
            self.entity_id = self.pm.read_int(self.player + self.m_iCrosshairId)
            self.entity = self.pm.read_int(self.client + self.dwEntityList + (self.entity_id - 1) * 0x10)
    
            self.entity_team = self.pm.read_int(self.entity + self.m_iTeamNum)
            self.player_team = self.pm.read_int(self.player + self.m_iTeamNum)
    
            if 0 < self.entity_id <= 64 and self.player_team != self.entity_team:
                self.pm.write_int(self.client + self.dwForceAttack, 6)
    
            time.sleep(0.006)


if __name__ == '__main__':
    AutoShoot()