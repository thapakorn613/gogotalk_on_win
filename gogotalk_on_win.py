import serial, time, sys
from pywinusb import hid


#* firmware init packet: 0x54 0xfe 0x04 0x00 0x00 0xc9 0xc9
beepPkt = [0x00, 0x00, 0x0b]
initPkt = [0x00, 0x00, 0xc9]
# initPkt = [0x00, 0x00, 0xca]

firmware_length = 0
# firmware_path = sys.argv[1] #? take first argument as firmware path
firmware_path = "C:/Users/peera/Documents/Works/LIL/gogo-6/esp32-firmware/.pio/build/esp32dev/firmware.bin"

def open_and_write_content():
    device = hid.HidDeviceFilter(vendor_id = 0x0461, product_id = 0x0020).get_devices()[0]
    # print(device)
    device.open()
    for out_report in device.find_output_reports():
        print(out_report)

        SIZE = 64
        
        buffer = [0 for i in range(SIZE-len(beepPkt))]
        beepPkt.extend(buffer)
        print(beepPkt, len(beepPkt))

        print("send init packet")
        if out_report.send(beepPkt):
            print("success")
        time.sleep(2)

if __name__ == "__main__":
    open_and_write_content()
    print("finish")
