from database import Database

class Ingresso():
	def __init__(self):
		self.table = "Ingresso"
		self.Etable = "Evento"
		self.db = Database().conn()
		self.cursor = self.db.cursor()

	def findAll(self,Usuario_Id):		
		try:
			sql = "SELECT ingresso.Id,ingresso.Tipo,ingresso.Quantidade,ingresso.Preco,evento.Titulo FROM ingresso JOIN evento ON evento.Id = ingresso.Evento_Id WHERE ingresso.Usuario_Id = ?".format(ingresso=self.table,evento=self.Etable)
			self.cursor.execute(sql,[Usuario_Id])
			return self.cursor.fetchall()
		except Exception:
			self.db.close()
			
	def find(self,Usuario_Id,Id):
		try:
			sql = "SELECT ingresso.Id,ingresso.Tipo,ingresso.Quantidade,ingresso.Preco,evento.Id,evento.Titulo FROM ingresso JOIN evento ON evento.Id = ingresso.Evento_Id WHERE ingresso.Usuario_Id = ? AND ingresso.Id = ?".format(ingresso=self.table,evento=self.Etable)
			self.cursor.execute(sql,[Usuario_Id,Id])
			return self.cursor.fetchone()
		except Exception:
			self.db.close()

	def update(self,Tipo,Quantidade,Preco,Evento_Id,Usuario_Id,Id):
		try:
			sql = "UPDATE %s SET Tipo = ? , Quantidade = ?, Preco = ?, Evento_Id = ? WHERE Usuario_Id = ? AND Id = ?" % self.table
			self.cursor.execute(sql,[Tipo,Quantidade,Preco,Evento_Id,Usuario_Id,Id])
			self.db.commit()
			self.db.close()
			return True
		except Exception:
			return False

	def add(self,Tipo,Quantidade,Preco,Usuario_Id,Evento_Id):
		try:
			sql = "INSERT INTO %s (Tipo,Quantidade,Preco,Usuario_Id,Evento_Id) VALUES (?,?,?,?,?)" % self.table
			self.cursor.execute(sql,[Tipo,Quantidade,Preco,Usuario_Id,Evento_Id])
			self.db.commit()
			self.db.close()
			return True
		except Exception:
			return False

	def delete(self,Usuario_Id,Id):
		try:
			sql = "DELETE FROM %s WHERE Usuario_Id = ? AND Id = ?" % self.table
			self.cursor.execute(sql,[Usuario_Id,Id])
			self.db.commit()
			self.db.close()
			return True
		except Exception:
			return False

	def find_by_evento_id(self,Evento_Id):
		try:
			sql = "SELECT ingresso.Id,ingresso.Tipo,ingresso.Quantidade,ingresso.Preco FROM %s WHERE Evento_Id = ? AND ingresso.Quantidade > 0" % self.table
			self.cursor.execute(sql,[Evento_Id])
			return self.cursor.fetchall()
		except Exception:
			self.db.close()

	def delete_by_usuario(self,Usuario_Id):
		try:
			sql = "DELETE FROM %s WHERE Usuario_Id = ?" % self.table
			self.cursor.execute(sql,[Usuario_Id])
			self.db.commit()
			self.db.close()
			return True
		except Exception:
			return False