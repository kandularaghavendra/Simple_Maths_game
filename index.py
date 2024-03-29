import random,time
while 1:
	print("\n\n\n=========== Math Game App ===========\n\n\nYour score is 2,000 divided by your time as you answer the question.\n\n")
	difficulty=0
	while difficulty!="1" and difficulty!="2" and difficulty!="3":
		difficulty=input("Enter a difficulty (1,2,3) to start: ")
		if difficulty!="1" and difficulty!="2" and difficulty!="3":
			print("Please type 1, 2, or 3. ")
	difficulty=int(difficulty)
	score=0
	begin=time.time()
	while score<10:
	
		if difficulty==1:
			puzzle=random.randint(1,4)
		elif difficulty==2:
			puzzle=random.randint(1,6)
		elif difficulty==3:
			puzzle=random.randint(1,11)
	
		if puzzle==1:
			
			a=random.randint(0,9)
			b=random.randint(0,9)
			try:
				guess=int(input(str(a)+"+"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a+b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==2:
			
			a=random.randint(0,9)
			b=random.randint(0,9)
			try:
				guess=int(input(str(a)+"-"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a-b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==3:
			
			a=random.randint(1,9)
			b=random.randint(1,9)
			try:
				guess=int(input(str(a)+"*"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a*b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==4:
		
			a=random.randint(1,9)
			b=random.randint(1,9)
			try:
				guess=int(input(str(a*b)+"/"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==5:
			
			a=random.randint(0,16)
			try:
				guess=int(input(str(a)+"^2=?"))
			except:
				guess="mocha"
			if guess==a**2:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==6:
			
			a=random.randint(0,16)
			try:
				guess=int(input("sqrt("+str(a**2)+")=?"))
			except:
				guess="mocha"
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==7:
			
			m=random.randint(1,9)
			zero=random.randint(-9,9)
			try:
				guess=int(input(str(m)+"x+"+str(-m*zero)+"=0, solve for x"))
			except:
				guess="mocha"
			if guess==zero:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==8:
			
			a=random.randint(0,19)
			b=random.randint(0,19)
			try:
				guess=int(input(str(a)+"+"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a+b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==9:
			
			a=random.randint(0,19)
			b=random.randint(0,19)
			try:
				guess=int(input(str(a)+"-"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a-b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==10:
			
			a=random.randint(10,19)
			b=random.randint(1,19)
			try:
				guess=int(input(str(a)+"*"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a*b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==11:
			
			a=random.randint(10,19)
			b=random.randint(1,19)
			try:
				guess=int(input(str(a*b)+"/"+str(b)+"=?"))
			except:
				guess="mocha"
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
	end=time.time()
	score=str(round(2000/(end-begin)))
	#recording score
	open("math.csv", "a").write("\n"+str(round(end))+","+str(difficulty)+","+score)
	#displaying
	input("Your final score is "+score+".")
