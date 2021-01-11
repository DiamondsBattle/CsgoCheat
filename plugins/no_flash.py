import pymem
import pymem.process
import time


class NoFlash:
    def __init__(self):
        self.dwLocalPlayer = 0xD36B94
        self.m_flFlashMaxAlpha = 0xA40C

        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll

        while True:
            self.player = self.pm.read_int(self.client + self.dwLocalPlayer)
            if self.player:
                self.flash_value = self.player + self.m_flFlashMaxAlpha
                if self.flash_value:
                    self.pm.write_float(self.flash_value, float(0))
            time.sleep(1)


if __name__ == '__main__':
    main()