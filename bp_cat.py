out_file = open("bp_cat.csv", 'w')
out_file.write("P_ID,sbp_g160,sbp_g180,dbp_g100,dbp_g120\n")

bp_data = {}

bp_file = open("bp_data.csv", 'r')

for line in bp_file.readlines():
	line = line.strip().split(',')

	patient = line[0]
	systolic = line[1]
	diastolic = line[2]

	if not patient in bp_data:
		bp_data[patient] = [0, 0, 0, 0]
	
	if int(systolic) > 160: bp_data[patient][0] = 1
	if int(systolic) > 180: bp_data[patient][1] = 1
	if int(diastolic) > 100: bp_data[patient][2] = 1
	if int(diastolic) > 120: bp_data[patient][3] = 1


for patient in sorted(bp_data):
	print(patient)

	bp_list = bp_data[patient]
	out_file.write(patient)

	for bp_reading in bp_list:
		out_file.write(","+str(bp_reading))
	out_file.write("\n")

out_file.close()



