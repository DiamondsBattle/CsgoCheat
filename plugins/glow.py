import pymem
import pymem.process
import keyboard
import win32gui

class Glow:
    def __init__(self):
        self.dwEntityList = 0x4D5022C
        self.dwLocalPlayer = 0xD3BBEC
        self.m_iTeamNum = 0xF4
        self.dwGlowObjectManager = 0x5298070
        self.m_iGlowIndex = 0xA438

        self.pm = pymem.Pymem('csgo.exe')
        self.client = pymem.process.module_from_name(self.pm.process_handle, 'client.dll').lpBaseOfDll

        while True:
            self.glow_manager = self.pm.read_int(self.client + self.dwGlowObjectManager)
            for i in range(1, 32):
                self.entity = self.pm.read_int(client + self.dwEntityList + i * 0x10)

                if self.entity:
                    self.entity_team_id = self.pm.read_int(self.entity + self.m_iTeamNum)
                    self.entity_glow = self.pm.read_int(self.entity + self.m_iGlowIndex)

                if self.entity_team_id == 3:
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x4, float(1))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x8, float(0))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0xC, float(0))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x10, float(1))
                    self.pm.write_int(self.glow_manager + self.entity_glow * 0x38 + 0x24, 1)

                elif self.entity_team_id == 2:
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x4, float(0))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x8, float(1))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0xC, float(0))
                    self.pm.write_float(self.glow_manager + self.entity_glow * 0x38 + 0x10, float(1))
                    self.pm.write_int(self.glow_manager + self.entity_glow * 0x38 + 0x24, 1)
