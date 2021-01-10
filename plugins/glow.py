import pymem
import pymem.process
import keyboard
import win32gui

dwEntityList = 0x4D5022C
dwLocalPlayer = 0xD3BBEC
m_iTeamNum = 0xF4
dwGlowObjectManager = 0x5298070
m_iGlowIndex = 0xA438

def main():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

            if entity_team_id == 3:
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

            elif entity_team_id == 2:
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
