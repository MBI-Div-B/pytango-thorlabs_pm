from ThorlabsPM100 import ThorlabsPM100, USBTMC

from tango import AttrQuality, AttrWriteType, DispLevel, DevState, DebugIt
from tango.server import Device, attribute, command, pipe, device_property

class ThorlabsPM100(Device):

    wavelength = attribute(label="Wavelength (nm)", dtype=float,
                         display_level=DispLevel.OPERATOR,
                         access=AttrWriteType.READ_WRITE,
                         doc="Correction wavelength")

    power = attribute(label="Power (W)", dtype=float,
                         display_level=DispLevel.OPERATOR,
                         access=AttrWriteType.READ,
                         doc="Measured power")



    def init_device(self):
        Device.init_device(self)
        self.inst = USBTMC(device="/dev/usbtmc0")
        self.power_meter = ThorlabsPM100(inst=self.inst)
        self.set_state(DevState.ON)

    def read_wavelength(self):
        return self.power_meter.sense.correction.wavelength
    
    def write_wavelength(self, wav):
        self.wavelength = wav
        self.power_meter.sense.correction.wavelength = wav

    def read_power(self):
        return self.power_meter.read


if __name__ == "__main__":
    ThorlabsPM100.run_server()