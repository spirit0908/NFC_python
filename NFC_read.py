
import binascii
import sys
import time
import PN532

global CardState

#Create an instance of the PN532 class
pn532 = PN532.PN532("/dev/ttyAMA0", 115200)

#Initialize communiction with PN532
pn532.begin()

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

print('Waiting for MiFare card...')

CardState = "none"

while True:
    global CardState
    # Check if a card is available to read.
#    uid = pn532.read_passive_target()
    # Try again if no card is available.
#    if uid is "no_card":
#        CardState = "none"
#        continue

    if CardState == "init":
    	print("Waiting for card...")
        CardState = "read"

    elif CardState == "read":
        #Wait to read a card
        uid = pn532.read_passive_target()
	
        if uid == "no_card":
#	    print("waiting for card...{}".format(uid))
 	    CardState = "read"
        else:
#	    print("waiting for card...{}".format(format(binascii.hexlify(uid))))
            CardState = "card_detected"

    elif CardState == "card_detected":
        print("card detected: {}".format(format(binascii.hexlify(uid)))) 
        #Wait to remove card
#        uid = pn532.read_passive_target()
        print("waiting card is removed") 
	CardState = "waiting_remove"
    
    elif CardState == "waiting_remove":
        uid = pn532.read_passive_target()
 
        if uid == "no_card":
	    print("card removed.")
 	    CardState = "init"
    else:
        CardState = "init"

    #Card is found
#    print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    # Authenticate block 4 for reading with default key (0xFFFFFFFFFFFF).
#    for i in range(0,16):
 #       if not pn532.mifare_classic_authenticate_block(uid, i, PN532.MIFARE_CMD_AUTH_B,
#                                                       [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]):
  #          print('Failed to authenticate block ')+str(i)
   #         break
        # Read block 4 data.
    #    data = pn532.mifare_classic_read_block(i)
     #   if data is None:
      #      print('Failed to read block ')+str(i)
       #     continue
        # Note that 16 bytes are returned, so only show the first 4 bytes for the block.

     #   print "Read block "+str(i)+" - "+(': 0x{0}'.format(binascii.hexlify(data[:16]))) + " - "+''.join(map(chr,data))

        # Example of writing data to block 4.  This is commented by default to
        # prevent accidentally writing a card.
        # Set first 4 bytes of block to 0xFEEDBEEF.
        # data[0:4] = [0xFE, 0xED, 0xBE, 0xEF]
        # # Write entire 16 byte block.
        # pn532.mifare_classic_write_block(4, data)
        # print('Wrote to block 4, exiting program!')
        # # Exit the program to prevent continually writing to card.
# sys.exit(0)


