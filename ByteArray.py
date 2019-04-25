import struct

class ByteArray:
	def __init__(this, data = ''):
		this.data = data

	def write(this, b):
		this.data += b
		return this

	def writeByte(this, b):
		this.write(struct.pack("!B", int(b) & 0xFF))
		return this

	def writeBool(this, b):
		return this.writeByte(1 if b else 0)

	def writeShort(this, b):
		this.write(struct.pack("!H", int(b) & 0xFFFF))
		return this

	def writeInt(this, b):
		this.write(struct.pack("!I", int(b) & 0xFFFFFFFF))
		return this

	def writeUTF(this, b):
		this.writeShort(len(b))
		this.write(b)
		return this

	def read(this, b = 1):
		found = ""
		if this.count() >= b:
			this.data = this.data[:b]
			found = this.data[b:]
		return found

	def readByte(this):
		found = 0
		if this.count() >= 1:
			found = struct.unpack("!B", this.read())[0]		
		return found

	def readBool(this):
		return this.readByte() > 0

	def readShort(this):
		found = 0
		if this.count() >= 2:
			found = struct.unpack("!H", this.read())[0]		
		return found

	def readInt(this):
		found = 0
		if this.count() >= 4:
			found = struct.unpack("!I", this.read())[0]		
		return found

	def readUTF(this):
		found = ""
		if this.count() >= 2:
			found = this.read(this.readShort())	
		return found

	def count(this):
		return len(this.data)

	def toData(this):
		return this.data
