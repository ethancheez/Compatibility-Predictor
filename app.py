import math
import json

# Calculate the mean of the data attribute
def mean(data, attribute, len, applicant = None):
	sum = 0
	for i in range(len):
		sum += data[i]['attributes'][attribute]

	if applicant is not None:
		sum += applicant['attributes'][attribute]
		len += 1

	return sum / len

# Calculate the stdev of the data attribute
def stdev(data, attribute, mean, len, applicant = None):
	num_sum = 0
	for i in range(len):
		num_sum += (data[i]['attributes'][attribute] - mean) ** 2

	if applicant is not None:
		num_sum += (applicant['attributes'][attribute] - mean) ** 2
		len += 1

	return math.sqrt( num_sum / len )

# Score the mean of the attribute
def scoreMean(score, meanTeam, meanApplicant):
	if meanApplicant > meanTeam:
		return score
	meanDiff = (meanTeam - meanApplicant) / meanTeam
	return round(score * (1-meanDiff), 2)

# Score the stdev of the attribute
def scoreSTDEV(score, stdevTeam, stdevApplicant):
	if stdevApplicant < stdevTeam:
		return score
	stdevDiff = (stdevApplicant - stdevTeam) / stdevApplicant
	return round(score * (1-stdevDiff), 2)


# MAIN
if __name__ == '__main__':
	# Open json file and parse data
	JSON_INPUT = open('input.json')
	PARSE_JSON_IN = json.load(JSON_INPUT)

	team = PARSE_JSON_IN['team']
	applicants = PARSE_JSON_IN['applicants']

	# Create output JSON
	JSON_OUTPUT = open('output.json', 'w')
	PARSE_JSON_OUT = []

	# Find number of members in team
	team_Size = len(team)

	# Find number of applicants
	num_Applicants = len(applicants)

	# Find mean and stdev of team intelligence
	team_mean_intelligence = mean(team, 'intelligence', team_Size)
	team_stdev_intelligence = stdev(team, 'intelligence', team_mean_intelligence, team_Size)

	# Find mean and stdev of team strength
	team_mean_strength = mean(team, 'strength', team_Size)
	team_stdev_strength = stdev(team, 'strength', team_mean_strength, team_Size)

	# Find mean and stdev of team endurance
	team_mean_endurance = mean(team, 'endurance', team_Size)
	team_stdev_endurance = stdev(team, 'endurance', team_mean_endurance, team_Size)

	# Find mean and stdev of team spicyFoodTolerance
	team_mean_spicyFoodTolerance = mean(team, 'spicyFoodTolerance', team_Size)
	team_stdev_spicyFoodTolerance = stdev(team, 'spicyFoodTolerance', team_mean_spicyFoodTolerance, team_Size)

	for i in range(num_Applicants):
		# Begin scoring (start with 1)
		score = 1

		# Find new mean and stdev of intelligence
		new_mean_intelligence = mean(team, 'intelligence', team_Size, applicants[i])
		new_stdev_intelligence = stdev(team, 'intelligence', new_mean_intelligence, team_Size, applicants[i])

		# Find mean and stdev of team strength
		new_mean_strength = mean(team, 'strength', team_Size, applicants[i])
		new_stdev_strength = stdev(team, 'strength', new_mean_strength, team_Size, applicants[i])

		# Find mean and stdev of team endurance
		new_mean_endurance = mean(team, 'endurance', team_Size, applicants[i])
		new_stdev_endurance = stdev(team, 'endurance', new_mean_endurance, team_Size, applicants[i])

		# Find mean and stdev of team spicyFoodTolerance
		new_mean_spicyFoodTolerance = mean(team, 'spicyFoodTolerance', team_Size, applicants[i])
		new_stdev_spicyFoodTolerance = stdev(team, 'spicyFoodTolerance', new_mean_spicyFoodTolerance, team_Size, applicants[i])

		# Debug
		print('Name: ', applicants[i]['name'])
		print(f"\t\t\t Mean (T) \tstdev (T) \tMean (A) \tstdev (A)")
		print(f"Intelligence \t\t {team_mean_intelligence:.6f}\t{team_stdev_intelligence:.6f}\t{new_mean_intelligence:.6f}\t{new_stdev_intelligence:.6f}")
		print(f"Strength \t\t {team_mean_strength:.6f}\t{team_stdev_strength:.6f}\t{new_mean_strength:.6f}\t{new_stdev_strength:.6f}")
		print(f"Endurance \t\t {team_mean_endurance:.6f}\t{team_stdev_endurance:.6f}\t{new_mean_endurance:.6f}\t{new_stdev_endurance:.6f}")
		print(f"spicyFoodTolerance \t {team_mean_spicyFoodTolerance:.6f}\t{team_stdev_spicyFoodTolerance:.6f}\t{new_mean_spicyFoodTolerance:.6f}\t{new_stdev_spicyFoodTolerance:.6f}")
		print('\n')

		# Calculate scores
		score = scoreMean(score, team_mean_intelligence, new_mean_intelligence)
		score = scoreMean(score, team_mean_strength, new_mean_strength)
		score = scoreMean(score, team_mean_endurance, new_mean_endurance)

		score = scoreSTDEV(score, team_stdev_intelligence, new_stdev_intelligence)
		score = scoreSTDEV(score, team_stdev_strength, new_stdev_strength)
		score = scoreSTDEV(score, team_stdev_endurance, new_mean_endurance)
		score = scoreSTDEV(score, team_stdev_spicyFoodTolerance, new_stdev_spicyFoodTolerance)

		# Add score to JSON object
		PARSE_JSON_OUT.append({
			"name" : applicants[i]['name'],
			"score" : score
		})

	scoredApplicants =  {"scoredApplicants" : PARSE_JSON_OUT}

	# Write JSON to file
	json.dump(scoredApplicants, JSON_OUTPUT, indent=5, separators=(',', ': '))

	# Close files
	JSON_INPUT.close()
	JSON_OUTPUT.close()
