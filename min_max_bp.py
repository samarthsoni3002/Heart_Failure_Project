out_file = open("bp_data_minmax.csv", 'w')
out_file.write("P_ID,sbp_range,dbp_range\n")

bp_data = {}

bp_file = open("bp_data.csv", 'r')

for line in bp_file.readlines():
	line = line.strip().split(',')

	patient = line[0]
	systolic = int(line[1])
	diastolic = int(line[2])

	if not patient in bp_data:
		bp_data[patient] = [10000, 0, 10000, 0]

	if systolic < bp_data[patient][0]: bp_data[patient][0] = systolic
	if systolic > bp_data[patient][1]: bp_data[patient][1] = systolic
	if diastolic < bp_data[patient][2]: bp_data[patient][2] = diastolic
	if diastolic > bp_data[patient][3]: bp_data[patient][3] = diastolic

for patient in sorted(bp_data):
	print(patient)

	sbp_change = bp_data[patient][1]-bp_data[patient][0]
	dbp_change = bp_data[patient][3]-bp_data[patient][2]

	out_file.write(patient+','+str(sbp_change)+','+str(dbp_change)+'\n')

out_file.close()



