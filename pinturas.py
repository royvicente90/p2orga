class Pinturas:
  
  def __init__(self, cota, nombre, precio, status):
    self.cota = cota
    self.nombre = nombre
    self.precio = precio
    self.status= status

  def mostrar_cota(self):
   return self.cota

  def mostrar_nombre(self):
   return self.nombre
    
      