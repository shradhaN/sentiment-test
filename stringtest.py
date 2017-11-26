# sentiment analysis



neg_file_obj = open("negative-words.txt")
neg_text = neg_file_obj.read().strip().split()

pos_file_obj = open("positive-words.txt")
pos_text = pos_file_obj.read().strip().split()

negcount = 0
poscount = 0

while 1:
	st = input("Enter a string:")
	inptwords = st.strip().split()

	for word in inptwords:
		if st == "":
			continue
		if word in neg_text:
			negcount = negcount+1
			break
		if word in pos_text:
			poscount = poscount+1
		else:
			continue

	if negcount >=1:
		print(negcount)
		print("negative")
	if poscount >=1:
		print(poscount)
		print("positive")
	else:
		print("neutral")

	negcount = 0
	poscount = 0
neg_file_obj.close()
pos_file_obj.close()


