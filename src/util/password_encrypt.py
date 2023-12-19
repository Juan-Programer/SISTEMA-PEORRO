import bcrypt

class PasswordEncrypt():
	def __init__(self, password: str = "", hashed: str = ""):
		self.hashed = hashed or ""
		self.salt = "987654321"
		self.password = password

	def compare(self, hashed: str) -> bool:
		return bcrypt.checkpw( hashed.encode('utf-8'), self.get_hash().encode('utf-8') )

	def get_hash(self) -> str:
		if self.hashed == "":
			hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
			self.hashed = hashed_password.decode('utf-8')

		return self.hashed
