class SmartPhone:
  def __init__(self, storage, ram, color):
    self.storage = storage
    self.ram = ram
    self.color = color

class Tecno(SmartPhone):
  pass

class Infinix(SmartPhone):
  pass

class Itel(SmartPhone):
  pass

tecno_spark_9 = Tecno("128GB", "4GB", "Blue")
infinix_hot_12 = Infinix("64GB", "4GB", "Black")
itel_s16 = Itel("32GB", "2GB", "White")

print(f"Tecno Spark 9: Storage={tecno_spark_9.storage}, RAM={tecno_spark_9.ram}, Color={tecno_spark_9.color}")
print(f"Infinix Hot 12: Storage={infinix_hot_12.storage}, RAM={infinix_hot_12.ram}, Color={infinix_hot_12.color}")
print(f"Itel S16: Storage={itel_s16.storage}, RAM={itel_s16.ram}, Color={itel_s16.color}")
