dmesg

[932577.953102] usb 5-1: USB disconnect, device number 3
[932580.366034] usb 5-1: new full-speed USB device number 4 using uhci_hcd
[932580.755085] usb 5-1: New USB device found, idVendor=24e0, idProduct=0050, bcdDevice= 0.01
[932580.755093] usb 5-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[932580.755096] usb 5-1: Product: Yocto-Light-V3
[932580.755099] usb 5-1: Manufacturer: Yoctopuce
[932580.755102] usb 5-1: SerialNumber: LIGHTMK3-1715EA
[932580.763767] hid-generic 0003:24E0:0050.0005: hiddev0,hidraw3: USB HID v1.11 Device [Yoctopuce Yocto-Light-V3] on usb-0000:00:1d.3-1/input0



permissions
https://www.yoctopuce.com/EN/article/how-to-begin-with-yoctopuce-devices-on-linux

docker build -t lux . 

docker run -it --device /dev/bus/usb:/dev/bus/usb lux:latest 
