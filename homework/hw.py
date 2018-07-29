#1
class Student:
	def __init__(self,nm,ag,gd=[]):
		self.name = nm
		self.age = ag
		self.grade = gd
	def get_name(self):
		print(self.name)
	def get_age(self):
		print(int(self.age))
	def get_course(self):
		print(int(max(self.grade)))
zm = Student('Zhangming',20,[69,88,100])
zm.get_name()
zm.get_age()
zm.get_course()
#2
class dictclass:
	def __init__(self,mydict):
		self.mydict = mydict
	def del_dict(self,key):
		if key in self.mydict:
			self.mydict.pop(key)
			return self.mydict
		else:
			return 'not found'
	def get_dict(self,key):
		if key in self.mydict:
			return key
		else:
			return 'not found'
	def get_key(self):
		return list(self.mydict.keys())
	def update_dict(self,newdict):
		return list(self.mydict.values()) + list(newdict.values())
def main():
	d = {'姓名':'高鑫','年龄':'22','性别':'女','身高':'167','体重':'**'}
	d2 = {'爱好':'舞蹈'}
	d1 = dictclass(d)
	print(d1.del_dict('体重'))
	print(d1.get_dict('身高'))
	print(d1.get_key())
	print(d1.update_dict(d2))
if __name__ == '__main__':
	main()


#3
class Student:
	def __init__(self,Dict):
		self.Dict = Dict
	def add_info(self,aDict):
		self.Dict.update(aDict)
		print(self.Dict)
	def del_info(self,dkey):
		self.Dict.pop(dkey)
		print(self.Dict)
	def mod_info(self,mkey,mval):
		self.Dict[mkey]=mval
		print(self.Dict)
	def see_info(self,skey):
		print(skey,':',self.Dict[skey] if skey in self.Dict else '未知')
gxindex = Student({'计算机组成原理':'89','数据库':'76','线性代数':'92','网页设计':'95'})
gxindex.add_info({'js':'优'})
gxindex.del_info('线性代数')
gxindex.mod_info('js','91')
gxindex.see_info('数据库')







