import time,datetime,os,pickle

filename='timerdatas'
root='/storage/emulated/0/'
file=os.path.join(root,filename)

targets=[]#1608750000,1608836400]

def save(data,file):
		pickle.dump(data,open(file,'wb'))
		print('saved')
def timefmt(hours,neg=False):
	out=[]
	s=hours
	names=[['year',365*24*60*60],['month',730.001*60*60],['week',7*24*60*60],['day',24*60*60],['hour',60*60],['minute',60],['second',1]]
	while names and s>= 0:
		cur=names.pop(0)
		if s<cur[1]:continue
		
		if s//cur[1] >1: cur[0]+='s'
		
		out.append('-'*neg+str(int(s//cur[1])) +' '+cur[0])
		s %= cur[1]
	return ', '.join(out)

i='not'

if os.path.exists(file):
	try: targets=pickle.load(open(file,'rb'))
	except: print('load error')

while(i!='exit'):
	targets.sort(reverse=True)
	print('\n'*3)
	
	
	'''todel=[]
	for i,t in enumerate(targets):
		if t < time.time():
			todel.append(i)
	todel=todel[::-1]
	for x in todel: del targets[x]
	'''
	
	for index,target in enumerate(targets):
		print('\n'+'-'*60)
		
		print('['+str(index)+']'+':',"{:,d}".format(target))
		t=time.time()
		print(time.ctime(target),'is')
		if target>t: print(' '+timefmt(target-t))
		else: print(' '+timefmt(t-target,neg=True))
		
	print('_'*60)
	i=input(' c=new target\n d=delete a target\n s=save: ')
	
	if i.lower().strip() == 'c':
		y=int(input('enter year: '))
		mon=int(input('enter month: '))
		day=int(input('enter day: '))
		hr=int(input('enter hour: '))
		m=int(input('enter minutes: '))
		s=int(input("enter seconds: "))
		targets.append(round(datetime.datetime(y,mon,day,hr,m,s).timestamp()))
	
	elif i.lower().strip()=='s':
		save(targets,file)
	
	elif i.lower().strip()=='d':
		inp=input(' enter index to delete: ')
		try: del targets[int(inp)]
		except: print('error thrown')