out_file = open("bp_data_mean.csv", 'w')
out_file.write("P_ID,sbp,dbp\n")

bp_data = {}

bp_file = open("bp_data.csv", 'r')

for line in bp_file.readlines():
	line = line.strip().split(',')

	patient = line[0]
	systolic = int(line[1])
	diastolic = int(line[2])

	if not patient in bp_data:
		bp_data[patient] = [[],[]]

	bp_data[patient][0].append(systolic)
	bp_data[patient][1].append(diastolic)


for patient in sorted(bp_data):
	print(patient)

	sbp_list = bp_data[patient][0]
	dbp_list = bp_data[patient][1]
	sbp_mean = sum(sbp_list) / float(len(sbp_list))
	dbp_mean = sum(dbp_list) / float(len(dbp_list))

	out_file.write(patient+","+str(sbp_mean)+","+str(dbp_mean)+'\n')

out_file.close()



